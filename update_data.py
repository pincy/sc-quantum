"""Refreshes the local data base after a Star Citizen patch.

Steps:
  1. Fetch all ships (ships/pN.json) and all quantum drives (drives/<uuid>.json) from the Star Citizen Wiki API.
     Data is downloaded into a temporary directory first; the old data is only replaced if everything succeeded.
  2. Rebuild combos.json (ship x drive of matching size).
  3. Regenerate ranking.md, flighttime.json and web/data.js.
  4. Write the game version from version.json into README.md (title, contents, data sources, result heading).

Usage:  python3 update_data.py [--no-fetch]   (--no-fetch only rebuilds the derived files)
"""
import json, os, shutil, subprocess, sys, tempfile, time, urllib.request

API = 'https://api.star-citizen.wiki/api'
HEADERS = {'User-Agent': 'Mozilla/5.0 (sc-quantum updater)'}
ROOT = os.path.dirname(os.path.abspath(__file__))
EXCLUDED_DRIVES = {'Mauler Quantum Drive'}


def get(url, retries=4):
    for attempt in range(retries):
        try:
            req = urllib.request.Request(url, headers=HEADERS)
            with urllib.request.urlopen(req, timeout=120) as r:
                return r.read()
        except Exception as e:
            if attempt == retries - 1:
                raise RuntimeError(f'{url}: {e}')
            time.sleep(2 * (attempt + 1))


def get_json(url):
    return json.loads(get(url))


def fetch_all(tmp):
    version = get_json(f'{API}/v2/game-versions')['data'][0]
    default = next((v for v in get_json(f'{API}/v2/game-versions')['data'] if v.get('is_default')), version)
    os.makedirs(f'{tmp}/ships')
    os.makedirs(f'{tmp}/drives')

    first = get(f'{API}/v2/vehicles?page%5Bnumber%5D=1')
    open(f'{tmp}/ships/p1.json', 'wb').write(first)
    last = json.loads(first)['meta']['last_page']
    for p in range(2, last + 1):
        print(f'ships page {p}/{last}')
        open(f'{tmp}/ships/p{p}.json', 'wb').write(get(f'{API}/v2/vehicles?page%5Bnumber%5D={p}'))

    items = get_json(f'{API}/v2/items?filter%5Btype%5D=QuantumDrive&page%5Bsize%5D=100')
    if items['meta']['last_page'] > 1:
        raise RuntimeError('more than 100 quantum drives: pagination needs to be added')
    for i, it in enumerate(items['data'], 1):
        print(f'drive {i}/{len(items["data"])}: {it["name"]}')
        open(f'{tmp}/drives/{it["uuid"]}.json', 'wb').write(get(it['link']))

    # Some drives are equipped on ships but missing from the item list: fetch them via the ship ports.
    known = set(os.listdir(f'{tmp}/drives'))
    equipped = {}
    for f in os.listdir(f'{tmp}/ships'):
        for d in json.load(open(f'{tmp}/ships/{f}'))['data']:
            found = []
            drive_ports(d.get('ports'), found)
            equipped.update({e['uuid']: e['link'] for e in found})
    for uuid, link in equipped.items():
        if f'{uuid}.json' not in known:
            print('extra drive from ship ports:', uuid)
            open(f'{tmp}/drives/{uuid}.json', 'wb').write(get(link))
    json.dump(default, open(f'{tmp}/version.json', 'w'), indent=1)
    return default


def swap(tmp):
    for name in ('ships', 'drives'):
        shutil.rmtree(f'{ROOT}/{name}', ignore_errors=True)
        shutil.move(f'{tmp}/{name}', f'{ROOT}/{name}')
    shutil.move(f'{tmp}/version.json', f'{ROOT}/version.json')


def drive_ports(ports, out):
    for p in ports or []:
        item = p.get('equipped_item') or {}
        if item.get('type') == 'QuantumDrive':
            out.append(item)
        drive_ports(p.get('ports'), out)


def build_combos():
    drives = []
    for f in os.listdir(f'{ROOT}/drives'):
        d = json.load(open(f'{ROOT}/drives/{f}'))['data']
        if 'PLACEHOLDER' in d['name'] or d['name'] in EXCLUDED_DRIVES:
            continue
        drives.append(d)

    ships = {}
    files = sorted(os.listdir(f'{ROOT}/ships'), key=lambda n: int(n[1:-5]))
    for f in files:
        for d in json.load(open(f'{ROOT}/ships/{f}'))['data']:
            stock = []
            drive_ports(d.get('ports'), stock)
            q = d.get('quantum') or {}
            buy = [p['price_buy'] for p in (d.get('uex_prices') or {}).get('purchase', []) if p.get('price_buy')]
            if not stock or not d.get('is_spaceship') or not q.get('quantum_fuel_capacity') or not buy:
                continue
            ships.setdefault(d['game_name'], dict(name=d['game_name'], size=stock[0]['size'], stock=stock[0]['name'],
                                                  tank=q['quantum_fuel_capacity'], mass=d['mass_total']))

    rows = []
    for s in ships.values():
        for d in drives:
            if d['size'] != s['size']:
                continue
            c = d['quantum_drive']['fuel_consumption_scu_per_gm']
            rows.append(dict(**s, qd=d['name'], grade=d['grade'], cls=d['classification_label'], c=c,
                             rng=s['tank'] / c, spd=d['quantum_drive']['modes'][0]['drive_speed'] / 1e6,
                             stk=d['name'] == s['stock']))
    json.dump(rows, open(f'{ROOT}/combos.json', 'w'))
    print(f'combos.json: {len(ships)} ships, {len(drives)} drives, {len(rows)} combinations')


def update_readme():
    """Writes the game version from version.json into the README (idempotent)."""
    import re
    v = json.load(open(f'{ROOT}/version.json'))
    code = v['code']
    short = code.split('.')[0:3]
    short = '.'.join(short)                      # 4.10.2-LIVE
    base = short.split('-')[0]                   # 4.10.2
    date = (v.get('released_at') or '')[:10]
    path = f'{ROOT}/README.md'
    text = open(path, encoding='utf-8').read()
    subs = [
        (r'(Star Citizen )\S+(\))', rf'\g<1>{short}\g<2>', 1),
        (r'(\(\d+ entries, version )[^,)]+(,)', rf'\g<1>{code}\g<2>', 1),
        (r'(\(currently )[^,)]+, [\d-]+(\))', rf'\g<1>{code}, {date}\g<2>', 1),
        (r'(#### Result \(seconds, )[^)]+(\))', rf'\g<1>{base}\g<2>', 1),
    ]
    for pattern, repl, count in subs:
        text, n = re.subn(pattern, repl, text, count=count)
        if not n:
            print('warning: README pattern not found:', pattern)
    open(path, 'w', encoding='utf-8').write(text)
    print('README version:', code)


def main():
    os.chdir(ROOT)
    if '--no-fetch' not in sys.argv:
        tmp = tempfile.mkdtemp(prefix='sc-update-', dir=ROOT)
        try:
            version = fetch_all(tmp)
            swap(tmp)
        finally:
            shutil.rmtree(tmp, ignore_errors=True)
        print('data version:', version['code'])
    update_readme()
    build_combos()
    for script in ('build_ranking.py', 'flighttime.py', 'build_web.py'):
        print('running', script)
        subprocess.run([sys.executable, script], check=True, stdout=subprocess.DEVNULL if script == 'flighttime.py' else None)


if __name__ == '__main__':
    main()
