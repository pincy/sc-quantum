import json, glob, os
import flighttime

HDR = ["Ship", "QD size", "Quantum drive", "Grade", "SCU/Gm", "Range Gm", "Speed Mm/s",
       "Cooldown s", "Spool s", "Cargo SCU", "SCM m/s", "Ship aUEC", "Drive aUEC", "Total aUEC",
       "Flight total s", "QT 60 Gm s", "QT 3 Gm s", "QT 30 Gm s", "Spool+wait s", "Short-range s",
       "Tank SCU", "Mass t", "Stock"]
ORIGIN = {'Civilian': 'Civ', 'Industrial': 'Ind', 'Military': 'Mil', 'Stealth': 'Sta', 'Competition': 'Com'}


def prices(d):
    up = d.get('uex_prices') or {}
    return [p['price_buy'] for p in up.get('purchase', []) if p.get('price_buy')]


drives = {}
for f in os.listdir('drives'):
    d = json.load(open('drives/' + f))['data']
    b = prices(d)
    m = d['quantum_drive']['modes'][0]
    drives[d['name']] = dict(origin=ORIGIN.get(d.get('class')), cd=m['cooldown_time'], spool=m['spool_up_time'], price=min(b) if b else None)

# Per ship name: prefer the entry with a price; price = minimum over all entries with the same name
ships = {}
for f in sorted(glob.glob('ships/p*.json')):
    for d in json.load(open(f))['data']:
        b = prices(d)
        s = ships.setdefault(d['game_name'], dict(price=None, cargo=0, scm=0, priced=False))
        if b:
            s['price'] = min(b) if s['price'] is None else min(s['price'], min(b))
        if b and not s['priced'] or not s.get('seen'):
            s.update(cargo=d['cargo_capacity'] or 0, scm=d['speed']['scm'], priced=bool(b), seen=True)

raw_ships, raw_drives = flighttime.load()
rows = []
for r in json.load(open('combos.json')):
    s = ships[r['name']]
    dr = drives[r['qd']]
    total = s['price'] + dr['price'] if s['price'] and dr['price'] else None
    grade = f"{r['grade']} - {dr['origin']}" if dr['origin'] else r['grade']
    flight = [None] * 6
    if flighttime.has_flight_data(raw_ships[r['name']]):
        p, _ = flighttime.simulate(raw_ships[r['name']], raw_drives[r['qd']])
        spool_wait = p['spool1'] + p['spool_s'] + p['spool2'] + p['cd_wait1'] + p['cd_wait2']
        near = p['scm'] + p['nav'] + p['arr1'] + p['gain1'] + p['arr_s'] + p['gain2'] + p['arr2']
        flight = [round(sum(p.values()), 1), round(p['qt1'], 1), round(p['qt_s'], 1), round(p['qt2'], 1),
                  round(spool_wait, 1), round(near, 1)]
    rows.append([r['name'], r['size'], r['qd'], grade, r['c'], round(r['rng'], 1), round(r['spd'], 1),
                 dr['cd'], dr['spool'], s['cargo'], s['scm'], s['price'], dr['price'], total] + flight +
                [r['tank'], round(r['mass'] / 1000, 1), '\u2713' if r['stk'] else ''])

VERSION = json.load(open('version.json'))['code'].split('.')[0:3]
VERSION = '.'.join(VERSION)
open('web/data.js', 'w').write('const VERSION=' + json.dumps(VERSION) + ';\nconst HEAD=' + json.dumps(HDR) + ';\nconst ROWS=' + json.dumps(rows) + ';\n')
print(sum(1 for r in rows if r[14] is None), 'rows without flight data;', len(rows), 'rows; without ship price:', sorted({r[0] for r in rows if r[11] is None}))
