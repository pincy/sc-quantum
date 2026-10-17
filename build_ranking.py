"""Builds ranking.md: quantum range per ship x quantum drive of matching size.

Range (Gm) = quantum tank (SCU) / fuel_consumption_scu_per_gm. Reads combos.json (see README).
"""
import json

rows = json.load(open('combos.json'))
md = [
    "# Star Citizen 4.10.2-LIVE – Quantum range per ship × quantum drive\n",
    "Formula: **range (Gm) = QT tank (SCU) / fuel_consumption_scu_per_gm**. This is the lower bound of the SPViewer "
    "range span; the SPViewer maximum is unexplained. Only drives of matching size are combined. Only purchasable "
    "ships (UEX purchase price). Size and tank come from the stock loadout. ★ = stock drive.\n",
    "Sources: ships https://api.star-citizen.wiki/api/v2/vehicles, drives "
    "https://api.star-citizen.wiki/api/v2/items?filter[type]=QuantumDrive (version 4.10.2-LIVE.12881860). "
    "Placeholder drives and the Mauler drive are excluded.\n",
    "Note: `fuel_consumption_scu_per_gm` is rounded to 3 decimals in the API; for size 1 (0.004/0.005) the error is large.\n",
]
for size in sorted({r['size'] for r in rows}):
    group = sorted((r for r in rows if r['size'] == size), key=lambda r: -r['rng'])
    ships = len({r['name'] for r in group})
    md.append(f"\n## Quantum drive size {size} ({ships} ships, {len(group)} combinations)\n\n"
              "| # | Ship | Quantum drive | Grade | Class | Tank SCU | SCU/Gm | Range Gm | Speed Mm/s |\n"
              "|--|--|--|--|--|--|--|--|--|")
    for i, r in enumerate(group, 1):
        star = ' ★' if r['stk'] else ''
        md.append(f"| {i} | {r['name']} | {r['qd']}{star} | {r['grade']} | {r['cls']} | {r['tank']} | "
                  f"{r['c']} | {r['rng']:.1f} | {r['spd']:.0f} |")
open('ranking.md', 'w').write("\n".join(md) + "\n")
print(len(rows), 'combinations written to ranking.md')
