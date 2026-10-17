"""Flugzeit-Simulation: Undock -> QT 60 Gm -> Ziel -> Abstand -> QT 3 Gm -> Ziel -> Abstand -> QT 30 Gm -> Ziel.

Alle Eingaben stammen aus den persistierten API-Daten (ships/, drives/).
Annahmen stehen in ASSUMPTIONS und werden in der Ausgabe wiederholt.
"""
import json, glob, os, math, sys

UNDOCK_SCM_M = 5_000      # SCM nach dem Abdocken
NAV_TO_QT_M = 10_000      # NAV bis zum QT-Punkt
QT1_M = 60e9
QT_SHORT_M = 3e9
QT2_M = 30e9
ARRIVAL_M = 30_000        # Rest bis zum Ziel nach dem QT-Drop
GAIN_M = 10_000           # Abstand gewinnen vor dem 2. Sprung (NAV, aus dem Stand)

COMBOS = [  # (Schiff game_name, Drive)
    ("Drake Corsair", "SunFire"),
    ("Crusader C2 Hercules Starlifter", "Erebos"),
    ("Origin 315p", "FoxFire"),
    ("Drake Cutlass Black", "SunFire"),
    ("Crusader C1 Spirit", "SunFire"),
    ("RSI Constellation Mk IV Andromeda", "SunFire"),
    ("RSI Constellation Mk IV Aquila", "SunFire"),
    ("RSI Constellation Mk IV Phoenix", "SunFire"),
    ("RSI Constellation Mk IV Phoenix Emerald", "SunFire"),
    ("RSI Constellation Mk IV Taurus", "SunFire"),
    ("RSI Constellation Mk V Centaurus", "SunFire"),
]


def accel_run(v0, v1, a):
    """Zeit und Strecke fuer v0 -> v1 mit konstanter Beschleunigung a."""
    t = (v1 - v0) / a
    return t, (v1 * v1 - v0 * v0) / (2 * a)


def move(dist, v0, vmax, a_up, a_down=None, stop=True):
    """Strecke dist mit Beschleunigen, ggf. Halten und optional Abbremsen auf 0."""
    t1, d1 = accel_run(v0, vmax, a_up)
    t3, d3 = accel_run(0, vmax, a_down) if stop else (0, 0)
    t3 = t3 if stop else 0
    if d1 + d3 <= dist:
        return t1 + (dist - d1 - d3) / vmax + t3
    # Vmax nicht erreicht
    if not stop:
        v = math.sqrt(v0 * v0 + 2 * a_up * dist)
        return (v - v0) / a_up
    v = math.sqrt((2 * dist + v0 * v0 / a_up) / (1 / a_up + 1 / a_down))
    return (v - v0) / a_up + v / a_down


def qt_time(dist, d):
    """QT-Flug: 2 Beschleunigungsstufen, Abbremsen spiegelbildlich."""
    v_e, v_max = d["engage_speed"], d["drive_speed"]
    a1, a2 = d["stage_one_accel_rate"], d["stage_two_accel_rate"]
    t1, d1 = accel_run(0, v_e, a1)
    t2, d2 = accel_run(v_e, v_max, a2)
    if 2 * (d1 + d2) <= dist:
        return 2 * (t1 + t2) + (dist - 2 * (d1 + d2)) / v_max, v_max
    half = dist / 2
    if half <= d1:
        v = math.sqrt(2 * a1 * half)
        return 2 * v / a1, v
    v = math.sqrt(v_e * v_e + 2 * a2 * (half - d1))
    return 2 * (t1 + (v - v_e) / a2), v


def has_flight_data(s):
    sp = s.get('speed') or {}
    return all(sp.get(k) for k in ('scm', 'max', 'zero_to_scm', 'zero_to_max', 'max_to_zero'))


def load():
    ships = {}
    for f in sorted(glob.glob('ships/p*.json')):
        for s in json.load(open(f))['data']:
            if has_flight_data(s) or s['game_name'] not in ships:
                ships.setdefault(s['game_name'], s)
                if not has_flight_data(ships[s['game_name']]):
                    ships[s['game_name']] = s
    drives = {}
    for f in os.listdir('drives'):
        dr = json.load(open('drives/' + f))['data']
        drives[dr['name']] = dr
    return ships, drives


def simulate(ship, drive):
    sp = ship['speed']
    scm, vmax = sp['scm'], sp['max']
    a_scm = scm / sp['zero_to_scm']
    a_nav = vmax / sp['zero_to_max']
    a_brk = vmax / sp['max_to_zero']
    m = drive['quantum_drive']['modes'][0]
    spool, cd = m['spool_up_time'], m['cooldown_time']

    t_scm = move(UNDOCK_SCM_M, 0, scm, a_scm, stop=False)
    # NAV beginnt mit SCM-Geschwindigkeit
    t_nav = move(NAV_TO_QT_M, scm, vmax, a_nav, stop=False)
    t_qt1, v1 = qt_time(QT1_M, m)
    t_arr1 = move(ARRIVAL_M, 0, vmax, a_nav, a_brk)
    t_gain1 = move(GAIN_M, 0, vmax, a_nav, stop=False)
    cd_wait1 = max(0.0, cd - (t_arr1 + t_gain1))
    t_qts, vs = qt_time(QT_SHORT_M, m)
    t_arrs = move(ARRIVAL_M, 0, vmax, a_nav, a_brk)
    t_gain2 = move(GAIN_M, 0, vmax, a_nav, stop=False)
    cd_wait2 = max(0.0, cd - (t_arrs + t_gain2))
    t_qt2, v2 = qt_time(QT2_M, m)
    t_arr2 = move(ARRIVAL_M, 0, vmax, a_nav, a_brk)
    parts = dict(scm=t_scm, nav=t_nav, spool1=spool, qt1=t_qt1, arr1=t_arr1, gain1=t_gain1, cd_wait1=cd_wait1,
                 spool_s=spool, qt_s=t_qts, arr_s=t_arrs, gain2=t_gain2, cd_wait2=cd_wait2,
                 spool2=spool, qt2=t_qt2, arr2=t_arr2)
    return parts, dict(spool=spool, cd=cd, qt_speed=m['drive_speed'] / 1e6, v1=v1 / 1e6, vs=vs / 1e6, v2=v2 / 1e6,
                       scm=scm, max=vmax, a_nav=a_nav, a_brk=a_brk)


if __name__ == '__main__':
    ships, drives = load()
    rows = []
    for sn, dn in COMBOS:
        if sn not in ships:
            print('FEHLT', sn, file=sys.stderr)
            continue
        p, info = simulate(ships[sn], drives[dn])
        rows.append((sn, dn, drives[dn]['size'], p, info, sum(p.values())))
    rows.sort(key=lambda r: r[5])
    json.dump([dict(ship=r[0], drive=r[1], size=r[2], parts=r[3], info=r[4], total=r[5]) for r in rows],
              open('flighttime.json', 'w'), indent=1)
    for r in rows:
        print(f"{r[0]:42s} {r[1]:8s} S{r[2]} total {r[5]:6.1f}s", {k: round(v, 1) for k, v in r[3].items()},
              'peak1', round(r[4]['v1']), '/', round(r[4]['qt_speed']))
