# Star Citizen 4.10.2-LIVE – Quantum range per ship × quantum drive

Formula: **range (Gm) = QT tank (SCU) / fuel_consumption_scu_per_gm**. This is the lower bound of the SPViewer range span; the SPViewer maximum is unexplained. Only drives of matching size are combined. Only purchasable ships (UEX purchase price). Size and tank come from the stock loadout. ★ = stock drive.

Sources: ships https://api.star-citizen.wiki/api/v2/vehicles, drives https://api.star-citizen.wiki/api/v2/items?filter[type]=QuantumDrive (version 4.10.2-LIVE.12881860). Placeholder drives and the Mauler drive are excluded.

Note: `fuel_consumption_scu_per_gm` is rounded to 3 decimals in the API; for size 1 (0.004/0.005) the error is large.


## Quantum drive size 1 (72 ships, 1440 combinations)

| # | Ship | Quantum drive | Grade | Class | Tank SCU | SCU/Gm | Range Gm | Speed Mm/s |
|--|--|--|--|--|--|--|--|--|
| 1 | Drake Cutter Rambler | Spectre | A | Quantum Drive | 1.7 | 0.004 | 425.0 | 218 |
| 2 | Drake Cutter Rambler | Zephyr | B | Quantum Drive | 1.7 | 0.004 | 425.0 | 184 |
| 3 | Drake Cutter Rambler | Drift | C | Quantum Drive | 1.7 | 0.004 | 425.0 | 167 |
| 4 | Anvil Terrapin | Spectre | A | Quantum Drive | 1.6 | 0.004 | 400.0 | 218 |
| 5 | Anvil Terrapin | Zephyr | B | Quantum Drive | 1.6 | 0.004 | 400.0 | 184 |
| 6 | Anvil Terrapin | Drift | C | Quantum Drive | 1.6 | 0.004 | 400.0 | 167 |
| 7 | Anvil Terrapin Medic | Spectre | A | Quantum Drive | 1.4 | 0.004 | 350.0 | 218 |
| 8 | Anvil Terrapin Medic | Zephyr | B | Quantum Drive | 1.4 | 0.004 | 350.0 | 184 |
| 9 | Anvil Terrapin Medic | Drift | C | Quantum Drive | 1.4 | 0.004 | 350.0 | 167 |
| 10 | Drake Cutter Rambler | Goliath | C | Quantum Drive | 1.7 | 0.005 | 340.0 | 219 |
| 11 | Drake Cutter Rambler | Siren | B | Quantum Drive | 1.7 | 0.005 | 340.0 | 178 |
| 12 | Drake Cutter Rambler | Voyage | B | Quantum Drive | 1.7 | 0.005 | 340.0 | 208 |
| 13 | Drake Cutter Rambler | Eos | C | Quantum Drive | 1.7 | 0.005 | 340.0 | 199 |
| 14 | Drake Cutter Rambler | Flood | D | Quantum Drive | 1.7 | 0.005 | 340.0 | 188 |
| 15 | Drake Cutter Rambler | LightFire | C | Quantum Drive | 1.7 | 0.005 | 340.0 | 239 |
| 16 | Drake Cutter Rambler | Hyperion | B | Quantum Drive | 1.7 | 0.005 | 340.0 | 219 |
| 17 | Drake Cutter Rambler | Atlas | A | Quantum Drive | 1.7 | 0.005 | 340.0 | 259 |
| 18 | Drake Cutter Rambler | FoxFire ★ | B | Quantum Drive | 1.7 | 0.005 | 340.0 | 263 |
| 19 | Drake Cutter Rambler | Burst | B | Quantum Drive | 1.7 | 0.005 | 340.0 | 230 |
| 20 | Drake Cutter Rambler | Beacon | C | Quantum Drive | 1.7 | 0.005 | 340.0 | 161 |
| 21 | Drake Cutter Rambler | Colossus | B | Quantum Drive | 1.7 | 0.005 | 340.0 | 241 |
| 22 | Drake Cutter Rambler | VK-00 | A | Quantum Drive | 1.7 | 0.005 | 340.0 | 210 |
| 23 | Drake Cutter Rambler | Vulcan | D | Quantum Drive | 1.7 | 0.005 | 340.0 | 197 |
| 24 | Drake Cutter Rambler | Wayfare | D | Quantum Drive | 1.7 | 0.005 | 340.0 | 170 |
| 25 | Drake Cutter Rambler | Expedition | C | Quantum Drive | 1.7 | 0.005 | 340.0 | 189 |
| 26 | Drake Cutter Rambler | Rush | C | Quantum Drive | 1.7 | 0.005 | 340.0 | 209 |
| 27 | Anvil Terrapin | Goliath | C | Quantum Drive | 1.6 | 0.005 | 320.0 | 219 |
| 28 | Anvil Terrapin | Siren | B | Quantum Drive | 1.6 | 0.005 | 320.0 | 178 |
| 29 | Anvil Terrapin | Voyage | B | Quantum Drive | 1.6 | 0.005 | 320.0 | 208 |
| 30 | Anvil Terrapin | Eos ★ | C | Quantum Drive | 1.6 | 0.005 | 320.0 | 199 |
| 31 | Anvil Terrapin | Flood | D | Quantum Drive | 1.6 | 0.005 | 320.0 | 188 |
| 32 | Anvil Terrapin | LightFire | C | Quantum Drive | 1.6 | 0.005 | 320.0 | 239 |
| 33 | Anvil Terrapin | Hyperion | B | Quantum Drive | 1.6 | 0.005 | 320.0 | 219 |
| 34 | Anvil Terrapin | Atlas | A | Quantum Drive | 1.6 | 0.005 | 320.0 | 259 |
| 35 | Anvil Terrapin | FoxFire | B | Quantum Drive | 1.6 | 0.005 | 320.0 | 263 |
| 36 | Anvil Terrapin | Burst | B | Quantum Drive | 1.6 | 0.005 | 320.0 | 230 |
| 37 | Anvil Terrapin | Beacon | C | Quantum Drive | 1.6 | 0.005 | 320.0 | 161 |
| 38 | Anvil Terrapin | Colossus | B | Quantum Drive | 1.6 | 0.005 | 320.0 | 241 |
| 39 | Anvil Terrapin | VK-00 | A | Quantum Drive | 1.6 | 0.005 | 320.0 | 210 |
| 40 | Anvil Terrapin | Vulcan | D | Quantum Drive | 1.6 | 0.005 | 320.0 | 197 |
| 41 | Anvil Terrapin | Wayfare | D | Quantum Drive | 1.6 | 0.005 | 320.0 | 170 |
| 42 | Anvil Terrapin | Expedition | C | Quantum Drive | 1.6 | 0.005 | 320.0 | 189 |
| 43 | Anvil Terrapin | Rush | C | Quantum Drive | 1.6 | 0.005 | 320.0 | 209 |
| 44 | MISC Hull A | Spectre | A | Quantum Drive | 1.2 | 0.004 | 300.0 | 218 |
| 45 | MISC Hull A | Zephyr | B | Quantum Drive | 1.2 | 0.004 | 300.0 | 184 |
| 46 | MISC Hull A | Drift | C | Quantum Drive | 1.2 | 0.004 | 300.0 | 167 |
| 47 | Anvil Terrapin Medic | Goliath | C | Quantum Drive | 1.4 | 0.005 | 280.0 | 219 |
| 48 | Anvil Terrapin Medic | Siren | B | Quantum Drive | 1.4 | 0.005 | 280.0 | 178 |
| 49 | Anvil Terrapin Medic | Voyage | B | Quantum Drive | 1.4 | 0.005 | 280.0 | 208 |
| 50 | Anvil Terrapin Medic | Eos ★ | C | Quantum Drive | 1.4 | 0.005 | 280.0 | 199 |
| 51 | Anvil Terrapin Medic | Flood | D | Quantum Drive | 1.4 | 0.005 | 280.0 | 188 |
| 52 | Anvil Terrapin Medic | LightFire | C | Quantum Drive | 1.4 | 0.005 | 280.0 | 239 |
| 53 | Anvil Terrapin Medic | Hyperion | B | Quantum Drive | 1.4 | 0.005 | 280.0 | 219 |
| 54 | Anvil Terrapin Medic | Atlas | A | Quantum Drive | 1.4 | 0.005 | 280.0 | 259 |
| 55 | Anvil Terrapin Medic | FoxFire | B | Quantum Drive | 1.4 | 0.005 | 280.0 | 263 |
| 56 | Anvil Terrapin Medic | Burst | B | Quantum Drive | 1.4 | 0.005 | 280.0 | 230 |
| 57 | Anvil Terrapin Medic | Beacon | C | Quantum Drive | 1.4 | 0.005 | 280.0 | 161 |
| 58 | Anvil Terrapin Medic | Colossus | B | Quantum Drive | 1.4 | 0.005 | 280.0 | 241 |
| 59 | Anvil Terrapin Medic | VK-00 | A | Quantum Drive | 1.4 | 0.005 | 280.0 | 210 |
| 60 | Anvil Terrapin Medic | Vulcan | D | Quantum Drive | 1.4 | 0.005 | 280.0 | 197 |
| 61 | Anvil Terrapin Medic | Wayfare | D | Quantum Drive | 1.4 | 0.005 | 280.0 | 170 |
| 62 | Anvil Terrapin Medic | Expedition | C | Quantum Drive | 1.4 | 0.005 | 280.0 | 189 |
| 63 | Anvil Terrapin Medic | Rush | C | Quantum Drive | 1.4 | 0.005 | 280.0 | 209 |
| 64 | Anvil Gladiator | Spectre | A | Quantum Drive | 1.1 | 0.004 | 275.0 | 218 |
| 65 | Anvil Gladiator | Zephyr | B | Quantum Drive | 1.1 | 0.004 | 275.0 | 184 |
| 66 | Anvil Gladiator | Drift | C | Quantum Drive | 1.1 | 0.004 | 275.0 | 167 |
| 67 | Banu Defender | Spectre | A | Quantum Drive | 1.1 | 0.004 | 275.0 | 218 |
| 68 | Banu Defender | Zephyr | B | Quantum Drive | 1.1 | 0.004 | 275.0 | 184 |
| 69 | Banu Defender | Drift | C | Quantum Drive | 1.1 | 0.004 | 275.0 | 167 |
| 70 | Drake Golem OX | Spectre | A | Quantum Drive | 1.1 | 0.004 | 275.0 | 218 |
| 71 | Drake Golem OX | Zephyr | B | Quantum Drive | 1.1 | 0.004 | 275.0 | 184 |
| 72 | Drake Golem OX | Drift | C | Quantum Drive | 1.1 | 0.004 | 275.0 | 167 |
| 73 | C.O. Nomad | Spectre | A | Quantum Drive | 1 | 0.004 | 250.0 | 218 |
| 74 | C.O. Nomad | Zephyr | B | Quantum Drive | 1 | 0.004 | 250.0 | 184 |
| 75 | C.O. Nomad | Drift | C | Quantum Drive | 1 | 0.004 | 250.0 | 167 |
| 76 | Drake Clipper | Spectre | A | Quantum Drive | 1 | 0.004 | 250.0 | 218 |
| 77 | Drake Clipper | Zephyr | B | Quantum Drive | 1 | 0.004 | 250.0 | 184 |
| 78 | Drake Clipper | Drift | C | Quantum Drive | 1 | 0.004 | 250.0 | 167 |
| 79 | Drake Golem | Spectre | A | Quantum Drive | 1 | 0.004 | 250.0 | 218 |
| 80 | Drake Golem | Zephyr | B | Quantum Drive | 1 | 0.004 | 250.0 | 184 |
| 81 | Drake Golem | Drift | C | Quantum Drive | 1 | 0.004 | 250.0 | 167 |
| 82 | Drake Herald | Spectre | A | Quantum Drive | 1 | 0.004 | 250.0 | 218 |
| 83 | Drake Herald | Zephyr | B | Quantum Drive | 1 | 0.004 | 250.0 | 184 |
| 84 | Drake Herald | Drift | C | Quantum Drive | 1 | 0.004 | 250.0 | 167 |
| 85 | MISC Hull A | Goliath ★ | C | Quantum Drive | 1.2 | 0.005 | 240.0 | 219 |
| 86 | MISC Hull A | Siren | B | Quantum Drive | 1.2 | 0.005 | 240.0 | 178 |
| 87 | MISC Hull A | Voyage | B | Quantum Drive | 1.2 | 0.005 | 240.0 | 208 |
| 88 | MISC Hull A | Eos | C | Quantum Drive | 1.2 | 0.005 | 240.0 | 199 |
| 89 | MISC Hull A | Flood | D | Quantum Drive | 1.2 | 0.005 | 240.0 | 188 |
| 90 | MISC Hull A | LightFire | C | Quantum Drive | 1.2 | 0.005 | 240.0 | 239 |
| 91 | MISC Hull A | Hyperion | B | Quantum Drive | 1.2 | 0.005 | 240.0 | 219 |
| 92 | MISC Hull A | Atlas | A | Quantum Drive | 1.2 | 0.005 | 240.0 | 259 |
| 93 | MISC Hull A | FoxFire | B | Quantum Drive | 1.2 | 0.005 | 240.0 | 263 |
| 94 | MISC Hull A | Burst | B | Quantum Drive | 1.2 | 0.005 | 240.0 | 230 |
| 95 | MISC Hull A | Beacon | C | Quantum Drive | 1.2 | 0.005 | 240.0 | 161 |
| 96 | MISC Hull A | Colossus | B | Quantum Drive | 1.2 | 0.005 | 240.0 | 241 |
| 97 | MISC Hull A | VK-00 | A | Quantum Drive | 1.2 | 0.005 | 240.0 | 210 |
| 98 | MISC Hull A | Vulcan | D | Quantum Drive | 1.2 | 0.005 | 240.0 | 197 |
| 99 | MISC Hull A | Wayfare | D | Quantum Drive | 1.2 | 0.005 | 240.0 | 170 |
| 100 | MISC Hull A | Expedition | C | Quantum Drive | 1.2 | 0.005 | 240.0 | 189 |
| 101 | MISC Hull A | Rush | C | Quantum Drive | 1.2 | 0.005 | 240.0 | 209 |
| 102 | Aegis Eclipse | Spectre | A | Quantum Drive | 0.9 | 0.004 | 225.0 | 218 |
| 103 | Aegis Eclipse | Zephyr | B | Quantum Drive | 0.9 | 0.004 | 225.0 | 184 |
| 104 | Aegis Eclipse | Drift ★ | C | Quantum Drive | 0.9 | 0.004 | 225.0 | 167 |
| 105 | Aegis Sabre | Spectre | A | Quantum Drive | 0.9 | 0.004 | 225.0 | 218 |
| 106 | Aegis Sabre | Zephyr | B | Quantum Drive | 0.9 | 0.004 | 225.0 | 184 |
| 107 | Aegis Sabre | Drift ★ | C | Quantum Drive | 0.9 | 0.004 | 225.0 | 167 |
| 108 | Aegis Sabre Comet | Spectre | A | Quantum Drive | 0.9 | 0.004 | 225.0 | 218 |
| 109 | Aegis Sabre Comet | Zephyr | B | Quantum Drive | 0.9 | 0.004 | 225.0 | 184 |
| 110 | Aegis Sabre Comet | Drift ★ | C | Quantum Drive | 0.9 | 0.004 | 225.0 | 167 |
| 111 | Aegis Sabre Firebird | Spectre | A | Quantum Drive | 0.9 | 0.004 | 225.0 | 218 |
| 112 | Aegis Sabre Firebird | Zephyr | B | Quantum Drive | 0.9 | 0.004 | 225.0 | 184 |
| 113 | Aegis Sabre Firebird | Drift ★ | C | Quantum Drive | 0.9 | 0.004 | 225.0 | 167 |
| 114 | Aegis Sabre Peregrine | Spectre | A | Quantum Drive | 0.9 | 0.004 | 225.0 | 218 |
| 115 | Aegis Sabre Peregrine | Zephyr | B | Quantum Drive | 0.9 | 0.004 | 225.0 | 184 |
| 116 | Aegis Sabre Peregrine | Drift ★ | C | Quantum Drive | 0.9 | 0.004 | 225.0 | 167 |
| 117 | RSI Mantis | Spectre | A | Quantum Drive | 0.9 | 0.004 | 225.0 | 218 |
| 118 | RSI Mantis | Zephyr | B | Quantum Drive | 0.9 | 0.004 | 225.0 | 184 |
| 119 | RSI Mantis | Drift | C | Quantum Drive | 0.9 | 0.004 | 225.0 | 167 |
| 120 | RSI Meteor | Spectre | A | Quantum Drive | 0.9 | 0.004 | 225.0 | 218 |
| 121 | RSI Meteor | Zephyr | B | Quantum Drive | 0.9 | 0.004 | 225.0 | 184 |
| 122 | RSI Meteor | Drift | C | Quantum Drive | 0.9 | 0.004 | 225.0 | 167 |
| 123 | RSI Scorpius | Spectre | A | Quantum Drive | 0.9 | 0.004 | 225.0 | 218 |
| 124 | RSI Scorpius | Zephyr | B | Quantum Drive | 0.9 | 0.004 | 225.0 | 184 |
| 125 | RSI Scorpius | Drift | C | Quantum Drive | 0.9 | 0.004 | 225.0 | 167 |
| 126 | RSI Scorpius Antares | Spectre | A | Quantum Drive | 0.9 | 0.004 | 225.0 | 218 |
| 127 | RSI Scorpius Antares | Zephyr | B | Quantum Drive | 0.9 | 0.004 | 225.0 | 184 |
| 128 | RSI Scorpius Antares | Drift | C | Quantum Drive | 0.9 | 0.004 | 225.0 | 167 |
| 129 | Anvil C8 Pisces | Spectre | A | Quantum Drive | 0.9 | 0.004 | 225.0 | 218 |
| 130 | Anvil C8 Pisces | Zephyr | B | Quantum Drive | 0.9 | 0.004 | 225.0 | 184 |
| 131 | Anvil C8 Pisces | Drift | C | Quantum Drive | 0.9 | 0.004 | 225.0 | 167 |
| 132 | Anvil C8R Pisces Rescue | Spectre | A | Quantum Drive | 0.9 | 0.004 | 225.0 | 218 |
| 133 | Anvil C8R Pisces Rescue | Zephyr | B | Quantum Drive | 0.9 | 0.004 | 225.0 | 184 |
| 134 | Anvil C8R Pisces Rescue | Drift | C | Quantum Drive | 0.9 | 0.004 | 225.0 | 167 |
| 135 | Anvil C8X Pisces Expedition | Spectre | A | Quantum Drive | 0.9 | 0.004 | 225.0 | 218 |
| 136 | Anvil C8X Pisces Expedition | Zephyr | B | Quantum Drive | 0.9 | 0.004 | 225.0 | 184 |
| 137 | Anvil C8X Pisces Expedition | Drift | C | Quantum Drive | 0.9 | 0.004 | 225.0 | 167 |
| 138 | Anvil F7C Hornet Mk II | Spectre | A | Quantum Drive | 0.9 | 0.004 | 225.0 | 218 |
| 139 | Anvil F7C Hornet Mk II | Zephyr | B | Quantum Drive | 0.9 | 0.004 | 225.0 | 184 |
| 140 | Anvil F7C Hornet Mk II | Drift | C | Quantum Drive | 0.9 | 0.004 | 225.0 | 167 |
| 141 | Anvil F7C-R Hornet Tracker Mk II | Spectre | A | Quantum Drive | 0.9 | 0.004 | 225.0 | 218 |
| 142 | Anvil F7C-R Hornet Tracker Mk II | Zephyr | B | Quantum Drive | 0.9 | 0.004 | 225.0 | 184 |
| 143 | Anvil F7C-R Hornet Tracker Mk II | Drift | C | Quantum Drive | 0.9 | 0.004 | 225.0 | 167 |
| 144 | Anvil F7C-S Hornet Ghost Mk II | Spectre | A | Quantum Drive | 0.9 | 0.004 | 225.0 | 218 |
| 145 | Anvil F7C-S Hornet Ghost Mk II | Zephyr | B | Quantum Drive | 0.9 | 0.004 | 225.0 | 184 |
| 146 | Anvil F7C-S Hornet Ghost Mk II | Drift ★ | C | Quantum Drive | 0.9 | 0.004 | 225.0 | 167 |
| 147 | Anvil Hurricane | Spectre | A | Quantum Drive | 0.9 | 0.004 | 225.0 | 218 |
| 148 | Anvil Hurricane | Zephyr | B | Quantum Drive | 0.9 | 0.004 | 225.0 | 184 |
| 149 | Anvil Hurricane | Drift | C | Quantum Drive | 0.9 | 0.004 | 225.0 | 167 |
| 150 | Aopoa San'tok.yāi | Spectre | A | Quantum Drive | 0.9 | 0.004 | 225.0 | 218 |
| 151 | Aopoa San'tok.yāi | Zephyr | B | Quantum Drive | 0.9 | 0.004 | 225.0 | 184 |
| 152 | Aopoa San'tok.yāi | Drift | C | Quantum Drive | 0.9 | 0.004 | 225.0 | 167 |
| 153 | Crusader Intrepid | Spectre | A | Quantum Drive | 0.9 | 0.004 | 225.0 | 218 |
| 154 | Crusader Intrepid | Zephyr | B | Quantum Drive | 0.9 | 0.004 | 225.0 | 184 |
| 155 | Crusader Intrepid | Drift | C | Quantum Drive | 0.9 | 0.004 | 225.0 | 167 |
| 156 | Drake Vulture | Spectre | A | Quantum Drive | 0.9 | 0.004 | 225.0 | 218 |
| 157 | Drake Vulture | Zephyr | B | Quantum Drive | 0.9 | 0.004 | 225.0 | 184 |
| 158 | Drake Vulture | Drift | C | Quantum Drive | 0.9 | 0.004 | 225.0 | 167 |
| 159 | Gatac Syulen | Spectre | A | Quantum Drive | 0.9 | 0.004 | 225.0 | 218 |
| 160 | Gatac Syulen | Zephyr | B | Quantum Drive | 0.9 | 0.004 | 225.0 | 184 |
| 161 | Gatac Syulen | Drift | C | Quantum Drive | 0.9 | 0.004 | 225.0 | 167 |
| 162 | MISC Fortune | Spectre | A | Quantum Drive | 0.9 | 0.004 | 225.0 | 218 |
| 163 | MISC Fortune | Zephyr | B | Quantum Drive | 0.9 | 0.004 | 225.0 | 184 |
| 164 | MISC Fortune | Drift | C | Quantum Drive | 0.9 | 0.004 | 225.0 | 167 |
| 165 | MISC Prospector | Spectre | A | Quantum Drive | 0.9 | 0.004 | 225.0 | 218 |
| 166 | MISC Prospector | Zephyr | B | Quantum Drive | 0.9 | 0.004 | 225.0 | 184 |
| 167 | MISC Prospector | Drift | C | Quantum Drive | 0.9 | 0.004 | 225.0 | 167 |
| 168 | Origin 100i | Spectre | A | Quantum Drive | 0.9 | 0.004 | 225.0 | 218 |
| 169 | Origin 100i | Zephyr | B | Quantum Drive | 0.9 | 0.004 | 225.0 | 184 |
| 170 | Origin 100i | Drift | C | Quantum Drive | 0.9 | 0.004 | 225.0 | 167 |
| 171 | Origin 125a | Spectre | A | Quantum Drive | 0.9 | 0.004 | 225.0 | 218 |
| 172 | Origin 125a | Zephyr | B | Quantum Drive | 0.9 | 0.004 | 225.0 | 184 |
| 173 | Origin 125a | Drift | C | Quantum Drive | 0.9 | 0.004 | 225.0 | 167 |
| 174 | Origin 135c | Spectre | A | Quantum Drive | 0.9 | 0.004 | 225.0 | 218 |
| 175 | Origin 135c | Zephyr | B | Quantum Drive | 0.9 | 0.004 | 225.0 | 184 |
| 176 | Origin 135c | Drift | C | Quantum Drive | 0.9 | 0.004 | 225.0 | 167 |
| 177 | Origin 315p | Spectre | A | Quantum Drive | 0.9 | 0.004 | 225.0 | 218 |
| 178 | Origin 315p | Zephyr | B | Quantum Drive | 0.9 | 0.004 | 225.0 | 184 |
| 179 | Origin 315p | Drift | C | Quantum Drive | 0.9 | 0.004 | 225.0 | 167 |
| 180 | RSI Aurora Mk II | Spectre | A | Quantum Drive | 0.9 | 0.004 | 225.0 | 218 |
| 181 | RSI Aurora Mk II | Zephyr | B | Quantum Drive | 0.9 | 0.004 | 225.0 | 184 |
| 182 | RSI Aurora Mk II | Drift | C | Quantum Drive | 0.9 | 0.004 | 225.0 | 167 |
| 183 | Anvil Gladiator | Goliath | C | Quantum Drive | 1.1 | 0.005 | 220.0 | 219 |
| 184 | Anvil Gladiator | Siren | B | Quantum Drive | 1.1 | 0.005 | 220.0 | 178 |
| 185 | Anvil Gladiator | Voyage | B | Quantum Drive | 1.1 | 0.005 | 220.0 | 208 |
| 186 | Anvil Gladiator | Eos | C | Quantum Drive | 1.1 | 0.005 | 220.0 | 199 |
| 187 | Anvil Gladiator | Flood | D | Quantum Drive | 1.1 | 0.005 | 220.0 | 188 |
| 188 | Anvil Gladiator | LightFire | C | Quantum Drive | 1.1 | 0.005 | 220.0 | 239 |
| 189 | Anvil Gladiator | Hyperion | B | Quantum Drive | 1.1 | 0.005 | 220.0 | 219 |
| 190 | Anvil Gladiator | Atlas | A | Quantum Drive | 1.1 | 0.005 | 220.0 | 259 |
| 191 | Anvil Gladiator | FoxFire | B | Quantum Drive | 1.1 | 0.005 | 220.0 | 263 |
| 192 | Anvil Gladiator | Burst | B | Quantum Drive | 1.1 | 0.005 | 220.0 | 230 |
| 193 | Anvil Gladiator | Beacon ★ | C | Quantum Drive | 1.1 | 0.005 | 220.0 | 161 |
| 194 | Anvil Gladiator | Colossus | B | Quantum Drive | 1.1 | 0.005 | 220.0 | 241 |
| 195 | Anvil Gladiator | VK-00 | A | Quantum Drive | 1.1 | 0.005 | 220.0 | 210 |
| 196 | Anvil Gladiator | Vulcan | D | Quantum Drive | 1.1 | 0.005 | 220.0 | 197 |
| 197 | Anvil Gladiator | Wayfare | D | Quantum Drive | 1.1 | 0.005 | 220.0 | 170 |
| 198 | Anvil Gladiator | Expedition | C | Quantum Drive | 1.1 | 0.005 | 220.0 | 189 |
| 199 | Anvil Gladiator | Rush | C | Quantum Drive | 1.1 | 0.005 | 220.0 | 209 |
| 200 | Banu Defender | Goliath | C | Quantum Drive | 1.1 | 0.005 | 220.0 | 219 |
| 201 | Banu Defender | Siren | B | Quantum Drive | 1.1 | 0.005 | 220.0 | 178 |
| 202 | Banu Defender | Voyage | B | Quantum Drive | 1.1 | 0.005 | 220.0 | 208 |
| 203 | Banu Defender | Eos | C | Quantum Drive | 1.1 | 0.005 | 220.0 | 199 |
| 204 | Banu Defender | Flood | D | Quantum Drive | 1.1 | 0.005 | 220.0 | 188 |
| 205 | Banu Defender | LightFire | C | Quantum Drive | 1.1 | 0.005 | 220.0 | 239 |
| 206 | Banu Defender | Hyperion | B | Quantum Drive | 1.1 | 0.005 | 220.0 | 219 |
| 207 | Banu Defender | Atlas | A | Quantum Drive | 1.1 | 0.005 | 220.0 | 259 |
| 208 | Banu Defender | FoxFire | B | Quantum Drive | 1.1 | 0.005 | 220.0 | 263 |
| 209 | Banu Defender | Burst | B | Quantum Drive | 1.1 | 0.005 | 220.0 | 230 |
| 210 | Banu Defender | Beacon ★ | C | Quantum Drive | 1.1 | 0.005 | 220.0 | 161 |
| 211 | Banu Defender | Colossus | B | Quantum Drive | 1.1 | 0.005 | 220.0 | 241 |
| 212 | Banu Defender | VK-00 | A | Quantum Drive | 1.1 | 0.005 | 220.0 | 210 |
| 213 | Banu Defender | Vulcan | D | Quantum Drive | 1.1 | 0.005 | 220.0 | 197 |
| 214 | Banu Defender | Wayfare | D | Quantum Drive | 1.1 | 0.005 | 220.0 | 170 |
| 215 | Banu Defender | Expedition | C | Quantum Drive | 1.1 | 0.005 | 220.0 | 189 |
| 216 | Banu Defender | Rush | C | Quantum Drive | 1.1 | 0.005 | 220.0 | 209 |
| 217 | Drake Golem OX | Goliath ★ | C | Quantum Drive | 1.1 | 0.005 | 220.0 | 219 |
| 218 | Drake Golem OX | Siren | B | Quantum Drive | 1.1 | 0.005 | 220.0 | 178 |
| 219 | Drake Golem OX | Voyage | B | Quantum Drive | 1.1 | 0.005 | 220.0 | 208 |
| 220 | Drake Golem OX | Eos | C | Quantum Drive | 1.1 | 0.005 | 220.0 | 199 |
| 221 | Drake Golem OX | Flood | D | Quantum Drive | 1.1 | 0.005 | 220.0 | 188 |
| 222 | Drake Golem OX | LightFire | C | Quantum Drive | 1.1 | 0.005 | 220.0 | 239 |
| 223 | Drake Golem OX | Hyperion | B | Quantum Drive | 1.1 | 0.005 | 220.0 | 219 |
| 224 | Drake Golem OX | Atlas | A | Quantum Drive | 1.1 | 0.005 | 220.0 | 259 |
| 225 | Drake Golem OX | FoxFire | B | Quantum Drive | 1.1 | 0.005 | 220.0 | 263 |
| 226 | Drake Golem OX | Burst | B | Quantum Drive | 1.1 | 0.005 | 220.0 | 230 |
| 227 | Drake Golem OX | Beacon | C | Quantum Drive | 1.1 | 0.005 | 220.0 | 161 |
| 228 | Drake Golem OX | Colossus | B | Quantum Drive | 1.1 | 0.005 | 220.0 | 241 |
| 229 | Drake Golem OX | VK-00 | A | Quantum Drive | 1.1 | 0.005 | 220.0 | 210 |
| 230 | Drake Golem OX | Vulcan | D | Quantum Drive | 1.1 | 0.005 | 220.0 | 197 |
| 231 | Drake Golem OX | Wayfare | D | Quantum Drive | 1.1 | 0.005 | 220.0 | 170 |
| 232 | Drake Golem OX | Expedition | C | Quantum Drive | 1.1 | 0.005 | 220.0 | 189 |
| 233 | Drake Golem OX | Rush | C | Quantum Drive | 1.1 | 0.005 | 220.0 | 209 |
| 234 | RSI Salvation | Spectre | A | Quantum Drive | 0.8 | 0.004 | 200.0 | 218 |
| 235 | RSI Salvation | Zephyr | B | Quantum Drive | 0.8 | 0.004 | 200.0 | 184 |
| 236 | RSI Salvation | Drift | C | Quantum Drive | 0.8 | 0.004 | 200.0 | 167 |
| 237 | C.O. Nomad | Goliath | C | Quantum Drive | 1 | 0.005 | 200.0 | 219 |
| 238 | C.O. Nomad | Siren | B | Quantum Drive | 1 | 0.005 | 200.0 | 178 |
| 239 | C.O. Nomad | Voyage | B | Quantum Drive | 1 | 0.005 | 200.0 | 208 |
| 240 | C.O. Nomad | Eos | C | Quantum Drive | 1 | 0.005 | 200.0 | 199 |
| 241 | C.O. Nomad | Flood | D | Quantum Drive | 1 | 0.005 | 200.0 | 188 |
| 242 | C.O. Nomad | LightFire | C | Quantum Drive | 1 | 0.005 | 200.0 | 239 |
| 243 | C.O. Nomad | Hyperion | B | Quantum Drive | 1 | 0.005 | 200.0 | 219 |
| 244 | C.O. Nomad | Atlas | A | Quantum Drive | 1 | 0.005 | 200.0 | 259 |
| 245 | C.O. Nomad | FoxFire | B | Quantum Drive | 1 | 0.005 | 200.0 | 263 |
| 246 | C.O. Nomad | Burst | B | Quantum Drive | 1 | 0.005 | 200.0 | 230 |
| 247 | C.O. Nomad | Beacon | C | Quantum Drive | 1 | 0.005 | 200.0 | 161 |
| 248 | C.O. Nomad | Colossus | B | Quantum Drive | 1 | 0.005 | 200.0 | 241 |
| 249 | C.O. Nomad | VK-00 | A | Quantum Drive | 1 | 0.005 | 200.0 | 210 |
| 250 | C.O. Nomad | Vulcan | D | Quantum Drive | 1 | 0.005 | 200.0 | 197 |
| 251 | C.O. Nomad | Wayfare | D | Quantum Drive | 1 | 0.005 | 200.0 | 170 |
| 252 | C.O. Nomad | Expedition ★ | C | Quantum Drive | 1 | 0.005 | 200.0 | 189 |
| 253 | C.O. Nomad | Rush | C | Quantum Drive | 1 | 0.005 | 200.0 | 209 |
| 254 | Drake Clipper | Goliath | C | Quantum Drive | 1 | 0.005 | 200.0 | 219 |
| 255 | Drake Clipper | Siren | B | Quantum Drive | 1 | 0.005 | 200.0 | 178 |
| 256 | Drake Clipper | Voyage | B | Quantum Drive | 1 | 0.005 | 200.0 | 208 |
| 257 | Drake Clipper | Eos | C | Quantum Drive | 1 | 0.005 | 200.0 | 199 |
| 258 | Drake Clipper | Flood ★ | D | Quantum Drive | 1 | 0.005 | 200.0 | 188 |
| 259 | Drake Clipper | LightFire | C | Quantum Drive | 1 | 0.005 | 200.0 | 239 |
| 260 | Drake Clipper | Hyperion | B | Quantum Drive | 1 | 0.005 | 200.0 | 219 |
| 261 | Drake Clipper | Atlas | A | Quantum Drive | 1 | 0.005 | 200.0 | 259 |
| 262 | Drake Clipper | FoxFire | B | Quantum Drive | 1 | 0.005 | 200.0 | 263 |
| 263 | Drake Clipper | Burst | B | Quantum Drive | 1 | 0.005 | 200.0 | 230 |
| 264 | Drake Clipper | Beacon | C | Quantum Drive | 1 | 0.005 | 200.0 | 161 |
| 265 | Drake Clipper | Colossus | B | Quantum Drive | 1 | 0.005 | 200.0 | 241 |
| 266 | Drake Clipper | VK-00 | A | Quantum Drive | 1 | 0.005 | 200.0 | 210 |
| 267 | Drake Clipper | Vulcan | D | Quantum Drive | 1 | 0.005 | 200.0 | 197 |
| 268 | Drake Clipper | Wayfare | D | Quantum Drive | 1 | 0.005 | 200.0 | 170 |
| 269 | Drake Clipper | Expedition | C | Quantum Drive | 1 | 0.005 | 200.0 | 189 |
| 270 | Drake Clipper | Rush | C | Quantum Drive | 1 | 0.005 | 200.0 | 209 |
| 271 | Drake Cutter | Spectre | A | Quantum Drive | 0.8 | 0.004 | 200.0 | 218 |
| 272 | Drake Cutter | Zephyr | B | Quantum Drive | 0.8 | 0.004 | 200.0 | 184 |
| 273 | Drake Cutter | Drift | C | Quantum Drive | 0.8 | 0.004 | 200.0 | 167 |
| 274 | Drake Cutter Scout | Spectre | A | Quantum Drive | 0.8 | 0.004 | 200.0 | 218 |
| 275 | Drake Cutter Scout | Zephyr | B | Quantum Drive | 0.8 | 0.004 | 200.0 | 184 |
| 276 | Drake Cutter Scout | Drift | C | Quantum Drive | 0.8 | 0.004 | 200.0 | 167 |
| 277 | Drake Golem | Goliath ★ | C | Quantum Drive | 1 | 0.005 | 200.0 | 219 |
| 278 | Drake Golem | Siren | B | Quantum Drive | 1 | 0.005 | 200.0 | 178 |
| 279 | Drake Golem | Voyage | B | Quantum Drive | 1 | 0.005 | 200.0 | 208 |
| 280 | Drake Golem | Eos | C | Quantum Drive | 1 | 0.005 | 200.0 | 199 |
| 281 | Drake Golem | Flood | D | Quantum Drive | 1 | 0.005 | 200.0 | 188 |
| 282 | Drake Golem | LightFire | C | Quantum Drive | 1 | 0.005 | 200.0 | 239 |
| 283 | Drake Golem | Hyperion | B | Quantum Drive | 1 | 0.005 | 200.0 | 219 |
| 284 | Drake Golem | Atlas | A | Quantum Drive | 1 | 0.005 | 200.0 | 259 |
| 285 | Drake Golem | FoxFire | B | Quantum Drive | 1 | 0.005 | 200.0 | 263 |
| 286 | Drake Golem | Burst | B | Quantum Drive | 1 | 0.005 | 200.0 | 230 |
| 287 | Drake Golem | Beacon | C | Quantum Drive | 1 | 0.005 | 200.0 | 161 |
| 288 | Drake Golem | Colossus | B | Quantum Drive | 1 | 0.005 | 200.0 | 241 |
| 289 | Drake Golem | VK-00 | A | Quantum Drive | 1 | 0.005 | 200.0 | 210 |
| 290 | Drake Golem | Vulcan | D | Quantum Drive | 1 | 0.005 | 200.0 | 197 |
| 291 | Drake Golem | Wayfare | D | Quantum Drive | 1 | 0.005 | 200.0 | 170 |
| 292 | Drake Golem | Expedition | C | Quantum Drive | 1 | 0.005 | 200.0 | 189 |
| 293 | Drake Golem | Rush | C | Quantum Drive | 1 | 0.005 | 200.0 | 209 |
| 294 | Drake Herald | Goliath | C | Quantum Drive | 1 | 0.005 | 200.0 | 219 |
| 295 | Drake Herald | Siren | B | Quantum Drive | 1 | 0.005 | 200.0 | 178 |
| 296 | Drake Herald | Voyage | B | Quantum Drive | 1 | 0.005 | 200.0 | 208 |
| 297 | Drake Herald | Eos | C | Quantum Drive | 1 | 0.005 | 200.0 | 199 |
| 298 | Drake Herald | Flood | D | Quantum Drive | 1 | 0.005 | 200.0 | 188 |
| 299 | Drake Herald | LightFire | C | Quantum Drive | 1 | 0.005 | 200.0 | 239 |
| 300 | Drake Herald | Hyperion | B | Quantum Drive | 1 | 0.005 | 200.0 | 219 |
| 301 | Drake Herald | Atlas | A | Quantum Drive | 1 | 0.005 | 200.0 | 259 |
| 302 | Drake Herald | FoxFire | B | Quantum Drive | 1 | 0.005 | 200.0 | 263 |
| 303 | Drake Herald | Burst | B | Quantum Drive | 1 | 0.005 | 200.0 | 230 |
| 304 | Drake Herald | Beacon | C | Quantum Drive | 1 | 0.005 | 200.0 | 161 |
| 305 | Drake Herald | Colossus | B | Quantum Drive | 1 | 0.005 | 200.0 | 241 |
| 306 | Drake Herald | VK-00 | A | Quantum Drive | 1 | 0.005 | 200.0 | 210 |
| 307 | Drake Herald | Vulcan | D | Quantum Drive | 1 | 0.005 | 200.0 | 197 |
| 308 | Drake Herald | Wayfare | D | Quantum Drive | 1 | 0.005 | 200.0 | 170 |
| 309 | Drake Herald | Expedition ★ | C | Quantum Drive | 1 | 0.005 | 200.0 | 189 |
| 310 | Drake Herald | Rush | C | Quantum Drive | 1 | 0.005 | 200.0 | 209 |
| 311 | MISC Reliant Sen | Spectre | A | Quantum Drive | 0.8 | 0.004 | 200.0 | 218 |
| 312 | MISC Reliant Sen | Zephyr | B | Quantum Drive | 0.8 | 0.004 | 200.0 | 184 |
| 313 | MISC Reliant Sen | Drift | C | Quantum Drive | 0.8 | 0.004 | 200.0 | 167 |
| 314 | Aegis Eclipse | Goliath | C | Quantum Drive | 0.9 | 0.005 | 180.0 | 219 |
| 315 | Aegis Eclipse | Siren | B | Quantum Drive | 0.9 | 0.005 | 180.0 | 178 |
| 316 | Aegis Eclipse | Voyage | B | Quantum Drive | 0.9 | 0.005 | 180.0 | 208 |
| 317 | Aegis Eclipse | Eos | C | Quantum Drive | 0.9 | 0.005 | 180.0 | 199 |
| 318 | Aegis Eclipse | Flood | D | Quantum Drive | 0.9 | 0.005 | 180.0 | 188 |
| 319 | Aegis Eclipse | LightFire | C | Quantum Drive | 0.9 | 0.005 | 180.0 | 239 |
| 320 | Aegis Eclipse | Hyperion | B | Quantum Drive | 0.9 | 0.005 | 180.0 | 219 |
| 321 | Aegis Eclipse | Atlas | A | Quantum Drive | 0.9 | 0.005 | 180.0 | 259 |
| 322 | Aegis Eclipse | FoxFire | B | Quantum Drive | 0.9 | 0.005 | 180.0 | 263 |
| 323 | Aegis Eclipse | Burst | B | Quantum Drive | 0.9 | 0.005 | 180.0 | 230 |
| 324 | Aegis Eclipse | Beacon | C | Quantum Drive | 0.9 | 0.005 | 180.0 | 161 |
| 325 | Aegis Eclipse | Colossus | B | Quantum Drive | 0.9 | 0.005 | 180.0 | 241 |
| 326 | Aegis Eclipse | VK-00 | A | Quantum Drive | 0.9 | 0.005 | 180.0 | 210 |
| 327 | Aegis Eclipse | Vulcan | D | Quantum Drive | 0.9 | 0.005 | 180.0 | 197 |
| 328 | Aegis Eclipse | Wayfare | D | Quantum Drive | 0.9 | 0.005 | 180.0 | 170 |
| 329 | Aegis Eclipse | Expedition | C | Quantum Drive | 0.9 | 0.005 | 180.0 | 189 |
| 330 | Aegis Eclipse | Rush | C | Quantum Drive | 0.9 | 0.005 | 180.0 | 209 |
| 331 | Aegis Sabre | Goliath | C | Quantum Drive | 0.9 | 0.005 | 180.0 | 219 |
| 332 | Aegis Sabre | Siren | B | Quantum Drive | 0.9 | 0.005 | 180.0 | 178 |
| 333 | Aegis Sabre | Voyage | B | Quantum Drive | 0.9 | 0.005 | 180.0 | 208 |
| 334 | Aegis Sabre | Eos | C | Quantum Drive | 0.9 | 0.005 | 180.0 | 199 |
| 335 | Aegis Sabre | Flood | D | Quantum Drive | 0.9 | 0.005 | 180.0 | 188 |
| 336 | Aegis Sabre | LightFire | C | Quantum Drive | 0.9 | 0.005 | 180.0 | 239 |
| 337 | Aegis Sabre | Hyperion | B | Quantum Drive | 0.9 | 0.005 | 180.0 | 219 |
| 338 | Aegis Sabre | Atlas | A | Quantum Drive | 0.9 | 0.005 | 180.0 | 259 |
| 339 | Aegis Sabre | FoxFire | B | Quantum Drive | 0.9 | 0.005 | 180.0 | 263 |
| 340 | Aegis Sabre | Burst | B | Quantum Drive | 0.9 | 0.005 | 180.0 | 230 |
| 341 | Aegis Sabre | Beacon | C | Quantum Drive | 0.9 | 0.005 | 180.0 | 161 |
| 342 | Aegis Sabre | Colossus | B | Quantum Drive | 0.9 | 0.005 | 180.0 | 241 |
| 343 | Aegis Sabre | VK-00 | A | Quantum Drive | 0.9 | 0.005 | 180.0 | 210 |
| 344 | Aegis Sabre | Vulcan | D | Quantum Drive | 0.9 | 0.005 | 180.0 | 197 |
| 345 | Aegis Sabre | Wayfare | D | Quantum Drive | 0.9 | 0.005 | 180.0 | 170 |
| 346 | Aegis Sabre | Expedition | C | Quantum Drive | 0.9 | 0.005 | 180.0 | 189 |
| 347 | Aegis Sabre | Rush | C | Quantum Drive | 0.9 | 0.005 | 180.0 | 209 |
| 348 | Aegis Sabre Comet | Goliath | C | Quantum Drive | 0.9 | 0.005 | 180.0 | 219 |
| 349 | Aegis Sabre Comet | Siren | B | Quantum Drive | 0.9 | 0.005 | 180.0 | 178 |
| 350 | Aegis Sabre Comet | Voyage | B | Quantum Drive | 0.9 | 0.005 | 180.0 | 208 |
| 351 | Aegis Sabre Comet | Eos | C | Quantum Drive | 0.9 | 0.005 | 180.0 | 199 |
| 352 | Aegis Sabre Comet | Flood | D | Quantum Drive | 0.9 | 0.005 | 180.0 | 188 |
| 353 | Aegis Sabre Comet | LightFire | C | Quantum Drive | 0.9 | 0.005 | 180.0 | 239 |
| 354 | Aegis Sabre Comet | Hyperion | B | Quantum Drive | 0.9 | 0.005 | 180.0 | 219 |
| 355 | Aegis Sabre Comet | Atlas | A | Quantum Drive | 0.9 | 0.005 | 180.0 | 259 |
| 356 | Aegis Sabre Comet | FoxFire | B | Quantum Drive | 0.9 | 0.005 | 180.0 | 263 |
| 357 | Aegis Sabre Comet | Burst | B | Quantum Drive | 0.9 | 0.005 | 180.0 | 230 |
| 358 | Aegis Sabre Comet | Beacon | C | Quantum Drive | 0.9 | 0.005 | 180.0 | 161 |
| 359 | Aegis Sabre Comet | Colossus | B | Quantum Drive | 0.9 | 0.005 | 180.0 | 241 |
| 360 | Aegis Sabre Comet | VK-00 | A | Quantum Drive | 0.9 | 0.005 | 180.0 | 210 |
| 361 | Aegis Sabre Comet | Vulcan | D | Quantum Drive | 0.9 | 0.005 | 180.0 | 197 |
| 362 | Aegis Sabre Comet | Wayfare | D | Quantum Drive | 0.9 | 0.005 | 180.0 | 170 |
| 363 | Aegis Sabre Comet | Expedition | C | Quantum Drive | 0.9 | 0.005 | 180.0 | 189 |
| 364 | Aegis Sabre Comet | Rush | C | Quantum Drive | 0.9 | 0.005 | 180.0 | 209 |
| 365 | Aegis Sabre Firebird | Goliath | C | Quantum Drive | 0.9 | 0.005 | 180.0 | 219 |
| 366 | Aegis Sabre Firebird | Siren | B | Quantum Drive | 0.9 | 0.005 | 180.0 | 178 |
| 367 | Aegis Sabre Firebird | Voyage | B | Quantum Drive | 0.9 | 0.005 | 180.0 | 208 |
| 368 | Aegis Sabre Firebird | Eos | C | Quantum Drive | 0.9 | 0.005 | 180.0 | 199 |
| 369 | Aegis Sabre Firebird | Flood | D | Quantum Drive | 0.9 | 0.005 | 180.0 | 188 |
| 370 | Aegis Sabre Firebird | LightFire | C | Quantum Drive | 0.9 | 0.005 | 180.0 | 239 |
| 371 | Aegis Sabre Firebird | Hyperion | B | Quantum Drive | 0.9 | 0.005 | 180.0 | 219 |
| 372 | Aegis Sabre Firebird | Atlas | A | Quantum Drive | 0.9 | 0.005 | 180.0 | 259 |
| 373 | Aegis Sabre Firebird | FoxFire | B | Quantum Drive | 0.9 | 0.005 | 180.0 | 263 |
| 374 | Aegis Sabre Firebird | Burst | B | Quantum Drive | 0.9 | 0.005 | 180.0 | 230 |
| 375 | Aegis Sabre Firebird | Beacon | C | Quantum Drive | 0.9 | 0.005 | 180.0 | 161 |
| 376 | Aegis Sabre Firebird | Colossus | B | Quantum Drive | 0.9 | 0.005 | 180.0 | 241 |
| 377 | Aegis Sabre Firebird | VK-00 | A | Quantum Drive | 0.9 | 0.005 | 180.0 | 210 |
| 378 | Aegis Sabre Firebird | Vulcan | D | Quantum Drive | 0.9 | 0.005 | 180.0 | 197 |
| 379 | Aegis Sabre Firebird | Wayfare | D | Quantum Drive | 0.9 | 0.005 | 180.0 | 170 |
| 380 | Aegis Sabre Firebird | Expedition | C | Quantum Drive | 0.9 | 0.005 | 180.0 | 189 |
| 381 | Aegis Sabre Firebird | Rush | C | Quantum Drive | 0.9 | 0.005 | 180.0 | 209 |
| 382 | Aegis Sabre Peregrine | Goliath | C | Quantum Drive | 0.9 | 0.005 | 180.0 | 219 |
| 383 | Aegis Sabre Peregrine | Siren | B | Quantum Drive | 0.9 | 0.005 | 180.0 | 178 |
| 384 | Aegis Sabre Peregrine | Voyage | B | Quantum Drive | 0.9 | 0.005 | 180.0 | 208 |
| 385 | Aegis Sabre Peregrine | Eos | C | Quantum Drive | 0.9 | 0.005 | 180.0 | 199 |
| 386 | Aegis Sabre Peregrine | Flood | D | Quantum Drive | 0.9 | 0.005 | 180.0 | 188 |
| 387 | Aegis Sabre Peregrine | LightFire | C | Quantum Drive | 0.9 | 0.005 | 180.0 | 239 |
| 388 | Aegis Sabre Peregrine | Hyperion | B | Quantum Drive | 0.9 | 0.005 | 180.0 | 219 |
| 389 | Aegis Sabre Peregrine | Atlas | A | Quantum Drive | 0.9 | 0.005 | 180.0 | 259 |
| 390 | Aegis Sabre Peregrine | FoxFire | B | Quantum Drive | 0.9 | 0.005 | 180.0 | 263 |
| 391 | Aegis Sabre Peregrine | Burst | B | Quantum Drive | 0.9 | 0.005 | 180.0 | 230 |
| 392 | Aegis Sabre Peregrine | Beacon | C | Quantum Drive | 0.9 | 0.005 | 180.0 | 161 |
| 393 | Aegis Sabre Peregrine | Colossus | B | Quantum Drive | 0.9 | 0.005 | 180.0 | 241 |
| 394 | Aegis Sabre Peregrine | VK-00 | A | Quantum Drive | 0.9 | 0.005 | 180.0 | 210 |
| 395 | Aegis Sabre Peregrine | Vulcan | D | Quantum Drive | 0.9 | 0.005 | 180.0 | 197 |
| 396 | Aegis Sabre Peregrine | Wayfare | D | Quantum Drive | 0.9 | 0.005 | 180.0 | 170 |
| 397 | Aegis Sabre Peregrine | Expedition | C | Quantum Drive | 0.9 | 0.005 | 180.0 | 189 |
| 398 | Aegis Sabre Peregrine | Rush | C | Quantum Drive | 0.9 | 0.005 | 180.0 | 209 |
| 399 | RSI Mantis | Goliath | C | Quantum Drive | 0.9 | 0.005 | 180.0 | 219 |
| 400 | RSI Mantis | Siren | B | Quantum Drive | 0.9 | 0.005 | 180.0 | 178 |
| 401 | RSI Mantis | Voyage | B | Quantum Drive | 0.9 | 0.005 | 180.0 | 208 |
| 402 | RSI Mantis | Eos | C | Quantum Drive | 0.9 | 0.005 | 180.0 | 199 |
| 403 | RSI Mantis | Flood | D | Quantum Drive | 0.9 | 0.005 | 180.0 | 188 |
| 404 | RSI Mantis | LightFire | C | Quantum Drive | 0.9 | 0.005 | 180.0 | 239 |
| 405 | RSI Mantis | Hyperion | B | Quantum Drive | 0.9 | 0.005 | 180.0 | 219 |
| 406 | RSI Mantis | Atlas | A | Quantum Drive | 0.9 | 0.005 | 180.0 | 259 |
| 407 | RSI Mantis | FoxFire | B | Quantum Drive | 0.9 | 0.005 | 180.0 | 263 |
| 408 | RSI Mantis | Burst | B | Quantum Drive | 0.9 | 0.005 | 180.0 | 230 |
| 409 | RSI Mantis | Beacon ★ | C | Quantum Drive | 0.9 | 0.005 | 180.0 | 161 |
| 410 | RSI Mantis | Colossus | B | Quantum Drive | 0.9 | 0.005 | 180.0 | 241 |
| 411 | RSI Mantis | VK-00 | A | Quantum Drive | 0.9 | 0.005 | 180.0 | 210 |
| 412 | RSI Mantis | Vulcan | D | Quantum Drive | 0.9 | 0.005 | 180.0 | 197 |
| 413 | RSI Mantis | Wayfare | D | Quantum Drive | 0.9 | 0.005 | 180.0 | 170 |
| 414 | RSI Mantis | Expedition | C | Quantum Drive | 0.9 | 0.005 | 180.0 | 189 |
| 415 | RSI Mantis | Rush | C | Quantum Drive | 0.9 | 0.005 | 180.0 | 209 |
| 416 | RSI Meteor | Goliath | C | Quantum Drive | 0.9 | 0.005 | 180.0 | 219 |
| 417 | RSI Meteor | Siren | B | Quantum Drive | 0.9 | 0.005 | 180.0 | 178 |
| 418 | RSI Meteor | Voyage | B | Quantum Drive | 0.9 | 0.005 | 180.0 | 208 |
| 419 | RSI Meteor | Eos | C | Quantum Drive | 0.9 | 0.005 | 180.0 | 199 |
| 420 | RSI Meteor | Flood | D | Quantum Drive | 0.9 | 0.005 | 180.0 | 188 |
| 421 | RSI Meteor | LightFire | C | Quantum Drive | 0.9 | 0.005 | 180.0 | 239 |
| 422 | RSI Meteor | Hyperion | B | Quantum Drive | 0.9 | 0.005 | 180.0 | 219 |
| 423 | RSI Meteor | Atlas | A | Quantum Drive | 0.9 | 0.005 | 180.0 | 259 |
| 424 | RSI Meteor | FoxFire | B | Quantum Drive | 0.9 | 0.005 | 180.0 | 263 |
| 425 | RSI Meteor | Burst | B | Quantum Drive | 0.9 | 0.005 | 180.0 | 230 |
| 426 | RSI Meteor | Beacon ★ | C | Quantum Drive | 0.9 | 0.005 | 180.0 | 161 |
| 427 | RSI Meteor | Colossus | B | Quantum Drive | 0.9 | 0.005 | 180.0 | 241 |
| 428 | RSI Meteor | VK-00 | A | Quantum Drive | 0.9 | 0.005 | 180.0 | 210 |
| 429 | RSI Meteor | Vulcan | D | Quantum Drive | 0.9 | 0.005 | 180.0 | 197 |
| 430 | RSI Meteor | Wayfare | D | Quantum Drive | 0.9 | 0.005 | 180.0 | 170 |
| 431 | RSI Meteor | Expedition | C | Quantum Drive | 0.9 | 0.005 | 180.0 | 189 |
| 432 | RSI Meteor | Rush | C | Quantum Drive | 0.9 | 0.005 | 180.0 | 209 |
| 433 | RSI Scorpius | Goliath | C | Quantum Drive | 0.9 | 0.005 | 180.0 | 219 |
| 434 | RSI Scorpius | Siren | B | Quantum Drive | 0.9 | 0.005 | 180.0 | 178 |
| 435 | RSI Scorpius | Voyage | B | Quantum Drive | 0.9 | 0.005 | 180.0 | 208 |
| 436 | RSI Scorpius | Eos ★ | C | Quantum Drive | 0.9 | 0.005 | 180.0 | 199 |
| 437 | RSI Scorpius | Flood | D | Quantum Drive | 0.9 | 0.005 | 180.0 | 188 |
| 438 | RSI Scorpius | LightFire | C | Quantum Drive | 0.9 | 0.005 | 180.0 | 239 |
| 439 | RSI Scorpius | Hyperion | B | Quantum Drive | 0.9 | 0.005 | 180.0 | 219 |
| 440 | RSI Scorpius | Atlas | A | Quantum Drive | 0.9 | 0.005 | 180.0 | 259 |
| 441 | RSI Scorpius | FoxFire | B | Quantum Drive | 0.9 | 0.005 | 180.0 | 263 |
| 442 | RSI Scorpius | Burst | B | Quantum Drive | 0.9 | 0.005 | 180.0 | 230 |
| 443 | RSI Scorpius | Beacon | C | Quantum Drive | 0.9 | 0.005 | 180.0 | 161 |
| 444 | RSI Scorpius | Colossus | B | Quantum Drive | 0.9 | 0.005 | 180.0 | 241 |
| 445 | RSI Scorpius | VK-00 | A | Quantum Drive | 0.9 | 0.005 | 180.0 | 210 |
| 446 | RSI Scorpius | Vulcan | D | Quantum Drive | 0.9 | 0.005 | 180.0 | 197 |
| 447 | RSI Scorpius | Wayfare | D | Quantum Drive | 0.9 | 0.005 | 180.0 | 170 |
| 448 | RSI Scorpius | Expedition | C | Quantum Drive | 0.9 | 0.005 | 180.0 | 189 |
| 449 | RSI Scorpius | Rush | C | Quantum Drive | 0.9 | 0.005 | 180.0 | 209 |
| 450 | RSI Scorpius Antares | Goliath | C | Quantum Drive | 0.9 | 0.005 | 180.0 | 219 |
| 451 | RSI Scorpius Antares | Siren | B | Quantum Drive | 0.9 | 0.005 | 180.0 | 178 |
| 452 | RSI Scorpius Antares | Voyage | B | Quantum Drive | 0.9 | 0.005 | 180.0 | 208 |
| 453 | RSI Scorpius Antares | Eos ★ | C | Quantum Drive | 0.9 | 0.005 | 180.0 | 199 |
| 454 | RSI Scorpius Antares | Flood | D | Quantum Drive | 0.9 | 0.005 | 180.0 | 188 |
| 455 | RSI Scorpius Antares | LightFire | C | Quantum Drive | 0.9 | 0.005 | 180.0 | 239 |
| 456 | RSI Scorpius Antares | Hyperion | B | Quantum Drive | 0.9 | 0.005 | 180.0 | 219 |
| 457 | RSI Scorpius Antares | Atlas | A | Quantum Drive | 0.9 | 0.005 | 180.0 | 259 |
| 458 | RSI Scorpius Antares | FoxFire | B | Quantum Drive | 0.9 | 0.005 | 180.0 | 263 |
| 459 | RSI Scorpius Antares | Burst | B | Quantum Drive | 0.9 | 0.005 | 180.0 | 230 |
| 460 | RSI Scorpius Antares | Beacon | C | Quantum Drive | 0.9 | 0.005 | 180.0 | 161 |
| 461 | RSI Scorpius Antares | Colossus | B | Quantum Drive | 0.9 | 0.005 | 180.0 | 241 |
| 462 | RSI Scorpius Antares | VK-00 | A | Quantum Drive | 0.9 | 0.005 | 180.0 | 210 |
| 463 | RSI Scorpius Antares | Vulcan | D | Quantum Drive | 0.9 | 0.005 | 180.0 | 197 |
| 464 | RSI Scorpius Antares | Wayfare | D | Quantum Drive | 0.9 | 0.005 | 180.0 | 170 |
| 465 | RSI Scorpius Antares | Expedition | C | Quantum Drive | 0.9 | 0.005 | 180.0 | 189 |
| 466 | RSI Scorpius Antares | Rush | C | Quantum Drive | 0.9 | 0.005 | 180.0 | 209 |
| 467 | Anvil C8 Pisces | Goliath | C | Quantum Drive | 0.9 | 0.005 | 180.0 | 219 |
| 468 | Anvil C8 Pisces | Siren | B | Quantum Drive | 0.9 | 0.005 | 180.0 | 178 |
| 469 | Anvil C8 Pisces | Voyage | B | Quantum Drive | 0.9 | 0.005 | 180.0 | 208 |
| 470 | Anvil C8 Pisces | Eos | C | Quantum Drive | 0.9 | 0.005 | 180.0 | 199 |
| 471 | Anvil C8 Pisces | Flood | D | Quantum Drive | 0.9 | 0.005 | 180.0 | 188 |
| 472 | Anvil C8 Pisces | LightFire | C | Quantum Drive | 0.9 | 0.005 | 180.0 | 239 |
| 473 | Anvil C8 Pisces | Hyperion | B | Quantum Drive | 0.9 | 0.005 | 180.0 | 219 |
| 474 | Anvil C8 Pisces | Atlas | A | Quantum Drive | 0.9 | 0.005 | 180.0 | 259 |
| 475 | Anvil C8 Pisces | FoxFire | B | Quantum Drive | 0.9 | 0.005 | 180.0 | 263 |
| 476 | Anvil C8 Pisces | Burst | B | Quantum Drive | 0.9 | 0.005 | 180.0 | 230 |
| 477 | Anvil C8 Pisces | Beacon | C | Quantum Drive | 0.9 | 0.005 | 180.0 | 161 |
| 478 | Anvil C8 Pisces | Colossus | B | Quantum Drive | 0.9 | 0.005 | 180.0 | 241 |
| 479 | Anvil C8 Pisces | VK-00 | A | Quantum Drive | 0.9 | 0.005 | 180.0 | 210 |
| 480 | Anvil C8 Pisces | Vulcan | D | Quantum Drive | 0.9 | 0.005 | 180.0 | 197 |
| 481 | Anvil C8 Pisces | Wayfare | D | Quantum Drive | 0.9 | 0.005 | 180.0 | 170 |
| 482 | Anvil C8 Pisces | Expedition ★ | C | Quantum Drive | 0.9 | 0.005 | 180.0 | 189 |
| 483 | Anvil C8 Pisces | Rush | C | Quantum Drive | 0.9 | 0.005 | 180.0 | 209 |
| 484 | Anvil C8R Pisces Rescue | Goliath | C | Quantum Drive | 0.9 | 0.005 | 180.0 | 219 |
| 485 | Anvil C8R Pisces Rescue | Siren | B | Quantum Drive | 0.9 | 0.005 | 180.0 | 178 |
| 486 | Anvil C8R Pisces Rescue | Voyage | B | Quantum Drive | 0.9 | 0.005 | 180.0 | 208 |
| 487 | Anvil C8R Pisces Rescue | Eos | C | Quantum Drive | 0.9 | 0.005 | 180.0 | 199 |
| 488 | Anvil C8R Pisces Rescue | Flood | D | Quantum Drive | 0.9 | 0.005 | 180.0 | 188 |
| 489 | Anvil C8R Pisces Rescue | LightFire | C | Quantum Drive | 0.9 | 0.005 | 180.0 | 239 |
| 490 | Anvil C8R Pisces Rescue | Hyperion | B | Quantum Drive | 0.9 | 0.005 | 180.0 | 219 |
| 491 | Anvil C8R Pisces Rescue | Atlas | A | Quantum Drive | 0.9 | 0.005 | 180.0 | 259 |
| 492 | Anvil C8R Pisces Rescue | FoxFire | B | Quantum Drive | 0.9 | 0.005 | 180.0 | 263 |
| 493 | Anvil C8R Pisces Rescue | Burst | B | Quantum Drive | 0.9 | 0.005 | 180.0 | 230 |
| 494 | Anvil C8R Pisces Rescue | Beacon | C | Quantum Drive | 0.9 | 0.005 | 180.0 | 161 |
| 495 | Anvil C8R Pisces Rescue | Colossus | B | Quantum Drive | 0.9 | 0.005 | 180.0 | 241 |
| 496 | Anvil C8R Pisces Rescue | VK-00 | A | Quantum Drive | 0.9 | 0.005 | 180.0 | 210 |
| 497 | Anvil C8R Pisces Rescue | Vulcan | D | Quantum Drive | 0.9 | 0.005 | 180.0 | 197 |
| 498 | Anvil C8R Pisces Rescue | Wayfare | D | Quantum Drive | 0.9 | 0.005 | 180.0 | 170 |
| 499 | Anvil C8R Pisces Rescue | Expedition ★ | C | Quantum Drive | 0.9 | 0.005 | 180.0 | 189 |
| 500 | Anvil C8R Pisces Rescue | Rush | C | Quantum Drive | 0.9 | 0.005 | 180.0 | 209 |
| 501 | Anvil C8X Pisces Expedition | Goliath | C | Quantum Drive | 0.9 | 0.005 | 180.0 | 219 |
| 502 | Anvil C8X Pisces Expedition | Siren | B | Quantum Drive | 0.9 | 0.005 | 180.0 | 178 |
| 503 | Anvil C8X Pisces Expedition | Voyage | B | Quantum Drive | 0.9 | 0.005 | 180.0 | 208 |
| 504 | Anvil C8X Pisces Expedition | Eos | C | Quantum Drive | 0.9 | 0.005 | 180.0 | 199 |
| 505 | Anvil C8X Pisces Expedition | Flood | D | Quantum Drive | 0.9 | 0.005 | 180.0 | 188 |
| 506 | Anvil C8X Pisces Expedition | LightFire | C | Quantum Drive | 0.9 | 0.005 | 180.0 | 239 |
| 507 | Anvil C8X Pisces Expedition | Hyperion | B | Quantum Drive | 0.9 | 0.005 | 180.0 | 219 |
| 508 | Anvil C8X Pisces Expedition | Atlas | A | Quantum Drive | 0.9 | 0.005 | 180.0 | 259 |
| 509 | Anvil C8X Pisces Expedition | FoxFire | B | Quantum Drive | 0.9 | 0.005 | 180.0 | 263 |
| 510 | Anvil C8X Pisces Expedition | Burst | B | Quantum Drive | 0.9 | 0.005 | 180.0 | 230 |
| 511 | Anvil C8X Pisces Expedition | Beacon | C | Quantum Drive | 0.9 | 0.005 | 180.0 | 161 |
| 512 | Anvil C8X Pisces Expedition | Colossus | B | Quantum Drive | 0.9 | 0.005 | 180.0 | 241 |
| 513 | Anvil C8X Pisces Expedition | VK-00 | A | Quantum Drive | 0.9 | 0.005 | 180.0 | 210 |
| 514 | Anvil C8X Pisces Expedition | Vulcan | D | Quantum Drive | 0.9 | 0.005 | 180.0 | 197 |
| 515 | Anvil C8X Pisces Expedition | Wayfare | D | Quantum Drive | 0.9 | 0.005 | 180.0 | 170 |
| 516 | Anvil C8X Pisces Expedition | Expedition ★ | C | Quantum Drive | 0.9 | 0.005 | 180.0 | 189 |
| 517 | Anvil C8X Pisces Expedition | Rush | C | Quantum Drive | 0.9 | 0.005 | 180.0 | 209 |
| 518 | Anvil F7C Hornet Mk II | Goliath | C | Quantum Drive | 0.9 | 0.005 | 180.0 | 219 |
| 519 | Anvil F7C Hornet Mk II | Siren | B | Quantum Drive | 0.9 | 0.005 | 180.0 | 178 |
| 520 | Anvil F7C Hornet Mk II | Voyage | B | Quantum Drive | 0.9 | 0.005 | 180.0 | 208 |
| 521 | Anvil F7C Hornet Mk II | Eos ★ | C | Quantum Drive | 0.9 | 0.005 | 180.0 | 199 |
| 522 | Anvil F7C Hornet Mk II | Flood | D | Quantum Drive | 0.9 | 0.005 | 180.0 | 188 |
| 523 | Anvil F7C Hornet Mk II | LightFire | C | Quantum Drive | 0.9 | 0.005 | 180.0 | 239 |
| 524 | Anvil F7C Hornet Mk II | Hyperion | B | Quantum Drive | 0.9 | 0.005 | 180.0 | 219 |
| 525 | Anvil F7C Hornet Mk II | Atlas | A | Quantum Drive | 0.9 | 0.005 | 180.0 | 259 |
| 526 | Anvil F7C Hornet Mk II | FoxFire | B | Quantum Drive | 0.9 | 0.005 | 180.0 | 263 |
| 527 | Anvil F7C Hornet Mk II | Burst | B | Quantum Drive | 0.9 | 0.005 | 180.0 | 230 |
| 528 | Anvil F7C Hornet Mk II | Beacon | C | Quantum Drive | 0.9 | 0.005 | 180.0 | 161 |
| 529 | Anvil F7C Hornet Mk II | Colossus | B | Quantum Drive | 0.9 | 0.005 | 180.0 | 241 |
| 530 | Anvil F7C Hornet Mk II | VK-00 | A | Quantum Drive | 0.9 | 0.005 | 180.0 | 210 |
| 531 | Anvil F7C Hornet Mk II | Vulcan | D | Quantum Drive | 0.9 | 0.005 | 180.0 | 197 |
| 532 | Anvil F7C Hornet Mk II | Wayfare | D | Quantum Drive | 0.9 | 0.005 | 180.0 | 170 |
| 533 | Anvil F7C Hornet Mk II | Expedition | C | Quantum Drive | 0.9 | 0.005 | 180.0 | 189 |
| 534 | Anvil F7C Hornet Mk II | Rush | C | Quantum Drive | 0.9 | 0.005 | 180.0 | 209 |
| 535 | Anvil F7C-R Hornet Tracker Mk II | Goliath | C | Quantum Drive | 0.9 | 0.005 | 180.0 | 219 |
| 536 | Anvil F7C-R Hornet Tracker Mk II | Siren | B | Quantum Drive | 0.9 | 0.005 | 180.0 | 178 |
| 537 | Anvil F7C-R Hornet Tracker Mk II | Voyage | B | Quantum Drive | 0.9 | 0.005 | 180.0 | 208 |
| 538 | Anvil F7C-R Hornet Tracker Mk II | Eos ★ | C | Quantum Drive | 0.9 | 0.005 | 180.0 | 199 |
| 539 | Anvil F7C-R Hornet Tracker Mk II | Flood | D | Quantum Drive | 0.9 | 0.005 | 180.0 | 188 |
| 540 | Anvil F7C-R Hornet Tracker Mk II | LightFire | C | Quantum Drive | 0.9 | 0.005 | 180.0 | 239 |
| 541 | Anvil F7C-R Hornet Tracker Mk II | Hyperion | B | Quantum Drive | 0.9 | 0.005 | 180.0 | 219 |
| 542 | Anvil F7C-R Hornet Tracker Mk II | Atlas | A | Quantum Drive | 0.9 | 0.005 | 180.0 | 259 |
| 543 | Anvil F7C-R Hornet Tracker Mk II | FoxFire | B | Quantum Drive | 0.9 | 0.005 | 180.0 | 263 |
| 544 | Anvil F7C-R Hornet Tracker Mk II | Burst | B | Quantum Drive | 0.9 | 0.005 | 180.0 | 230 |
| 545 | Anvil F7C-R Hornet Tracker Mk II | Beacon | C | Quantum Drive | 0.9 | 0.005 | 180.0 | 161 |
| 546 | Anvil F7C-R Hornet Tracker Mk II | Colossus | B | Quantum Drive | 0.9 | 0.005 | 180.0 | 241 |
| 547 | Anvil F7C-R Hornet Tracker Mk II | VK-00 | A | Quantum Drive | 0.9 | 0.005 | 180.0 | 210 |
| 548 | Anvil F7C-R Hornet Tracker Mk II | Vulcan | D | Quantum Drive | 0.9 | 0.005 | 180.0 | 197 |
| 549 | Anvil F7C-R Hornet Tracker Mk II | Wayfare | D | Quantum Drive | 0.9 | 0.005 | 180.0 | 170 |
| 550 | Anvil F7C-R Hornet Tracker Mk II | Expedition | C | Quantum Drive | 0.9 | 0.005 | 180.0 | 189 |
| 551 | Anvil F7C-R Hornet Tracker Mk II | Rush | C | Quantum Drive | 0.9 | 0.005 | 180.0 | 209 |
| 552 | Anvil F7C-S Hornet Ghost Mk II | Goliath | C | Quantum Drive | 0.9 | 0.005 | 180.0 | 219 |
| 553 | Anvil F7C-S Hornet Ghost Mk II | Siren | B | Quantum Drive | 0.9 | 0.005 | 180.0 | 178 |
| 554 | Anvil F7C-S Hornet Ghost Mk II | Voyage | B | Quantum Drive | 0.9 | 0.005 | 180.0 | 208 |
| 555 | Anvil F7C-S Hornet Ghost Mk II | Eos | C | Quantum Drive | 0.9 | 0.005 | 180.0 | 199 |
| 556 | Anvil F7C-S Hornet Ghost Mk II | Flood | D | Quantum Drive | 0.9 | 0.005 | 180.0 | 188 |
| 557 | Anvil F7C-S Hornet Ghost Mk II | LightFire | C | Quantum Drive | 0.9 | 0.005 | 180.0 | 239 |
| 558 | Anvil F7C-S Hornet Ghost Mk II | Hyperion | B | Quantum Drive | 0.9 | 0.005 | 180.0 | 219 |
| 559 | Anvil F7C-S Hornet Ghost Mk II | Atlas | A | Quantum Drive | 0.9 | 0.005 | 180.0 | 259 |
| 560 | Anvil F7C-S Hornet Ghost Mk II | FoxFire | B | Quantum Drive | 0.9 | 0.005 | 180.0 | 263 |
| 561 | Anvil F7C-S Hornet Ghost Mk II | Burst | B | Quantum Drive | 0.9 | 0.005 | 180.0 | 230 |
| 562 | Anvil F7C-S Hornet Ghost Mk II | Beacon | C | Quantum Drive | 0.9 | 0.005 | 180.0 | 161 |
| 563 | Anvil F7C-S Hornet Ghost Mk II | Colossus | B | Quantum Drive | 0.9 | 0.005 | 180.0 | 241 |
| 564 | Anvil F7C-S Hornet Ghost Mk II | VK-00 | A | Quantum Drive | 0.9 | 0.005 | 180.0 | 210 |
| 565 | Anvil F7C-S Hornet Ghost Mk II | Vulcan | D | Quantum Drive | 0.9 | 0.005 | 180.0 | 197 |
| 566 | Anvil F7C-S Hornet Ghost Mk II | Wayfare | D | Quantum Drive | 0.9 | 0.005 | 180.0 | 170 |
| 567 | Anvil F7C-S Hornet Ghost Mk II | Expedition | C | Quantum Drive | 0.9 | 0.005 | 180.0 | 189 |
| 568 | Anvil F7C-S Hornet Ghost Mk II | Rush | C | Quantum Drive | 0.9 | 0.005 | 180.0 | 209 |
| 569 | Anvil Hurricane | Goliath | C | Quantum Drive | 0.9 | 0.005 | 180.0 | 219 |
| 570 | Anvil Hurricane | Siren | B | Quantum Drive | 0.9 | 0.005 | 180.0 | 178 |
| 571 | Anvil Hurricane | Voyage | B | Quantum Drive | 0.9 | 0.005 | 180.0 | 208 |
| 572 | Anvil Hurricane | Eos | C | Quantum Drive | 0.9 | 0.005 | 180.0 | 199 |
| 573 | Anvil Hurricane | Flood | D | Quantum Drive | 0.9 | 0.005 | 180.0 | 188 |
| 574 | Anvil Hurricane | LightFire | C | Quantum Drive | 0.9 | 0.005 | 180.0 | 239 |
| 575 | Anvil Hurricane | Hyperion | B | Quantum Drive | 0.9 | 0.005 | 180.0 | 219 |
| 576 | Anvil Hurricane | Atlas | A | Quantum Drive | 0.9 | 0.005 | 180.0 | 259 |
| 577 | Anvil Hurricane | FoxFire | B | Quantum Drive | 0.9 | 0.005 | 180.0 | 263 |
| 578 | Anvil Hurricane | Burst | B | Quantum Drive | 0.9 | 0.005 | 180.0 | 230 |
| 579 | Anvil Hurricane | Beacon | C | Quantum Drive | 0.9 | 0.005 | 180.0 | 161 |
| 580 | Anvil Hurricane | Colossus | B | Quantum Drive | 0.9 | 0.005 | 180.0 | 241 |
| 581 | Anvil Hurricane | VK-00 | A | Quantum Drive | 0.9 | 0.005 | 180.0 | 210 |
| 582 | Anvil Hurricane | Vulcan | D | Quantum Drive | 0.9 | 0.005 | 180.0 | 197 |
| 583 | Anvil Hurricane | Wayfare | D | Quantum Drive | 0.9 | 0.005 | 180.0 | 170 |
| 584 | Anvil Hurricane | Expedition ★ | C | Quantum Drive | 0.9 | 0.005 | 180.0 | 189 |
| 585 | Anvil Hurricane | Rush | C | Quantum Drive | 0.9 | 0.005 | 180.0 | 209 |
| 586 | Aopoa San'tok.yāi | Goliath | C | Quantum Drive | 0.9 | 0.005 | 180.0 | 219 |
| 587 | Aopoa San'tok.yāi | Siren | B | Quantum Drive | 0.9 | 0.005 | 180.0 | 178 |
| 588 | Aopoa San'tok.yāi | Voyage | B | Quantum Drive | 0.9 | 0.005 | 180.0 | 208 |
| 589 | Aopoa San'tok.yāi | Eos | C | Quantum Drive | 0.9 | 0.005 | 180.0 | 199 |
| 590 | Aopoa San'tok.yāi | Flood | D | Quantum Drive | 0.9 | 0.005 | 180.0 | 188 |
| 591 | Aopoa San'tok.yāi | LightFire | C | Quantum Drive | 0.9 | 0.005 | 180.0 | 239 |
| 592 | Aopoa San'tok.yāi | Hyperion | B | Quantum Drive | 0.9 | 0.005 | 180.0 | 219 |
| 593 | Aopoa San'tok.yāi | Atlas | A | Quantum Drive | 0.9 | 0.005 | 180.0 | 259 |
| 594 | Aopoa San'tok.yāi | FoxFire | B | Quantum Drive | 0.9 | 0.005 | 180.0 | 263 |
| 595 | Aopoa San'tok.yāi | Burst | B | Quantum Drive | 0.9 | 0.005 | 180.0 | 230 |
| 596 | Aopoa San'tok.yāi | Beacon ★ | C | Quantum Drive | 0.9 | 0.005 | 180.0 | 161 |
| 597 | Aopoa San'tok.yāi | Colossus | B | Quantum Drive | 0.9 | 0.005 | 180.0 | 241 |
| 598 | Aopoa San'tok.yāi | VK-00 | A | Quantum Drive | 0.9 | 0.005 | 180.0 | 210 |
| 599 | Aopoa San'tok.yāi | Vulcan | D | Quantum Drive | 0.9 | 0.005 | 180.0 | 197 |
| 600 | Aopoa San'tok.yāi | Wayfare | D | Quantum Drive | 0.9 | 0.005 | 180.0 | 170 |
| 601 | Aopoa San'tok.yāi | Expedition | C | Quantum Drive | 0.9 | 0.005 | 180.0 | 189 |
| 602 | Aopoa San'tok.yāi | Rush | C | Quantum Drive | 0.9 | 0.005 | 180.0 | 209 |
| 603 | Crusader Intrepid | Goliath | C | Quantum Drive | 0.9 | 0.005 | 180.0 | 219 |
| 604 | Crusader Intrepid | Siren | B | Quantum Drive | 0.9 | 0.005 | 180.0 | 178 |
| 605 | Crusader Intrepid | Voyage | B | Quantum Drive | 0.9 | 0.005 | 180.0 | 208 |
| 606 | Crusader Intrepid | Eos | C | Quantum Drive | 0.9 | 0.005 | 180.0 | 199 |
| 607 | Crusader Intrepid | Flood | D | Quantum Drive | 0.9 | 0.005 | 180.0 | 188 |
| 608 | Crusader Intrepid | LightFire | C | Quantum Drive | 0.9 | 0.005 | 180.0 | 239 |
| 609 | Crusader Intrepid | Hyperion | B | Quantum Drive | 0.9 | 0.005 | 180.0 | 219 |
| 610 | Crusader Intrepid | Atlas | A | Quantum Drive | 0.9 | 0.005 | 180.0 | 259 |
| 611 | Crusader Intrepid | FoxFire ★ | B | Quantum Drive | 0.9 | 0.005 | 180.0 | 263 |
| 612 | Crusader Intrepid | Burst | B | Quantum Drive | 0.9 | 0.005 | 180.0 | 230 |
| 613 | Crusader Intrepid | Beacon | C | Quantum Drive | 0.9 | 0.005 | 180.0 | 161 |
| 614 | Crusader Intrepid | Colossus | B | Quantum Drive | 0.9 | 0.005 | 180.0 | 241 |
| 615 | Crusader Intrepid | VK-00 | A | Quantum Drive | 0.9 | 0.005 | 180.0 | 210 |
| 616 | Crusader Intrepid | Vulcan | D | Quantum Drive | 0.9 | 0.005 | 180.0 | 197 |
| 617 | Crusader Intrepid | Wayfare | D | Quantum Drive | 0.9 | 0.005 | 180.0 | 170 |
| 618 | Crusader Intrepid | Expedition | C | Quantum Drive | 0.9 | 0.005 | 180.0 | 189 |
| 619 | Crusader Intrepid | Rush | C | Quantum Drive | 0.9 | 0.005 | 180.0 | 209 |
| 620 | Drake Vulture | Goliath ★ | C | Quantum Drive | 0.9 | 0.005 | 180.0 | 219 |
| 621 | Drake Vulture | Siren | B | Quantum Drive | 0.9 | 0.005 | 180.0 | 178 |
| 622 | Drake Vulture | Voyage | B | Quantum Drive | 0.9 | 0.005 | 180.0 | 208 |
| 623 | Drake Vulture | Eos | C | Quantum Drive | 0.9 | 0.005 | 180.0 | 199 |
| 624 | Drake Vulture | Flood | D | Quantum Drive | 0.9 | 0.005 | 180.0 | 188 |
| 625 | Drake Vulture | LightFire | C | Quantum Drive | 0.9 | 0.005 | 180.0 | 239 |
| 626 | Drake Vulture | Hyperion | B | Quantum Drive | 0.9 | 0.005 | 180.0 | 219 |
| 627 | Drake Vulture | Atlas | A | Quantum Drive | 0.9 | 0.005 | 180.0 | 259 |
| 628 | Drake Vulture | FoxFire | B | Quantum Drive | 0.9 | 0.005 | 180.0 | 263 |
| 629 | Drake Vulture | Burst | B | Quantum Drive | 0.9 | 0.005 | 180.0 | 230 |
| 630 | Drake Vulture | Beacon | C | Quantum Drive | 0.9 | 0.005 | 180.0 | 161 |
| 631 | Drake Vulture | Colossus | B | Quantum Drive | 0.9 | 0.005 | 180.0 | 241 |
| 632 | Drake Vulture | VK-00 | A | Quantum Drive | 0.9 | 0.005 | 180.0 | 210 |
| 633 | Drake Vulture | Vulcan | D | Quantum Drive | 0.9 | 0.005 | 180.0 | 197 |
| 634 | Drake Vulture | Wayfare | D | Quantum Drive | 0.9 | 0.005 | 180.0 | 170 |
| 635 | Drake Vulture | Expedition | C | Quantum Drive | 0.9 | 0.005 | 180.0 | 189 |
| 636 | Drake Vulture | Rush | C | Quantum Drive | 0.9 | 0.005 | 180.0 | 209 |
| 637 | Gatac Syulen | Goliath | C | Quantum Drive | 0.9 | 0.005 | 180.0 | 219 |
| 638 | Gatac Syulen | Siren | B | Quantum Drive | 0.9 | 0.005 | 180.0 | 178 |
| 639 | Gatac Syulen | Voyage | B | Quantum Drive | 0.9 | 0.005 | 180.0 | 208 |
| 640 | Gatac Syulen | Eos | C | Quantum Drive | 0.9 | 0.005 | 180.0 | 199 |
| 641 | Gatac Syulen | Flood | D | Quantum Drive | 0.9 | 0.005 | 180.0 | 188 |
| 642 | Gatac Syulen | LightFire | C | Quantum Drive | 0.9 | 0.005 | 180.0 | 239 |
| 643 | Gatac Syulen | Hyperion | B | Quantum Drive | 0.9 | 0.005 | 180.0 | 219 |
| 644 | Gatac Syulen | Atlas | A | Quantum Drive | 0.9 | 0.005 | 180.0 | 259 |
| 645 | Gatac Syulen | FoxFire ★ | B | Quantum Drive | 0.9 | 0.005 | 180.0 | 263 |
| 646 | Gatac Syulen | Burst | B | Quantum Drive | 0.9 | 0.005 | 180.0 | 230 |
| 647 | Gatac Syulen | Beacon | C | Quantum Drive | 0.9 | 0.005 | 180.0 | 161 |
| 648 | Gatac Syulen | Colossus | B | Quantum Drive | 0.9 | 0.005 | 180.0 | 241 |
| 649 | Gatac Syulen | VK-00 | A | Quantum Drive | 0.9 | 0.005 | 180.0 | 210 |
| 650 | Gatac Syulen | Vulcan | D | Quantum Drive | 0.9 | 0.005 | 180.0 | 197 |
| 651 | Gatac Syulen | Wayfare | D | Quantum Drive | 0.9 | 0.005 | 180.0 | 170 |
| 652 | Gatac Syulen | Expedition | C | Quantum Drive | 0.9 | 0.005 | 180.0 | 189 |
| 653 | Gatac Syulen | Rush | C | Quantum Drive | 0.9 | 0.005 | 180.0 | 209 |
| 654 | MISC Fortune | Goliath ★ | C | Quantum Drive | 0.9 | 0.005 | 180.0 | 219 |
| 655 | MISC Fortune | Siren | B | Quantum Drive | 0.9 | 0.005 | 180.0 | 178 |
| 656 | MISC Fortune | Voyage | B | Quantum Drive | 0.9 | 0.005 | 180.0 | 208 |
| 657 | MISC Fortune | Eos | C | Quantum Drive | 0.9 | 0.005 | 180.0 | 199 |
| 658 | MISC Fortune | Flood | D | Quantum Drive | 0.9 | 0.005 | 180.0 | 188 |
| 659 | MISC Fortune | LightFire | C | Quantum Drive | 0.9 | 0.005 | 180.0 | 239 |
| 660 | MISC Fortune | Hyperion | B | Quantum Drive | 0.9 | 0.005 | 180.0 | 219 |
| 661 | MISC Fortune | Atlas | A | Quantum Drive | 0.9 | 0.005 | 180.0 | 259 |
| 662 | MISC Fortune | FoxFire | B | Quantum Drive | 0.9 | 0.005 | 180.0 | 263 |
| 663 | MISC Fortune | Burst | B | Quantum Drive | 0.9 | 0.005 | 180.0 | 230 |
| 664 | MISC Fortune | Beacon | C | Quantum Drive | 0.9 | 0.005 | 180.0 | 161 |
| 665 | MISC Fortune | Colossus | B | Quantum Drive | 0.9 | 0.005 | 180.0 | 241 |
| 666 | MISC Fortune | VK-00 | A | Quantum Drive | 0.9 | 0.005 | 180.0 | 210 |
| 667 | MISC Fortune | Vulcan | D | Quantum Drive | 0.9 | 0.005 | 180.0 | 197 |
| 668 | MISC Fortune | Wayfare | D | Quantum Drive | 0.9 | 0.005 | 180.0 | 170 |
| 669 | MISC Fortune | Expedition | C | Quantum Drive | 0.9 | 0.005 | 180.0 | 189 |
| 670 | MISC Fortune | Rush | C | Quantum Drive | 0.9 | 0.005 | 180.0 | 209 |
| 671 | MISC Prospector | Goliath ★ | C | Quantum Drive | 0.9 | 0.005 | 180.0 | 219 |
| 672 | MISC Prospector | Siren | B | Quantum Drive | 0.9 | 0.005 | 180.0 | 178 |
| 673 | MISC Prospector | Voyage | B | Quantum Drive | 0.9 | 0.005 | 180.0 | 208 |
| 674 | MISC Prospector | Eos | C | Quantum Drive | 0.9 | 0.005 | 180.0 | 199 |
| 675 | MISC Prospector | Flood | D | Quantum Drive | 0.9 | 0.005 | 180.0 | 188 |
| 676 | MISC Prospector | LightFire | C | Quantum Drive | 0.9 | 0.005 | 180.0 | 239 |
| 677 | MISC Prospector | Hyperion | B | Quantum Drive | 0.9 | 0.005 | 180.0 | 219 |
| 678 | MISC Prospector | Atlas | A | Quantum Drive | 0.9 | 0.005 | 180.0 | 259 |
| 679 | MISC Prospector | FoxFire | B | Quantum Drive | 0.9 | 0.005 | 180.0 | 263 |
| 680 | MISC Prospector | Burst | B | Quantum Drive | 0.9 | 0.005 | 180.0 | 230 |
| 681 | MISC Prospector | Beacon | C | Quantum Drive | 0.9 | 0.005 | 180.0 | 161 |
| 682 | MISC Prospector | Colossus | B | Quantum Drive | 0.9 | 0.005 | 180.0 | 241 |
| 683 | MISC Prospector | VK-00 | A | Quantum Drive | 0.9 | 0.005 | 180.0 | 210 |
| 684 | MISC Prospector | Vulcan | D | Quantum Drive | 0.9 | 0.005 | 180.0 | 197 |
| 685 | MISC Prospector | Wayfare | D | Quantum Drive | 0.9 | 0.005 | 180.0 | 170 |
| 686 | MISC Prospector | Expedition | C | Quantum Drive | 0.9 | 0.005 | 180.0 | 189 |
| 687 | MISC Prospector | Rush | C | Quantum Drive | 0.9 | 0.005 | 180.0 | 209 |
| 688 | Origin 100i | Goliath | C | Quantum Drive | 0.9 | 0.005 | 180.0 | 219 |
| 689 | Origin 100i | Siren | B | Quantum Drive | 0.9 | 0.005 | 180.0 | 178 |
| 690 | Origin 100i | Voyage | B | Quantum Drive | 0.9 | 0.005 | 180.0 | 208 |
| 691 | Origin 100i | Eos | C | Quantum Drive | 0.9 | 0.005 | 180.0 | 199 |
| 692 | Origin 100i | Flood | D | Quantum Drive | 0.9 | 0.005 | 180.0 | 188 |
| 693 | Origin 100i | LightFire | C | Quantum Drive | 0.9 | 0.005 | 180.0 | 239 |
| 694 | Origin 100i | Hyperion | B | Quantum Drive | 0.9 | 0.005 | 180.0 | 219 |
| 695 | Origin 100i | Atlas | A | Quantum Drive | 0.9 | 0.005 | 180.0 | 259 |
| 696 | Origin 100i | FoxFire | B | Quantum Drive | 0.9 | 0.005 | 180.0 | 263 |
| 697 | Origin 100i | Burst | B | Quantum Drive | 0.9 | 0.005 | 180.0 | 230 |
| 698 | Origin 100i | Beacon | C | Quantum Drive | 0.9 | 0.005 | 180.0 | 161 |
| 699 | Origin 100i | Colossus | B | Quantum Drive | 0.9 | 0.005 | 180.0 | 241 |
| 700 | Origin 100i | VK-00 | A | Quantum Drive | 0.9 | 0.005 | 180.0 | 210 |
| 701 | Origin 100i | Vulcan | D | Quantum Drive | 0.9 | 0.005 | 180.0 | 197 |
| 702 | Origin 100i | Wayfare | D | Quantum Drive | 0.9 | 0.005 | 180.0 | 170 |
| 703 | Origin 100i | Expedition ★ | C | Quantum Drive | 0.9 | 0.005 | 180.0 | 189 |
| 704 | Origin 100i | Rush | C | Quantum Drive | 0.9 | 0.005 | 180.0 | 209 |
| 705 | Origin 125a | Goliath | C | Quantum Drive | 0.9 | 0.005 | 180.0 | 219 |
| 706 | Origin 125a | Siren | B | Quantum Drive | 0.9 | 0.005 | 180.0 | 178 |
| 707 | Origin 125a | Voyage | B | Quantum Drive | 0.9 | 0.005 | 180.0 | 208 |
| 708 | Origin 125a | Eos | C | Quantum Drive | 0.9 | 0.005 | 180.0 | 199 |
| 709 | Origin 125a | Flood | D | Quantum Drive | 0.9 | 0.005 | 180.0 | 188 |
| 710 | Origin 125a | LightFire | C | Quantum Drive | 0.9 | 0.005 | 180.0 | 239 |
| 711 | Origin 125a | Hyperion | B | Quantum Drive | 0.9 | 0.005 | 180.0 | 219 |
| 712 | Origin 125a | Atlas | A | Quantum Drive | 0.9 | 0.005 | 180.0 | 259 |
| 713 | Origin 125a | FoxFire | B | Quantum Drive | 0.9 | 0.005 | 180.0 | 263 |
| 714 | Origin 125a | Burst | B | Quantum Drive | 0.9 | 0.005 | 180.0 | 230 |
| 715 | Origin 125a | Beacon | C | Quantum Drive | 0.9 | 0.005 | 180.0 | 161 |
| 716 | Origin 125a | Colossus | B | Quantum Drive | 0.9 | 0.005 | 180.0 | 241 |
| 717 | Origin 125a | VK-00 | A | Quantum Drive | 0.9 | 0.005 | 180.0 | 210 |
| 718 | Origin 125a | Vulcan | D | Quantum Drive | 0.9 | 0.005 | 180.0 | 197 |
| 719 | Origin 125a | Wayfare | D | Quantum Drive | 0.9 | 0.005 | 180.0 | 170 |
| 720 | Origin 125a | Expedition ★ | C | Quantum Drive | 0.9 | 0.005 | 180.0 | 189 |
| 721 | Origin 125a | Rush | C | Quantum Drive | 0.9 | 0.005 | 180.0 | 209 |
| 722 | Origin 135c | Goliath | C | Quantum Drive | 0.9 | 0.005 | 180.0 | 219 |
| 723 | Origin 135c | Siren | B | Quantum Drive | 0.9 | 0.005 | 180.0 | 178 |
| 724 | Origin 135c | Voyage | B | Quantum Drive | 0.9 | 0.005 | 180.0 | 208 |
| 725 | Origin 135c | Eos | C | Quantum Drive | 0.9 | 0.005 | 180.0 | 199 |
| 726 | Origin 135c | Flood | D | Quantum Drive | 0.9 | 0.005 | 180.0 | 188 |
| 727 | Origin 135c | LightFire | C | Quantum Drive | 0.9 | 0.005 | 180.0 | 239 |
| 728 | Origin 135c | Hyperion | B | Quantum Drive | 0.9 | 0.005 | 180.0 | 219 |
| 729 | Origin 135c | Atlas | A | Quantum Drive | 0.9 | 0.005 | 180.0 | 259 |
| 730 | Origin 135c | FoxFire | B | Quantum Drive | 0.9 | 0.005 | 180.0 | 263 |
| 731 | Origin 135c | Burst | B | Quantum Drive | 0.9 | 0.005 | 180.0 | 230 |
| 732 | Origin 135c | Beacon | C | Quantum Drive | 0.9 | 0.005 | 180.0 | 161 |
| 733 | Origin 135c | Colossus | B | Quantum Drive | 0.9 | 0.005 | 180.0 | 241 |
| 734 | Origin 135c | VK-00 | A | Quantum Drive | 0.9 | 0.005 | 180.0 | 210 |
| 735 | Origin 135c | Vulcan | D | Quantum Drive | 0.9 | 0.005 | 180.0 | 197 |
| 736 | Origin 135c | Wayfare | D | Quantum Drive | 0.9 | 0.005 | 180.0 | 170 |
| 737 | Origin 135c | Expedition ★ | C | Quantum Drive | 0.9 | 0.005 | 180.0 | 189 |
| 738 | Origin 135c | Rush | C | Quantum Drive | 0.9 | 0.005 | 180.0 | 209 |
| 739 | Origin 315p | Goliath ★ | C | Quantum Drive | 0.9 | 0.005 | 180.0 | 219 |
| 740 | Origin 315p | Siren | B | Quantum Drive | 0.9 | 0.005 | 180.0 | 178 |
| 741 | Origin 315p | Voyage | B | Quantum Drive | 0.9 | 0.005 | 180.0 | 208 |
| 742 | Origin 315p | Eos | C | Quantum Drive | 0.9 | 0.005 | 180.0 | 199 |
| 743 | Origin 315p | Flood | D | Quantum Drive | 0.9 | 0.005 | 180.0 | 188 |
| 744 | Origin 315p | LightFire | C | Quantum Drive | 0.9 | 0.005 | 180.0 | 239 |
| 745 | Origin 315p | Hyperion | B | Quantum Drive | 0.9 | 0.005 | 180.0 | 219 |
| 746 | Origin 315p | Atlas | A | Quantum Drive | 0.9 | 0.005 | 180.0 | 259 |
| 747 | Origin 315p | FoxFire | B | Quantum Drive | 0.9 | 0.005 | 180.0 | 263 |
| 748 | Origin 315p | Burst | B | Quantum Drive | 0.9 | 0.005 | 180.0 | 230 |
| 749 | Origin 315p | Beacon | C | Quantum Drive | 0.9 | 0.005 | 180.0 | 161 |
| 750 | Origin 315p | Colossus | B | Quantum Drive | 0.9 | 0.005 | 180.0 | 241 |
| 751 | Origin 315p | VK-00 | A | Quantum Drive | 0.9 | 0.005 | 180.0 | 210 |
| 752 | Origin 315p | Vulcan | D | Quantum Drive | 0.9 | 0.005 | 180.0 | 197 |
| 753 | Origin 315p | Wayfare | D | Quantum Drive | 0.9 | 0.005 | 180.0 | 170 |
| 754 | Origin 315p | Expedition | C | Quantum Drive | 0.9 | 0.005 | 180.0 | 189 |
| 755 | Origin 315p | Rush | C | Quantum Drive | 0.9 | 0.005 | 180.0 | 209 |
| 756 | RSI Aurora Mk II | Goliath | C | Quantum Drive | 0.9 | 0.005 | 180.0 | 219 |
| 757 | RSI Aurora Mk II | Siren | B | Quantum Drive | 0.9 | 0.005 | 180.0 | 178 |
| 758 | RSI Aurora Mk II | Voyage | B | Quantum Drive | 0.9 | 0.005 | 180.0 | 208 |
| 759 | RSI Aurora Mk II | Eos ★ | C | Quantum Drive | 0.9 | 0.005 | 180.0 | 199 |
| 760 | RSI Aurora Mk II | Flood | D | Quantum Drive | 0.9 | 0.005 | 180.0 | 188 |
| 761 | RSI Aurora Mk II | LightFire | C | Quantum Drive | 0.9 | 0.005 | 180.0 | 239 |
| 762 | RSI Aurora Mk II | Hyperion | B | Quantum Drive | 0.9 | 0.005 | 180.0 | 219 |
| 763 | RSI Aurora Mk II | Atlas | A | Quantum Drive | 0.9 | 0.005 | 180.0 | 259 |
| 764 | RSI Aurora Mk II | FoxFire | B | Quantum Drive | 0.9 | 0.005 | 180.0 | 263 |
| 765 | RSI Aurora Mk II | Burst | B | Quantum Drive | 0.9 | 0.005 | 180.0 | 230 |
| 766 | RSI Aurora Mk II | Beacon | C | Quantum Drive | 0.9 | 0.005 | 180.0 | 161 |
| 767 | RSI Aurora Mk II | Colossus | B | Quantum Drive | 0.9 | 0.005 | 180.0 | 241 |
| 768 | RSI Aurora Mk II | VK-00 | A | Quantum Drive | 0.9 | 0.005 | 180.0 | 210 |
| 769 | RSI Aurora Mk II | Vulcan | D | Quantum Drive | 0.9 | 0.005 | 180.0 | 197 |
| 770 | RSI Aurora Mk II | Wayfare | D | Quantum Drive | 0.9 | 0.005 | 180.0 | 170 |
| 771 | RSI Aurora Mk II | Expedition | C | Quantum Drive | 0.9 | 0.005 | 180.0 | 189 |
| 772 | RSI Aurora Mk II | Rush | C | Quantum Drive | 0.9 | 0.005 | 180.0 | 209 |
| 773 | C.O. Mustang Beta | Spectre | A | Quantum Drive | 0.7 | 0.004 | 175.0 | 218 |
| 774 | C.O. Mustang Beta | Zephyr | B | Quantum Drive | 0.7 | 0.004 | 175.0 | 184 |
| 775 | C.O. Mustang Beta | Drift | C | Quantum Drive | 0.7 | 0.004 | 175.0 | 167 |
| 776 | Drake Buccaneer | Spectre | A | Quantum Drive | 0.7 | 0.004 | 175.0 | 218 |
| 777 | Drake Buccaneer | Zephyr | B | Quantum Drive | 0.7 | 0.004 | 175.0 | 184 |
| 778 | Drake Buccaneer | Drift | C | Quantum Drive | 0.7 | 0.004 | 175.0 | 167 |
| 779 | MISC Reliant Kore | Spectre | A | Quantum Drive | 0.7 | 0.004 | 175.0 | 218 |
| 780 | MISC Reliant Kore | Zephyr | B | Quantum Drive | 0.7 | 0.004 | 175.0 | 184 |
| 781 | MISC Reliant Kore | Drift | C | Quantum Drive | 0.7 | 0.004 | 175.0 | 167 |
| 782 | MISC Reliant Mako | Spectre | A | Quantum Drive | 0.7 | 0.004 | 175.0 | 218 |
| 783 | MISC Reliant Mako | Zephyr | B | Quantum Drive | 0.7 | 0.004 | 175.0 | 184 |
| 784 | MISC Reliant Mako | Drift ★ | C | Quantum Drive | 0.7 | 0.004 | 175.0 | 167 |
| 785 | MISC Reliant Tana | Spectre | A | Quantum Drive | 0.7 | 0.004 | 175.0 | 218 |
| 786 | MISC Reliant Tana | Zephyr | B | Quantum Drive | 0.7 | 0.004 | 175.0 | 184 |
| 787 | MISC Reliant Tana | Drift | C | Quantum Drive | 0.7 | 0.004 | 175.0 | 167 |
| 788 | Origin 300i | Spectre | A | Quantum Drive | 0.7 | 0.004 | 175.0 | 218 |
| 789 | Origin 300i | Zephyr | B | Quantum Drive | 0.7 | 0.004 | 175.0 | 184 |
| 790 | Origin 300i | Drift | C | Quantum Drive | 0.7 | 0.004 | 175.0 | 167 |
| 791 | Origin 325a | Spectre | A | Quantum Drive | 0.7 | 0.004 | 175.0 | 218 |
| 792 | Origin 325a | Zephyr | B | Quantum Drive | 0.7 | 0.004 | 175.0 | 184 |
| 793 | Origin 325a | Drift | C | Quantum Drive | 0.7 | 0.004 | 175.0 | 167 |
| 794 | RSI Salvation | Goliath | C | Quantum Drive | 0.8 | 0.005 | 160.0 | 219 |
| 795 | RSI Salvation | Siren | B | Quantum Drive | 0.8 | 0.005 | 160.0 | 178 |
| 796 | RSI Salvation | Voyage | B | Quantum Drive | 0.8 | 0.005 | 160.0 | 208 |
| 797 | RSI Salvation | Eos | C | Quantum Drive | 0.8 | 0.005 | 160.0 | 199 |
| 798 | RSI Salvation | Flood | D | Quantum Drive | 0.8 | 0.005 | 160.0 | 188 |
| 799 | RSI Salvation | LightFire | C | Quantum Drive | 0.8 | 0.005 | 160.0 | 239 |
| 800 | RSI Salvation | Hyperion | B | Quantum Drive | 0.8 | 0.005 | 160.0 | 219 |
| 801 | RSI Salvation | Atlas | A | Quantum Drive | 0.8 | 0.005 | 160.0 | 259 |
| 802 | RSI Salvation | FoxFire | B | Quantum Drive | 0.8 | 0.005 | 160.0 | 263 |
| 803 | RSI Salvation | Burst | B | Quantum Drive | 0.8 | 0.005 | 160.0 | 230 |
| 804 | RSI Salvation | Beacon | C | Quantum Drive | 0.8 | 0.005 | 160.0 | 161 |
| 805 | RSI Salvation | Colossus ★ | B | Quantum Drive | 0.8 | 0.005 | 160.0 | 241 |
| 806 | RSI Salvation | VK-00 | A | Quantum Drive | 0.8 | 0.005 | 160.0 | 210 |
| 807 | RSI Salvation | Vulcan | D | Quantum Drive | 0.8 | 0.005 | 160.0 | 197 |
| 808 | RSI Salvation | Wayfare | D | Quantum Drive | 0.8 | 0.005 | 160.0 | 170 |
| 809 | RSI Salvation | Expedition | C | Quantum Drive | 0.8 | 0.005 | 160.0 | 189 |
| 810 | RSI Salvation | Rush | C | Quantum Drive | 0.8 | 0.005 | 160.0 | 209 |
| 811 | Drake Cutter | Goliath | C | Quantum Drive | 0.8 | 0.005 | 160.0 | 219 |
| 812 | Drake Cutter | Siren | B | Quantum Drive | 0.8 | 0.005 | 160.0 | 178 |
| 813 | Drake Cutter | Voyage | B | Quantum Drive | 0.8 | 0.005 | 160.0 | 208 |
| 814 | Drake Cutter | Eos | C | Quantum Drive | 0.8 | 0.005 | 160.0 | 199 |
| 815 | Drake Cutter | Flood | D | Quantum Drive | 0.8 | 0.005 | 160.0 | 188 |
| 816 | Drake Cutter | LightFire | C | Quantum Drive | 0.8 | 0.005 | 160.0 | 239 |
| 817 | Drake Cutter | Hyperion | B | Quantum Drive | 0.8 | 0.005 | 160.0 | 219 |
| 818 | Drake Cutter | Atlas | A | Quantum Drive | 0.8 | 0.005 | 160.0 | 259 |
| 819 | Drake Cutter | FoxFire ★ | B | Quantum Drive | 0.8 | 0.005 | 160.0 | 263 |
| 820 | Drake Cutter | Burst | B | Quantum Drive | 0.8 | 0.005 | 160.0 | 230 |
| 821 | Drake Cutter | Beacon | C | Quantum Drive | 0.8 | 0.005 | 160.0 | 161 |
| 822 | Drake Cutter | Colossus | B | Quantum Drive | 0.8 | 0.005 | 160.0 | 241 |
| 823 | Drake Cutter | VK-00 | A | Quantum Drive | 0.8 | 0.005 | 160.0 | 210 |
| 824 | Drake Cutter | Vulcan | D | Quantum Drive | 0.8 | 0.005 | 160.0 | 197 |
| 825 | Drake Cutter | Wayfare | D | Quantum Drive | 0.8 | 0.005 | 160.0 | 170 |
| 826 | Drake Cutter | Expedition | C | Quantum Drive | 0.8 | 0.005 | 160.0 | 189 |
| 827 | Drake Cutter | Rush | C | Quantum Drive | 0.8 | 0.005 | 160.0 | 209 |
| 828 | Drake Cutter Scout | Goliath | C | Quantum Drive | 0.8 | 0.005 | 160.0 | 219 |
| 829 | Drake Cutter Scout | Siren | B | Quantum Drive | 0.8 | 0.005 | 160.0 | 178 |
| 830 | Drake Cutter Scout | Voyage | B | Quantum Drive | 0.8 | 0.005 | 160.0 | 208 |
| 831 | Drake Cutter Scout | Eos | C | Quantum Drive | 0.8 | 0.005 | 160.0 | 199 |
| 832 | Drake Cutter Scout | Flood | D | Quantum Drive | 0.8 | 0.005 | 160.0 | 188 |
| 833 | Drake Cutter Scout | LightFire | C | Quantum Drive | 0.8 | 0.005 | 160.0 | 239 |
| 834 | Drake Cutter Scout | Hyperion | B | Quantum Drive | 0.8 | 0.005 | 160.0 | 219 |
| 835 | Drake Cutter Scout | Atlas | A | Quantum Drive | 0.8 | 0.005 | 160.0 | 259 |
| 836 | Drake Cutter Scout | FoxFire ★ | B | Quantum Drive | 0.8 | 0.005 | 160.0 | 263 |
| 837 | Drake Cutter Scout | Burst | B | Quantum Drive | 0.8 | 0.005 | 160.0 | 230 |
| 838 | Drake Cutter Scout | Beacon | C | Quantum Drive | 0.8 | 0.005 | 160.0 | 161 |
| 839 | Drake Cutter Scout | Colossus | B | Quantum Drive | 0.8 | 0.005 | 160.0 | 241 |
| 840 | Drake Cutter Scout | VK-00 | A | Quantum Drive | 0.8 | 0.005 | 160.0 | 210 |
| 841 | Drake Cutter Scout | Vulcan | D | Quantum Drive | 0.8 | 0.005 | 160.0 | 197 |
| 842 | Drake Cutter Scout | Wayfare | D | Quantum Drive | 0.8 | 0.005 | 160.0 | 170 |
| 843 | Drake Cutter Scout | Expedition | C | Quantum Drive | 0.8 | 0.005 | 160.0 | 189 |
| 844 | Drake Cutter Scout | Rush | C | Quantum Drive | 0.8 | 0.005 | 160.0 | 209 |
| 845 | MISC Reliant Sen | Goliath ★ | C | Quantum Drive | 0.8 | 0.005 | 160.0 | 219 |
| 846 | MISC Reliant Sen | Siren | B | Quantum Drive | 0.8 | 0.005 | 160.0 | 178 |
| 847 | MISC Reliant Sen | Voyage | B | Quantum Drive | 0.8 | 0.005 | 160.0 | 208 |
| 848 | MISC Reliant Sen | Eos | C | Quantum Drive | 0.8 | 0.005 | 160.0 | 199 |
| 849 | MISC Reliant Sen | Flood | D | Quantum Drive | 0.8 | 0.005 | 160.0 | 188 |
| 850 | MISC Reliant Sen | LightFire | C | Quantum Drive | 0.8 | 0.005 | 160.0 | 239 |
| 851 | MISC Reliant Sen | Hyperion | B | Quantum Drive | 0.8 | 0.005 | 160.0 | 219 |
| 852 | MISC Reliant Sen | Atlas | A | Quantum Drive | 0.8 | 0.005 | 160.0 | 259 |
| 853 | MISC Reliant Sen | FoxFire | B | Quantum Drive | 0.8 | 0.005 | 160.0 | 263 |
| 854 | MISC Reliant Sen | Burst | B | Quantum Drive | 0.8 | 0.005 | 160.0 | 230 |
| 855 | MISC Reliant Sen | Beacon | C | Quantum Drive | 0.8 | 0.005 | 160.0 | 161 |
| 856 | MISC Reliant Sen | Colossus | B | Quantum Drive | 0.8 | 0.005 | 160.0 | 241 |
| 857 | MISC Reliant Sen | VK-00 | A | Quantum Drive | 0.8 | 0.005 | 160.0 | 210 |
| 858 | MISC Reliant Sen | Vulcan | D | Quantum Drive | 0.8 | 0.005 | 160.0 | 197 |
| 859 | MISC Reliant Sen | Wayfare | D | Quantum Drive | 0.8 | 0.005 | 160.0 | 170 |
| 860 | MISC Reliant Sen | Expedition | C | Quantum Drive | 0.8 | 0.005 | 160.0 | 189 |
| 861 | MISC Reliant Sen | Rush | C | Quantum Drive | 0.8 | 0.005 | 160.0 | 209 |
| 862 | Aegis Avenger Stalker | Spectre | A | Quantum Drive | 0.6 | 0.004 | 150.0 | 218 |
| 863 | Aegis Avenger Stalker | Zephyr | B | Quantum Drive | 0.6 | 0.004 | 150.0 | 184 |
| 864 | Aegis Avenger Stalker | Drift | C | Quantum Drive | 0.6 | 0.004 | 150.0 | 167 |
| 865 | Aegis Avenger Titan | Spectre | A | Quantum Drive | 0.6 | 0.004 | 150.0 | 218 |
| 866 | Aegis Avenger Titan | Zephyr | B | Quantum Drive | 0.6 | 0.004 | 150.0 | 184 |
| 867 | Aegis Avenger Titan | Drift | C | Quantum Drive | 0.6 | 0.004 | 150.0 | 167 |
| 868 | Aegis Avenger Titan Renegade | Spectre | A | Quantum Drive | 0.6 | 0.004 | 150.0 | 218 |
| 869 | Aegis Avenger Titan Renegade | Zephyr | B | Quantum Drive | 0.6 | 0.004 | 150.0 | 184 |
| 870 | Aegis Avenger Titan Renegade | Drift | C | Quantum Drive | 0.6 | 0.004 | 150.0 | 167 |
| 871 | Aegis Avenger Warlock | Spectre | A | Quantum Drive | 0.6 | 0.004 | 150.0 | 218 |
| 872 | Aegis Avenger Warlock | Zephyr | B | Quantum Drive | 0.6 | 0.004 | 150.0 | 184 |
| 873 | Aegis Avenger Warlock | Drift | C | Quantum Drive | 0.6 | 0.004 | 150.0 | 167 |
| 874 | Aegis Gladius | Spectre | A | Quantum Drive | 0.6 | 0.004 | 150.0 | 218 |
| 875 | Aegis Gladius | Zephyr | B | Quantum Drive | 0.6 | 0.004 | 150.0 | 184 |
| 876 | Aegis Gladius | Drift | C | Quantum Drive | 0.6 | 0.004 | 150.0 | 167 |
| 877 | Aegis Gladius Valiant | Spectre | A | Quantum Drive | 0.6 | 0.004 | 150.0 | 218 |
| 878 | Aegis Gladius Valiant | Zephyr | B | Quantum Drive | 0.6 | 0.004 | 150.0 | 184 |
| 879 | Aegis Gladius Valiant | Drift | C | Quantum Drive | 0.6 | 0.004 | 150.0 | 167 |
| 880 | Anvil Arrow | Spectre | A | Quantum Drive | 0.6 | 0.004 | 150.0 | 218 |
| 881 | Anvil Arrow | Zephyr | B | Quantum Drive | 0.6 | 0.004 | 150.0 | 184 |
| 882 | Anvil Arrow | Drift | C | Quantum Drive | 0.6 | 0.004 | 150.0 | 167 |
| 883 | Anvil Hawk | Spectre | A | Quantum Drive | 0.6 | 0.004 | 150.0 | 218 |
| 884 | Anvil Hawk | Zephyr | B | Quantum Drive | 0.6 | 0.004 | 150.0 | 184 |
| 885 | Anvil Hawk | Drift | C | Quantum Drive | 0.6 | 0.004 | 150.0 | 167 |
| 886 | Aopoa Khartu-al | Spectre | A | Quantum Drive | 0.6 | 0.004 | 150.0 | 218 |
| 887 | Aopoa Khartu-al | Zephyr | B | Quantum Drive | 0.6 | 0.004 | 150.0 | 184 |
| 888 | Aopoa Khartu-al | Drift | C | Quantum Drive | 0.6 | 0.004 | 150.0 | 167 |
| 889 | C.O. Mustang Alpha | Spectre | A | Quantum Drive | 0.6 | 0.004 | 150.0 | 218 |
| 890 | C.O. Mustang Alpha | Zephyr | B | Quantum Drive | 0.6 | 0.004 | 150.0 | 184 |
| 891 | C.O. Mustang Alpha | Drift | C | Quantum Drive | 0.6 | 0.004 | 150.0 | 167 |
| 892 | C.O. Mustang Delta | Spectre | A | Quantum Drive | 0.6 | 0.004 | 150.0 | 218 |
| 893 | C.O. Mustang Delta | Zephyr | B | Quantum Drive | 0.6 | 0.004 | 150.0 | 184 |
| 894 | C.O. Mustang Delta | Drift | C | Quantum Drive | 0.6 | 0.004 | 150.0 | 167 |
| 895 | C.O. Mustang Gamma | Spectre | A | Quantum Drive | 0.6 | 0.004 | 150.0 | 218 |
| 896 | C.O. Mustang Gamma | Zephyr | B | Quantum Drive | 0.6 | 0.004 | 150.0 | 184 |
| 897 | C.O. Mustang Gamma | Drift | C | Quantum Drive | 0.6 | 0.004 | 150.0 | 167 |
| 898 | Esperia Blade | Spectre | A | Quantum Drive | 0.6 | 0.004 | 150.0 | 218 |
| 899 | Esperia Blade | Zephyr | B | Quantum Drive | 0.6 | 0.004 | 150.0 | 184 |
| 900 | Esperia Blade | Drift | C | Quantum Drive | 0.6 | 0.004 | 150.0 | 167 |
| 901 | Esperia Talon | Spectre | A | Quantum Drive | 0.6 | 0.004 | 150.0 | 218 |
| 902 | Esperia Talon | Zephyr | B | Quantum Drive | 0.6 | 0.004 | 150.0 | 184 |
| 903 | Esperia Talon | Drift ★ | C | Quantum Drive | 0.6 | 0.004 | 150.0 | 167 |
| 904 | Esperia Talon Shrike | Spectre | A | Quantum Drive | 0.6 | 0.004 | 150.0 | 218 |
| 905 | Esperia Talon Shrike | Zephyr | B | Quantum Drive | 0.6 | 0.004 | 150.0 | 184 |
| 906 | Esperia Talon Shrike | Drift ★ | C | Quantum Drive | 0.6 | 0.004 | 150.0 | 167 |
| 907 | Kruger L-21 Wolf | Spectre | A | Quantum Drive | 0.6 | 0.004 | 150.0 | 218 |
| 908 | Kruger L-21 Wolf | Zephyr | B | Quantum Drive | 0.6 | 0.004 | 150.0 | 184 |
| 909 | Kruger L-21 Wolf | Drift | C | Quantum Drive | 0.6 | 0.004 | 150.0 | 167 |
| 910 | Kruger L-22 Alpha Wolf | Spectre | A | Quantum Drive | 0.6 | 0.004 | 150.0 | 218 |
| 911 | Kruger L-22 Alpha Wolf | Zephyr | B | Quantum Drive | 0.6 | 0.004 | 150.0 | 184 |
| 912 | Kruger L-22 Alpha Wolf | Drift | C | Quantum Drive | 0.6 | 0.004 | 150.0 | 167 |
| 913 | Mirai Razor | Spectre | A | Quantum Drive | 0.6 | 0.004 | 150.0 | 218 |
| 914 | Mirai Razor | Zephyr | B | Quantum Drive | 0.6 | 0.004 | 150.0 | 184 |
| 915 | Mirai Razor | Drift | C | Quantum Drive | 0.6 | 0.004 | 150.0 | 167 |
| 916 | Mirai Razor EX | Spectre | A | Quantum Drive | 0.6 | 0.004 | 150.0 | 218 |
| 917 | Mirai Razor EX | Zephyr | B | Quantum Drive | 0.6 | 0.004 | 150.0 | 184 |
| 918 | Mirai Razor EX | Drift | C | Quantum Drive | 0.6 | 0.004 | 150.0 | 167 |
| 919 | Mirai Razor LX | Spectre | A | Quantum Drive | 0.6 | 0.004 | 150.0 | 218 |
| 920 | Mirai Razor LX | Zephyr | B | Quantum Drive | 0.6 | 0.004 | 150.0 | 184 |
| 921 | Mirai Razor LX | Drift | C | Quantum Drive | 0.6 | 0.004 | 150.0 | 167 |
| 922 | Origin 350r | Spectre | A | Quantum Drive | 0.6 | 0.004 | 150.0 | 218 |
| 923 | Origin 350r | Zephyr | B | Quantum Drive | 0.6 | 0.004 | 150.0 | 184 |
| 924 | Origin 350r | Drift | C | Quantum Drive | 0.6 | 0.004 | 150.0 | 167 |
| 925 | Origin 85X Limited | Spectre | A | Quantum Drive | 0.6 | 0.004 | 150.0 | 218 |
| 926 | Origin 85X Limited | Zephyr | B | Quantum Drive | 0.6 | 0.004 | 150.0 | 184 |
| 927 | Origin 85X Limited | Drift | C | Quantum Drive | 0.6 | 0.004 | 150.0 | 167 |
| 928 | Origin M50 Interceptor | Spectre | A | Quantum Drive | 0.6 | 0.004 | 150.0 | 218 |
| 929 | Origin M50 Interceptor | Zephyr | B | Quantum Drive | 0.6 | 0.004 | 150.0 | 184 |
| 930 | Origin M50 Interceptor | Drift | C | Quantum Drive | 0.6 | 0.004 | 150.0 | 167 |
| 931 | C.O. Mustang Beta | Goliath | C | Quantum Drive | 0.7 | 0.005 | 140.0 | 219 |
| 932 | C.O. Mustang Beta | Siren | B | Quantum Drive | 0.7 | 0.005 | 140.0 | 178 |
| 933 | C.O. Mustang Beta | Voyage | B | Quantum Drive | 0.7 | 0.005 | 140.0 | 208 |
| 934 | C.O. Mustang Beta | Eos | C | Quantum Drive | 0.7 | 0.005 | 140.0 | 199 |
| 935 | C.O. Mustang Beta | Flood | D | Quantum Drive | 0.7 | 0.005 | 140.0 | 188 |
| 936 | C.O. Mustang Beta | LightFire | C | Quantum Drive | 0.7 | 0.005 | 140.0 | 239 |
| 937 | C.O. Mustang Beta | Hyperion | B | Quantum Drive | 0.7 | 0.005 | 140.0 | 219 |
| 938 | C.O. Mustang Beta | Atlas | A | Quantum Drive | 0.7 | 0.005 | 140.0 | 259 |
| 939 | C.O. Mustang Beta | FoxFire | B | Quantum Drive | 0.7 | 0.005 | 140.0 | 263 |
| 940 | C.O. Mustang Beta | Burst | B | Quantum Drive | 0.7 | 0.005 | 140.0 | 230 |
| 941 | C.O. Mustang Beta | Beacon | C | Quantum Drive | 0.7 | 0.005 | 140.0 | 161 |
| 942 | C.O. Mustang Beta | Colossus | B | Quantum Drive | 0.7 | 0.005 | 140.0 | 241 |
| 943 | C.O. Mustang Beta | VK-00 | A | Quantum Drive | 0.7 | 0.005 | 140.0 | 210 |
| 944 | C.O. Mustang Beta | Vulcan | D | Quantum Drive | 0.7 | 0.005 | 140.0 | 197 |
| 945 | C.O. Mustang Beta | Wayfare | D | Quantum Drive | 0.7 | 0.005 | 140.0 | 170 |
| 946 | C.O. Mustang Beta | Expedition | C | Quantum Drive | 0.7 | 0.005 | 140.0 | 189 |
| 947 | C.O. Mustang Beta | Rush ★ | C | Quantum Drive | 0.7 | 0.005 | 140.0 | 209 |
| 948 | Drake Buccaneer | Goliath | C | Quantum Drive | 0.7 | 0.005 | 140.0 | 219 |
| 949 | Drake Buccaneer | Siren | B | Quantum Drive | 0.7 | 0.005 | 140.0 | 178 |
| 950 | Drake Buccaneer | Voyage | B | Quantum Drive | 0.7 | 0.005 | 140.0 | 208 |
| 951 | Drake Buccaneer | Eos | C | Quantum Drive | 0.7 | 0.005 | 140.0 | 199 |
| 952 | Drake Buccaneer | Flood | D | Quantum Drive | 0.7 | 0.005 | 140.0 | 188 |
| 953 | Drake Buccaneer | LightFire | C | Quantum Drive | 0.7 | 0.005 | 140.0 | 239 |
| 954 | Drake Buccaneer | Hyperion | B | Quantum Drive | 0.7 | 0.005 | 140.0 | 219 |
| 955 | Drake Buccaneer | Atlas | A | Quantum Drive | 0.7 | 0.005 | 140.0 | 259 |
| 956 | Drake Buccaneer | FoxFire | B | Quantum Drive | 0.7 | 0.005 | 140.0 | 263 |
| 957 | Drake Buccaneer | Burst | B | Quantum Drive | 0.7 | 0.005 | 140.0 | 230 |
| 958 | Drake Buccaneer | Beacon | C | Quantum Drive | 0.7 | 0.005 | 140.0 | 161 |
| 959 | Drake Buccaneer | Colossus | B | Quantum Drive | 0.7 | 0.005 | 140.0 | 241 |
| 960 | Drake Buccaneer | VK-00 | A | Quantum Drive | 0.7 | 0.005 | 140.0 | 210 |
| 961 | Drake Buccaneer | Vulcan | D | Quantum Drive | 0.7 | 0.005 | 140.0 | 197 |
| 962 | Drake Buccaneer | Wayfare | D | Quantum Drive | 0.7 | 0.005 | 140.0 | 170 |
| 963 | Drake Buccaneer | Expedition | C | Quantum Drive | 0.7 | 0.005 | 140.0 | 189 |
| 964 | Drake Buccaneer | Rush ★ | C | Quantum Drive | 0.7 | 0.005 | 140.0 | 209 |
| 965 | MISC Reliant Kore | Goliath | C | Quantum Drive | 0.7 | 0.005 | 140.0 | 219 |
| 966 | MISC Reliant Kore | Siren | B | Quantum Drive | 0.7 | 0.005 | 140.0 | 178 |
| 967 | MISC Reliant Kore | Voyage | B | Quantum Drive | 0.7 | 0.005 | 140.0 | 208 |
| 968 | MISC Reliant Kore | Eos | C | Quantum Drive | 0.7 | 0.005 | 140.0 | 199 |
| 969 | MISC Reliant Kore | Flood | D | Quantum Drive | 0.7 | 0.005 | 140.0 | 188 |
| 970 | MISC Reliant Kore | LightFire | C | Quantum Drive | 0.7 | 0.005 | 140.0 | 239 |
| 971 | MISC Reliant Kore | Hyperion | B | Quantum Drive | 0.7 | 0.005 | 140.0 | 219 |
| 972 | MISC Reliant Kore | Atlas | A | Quantum Drive | 0.7 | 0.005 | 140.0 | 259 |
| 973 | MISC Reliant Kore | FoxFire | B | Quantum Drive | 0.7 | 0.005 | 140.0 | 263 |
| 974 | MISC Reliant Kore | Burst | B | Quantum Drive | 0.7 | 0.005 | 140.0 | 230 |
| 975 | MISC Reliant Kore | Beacon | C | Quantum Drive | 0.7 | 0.005 | 140.0 | 161 |
| 976 | MISC Reliant Kore | Colossus | B | Quantum Drive | 0.7 | 0.005 | 140.0 | 241 |
| 977 | MISC Reliant Kore | VK-00 | A | Quantum Drive | 0.7 | 0.005 | 140.0 | 210 |
| 978 | MISC Reliant Kore | Vulcan | D | Quantum Drive | 0.7 | 0.005 | 140.0 | 197 |
| 979 | MISC Reliant Kore | Wayfare | D | Quantum Drive | 0.7 | 0.005 | 140.0 | 170 |
| 980 | MISC Reliant Kore | Expedition | C | Quantum Drive | 0.7 | 0.005 | 140.0 | 189 |
| 981 | MISC Reliant Kore | Rush ★ | C | Quantum Drive | 0.7 | 0.005 | 140.0 | 209 |
| 982 | MISC Reliant Mako | Goliath | C | Quantum Drive | 0.7 | 0.005 | 140.0 | 219 |
| 983 | MISC Reliant Mako | Siren | B | Quantum Drive | 0.7 | 0.005 | 140.0 | 178 |
| 984 | MISC Reliant Mako | Voyage | B | Quantum Drive | 0.7 | 0.005 | 140.0 | 208 |
| 985 | MISC Reliant Mako | Eos | C | Quantum Drive | 0.7 | 0.005 | 140.0 | 199 |
| 986 | MISC Reliant Mako | Flood | D | Quantum Drive | 0.7 | 0.005 | 140.0 | 188 |
| 987 | MISC Reliant Mako | LightFire | C | Quantum Drive | 0.7 | 0.005 | 140.0 | 239 |
| 988 | MISC Reliant Mako | Hyperion | B | Quantum Drive | 0.7 | 0.005 | 140.0 | 219 |
| 989 | MISC Reliant Mako | Atlas | A | Quantum Drive | 0.7 | 0.005 | 140.0 | 259 |
| 990 | MISC Reliant Mako | FoxFire | B | Quantum Drive | 0.7 | 0.005 | 140.0 | 263 |
| 991 | MISC Reliant Mako | Burst | B | Quantum Drive | 0.7 | 0.005 | 140.0 | 230 |
| 992 | MISC Reliant Mako | Beacon | C | Quantum Drive | 0.7 | 0.005 | 140.0 | 161 |
| 993 | MISC Reliant Mako | Colossus | B | Quantum Drive | 0.7 | 0.005 | 140.0 | 241 |
| 994 | MISC Reliant Mako | VK-00 | A | Quantum Drive | 0.7 | 0.005 | 140.0 | 210 |
| 995 | MISC Reliant Mako | Vulcan | D | Quantum Drive | 0.7 | 0.005 | 140.0 | 197 |
| 996 | MISC Reliant Mako | Wayfare | D | Quantum Drive | 0.7 | 0.005 | 140.0 | 170 |
| 997 | MISC Reliant Mako | Expedition | C | Quantum Drive | 0.7 | 0.005 | 140.0 | 189 |
| 998 | MISC Reliant Mako | Rush | C | Quantum Drive | 0.7 | 0.005 | 140.0 | 209 |
| 999 | MISC Reliant Tana | Goliath | C | Quantum Drive | 0.7 | 0.005 | 140.0 | 219 |
| 1000 | MISC Reliant Tana | Siren | B | Quantum Drive | 0.7 | 0.005 | 140.0 | 178 |
| 1001 | MISC Reliant Tana | Voyage | B | Quantum Drive | 0.7 | 0.005 | 140.0 | 208 |
| 1002 | MISC Reliant Tana | Eos | C | Quantum Drive | 0.7 | 0.005 | 140.0 | 199 |
| 1003 | MISC Reliant Tana | Flood | D | Quantum Drive | 0.7 | 0.005 | 140.0 | 188 |
| 1004 | MISC Reliant Tana | LightFire | C | Quantum Drive | 0.7 | 0.005 | 140.0 | 239 |
| 1005 | MISC Reliant Tana | Hyperion | B | Quantum Drive | 0.7 | 0.005 | 140.0 | 219 |
| 1006 | MISC Reliant Tana | Atlas | A | Quantum Drive | 0.7 | 0.005 | 140.0 | 259 |
| 1007 | MISC Reliant Tana | FoxFire | B | Quantum Drive | 0.7 | 0.005 | 140.0 | 263 |
| 1008 | MISC Reliant Tana | Burst | B | Quantum Drive | 0.7 | 0.005 | 140.0 | 230 |
| 1009 | MISC Reliant Tana | Beacon ★ | C | Quantum Drive | 0.7 | 0.005 | 140.0 | 161 |
| 1010 | MISC Reliant Tana | Colossus | B | Quantum Drive | 0.7 | 0.005 | 140.0 | 241 |
| 1011 | MISC Reliant Tana | VK-00 | A | Quantum Drive | 0.7 | 0.005 | 140.0 | 210 |
| 1012 | MISC Reliant Tana | Vulcan | D | Quantum Drive | 0.7 | 0.005 | 140.0 | 197 |
| 1013 | MISC Reliant Tana | Wayfare | D | Quantum Drive | 0.7 | 0.005 | 140.0 | 170 |
| 1014 | MISC Reliant Tana | Expedition | C | Quantum Drive | 0.7 | 0.005 | 140.0 | 189 |
| 1015 | MISC Reliant Tana | Rush | C | Quantum Drive | 0.7 | 0.005 | 140.0 | 209 |
| 1016 | Origin 300i | Goliath | C | Quantum Drive | 0.7 | 0.005 | 140.0 | 219 |
| 1017 | Origin 300i | Siren | B | Quantum Drive | 0.7 | 0.005 | 140.0 | 178 |
| 1018 | Origin 300i | Voyage | B | Quantum Drive | 0.7 | 0.005 | 140.0 | 208 |
| 1019 | Origin 300i | Eos | C | Quantum Drive | 0.7 | 0.005 | 140.0 | 199 |
| 1020 | Origin 300i | Flood | D | Quantum Drive | 0.7 | 0.005 | 140.0 | 188 |
| 1021 | Origin 300i | LightFire | C | Quantum Drive | 0.7 | 0.005 | 140.0 | 239 |
| 1022 | Origin 300i | Hyperion | B | Quantum Drive | 0.7 | 0.005 | 140.0 | 219 |
| 1023 | Origin 300i | Atlas | A | Quantum Drive | 0.7 | 0.005 | 140.0 | 259 |
| 1024 | Origin 300i | FoxFire | B | Quantum Drive | 0.7 | 0.005 | 140.0 | 263 |
| 1025 | Origin 300i | Burst | B | Quantum Drive | 0.7 | 0.005 | 140.0 | 230 |
| 1026 | Origin 300i | Beacon | C | Quantum Drive | 0.7 | 0.005 | 140.0 | 161 |
| 1027 | Origin 300i | Colossus | B | Quantum Drive | 0.7 | 0.005 | 140.0 | 241 |
| 1028 | Origin 300i | VK-00 | A | Quantum Drive | 0.7 | 0.005 | 140.0 | 210 |
| 1029 | Origin 300i | Vulcan | D | Quantum Drive | 0.7 | 0.005 | 140.0 | 197 |
| 1030 | Origin 300i | Wayfare | D | Quantum Drive | 0.7 | 0.005 | 140.0 | 170 |
| 1031 | Origin 300i | Expedition ★ | C | Quantum Drive | 0.7 | 0.005 | 140.0 | 189 |
| 1032 | Origin 300i | Rush | C | Quantum Drive | 0.7 | 0.005 | 140.0 | 209 |
| 1033 | Origin 325a | Goliath | C | Quantum Drive | 0.7 | 0.005 | 140.0 | 219 |
| 1034 | Origin 325a | Siren | B | Quantum Drive | 0.7 | 0.005 | 140.0 | 178 |
| 1035 | Origin 325a | Voyage | B | Quantum Drive | 0.7 | 0.005 | 140.0 | 208 |
| 1036 | Origin 325a | Eos | C | Quantum Drive | 0.7 | 0.005 | 140.0 | 199 |
| 1037 | Origin 325a | Flood | D | Quantum Drive | 0.7 | 0.005 | 140.0 | 188 |
| 1038 | Origin 325a | LightFire | C | Quantum Drive | 0.7 | 0.005 | 140.0 | 239 |
| 1039 | Origin 325a | Hyperion | B | Quantum Drive | 0.7 | 0.005 | 140.0 | 219 |
| 1040 | Origin 325a | Atlas | A | Quantum Drive | 0.7 | 0.005 | 140.0 | 259 |
| 1041 | Origin 325a | FoxFire | B | Quantum Drive | 0.7 | 0.005 | 140.0 | 263 |
| 1042 | Origin 325a | Burst | B | Quantum Drive | 0.7 | 0.005 | 140.0 | 230 |
| 1043 | Origin 325a | Beacon ★ | C | Quantum Drive | 0.7 | 0.005 | 140.0 | 161 |
| 1044 | Origin 325a | Colossus | B | Quantum Drive | 0.7 | 0.005 | 140.0 | 241 |
| 1045 | Origin 325a | VK-00 | A | Quantum Drive | 0.7 | 0.005 | 140.0 | 210 |
| 1046 | Origin 325a | Vulcan | D | Quantum Drive | 0.7 | 0.005 | 140.0 | 197 |
| 1047 | Origin 325a | Wayfare | D | Quantum Drive | 0.7 | 0.005 | 140.0 | 170 |
| 1048 | Origin 325a | Expedition | C | Quantum Drive | 0.7 | 0.005 | 140.0 | 189 |
| 1049 | Origin 325a | Rush | C | Quantum Drive | 0.7 | 0.005 | 140.0 | 209 |
| 1050 | Aegis Avenger Stalker | Goliath | C | Quantum Drive | 0.6 | 0.005 | 120.0 | 219 |
| 1051 | Aegis Avenger Stalker | Siren | B | Quantum Drive | 0.6 | 0.005 | 120.0 | 178 |
| 1052 | Aegis Avenger Stalker | Voyage | B | Quantum Drive | 0.6 | 0.005 | 120.0 | 208 |
| 1053 | Aegis Avenger Stalker | Eos | C | Quantum Drive | 0.6 | 0.005 | 120.0 | 199 |
| 1054 | Aegis Avenger Stalker | Flood | D | Quantum Drive | 0.6 | 0.005 | 120.0 | 188 |
| 1055 | Aegis Avenger Stalker | LightFire | C | Quantum Drive | 0.6 | 0.005 | 120.0 | 239 |
| 1056 | Aegis Avenger Stalker | Hyperion | B | Quantum Drive | 0.6 | 0.005 | 120.0 | 219 |
| 1057 | Aegis Avenger Stalker | Atlas | A | Quantum Drive | 0.6 | 0.005 | 120.0 | 259 |
| 1058 | Aegis Avenger Stalker | FoxFire | B | Quantum Drive | 0.6 | 0.005 | 120.0 | 263 |
| 1059 | Aegis Avenger Stalker | Burst | B | Quantum Drive | 0.6 | 0.005 | 120.0 | 230 |
| 1060 | Aegis Avenger Stalker | Beacon | C | Quantum Drive | 0.6 | 0.005 | 120.0 | 161 |
| 1061 | Aegis Avenger Stalker | Colossus | B | Quantum Drive | 0.6 | 0.005 | 120.0 | 241 |
| 1062 | Aegis Avenger Stalker | VK-00 | A | Quantum Drive | 0.6 | 0.005 | 120.0 | 210 |
| 1063 | Aegis Avenger Stalker | Vulcan | D | Quantum Drive | 0.6 | 0.005 | 120.0 | 197 |
| 1064 | Aegis Avenger Stalker | Wayfare | D | Quantum Drive | 0.6 | 0.005 | 120.0 | 170 |
| 1065 | Aegis Avenger Stalker | Expedition ★ | C | Quantum Drive | 0.6 | 0.005 | 120.0 | 189 |
| 1066 | Aegis Avenger Stalker | Rush | C | Quantum Drive | 0.6 | 0.005 | 120.0 | 209 |
| 1067 | Aegis Avenger Titan | Goliath | C | Quantum Drive | 0.6 | 0.005 | 120.0 | 219 |
| 1068 | Aegis Avenger Titan | Siren | B | Quantum Drive | 0.6 | 0.005 | 120.0 | 178 |
| 1069 | Aegis Avenger Titan | Voyage | B | Quantum Drive | 0.6 | 0.005 | 120.0 | 208 |
| 1070 | Aegis Avenger Titan | Eos | C | Quantum Drive | 0.6 | 0.005 | 120.0 | 199 |
| 1071 | Aegis Avenger Titan | Flood | D | Quantum Drive | 0.6 | 0.005 | 120.0 | 188 |
| 1072 | Aegis Avenger Titan | LightFire | C | Quantum Drive | 0.6 | 0.005 | 120.0 | 239 |
| 1073 | Aegis Avenger Titan | Hyperion | B | Quantum Drive | 0.6 | 0.005 | 120.0 | 219 |
| 1074 | Aegis Avenger Titan | Atlas | A | Quantum Drive | 0.6 | 0.005 | 120.0 | 259 |
| 1075 | Aegis Avenger Titan | FoxFire | B | Quantum Drive | 0.6 | 0.005 | 120.0 | 263 |
| 1076 | Aegis Avenger Titan | Burst | B | Quantum Drive | 0.6 | 0.005 | 120.0 | 230 |
| 1077 | Aegis Avenger Titan | Beacon | C | Quantum Drive | 0.6 | 0.005 | 120.0 | 161 |
| 1078 | Aegis Avenger Titan | Colossus | B | Quantum Drive | 0.6 | 0.005 | 120.0 | 241 |
| 1079 | Aegis Avenger Titan | VK-00 | A | Quantum Drive | 0.6 | 0.005 | 120.0 | 210 |
| 1080 | Aegis Avenger Titan | Vulcan | D | Quantum Drive | 0.6 | 0.005 | 120.0 | 197 |
| 1081 | Aegis Avenger Titan | Wayfare | D | Quantum Drive | 0.6 | 0.005 | 120.0 | 170 |
| 1082 | Aegis Avenger Titan | Expedition ★ | C | Quantum Drive | 0.6 | 0.005 | 120.0 | 189 |
| 1083 | Aegis Avenger Titan | Rush | C | Quantum Drive | 0.6 | 0.005 | 120.0 | 209 |
| 1084 | Aegis Avenger Titan Renegade | Goliath | C | Quantum Drive | 0.6 | 0.005 | 120.0 | 219 |
| 1085 | Aegis Avenger Titan Renegade | Siren | B | Quantum Drive | 0.6 | 0.005 | 120.0 | 178 |
| 1086 | Aegis Avenger Titan Renegade | Voyage | B | Quantum Drive | 0.6 | 0.005 | 120.0 | 208 |
| 1087 | Aegis Avenger Titan Renegade | Eos | C | Quantum Drive | 0.6 | 0.005 | 120.0 | 199 |
| 1088 | Aegis Avenger Titan Renegade | Flood | D | Quantum Drive | 0.6 | 0.005 | 120.0 | 188 |
| 1089 | Aegis Avenger Titan Renegade | LightFire | C | Quantum Drive | 0.6 | 0.005 | 120.0 | 239 |
| 1090 | Aegis Avenger Titan Renegade | Hyperion | B | Quantum Drive | 0.6 | 0.005 | 120.0 | 219 |
| 1091 | Aegis Avenger Titan Renegade | Atlas | A | Quantum Drive | 0.6 | 0.005 | 120.0 | 259 |
| 1092 | Aegis Avenger Titan Renegade | FoxFire | B | Quantum Drive | 0.6 | 0.005 | 120.0 | 263 |
| 1093 | Aegis Avenger Titan Renegade | Burst | B | Quantum Drive | 0.6 | 0.005 | 120.0 | 230 |
| 1094 | Aegis Avenger Titan Renegade | Beacon | C | Quantum Drive | 0.6 | 0.005 | 120.0 | 161 |
| 1095 | Aegis Avenger Titan Renegade | Colossus | B | Quantum Drive | 0.6 | 0.005 | 120.0 | 241 |
| 1096 | Aegis Avenger Titan Renegade | VK-00 | A | Quantum Drive | 0.6 | 0.005 | 120.0 | 210 |
| 1097 | Aegis Avenger Titan Renegade | Vulcan | D | Quantum Drive | 0.6 | 0.005 | 120.0 | 197 |
| 1098 | Aegis Avenger Titan Renegade | Wayfare | D | Quantum Drive | 0.6 | 0.005 | 120.0 | 170 |
| 1099 | Aegis Avenger Titan Renegade | Expedition ★ | C | Quantum Drive | 0.6 | 0.005 | 120.0 | 189 |
| 1100 | Aegis Avenger Titan Renegade | Rush | C | Quantum Drive | 0.6 | 0.005 | 120.0 | 209 |
| 1101 | Aegis Avenger Warlock | Goliath | C | Quantum Drive | 0.6 | 0.005 | 120.0 | 219 |
| 1102 | Aegis Avenger Warlock | Siren | B | Quantum Drive | 0.6 | 0.005 | 120.0 | 178 |
| 1103 | Aegis Avenger Warlock | Voyage | B | Quantum Drive | 0.6 | 0.005 | 120.0 | 208 |
| 1104 | Aegis Avenger Warlock | Eos | C | Quantum Drive | 0.6 | 0.005 | 120.0 | 199 |
| 1105 | Aegis Avenger Warlock | Flood | D | Quantum Drive | 0.6 | 0.005 | 120.0 | 188 |
| 1106 | Aegis Avenger Warlock | LightFire | C | Quantum Drive | 0.6 | 0.005 | 120.0 | 239 |
| 1107 | Aegis Avenger Warlock | Hyperion | B | Quantum Drive | 0.6 | 0.005 | 120.0 | 219 |
| 1108 | Aegis Avenger Warlock | Atlas | A | Quantum Drive | 0.6 | 0.005 | 120.0 | 259 |
| 1109 | Aegis Avenger Warlock | FoxFire | B | Quantum Drive | 0.6 | 0.005 | 120.0 | 263 |
| 1110 | Aegis Avenger Warlock | Burst | B | Quantum Drive | 0.6 | 0.005 | 120.0 | 230 |
| 1111 | Aegis Avenger Warlock | Beacon | C | Quantum Drive | 0.6 | 0.005 | 120.0 | 161 |
| 1112 | Aegis Avenger Warlock | Colossus | B | Quantum Drive | 0.6 | 0.005 | 120.0 | 241 |
| 1113 | Aegis Avenger Warlock | VK-00 | A | Quantum Drive | 0.6 | 0.005 | 120.0 | 210 |
| 1114 | Aegis Avenger Warlock | Vulcan | D | Quantum Drive | 0.6 | 0.005 | 120.0 | 197 |
| 1115 | Aegis Avenger Warlock | Wayfare | D | Quantum Drive | 0.6 | 0.005 | 120.0 | 170 |
| 1116 | Aegis Avenger Warlock | Expedition ★ | C | Quantum Drive | 0.6 | 0.005 | 120.0 | 189 |
| 1117 | Aegis Avenger Warlock | Rush | C | Quantum Drive | 0.6 | 0.005 | 120.0 | 209 |
| 1118 | Aegis Gladius | Goliath | C | Quantum Drive | 0.6 | 0.005 | 120.0 | 219 |
| 1119 | Aegis Gladius | Siren | B | Quantum Drive | 0.6 | 0.005 | 120.0 | 178 |
| 1120 | Aegis Gladius | Voyage | B | Quantum Drive | 0.6 | 0.005 | 120.0 | 208 |
| 1121 | Aegis Gladius | Eos | C | Quantum Drive | 0.6 | 0.005 | 120.0 | 199 |
| 1122 | Aegis Gladius | Flood | D | Quantum Drive | 0.6 | 0.005 | 120.0 | 188 |
| 1123 | Aegis Gladius | LightFire | C | Quantum Drive | 0.6 | 0.005 | 120.0 | 239 |
| 1124 | Aegis Gladius | Hyperion | B | Quantum Drive | 0.6 | 0.005 | 120.0 | 219 |
| 1125 | Aegis Gladius | Atlas | A | Quantum Drive | 0.6 | 0.005 | 120.0 | 259 |
| 1126 | Aegis Gladius | FoxFire | B | Quantum Drive | 0.6 | 0.005 | 120.0 | 263 |
| 1127 | Aegis Gladius | Burst | B | Quantum Drive | 0.6 | 0.005 | 120.0 | 230 |
| 1128 | Aegis Gladius | Beacon ★ | C | Quantum Drive | 0.6 | 0.005 | 120.0 | 161 |
| 1129 | Aegis Gladius | Colossus | B | Quantum Drive | 0.6 | 0.005 | 120.0 | 241 |
| 1130 | Aegis Gladius | VK-00 | A | Quantum Drive | 0.6 | 0.005 | 120.0 | 210 |
| 1131 | Aegis Gladius | Vulcan | D | Quantum Drive | 0.6 | 0.005 | 120.0 | 197 |
| 1132 | Aegis Gladius | Wayfare | D | Quantum Drive | 0.6 | 0.005 | 120.0 | 170 |
| 1133 | Aegis Gladius | Expedition | C | Quantum Drive | 0.6 | 0.005 | 120.0 | 189 |
| 1134 | Aegis Gladius | Rush | C | Quantum Drive | 0.6 | 0.005 | 120.0 | 209 |
| 1135 | Aegis Gladius Valiant | Goliath | C | Quantum Drive | 0.6 | 0.005 | 120.0 | 219 |
| 1136 | Aegis Gladius Valiant | Siren | B | Quantum Drive | 0.6 | 0.005 | 120.0 | 178 |
| 1137 | Aegis Gladius Valiant | Voyage | B | Quantum Drive | 0.6 | 0.005 | 120.0 | 208 |
| 1138 | Aegis Gladius Valiant | Eos | C | Quantum Drive | 0.6 | 0.005 | 120.0 | 199 |
| 1139 | Aegis Gladius Valiant | Flood | D | Quantum Drive | 0.6 | 0.005 | 120.0 | 188 |
| 1140 | Aegis Gladius Valiant | LightFire | C | Quantum Drive | 0.6 | 0.005 | 120.0 | 239 |
| 1141 | Aegis Gladius Valiant | Hyperion | B | Quantum Drive | 0.6 | 0.005 | 120.0 | 219 |
| 1142 | Aegis Gladius Valiant | Atlas | A | Quantum Drive | 0.6 | 0.005 | 120.0 | 259 |
| 1143 | Aegis Gladius Valiant | FoxFire | B | Quantum Drive | 0.6 | 0.005 | 120.0 | 263 |
| 1144 | Aegis Gladius Valiant | Burst | B | Quantum Drive | 0.6 | 0.005 | 120.0 | 230 |
| 1145 | Aegis Gladius Valiant | Beacon ★ | C | Quantum Drive | 0.6 | 0.005 | 120.0 | 161 |
| 1146 | Aegis Gladius Valiant | Colossus | B | Quantum Drive | 0.6 | 0.005 | 120.0 | 241 |
| 1147 | Aegis Gladius Valiant | VK-00 | A | Quantum Drive | 0.6 | 0.005 | 120.0 | 210 |
| 1148 | Aegis Gladius Valiant | Vulcan | D | Quantum Drive | 0.6 | 0.005 | 120.0 | 197 |
| 1149 | Aegis Gladius Valiant | Wayfare | D | Quantum Drive | 0.6 | 0.005 | 120.0 | 170 |
| 1150 | Aegis Gladius Valiant | Expedition | C | Quantum Drive | 0.6 | 0.005 | 120.0 | 189 |
| 1151 | Aegis Gladius Valiant | Rush | C | Quantum Drive | 0.6 | 0.005 | 120.0 | 209 |
| 1152 | Anvil Arrow | Goliath | C | Quantum Drive | 0.6 | 0.005 | 120.0 | 219 |
| 1153 | Anvil Arrow | Siren | B | Quantum Drive | 0.6 | 0.005 | 120.0 | 178 |
| 1154 | Anvil Arrow | Voyage | B | Quantum Drive | 0.6 | 0.005 | 120.0 | 208 |
| 1155 | Anvil Arrow | Eos | C | Quantum Drive | 0.6 | 0.005 | 120.0 | 199 |
| 1156 | Anvil Arrow | Flood | D | Quantum Drive | 0.6 | 0.005 | 120.0 | 188 |
| 1157 | Anvil Arrow | LightFire | C | Quantum Drive | 0.6 | 0.005 | 120.0 | 239 |
| 1158 | Anvil Arrow | Hyperion | B | Quantum Drive | 0.6 | 0.005 | 120.0 | 219 |
| 1159 | Anvil Arrow | Atlas | A | Quantum Drive | 0.6 | 0.005 | 120.0 | 259 |
| 1160 | Anvil Arrow | FoxFire | B | Quantum Drive | 0.6 | 0.005 | 120.0 | 263 |
| 1161 | Anvil Arrow | Burst | B | Quantum Drive | 0.6 | 0.005 | 120.0 | 230 |
| 1162 | Anvil Arrow | Beacon ★ | C | Quantum Drive | 0.6 | 0.005 | 120.0 | 161 |
| 1163 | Anvil Arrow | Colossus | B | Quantum Drive | 0.6 | 0.005 | 120.0 | 241 |
| 1164 | Anvil Arrow | VK-00 | A | Quantum Drive | 0.6 | 0.005 | 120.0 | 210 |
| 1165 | Anvil Arrow | Vulcan | D | Quantum Drive | 0.6 | 0.005 | 120.0 | 197 |
| 1166 | Anvil Arrow | Wayfare | D | Quantum Drive | 0.6 | 0.005 | 120.0 | 170 |
| 1167 | Anvil Arrow | Expedition | C | Quantum Drive | 0.6 | 0.005 | 120.0 | 189 |
| 1168 | Anvil Arrow | Rush | C | Quantum Drive | 0.6 | 0.005 | 120.0 | 209 |
| 1169 | Anvil Hawk | Goliath | C | Quantum Drive | 0.6 | 0.005 | 120.0 | 219 |
| 1170 | Anvil Hawk | Siren | B | Quantum Drive | 0.6 | 0.005 | 120.0 | 178 |
| 1171 | Anvil Hawk | Voyage | B | Quantum Drive | 0.6 | 0.005 | 120.0 | 208 |
| 1172 | Anvil Hawk | Eos | C | Quantum Drive | 0.6 | 0.005 | 120.0 | 199 |
| 1173 | Anvil Hawk | Flood | D | Quantum Drive | 0.6 | 0.005 | 120.0 | 188 |
| 1174 | Anvil Hawk | LightFire | C | Quantum Drive | 0.6 | 0.005 | 120.0 | 239 |
| 1175 | Anvil Hawk | Hyperion | B | Quantum Drive | 0.6 | 0.005 | 120.0 | 219 |
| 1176 | Anvil Hawk | Atlas | A | Quantum Drive | 0.6 | 0.005 | 120.0 | 259 |
| 1177 | Anvil Hawk | FoxFire | B | Quantum Drive | 0.6 | 0.005 | 120.0 | 263 |
| 1178 | Anvil Hawk | Burst | B | Quantum Drive | 0.6 | 0.005 | 120.0 | 230 |
| 1179 | Anvil Hawk | Beacon | C | Quantum Drive | 0.6 | 0.005 | 120.0 | 161 |
| 1180 | Anvil Hawk | Colossus | B | Quantum Drive | 0.6 | 0.005 | 120.0 | 241 |
| 1181 | Anvil Hawk | VK-00 | A | Quantum Drive | 0.6 | 0.005 | 120.0 | 210 |
| 1182 | Anvil Hawk | Vulcan | D | Quantum Drive | 0.6 | 0.005 | 120.0 | 197 |
| 1183 | Anvil Hawk | Wayfare | D | Quantum Drive | 0.6 | 0.005 | 120.0 | 170 |
| 1184 | Anvil Hawk | Expedition | C | Quantum Drive | 0.6 | 0.005 | 120.0 | 189 |
| 1185 | Anvil Hawk | Rush ★ | C | Quantum Drive | 0.6 | 0.005 | 120.0 | 209 |
| 1186 | Aopoa Khartu-al | Goliath | C | Quantum Drive | 0.6 | 0.005 | 120.0 | 219 |
| 1187 | Aopoa Khartu-al | Siren | B | Quantum Drive | 0.6 | 0.005 | 120.0 | 178 |
| 1188 | Aopoa Khartu-al | Voyage | B | Quantum Drive | 0.6 | 0.005 | 120.0 | 208 |
| 1189 | Aopoa Khartu-al | Eos ★ | C | Quantum Drive | 0.6 | 0.005 | 120.0 | 199 |
| 1190 | Aopoa Khartu-al | Flood | D | Quantum Drive | 0.6 | 0.005 | 120.0 | 188 |
| 1191 | Aopoa Khartu-al | LightFire | C | Quantum Drive | 0.6 | 0.005 | 120.0 | 239 |
| 1192 | Aopoa Khartu-al | Hyperion | B | Quantum Drive | 0.6 | 0.005 | 120.0 | 219 |
| 1193 | Aopoa Khartu-al | Atlas | A | Quantum Drive | 0.6 | 0.005 | 120.0 | 259 |
| 1194 | Aopoa Khartu-al | FoxFire | B | Quantum Drive | 0.6 | 0.005 | 120.0 | 263 |
| 1195 | Aopoa Khartu-al | Burst | B | Quantum Drive | 0.6 | 0.005 | 120.0 | 230 |
| 1196 | Aopoa Khartu-al | Beacon | C | Quantum Drive | 0.6 | 0.005 | 120.0 | 161 |
| 1197 | Aopoa Khartu-al | Colossus | B | Quantum Drive | 0.6 | 0.005 | 120.0 | 241 |
| 1198 | Aopoa Khartu-al | VK-00 | A | Quantum Drive | 0.6 | 0.005 | 120.0 | 210 |
| 1199 | Aopoa Khartu-al | Vulcan | D | Quantum Drive | 0.6 | 0.005 | 120.0 | 197 |
| 1200 | Aopoa Khartu-al | Wayfare | D | Quantum Drive | 0.6 | 0.005 | 120.0 | 170 |
| 1201 | Aopoa Khartu-al | Expedition | C | Quantum Drive | 0.6 | 0.005 | 120.0 | 189 |
| 1202 | Aopoa Khartu-al | Rush | C | Quantum Drive | 0.6 | 0.005 | 120.0 | 209 |
| 1203 | C.O. Mustang Alpha | Goliath | C | Quantum Drive | 0.6 | 0.005 | 120.0 | 219 |
| 1204 | C.O. Mustang Alpha | Siren | B | Quantum Drive | 0.6 | 0.005 | 120.0 | 178 |
| 1205 | C.O. Mustang Alpha | Voyage | B | Quantum Drive | 0.6 | 0.005 | 120.0 | 208 |
| 1206 | C.O. Mustang Alpha | Eos | C | Quantum Drive | 0.6 | 0.005 | 120.0 | 199 |
| 1207 | C.O. Mustang Alpha | Flood | D | Quantum Drive | 0.6 | 0.005 | 120.0 | 188 |
| 1208 | C.O. Mustang Alpha | LightFire | C | Quantum Drive | 0.6 | 0.005 | 120.0 | 239 |
| 1209 | C.O. Mustang Alpha | Hyperion | B | Quantum Drive | 0.6 | 0.005 | 120.0 | 219 |
| 1210 | C.O. Mustang Alpha | Atlas | A | Quantum Drive | 0.6 | 0.005 | 120.0 | 259 |
| 1211 | C.O. Mustang Alpha | FoxFire | B | Quantum Drive | 0.6 | 0.005 | 120.0 | 263 |
| 1212 | C.O. Mustang Alpha | Burst | B | Quantum Drive | 0.6 | 0.005 | 120.0 | 230 |
| 1213 | C.O. Mustang Alpha | Beacon | C | Quantum Drive | 0.6 | 0.005 | 120.0 | 161 |
| 1214 | C.O. Mustang Alpha | Colossus | B | Quantum Drive | 0.6 | 0.005 | 120.0 | 241 |
| 1215 | C.O. Mustang Alpha | VK-00 | A | Quantum Drive | 0.6 | 0.005 | 120.0 | 210 |
| 1216 | C.O. Mustang Alpha | Vulcan | D | Quantum Drive | 0.6 | 0.005 | 120.0 | 197 |
| 1217 | C.O. Mustang Alpha | Wayfare | D | Quantum Drive | 0.6 | 0.005 | 120.0 | 170 |
| 1218 | C.O. Mustang Alpha | Expedition | C | Quantum Drive | 0.6 | 0.005 | 120.0 | 189 |
| 1219 | C.O. Mustang Alpha | Rush ★ | C | Quantum Drive | 0.6 | 0.005 | 120.0 | 209 |
| 1220 | C.O. Mustang Delta | Goliath | C | Quantum Drive | 0.6 | 0.005 | 120.0 | 219 |
| 1221 | C.O. Mustang Delta | Siren | B | Quantum Drive | 0.6 | 0.005 | 120.0 | 178 |
| 1222 | C.O. Mustang Delta | Voyage | B | Quantum Drive | 0.6 | 0.005 | 120.0 | 208 |
| 1223 | C.O. Mustang Delta | Eos | C | Quantum Drive | 0.6 | 0.005 | 120.0 | 199 |
| 1224 | C.O. Mustang Delta | Flood | D | Quantum Drive | 0.6 | 0.005 | 120.0 | 188 |
| 1225 | C.O. Mustang Delta | LightFire | C | Quantum Drive | 0.6 | 0.005 | 120.0 | 239 |
| 1226 | C.O. Mustang Delta | Hyperion | B | Quantum Drive | 0.6 | 0.005 | 120.0 | 219 |
| 1227 | C.O. Mustang Delta | Atlas | A | Quantum Drive | 0.6 | 0.005 | 120.0 | 259 |
| 1228 | C.O. Mustang Delta | FoxFire | B | Quantum Drive | 0.6 | 0.005 | 120.0 | 263 |
| 1229 | C.O. Mustang Delta | Burst | B | Quantum Drive | 0.6 | 0.005 | 120.0 | 230 |
| 1230 | C.O. Mustang Delta | Beacon | C | Quantum Drive | 0.6 | 0.005 | 120.0 | 161 |
| 1231 | C.O. Mustang Delta | Colossus | B | Quantum Drive | 0.6 | 0.005 | 120.0 | 241 |
| 1232 | C.O. Mustang Delta | VK-00 | A | Quantum Drive | 0.6 | 0.005 | 120.0 | 210 |
| 1233 | C.O. Mustang Delta | Vulcan | D | Quantum Drive | 0.6 | 0.005 | 120.0 | 197 |
| 1234 | C.O. Mustang Delta | Wayfare | D | Quantum Drive | 0.6 | 0.005 | 120.0 | 170 |
| 1235 | C.O. Mustang Delta | Expedition | C | Quantum Drive | 0.6 | 0.005 | 120.0 | 189 |
| 1236 | C.O. Mustang Delta | Rush ★ | C | Quantum Drive | 0.6 | 0.005 | 120.0 | 209 |
| 1237 | C.O. Mustang Gamma | Goliath | C | Quantum Drive | 0.6 | 0.005 | 120.0 | 219 |
| 1238 | C.O. Mustang Gamma | Siren | B | Quantum Drive | 0.6 | 0.005 | 120.0 | 178 |
| 1239 | C.O. Mustang Gamma | Voyage | B | Quantum Drive | 0.6 | 0.005 | 120.0 | 208 |
| 1240 | C.O. Mustang Gamma | Eos | C | Quantum Drive | 0.6 | 0.005 | 120.0 | 199 |
| 1241 | C.O. Mustang Gamma | Flood | D | Quantum Drive | 0.6 | 0.005 | 120.0 | 188 |
| 1242 | C.O. Mustang Gamma | LightFire | C | Quantum Drive | 0.6 | 0.005 | 120.0 | 239 |
| 1243 | C.O. Mustang Gamma | Hyperion | B | Quantum Drive | 0.6 | 0.005 | 120.0 | 219 |
| 1244 | C.O. Mustang Gamma | Atlas | A | Quantum Drive | 0.6 | 0.005 | 120.0 | 259 |
| 1245 | C.O. Mustang Gamma | FoxFire | B | Quantum Drive | 0.6 | 0.005 | 120.0 | 263 |
| 1246 | C.O. Mustang Gamma | Burst | B | Quantum Drive | 0.6 | 0.005 | 120.0 | 230 |
| 1247 | C.O. Mustang Gamma | Beacon | C | Quantum Drive | 0.6 | 0.005 | 120.0 | 161 |
| 1248 | C.O. Mustang Gamma | Colossus | B | Quantum Drive | 0.6 | 0.005 | 120.0 | 241 |
| 1249 | C.O. Mustang Gamma | VK-00 | A | Quantum Drive | 0.6 | 0.005 | 120.0 | 210 |
| 1250 | C.O. Mustang Gamma | Vulcan | D | Quantum Drive | 0.6 | 0.005 | 120.0 | 197 |
| 1251 | C.O. Mustang Gamma | Wayfare | D | Quantum Drive | 0.6 | 0.005 | 120.0 | 170 |
| 1252 | C.O. Mustang Gamma | Expedition | C | Quantum Drive | 0.6 | 0.005 | 120.0 | 189 |
| 1253 | C.O. Mustang Gamma | Rush ★ | C | Quantum Drive | 0.6 | 0.005 | 120.0 | 209 |
| 1254 | Esperia Blade | Goliath | C | Quantum Drive | 0.6 | 0.005 | 120.0 | 219 |
| 1255 | Esperia Blade | Siren | B | Quantum Drive | 0.6 | 0.005 | 120.0 | 178 |
| 1256 | Esperia Blade | Voyage | B | Quantum Drive | 0.6 | 0.005 | 120.0 | 208 |
| 1257 | Esperia Blade | Eos | C | Quantum Drive | 0.6 | 0.005 | 120.0 | 199 |
| 1258 | Esperia Blade | Flood | D | Quantum Drive | 0.6 | 0.005 | 120.0 | 188 |
| 1259 | Esperia Blade | LightFire | C | Quantum Drive | 0.6 | 0.005 | 120.0 | 239 |
| 1260 | Esperia Blade | Hyperion | B | Quantum Drive | 0.6 | 0.005 | 120.0 | 219 |
| 1261 | Esperia Blade | Atlas | A | Quantum Drive | 0.6 | 0.005 | 120.0 | 259 |
| 1262 | Esperia Blade | FoxFire | B | Quantum Drive | 0.6 | 0.005 | 120.0 | 263 |
| 1263 | Esperia Blade | Burst | B | Quantum Drive | 0.6 | 0.005 | 120.0 | 230 |
| 1264 | Esperia Blade | Beacon | C | Quantum Drive | 0.6 | 0.005 | 120.0 | 161 |
| 1265 | Esperia Blade | Colossus | B | Quantum Drive | 0.6 | 0.005 | 120.0 | 241 |
| 1266 | Esperia Blade | VK-00 | A | Quantum Drive | 0.6 | 0.005 | 120.0 | 210 |
| 1267 | Esperia Blade | Vulcan | D | Quantum Drive | 0.6 | 0.005 | 120.0 | 197 |
| 1268 | Esperia Blade | Wayfare | D | Quantum Drive | 0.6 | 0.005 | 120.0 | 170 |
| 1269 | Esperia Blade | Expedition | C | Quantum Drive | 0.6 | 0.005 | 120.0 | 189 |
| 1270 | Esperia Blade | Rush ★ | C | Quantum Drive | 0.6 | 0.005 | 120.0 | 209 |
| 1271 | Esperia Talon | Goliath | C | Quantum Drive | 0.6 | 0.005 | 120.0 | 219 |
| 1272 | Esperia Talon | Siren | B | Quantum Drive | 0.6 | 0.005 | 120.0 | 178 |
| 1273 | Esperia Talon | Voyage | B | Quantum Drive | 0.6 | 0.005 | 120.0 | 208 |
| 1274 | Esperia Talon | Eos | C | Quantum Drive | 0.6 | 0.005 | 120.0 | 199 |
| 1275 | Esperia Talon | Flood | D | Quantum Drive | 0.6 | 0.005 | 120.0 | 188 |
| 1276 | Esperia Talon | LightFire | C | Quantum Drive | 0.6 | 0.005 | 120.0 | 239 |
| 1277 | Esperia Talon | Hyperion | B | Quantum Drive | 0.6 | 0.005 | 120.0 | 219 |
| 1278 | Esperia Talon | Atlas | A | Quantum Drive | 0.6 | 0.005 | 120.0 | 259 |
| 1279 | Esperia Talon | FoxFire | B | Quantum Drive | 0.6 | 0.005 | 120.0 | 263 |
| 1280 | Esperia Talon | Burst | B | Quantum Drive | 0.6 | 0.005 | 120.0 | 230 |
| 1281 | Esperia Talon | Beacon | C | Quantum Drive | 0.6 | 0.005 | 120.0 | 161 |
| 1282 | Esperia Talon | Colossus | B | Quantum Drive | 0.6 | 0.005 | 120.0 | 241 |
| 1283 | Esperia Talon | VK-00 | A | Quantum Drive | 0.6 | 0.005 | 120.0 | 210 |
| 1284 | Esperia Talon | Vulcan | D | Quantum Drive | 0.6 | 0.005 | 120.0 | 197 |
| 1285 | Esperia Talon | Wayfare | D | Quantum Drive | 0.6 | 0.005 | 120.0 | 170 |
| 1286 | Esperia Talon | Expedition | C | Quantum Drive | 0.6 | 0.005 | 120.0 | 189 |
| 1287 | Esperia Talon | Rush | C | Quantum Drive | 0.6 | 0.005 | 120.0 | 209 |
| 1288 | Esperia Talon Shrike | Goliath | C | Quantum Drive | 0.6 | 0.005 | 120.0 | 219 |
| 1289 | Esperia Talon Shrike | Siren | B | Quantum Drive | 0.6 | 0.005 | 120.0 | 178 |
| 1290 | Esperia Talon Shrike | Voyage | B | Quantum Drive | 0.6 | 0.005 | 120.0 | 208 |
| 1291 | Esperia Talon Shrike | Eos | C | Quantum Drive | 0.6 | 0.005 | 120.0 | 199 |
| 1292 | Esperia Talon Shrike | Flood | D | Quantum Drive | 0.6 | 0.005 | 120.0 | 188 |
| 1293 | Esperia Talon Shrike | LightFire | C | Quantum Drive | 0.6 | 0.005 | 120.0 | 239 |
| 1294 | Esperia Talon Shrike | Hyperion | B | Quantum Drive | 0.6 | 0.005 | 120.0 | 219 |
| 1295 | Esperia Talon Shrike | Atlas | A | Quantum Drive | 0.6 | 0.005 | 120.0 | 259 |
| 1296 | Esperia Talon Shrike | FoxFire | B | Quantum Drive | 0.6 | 0.005 | 120.0 | 263 |
| 1297 | Esperia Talon Shrike | Burst | B | Quantum Drive | 0.6 | 0.005 | 120.0 | 230 |
| 1298 | Esperia Talon Shrike | Beacon | C | Quantum Drive | 0.6 | 0.005 | 120.0 | 161 |
| 1299 | Esperia Talon Shrike | Colossus | B | Quantum Drive | 0.6 | 0.005 | 120.0 | 241 |
| 1300 | Esperia Talon Shrike | VK-00 | A | Quantum Drive | 0.6 | 0.005 | 120.0 | 210 |
| 1301 | Esperia Talon Shrike | Vulcan | D | Quantum Drive | 0.6 | 0.005 | 120.0 | 197 |
| 1302 | Esperia Talon Shrike | Wayfare | D | Quantum Drive | 0.6 | 0.005 | 120.0 | 170 |
| 1303 | Esperia Talon Shrike | Expedition | C | Quantum Drive | 0.6 | 0.005 | 120.0 | 189 |
| 1304 | Esperia Talon Shrike | Rush | C | Quantum Drive | 0.6 | 0.005 | 120.0 | 209 |
| 1305 | Kruger L-21 Wolf | Goliath | C | Quantum Drive | 0.6 | 0.005 | 120.0 | 219 |
| 1306 | Kruger L-21 Wolf | Siren | B | Quantum Drive | 0.6 | 0.005 | 120.0 | 178 |
| 1307 | Kruger L-21 Wolf | Voyage | B | Quantum Drive | 0.6 | 0.005 | 120.0 | 208 |
| 1308 | Kruger L-21 Wolf | Eos | C | Quantum Drive | 0.6 | 0.005 | 120.0 | 199 |
| 1309 | Kruger L-21 Wolf | Flood | D | Quantum Drive | 0.6 | 0.005 | 120.0 | 188 |
| 1310 | Kruger L-21 Wolf | LightFire | C | Quantum Drive | 0.6 | 0.005 | 120.0 | 239 |
| 1311 | Kruger L-21 Wolf | Hyperion | B | Quantum Drive | 0.6 | 0.005 | 120.0 | 219 |
| 1312 | Kruger L-21 Wolf | Atlas | A | Quantum Drive | 0.6 | 0.005 | 120.0 | 259 |
| 1313 | Kruger L-21 Wolf | FoxFire ★ | B | Quantum Drive | 0.6 | 0.005 | 120.0 | 263 |
| 1314 | Kruger L-21 Wolf | Burst | B | Quantum Drive | 0.6 | 0.005 | 120.0 | 230 |
| 1315 | Kruger L-21 Wolf | Beacon | C | Quantum Drive | 0.6 | 0.005 | 120.0 | 161 |
| 1316 | Kruger L-21 Wolf | Colossus | B | Quantum Drive | 0.6 | 0.005 | 120.0 | 241 |
| 1317 | Kruger L-21 Wolf | VK-00 | A | Quantum Drive | 0.6 | 0.005 | 120.0 | 210 |
| 1318 | Kruger L-21 Wolf | Vulcan | D | Quantum Drive | 0.6 | 0.005 | 120.0 | 197 |
| 1319 | Kruger L-21 Wolf | Wayfare | D | Quantum Drive | 0.6 | 0.005 | 120.0 | 170 |
| 1320 | Kruger L-21 Wolf | Expedition | C | Quantum Drive | 0.6 | 0.005 | 120.0 | 189 |
| 1321 | Kruger L-21 Wolf | Rush | C | Quantum Drive | 0.6 | 0.005 | 120.0 | 209 |
| 1322 | Kruger L-22 Alpha Wolf | Goliath | C | Quantum Drive | 0.6 | 0.005 | 120.0 | 219 |
| 1323 | Kruger L-22 Alpha Wolf | Siren | B | Quantum Drive | 0.6 | 0.005 | 120.0 | 178 |
| 1324 | Kruger L-22 Alpha Wolf | Voyage | B | Quantum Drive | 0.6 | 0.005 | 120.0 | 208 |
| 1325 | Kruger L-22 Alpha Wolf | Eos | C | Quantum Drive | 0.6 | 0.005 | 120.0 | 199 |
| 1326 | Kruger L-22 Alpha Wolf | Flood | D | Quantum Drive | 0.6 | 0.005 | 120.0 | 188 |
| 1327 | Kruger L-22 Alpha Wolf | LightFire | C | Quantum Drive | 0.6 | 0.005 | 120.0 | 239 |
| 1328 | Kruger L-22 Alpha Wolf | Hyperion | B | Quantum Drive | 0.6 | 0.005 | 120.0 | 219 |
| 1329 | Kruger L-22 Alpha Wolf | Atlas | A | Quantum Drive | 0.6 | 0.005 | 120.0 | 259 |
| 1330 | Kruger L-22 Alpha Wolf | FoxFire | B | Quantum Drive | 0.6 | 0.005 | 120.0 | 263 |
| 1331 | Kruger L-22 Alpha Wolf | Burst | B | Quantum Drive | 0.6 | 0.005 | 120.0 | 230 |
| 1332 | Kruger L-22 Alpha Wolf | Beacon | C | Quantum Drive | 0.6 | 0.005 | 120.0 | 161 |
| 1333 | Kruger L-22 Alpha Wolf | Colossus | B | Quantum Drive | 0.6 | 0.005 | 120.0 | 241 |
| 1334 | Kruger L-22 Alpha Wolf | VK-00 ★ | A | Quantum Drive | 0.6 | 0.005 | 120.0 | 210 |
| 1335 | Kruger L-22 Alpha Wolf | Vulcan | D | Quantum Drive | 0.6 | 0.005 | 120.0 | 197 |
| 1336 | Kruger L-22 Alpha Wolf | Wayfare | D | Quantum Drive | 0.6 | 0.005 | 120.0 | 170 |
| 1337 | Kruger L-22 Alpha Wolf | Expedition | C | Quantum Drive | 0.6 | 0.005 | 120.0 | 189 |
| 1338 | Kruger L-22 Alpha Wolf | Rush | C | Quantum Drive | 0.6 | 0.005 | 120.0 | 209 |
| 1339 | Mirai Razor | Goliath | C | Quantum Drive | 0.6 | 0.005 | 120.0 | 219 |
| 1340 | Mirai Razor | Siren | B | Quantum Drive | 0.6 | 0.005 | 120.0 | 178 |
| 1341 | Mirai Razor | Voyage | B | Quantum Drive | 0.6 | 0.005 | 120.0 | 208 |
| 1342 | Mirai Razor | Eos | C | Quantum Drive | 0.6 | 0.005 | 120.0 | 199 |
| 1343 | Mirai Razor | Flood | D | Quantum Drive | 0.6 | 0.005 | 120.0 | 188 |
| 1344 | Mirai Razor | LightFire ★ | C | Quantum Drive | 0.6 | 0.005 | 120.0 | 239 |
| 1345 | Mirai Razor | Hyperion | B | Quantum Drive | 0.6 | 0.005 | 120.0 | 219 |
| 1346 | Mirai Razor | Atlas | A | Quantum Drive | 0.6 | 0.005 | 120.0 | 259 |
| 1347 | Mirai Razor | FoxFire | B | Quantum Drive | 0.6 | 0.005 | 120.0 | 263 |
| 1348 | Mirai Razor | Burst | B | Quantum Drive | 0.6 | 0.005 | 120.0 | 230 |
| 1349 | Mirai Razor | Beacon | C | Quantum Drive | 0.6 | 0.005 | 120.0 | 161 |
| 1350 | Mirai Razor | Colossus | B | Quantum Drive | 0.6 | 0.005 | 120.0 | 241 |
| 1351 | Mirai Razor | VK-00 | A | Quantum Drive | 0.6 | 0.005 | 120.0 | 210 |
| 1352 | Mirai Razor | Vulcan | D | Quantum Drive | 0.6 | 0.005 | 120.0 | 197 |
| 1353 | Mirai Razor | Wayfare | D | Quantum Drive | 0.6 | 0.005 | 120.0 | 170 |
| 1354 | Mirai Razor | Expedition | C | Quantum Drive | 0.6 | 0.005 | 120.0 | 189 |
| 1355 | Mirai Razor | Rush | C | Quantum Drive | 0.6 | 0.005 | 120.0 | 209 |
| 1356 | Mirai Razor EX | Goliath | C | Quantum Drive | 0.6 | 0.005 | 120.0 | 219 |
| 1357 | Mirai Razor EX | Siren | B | Quantum Drive | 0.6 | 0.005 | 120.0 | 178 |
| 1358 | Mirai Razor EX | Voyage | B | Quantum Drive | 0.6 | 0.005 | 120.0 | 208 |
| 1359 | Mirai Razor EX | Eos | C | Quantum Drive | 0.6 | 0.005 | 120.0 | 199 |
| 1360 | Mirai Razor EX | Flood | D | Quantum Drive | 0.6 | 0.005 | 120.0 | 188 |
| 1361 | Mirai Razor EX | LightFire ★ | C | Quantum Drive | 0.6 | 0.005 | 120.0 | 239 |
| 1362 | Mirai Razor EX | Hyperion | B | Quantum Drive | 0.6 | 0.005 | 120.0 | 219 |
| 1363 | Mirai Razor EX | Atlas | A | Quantum Drive | 0.6 | 0.005 | 120.0 | 259 |
| 1364 | Mirai Razor EX | FoxFire | B | Quantum Drive | 0.6 | 0.005 | 120.0 | 263 |
| 1365 | Mirai Razor EX | Burst | B | Quantum Drive | 0.6 | 0.005 | 120.0 | 230 |
| 1366 | Mirai Razor EX | Beacon | C | Quantum Drive | 0.6 | 0.005 | 120.0 | 161 |
| 1367 | Mirai Razor EX | Colossus | B | Quantum Drive | 0.6 | 0.005 | 120.0 | 241 |
| 1368 | Mirai Razor EX | VK-00 | A | Quantum Drive | 0.6 | 0.005 | 120.0 | 210 |
| 1369 | Mirai Razor EX | Vulcan | D | Quantum Drive | 0.6 | 0.005 | 120.0 | 197 |
| 1370 | Mirai Razor EX | Wayfare | D | Quantum Drive | 0.6 | 0.005 | 120.0 | 170 |
| 1371 | Mirai Razor EX | Expedition | C | Quantum Drive | 0.6 | 0.005 | 120.0 | 189 |
| 1372 | Mirai Razor EX | Rush | C | Quantum Drive | 0.6 | 0.005 | 120.0 | 209 |
| 1373 | Mirai Razor LX | Goliath | C | Quantum Drive | 0.6 | 0.005 | 120.0 | 219 |
| 1374 | Mirai Razor LX | Siren | B | Quantum Drive | 0.6 | 0.005 | 120.0 | 178 |
| 1375 | Mirai Razor LX | Voyage | B | Quantum Drive | 0.6 | 0.005 | 120.0 | 208 |
| 1376 | Mirai Razor LX | Eos | C | Quantum Drive | 0.6 | 0.005 | 120.0 | 199 |
| 1377 | Mirai Razor LX | Flood | D | Quantum Drive | 0.6 | 0.005 | 120.0 | 188 |
| 1378 | Mirai Razor LX | LightFire ★ | C | Quantum Drive | 0.6 | 0.005 | 120.0 | 239 |
| 1379 | Mirai Razor LX | Hyperion | B | Quantum Drive | 0.6 | 0.005 | 120.0 | 219 |
| 1380 | Mirai Razor LX | Atlas | A | Quantum Drive | 0.6 | 0.005 | 120.0 | 259 |
| 1381 | Mirai Razor LX | FoxFire | B | Quantum Drive | 0.6 | 0.005 | 120.0 | 263 |
| 1382 | Mirai Razor LX | Burst | B | Quantum Drive | 0.6 | 0.005 | 120.0 | 230 |
| 1383 | Mirai Razor LX | Beacon | C | Quantum Drive | 0.6 | 0.005 | 120.0 | 161 |
| 1384 | Mirai Razor LX | Colossus | B | Quantum Drive | 0.6 | 0.005 | 120.0 | 241 |
| 1385 | Mirai Razor LX | VK-00 | A | Quantum Drive | 0.6 | 0.005 | 120.0 | 210 |
| 1386 | Mirai Razor LX | Vulcan | D | Quantum Drive | 0.6 | 0.005 | 120.0 | 197 |
| 1387 | Mirai Razor LX | Wayfare | D | Quantum Drive | 0.6 | 0.005 | 120.0 | 170 |
| 1388 | Mirai Razor LX | Expedition | C | Quantum Drive | 0.6 | 0.005 | 120.0 | 189 |
| 1389 | Mirai Razor LX | Rush | C | Quantum Drive | 0.6 | 0.005 | 120.0 | 209 |
| 1390 | Origin 350r | Goliath | C | Quantum Drive | 0.6 | 0.005 | 120.0 | 219 |
| 1391 | Origin 350r | Siren | B | Quantum Drive | 0.6 | 0.005 | 120.0 | 178 |
| 1392 | Origin 350r | Voyage | B | Quantum Drive | 0.6 | 0.005 | 120.0 | 208 |
| 1393 | Origin 350r | Eos ★ | C | Quantum Drive | 0.6 | 0.005 | 120.0 | 199 |
| 1394 | Origin 350r | Flood | D | Quantum Drive | 0.6 | 0.005 | 120.0 | 188 |
| 1395 | Origin 350r | LightFire | C | Quantum Drive | 0.6 | 0.005 | 120.0 | 239 |
| 1396 | Origin 350r | Hyperion | B | Quantum Drive | 0.6 | 0.005 | 120.0 | 219 |
| 1397 | Origin 350r | Atlas | A | Quantum Drive | 0.6 | 0.005 | 120.0 | 259 |
| 1398 | Origin 350r | FoxFire | B | Quantum Drive | 0.6 | 0.005 | 120.0 | 263 |
| 1399 | Origin 350r | Burst | B | Quantum Drive | 0.6 | 0.005 | 120.0 | 230 |
| 1400 | Origin 350r | Beacon | C | Quantum Drive | 0.6 | 0.005 | 120.0 | 161 |
| 1401 | Origin 350r | Colossus | B | Quantum Drive | 0.6 | 0.005 | 120.0 | 241 |
| 1402 | Origin 350r | VK-00 | A | Quantum Drive | 0.6 | 0.005 | 120.0 | 210 |
| 1403 | Origin 350r | Vulcan | D | Quantum Drive | 0.6 | 0.005 | 120.0 | 197 |
| 1404 | Origin 350r | Wayfare | D | Quantum Drive | 0.6 | 0.005 | 120.0 | 170 |
| 1405 | Origin 350r | Expedition | C | Quantum Drive | 0.6 | 0.005 | 120.0 | 189 |
| 1406 | Origin 350r | Rush | C | Quantum Drive | 0.6 | 0.005 | 120.0 | 209 |
| 1407 | Origin 85X Limited | Goliath | C | Quantum Drive | 0.6 | 0.005 | 120.0 | 219 |
| 1408 | Origin 85X Limited | Siren | B | Quantum Drive | 0.6 | 0.005 | 120.0 | 178 |
| 1409 | Origin 85X Limited | Voyage | B | Quantum Drive | 0.6 | 0.005 | 120.0 | 208 |
| 1410 | Origin 85X Limited | Eos | C | Quantum Drive | 0.6 | 0.005 | 120.0 | 199 |
| 1411 | Origin 85X Limited | Flood | D | Quantum Drive | 0.6 | 0.005 | 120.0 | 188 |
| 1412 | Origin 85X Limited | LightFire | C | Quantum Drive | 0.6 | 0.005 | 120.0 | 239 |
| 1413 | Origin 85X Limited | Hyperion | B | Quantum Drive | 0.6 | 0.005 | 120.0 | 219 |
| 1414 | Origin 85X Limited | Atlas | A | Quantum Drive | 0.6 | 0.005 | 120.0 | 259 |
| 1415 | Origin 85X Limited | FoxFire | B | Quantum Drive | 0.6 | 0.005 | 120.0 | 263 |
| 1416 | Origin 85X Limited | Burst | B | Quantum Drive | 0.6 | 0.005 | 120.0 | 230 |
| 1417 | Origin 85X Limited | Beacon ★ | C | Quantum Drive | 0.6 | 0.005 | 120.0 | 161 |
| 1418 | Origin 85X Limited | Colossus | B | Quantum Drive | 0.6 | 0.005 | 120.0 | 241 |
| 1419 | Origin 85X Limited | VK-00 | A | Quantum Drive | 0.6 | 0.005 | 120.0 | 210 |
| 1420 | Origin 85X Limited | Vulcan | D | Quantum Drive | 0.6 | 0.005 | 120.0 | 197 |
| 1421 | Origin 85X Limited | Wayfare | D | Quantum Drive | 0.6 | 0.005 | 120.0 | 170 |
| 1422 | Origin 85X Limited | Expedition | C | Quantum Drive | 0.6 | 0.005 | 120.0 | 189 |
| 1423 | Origin 85X Limited | Rush | C | Quantum Drive | 0.6 | 0.005 | 120.0 | 209 |
| 1424 | Origin M50 Interceptor | Goliath | C | Quantum Drive | 0.6 | 0.005 | 120.0 | 219 |
| 1425 | Origin M50 Interceptor | Siren | B | Quantum Drive | 0.6 | 0.005 | 120.0 | 178 |
| 1426 | Origin M50 Interceptor | Voyage | B | Quantum Drive | 0.6 | 0.005 | 120.0 | 208 |
| 1427 | Origin M50 Interceptor | Eos | C | Quantum Drive | 0.6 | 0.005 | 120.0 | 199 |
| 1428 | Origin M50 Interceptor | Flood | D | Quantum Drive | 0.6 | 0.005 | 120.0 | 188 |
| 1429 | Origin M50 Interceptor | LightFire ★ | C | Quantum Drive | 0.6 | 0.005 | 120.0 | 239 |
| 1430 | Origin M50 Interceptor | Hyperion | B | Quantum Drive | 0.6 | 0.005 | 120.0 | 219 |
| 1431 | Origin M50 Interceptor | Atlas | A | Quantum Drive | 0.6 | 0.005 | 120.0 | 259 |
| 1432 | Origin M50 Interceptor | FoxFire | B | Quantum Drive | 0.6 | 0.005 | 120.0 | 263 |
| 1433 | Origin M50 Interceptor | Burst | B | Quantum Drive | 0.6 | 0.005 | 120.0 | 230 |
| 1434 | Origin M50 Interceptor | Beacon | C | Quantum Drive | 0.6 | 0.005 | 120.0 | 161 |
| 1435 | Origin M50 Interceptor | Colossus | B | Quantum Drive | 0.6 | 0.005 | 120.0 | 241 |
| 1436 | Origin M50 Interceptor | VK-00 | A | Quantum Drive | 0.6 | 0.005 | 120.0 | 210 |
| 1437 | Origin M50 Interceptor | Vulcan | D | Quantum Drive | 0.6 | 0.005 | 120.0 | 197 |
| 1438 | Origin M50 Interceptor | Wayfare | D | Quantum Drive | 0.6 | 0.005 | 120.0 | 170 |
| 1439 | Origin M50 Interceptor | Expedition | C | Quantum Drive | 0.6 | 0.005 | 120.0 | 189 |
| 1440 | Origin M50 Interceptor | Rush | C | Quantum Drive | 0.6 | 0.005 | 120.0 | 209 |

## Quantum drive size 2 (47 ships, 940 combinations)

| # | Ship | Quantum drive | Grade | Class | Tank SCU | SCU/Gm | Range Gm | Speed Mm/s |
|--|--|--|--|--|--|--|--|--|
| 1 | Origin 600i | Nova | C | Quantum Drive | 9.9 | 0.018 | 550.0 | 211 |
| 2 | Origin 600i | Spicule | A | Quantum Drive | 9.9 | 0.018 | 550.0 | 274 |
| 3 | Origin 600i | Bolt | B | Quantum Drive | 9.9 | 0.018 | 550.0 | 232 |
| 4 | Origin 600i Touring | Nova | C | Quantum Drive | 9.9 | 0.018 | 550.0 | 211 |
| 5 | Origin 600i Touring | Spicule | A | Quantum Drive | 9.9 | 0.018 | 550.0 | 274 |
| 6 | Origin 600i Touring | Bolt | B | Quantum Drive | 9.9 | 0.018 | 550.0 | 232 |
| 7 | RSI Hermes | Nova | C | Quantum Drive | 9.4 | 0.018 | 522.2 | 211 |
| 8 | RSI Hermes | Spicule | A | Quantum Drive | 9.4 | 0.018 | 522.2 | 274 |
| 9 | RSI Hermes | Bolt | B | Quantum Drive | 9.4 | 0.018 | 522.2 | 232 |
| 10 | RSI Apollo Medivac | Nova | C | Quantum Drive | 9.4 | 0.018 | 522.2 | 211 |
| 11 | RSI Apollo Medivac | Spicule | A | Quantum Drive | 9.4 | 0.018 | 522.2 | 274 |
| 12 | RSI Apollo Medivac | Bolt | B | Quantum Drive | 9.4 | 0.018 | 522.2 | 232 |
| 13 | RSI Apollo Triage | Nova | C | Quantum Drive | 9.4 | 0.018 | 522.2 | 211 |
| 14 | RSI Apollo Triage | Spicule | A | Quantum Drive | 9.4 | 0.018 | 522.2 | 274 |
| 15 | RSI Apollo Triage | Bolt | B | Quantum Drive | 9.4 | 0.018 | 522.2 | 232 |
| 16 | Origin 600i | Yaluk | D | Quantum Drive | 9.9 | 0.02 | 495.0 | 248 |
| 17 | Origin 600i | Bolon | C | Quantum Drive | 9.9 | 0.02 | 495.0 | 276 |
| 18 | Origin 600i | Huracan | B | Quantum Drive | 9.9 | 0.02 | 495.0 | 304 |
| 19 | Origin 600i Touring | Yaluk | D | Quantum Drive | 9.9 | 0.02 | 495.0 | 248 |
| 20 | Origin 600i Touring | Bolon | C | Quantum Drive | 9.9 | 0.02 | 495.0 | 276 |
| 21 | Origin 600i Touring | Huracan | B | Quantum Drive | 9.9 | 0.02 | 495.0 | 304 |
| 22 | MISC Starlancer MAX | Nova | C | Quantum Drive | 8.6 | 0.018 | 477.8 | 211 |
| 23 | MISC Starlancer MAX | Spicule | A | Quantum Drive | 8.6 | 0.018 | 477.8 | 274 |
| 24 | MISC Starlancer MAX | Bolt | B | Quantum Drive | 8.6 | 0.018 | 477.8 | 232 |
| 25 | MISC Starlancer TAC | Nova | C | Quantum Drive | 8.6 | 0.018 | 477.8 | 211 |
| 26 | MISC Starlancer TAC | Spicule | A | Quantum Drive | 8.6 | 0.018 | 477.8 | 274 |
| 27 | MISC Starlancer TAC | Bolt | B | Quantum Drive | 8.6 | 0.018 | 477.8 | 232 |
| 28 | Origin 600i | Crossfield | C | Quantum Drive | 9.9 | 0.021 | 471.4 | 203 |
| 29 | Origin 600i | XL-1 | A | Quantum Drive | 9.9 | 0.021 | 471.4 | 264 |
| 30 | Origin 600i | Yeager | B | Quantum Drive | 9.9 | 0.021 | 471.4 | 224 |
| 31 | Origin 600i Touring | Crossfield | C | Quantum Drive | 9.9 | 0.021 | 471.4 | 203 |
| 32 | Origin 600i Touring | XL-1 | A | Quantum Drive | 9.9 | 0.021 | 471.4 | 264 |
| 33 | Origin 600i Touring | Yeager | B | Quantum Drive | 9.9 | 0.021 | 471.4 | 224 |
| 34 | RSI Hermes | Yaluk | D | Quantum Drive | 9.4 | 0.02 | 470.0 | 248 |
| 35 | RSI Hermes | Bolon | C | Quantum Drive | 9.4 | 0.02 | 470.0 | 276 |
| 36 | RSI Hermes | Huracan | B | Quantum Drive | 9.4 | 0.02 | 470.0 | 304 |
| 37 | RSI Apollo Medivac | Yaluk | D | Quantum Drive | 9.4 | 0.02 | 470.0 | 248 |
| 38 | RSI Apollo Medivac | Bolon | C | Quantum Drive | 9.4 | 0.02 | 470.0 | 276 |
| 39 | RSI Apollo Medivac | Huracan | B | Quantum Drive | 9.4 | 0.02 | 470.0 | 304 |
| 40 | RSI Apollo Triage | Yaluk | D | Quantum Drive | 9.4 | 0.02 | 470.0 | 248 |
| 41 | RSI Apollo Triage | Bolon | C | Quantum Drive | 9.4 | 0.02 | 470.0 | 276 |
| 42 | RSI Apollo Triage | Huracan | B | Quantum Drive | 9.4 | 0.02 | 470.0 | 304 |
| 43 | MISC Hull B | Nova | C | Quantum Drive | 8.4 | 0.018 | 466.7 | 211 |
| 44 | MISC Hull B | Spicule | A | Quantum Drive | 8.4 | 0.018 | 466.7 | 274 |
| 45 | MISC Hull B | Bolt | B | Quantum Drive | 8.4 | 0.018 | 466.7 | 232 |
| 46 | Origin 600i | Cascade | D | Quantum Drive | 9.9 | 0.022 | 450.0 | 237 |
| 47 | Origin 600i | SparkFire | C | Quantum Drive | 9.9 | 0.022 | 450.0 | 301 |
| 48 | Origin 600i | Flash | B | Quantum Drive | 9.9 | 0.022 | 450.0 | 290 |
| 49 | Origin 600i | Hemera | A | Quantum Drive | 9.9 | 0.022 | 450.0 | 326 |
| 50 | Origin 600i | Sojourn | B | Quantum Drive | 9.9 | 0.022 | 450.0 | 262 |
| 51 | Origin 600i | SunFire | B | Quantum Drive | 9.9 | 0.022 | 450.0 | 331 |
| 52 | Origin 600i | Aither | B | Quantum Drive | 9.9 | 0.022 | 450.0 | 276 |
| 53 | Origin 600i | Torrent | C | Quantum Drive | 9.9 | 0.022 | 450.0 | 263 |
| 54 | Origin 600i | Khaos | C | Quantum Drive | 9.9 | 0.022 | 450.0 | 251 |
| 55 | Origin 600i | Quest | D | Quantum Drive | 9.9 | 0.022 | 450.0 | 214 |
| 56 | Origin 600i | Odyssey ★ | C | Quantum Drive | 9.9 | 0.022 | 450.0 | 238 |
| 57 | Origin 600i Touring | Cascade | D | Quantum Drive | 9.9 | 0.022 | 450.0 | 237 |
| 58 | Origin 600i Touring | SparkFire | C | Quantum Drive | 9.9 | 0.022 | 450.0 | 301 |
| 59 | Origin 600i Touring | Flash | B | Quantum Drive | 9.9 | 0.022 | 450.0 | 290 |
| 60 | Origin 600i Touring | Hemera | A | Quantum Drive | 9.9 | 0.022 | 450.0 | 326 |
| 61 | Origin 600i Touring | Sojourn | B | Quantum Drive | 9.9 | 0.022 | 450.0 | 262 |
| 62 | Origin 600i Touring | SunFire | B | Quantum Drive | 9.9 | 0.022 | 450.0 | 331 |
| 63 | Origin 600i Touring | Aither | B | Quantum Drive | 9.9 | 0.022 | 450.0 | 276 |
| 64 | Origin 600i Touring | Torrent | C | Quantum Drive | 9.9 | 0.022 | 450.0 | 263 |
| 65 | Origin 600i Touring | Khaos | C | Quantum Drive | 9.9 | 0.022 | 450.0 | 251 |
| 66 | Origin 600i Touring | Quest | D | Quantum Drive | 9.9 | 0.022 | 450.0 | 214 |
| 67 | Origin 600i Touring | Odyssey ★ | C | Quantum Drive | 9.9 | 0.022 | 450.0 | 238 |
| 68 | Crusader Mercury Star Runner | Nova | C | Quantum Drive | 8.1 | 0.018 | 450.0 | 211 |
| 69 | Crusader Mercury Star Runner | Spicule | A | Quantum Drive | 8.1 | 0.018 | 450.0 | 274 |
| 70 | Crusader Mercury Star Runner | Bolt | B | Quantum Drive | 8.1 | 0.018 | 450.0 | 232 |
| 71 | Drake Corsair | Nova | C | Quantum Drive | 8.1 | 0.018 | 450.0 | 211 |
| 72 | Drake Corsair | Spicule | A | Quantum Drive | 8.1 | 0.018 | 450.0 | 274 |
| 73 | Drake Corsair | Bolt | B | Quantum Drive | 8.1 | 0.018 | 450.0 | 232 |
| 74 | Origin 400i | Nova | C | Quantum Drive | 8.1 | 0.018 | 450.0 | 211 |
| 75 | Origin 400i | Spicule | A | Quantum Drive | 8.1 | 0.018 | 450.0 | 274 |
| 76 | Origin 400i | Bolt | B | Quantum Drive | 8.1 | 0.018 | 450.0 | 232 |
| 77 | RSI Constellation Mk IV Aquila | Nova | C | Quantum Drive | 8.1 | 0.018 | 450.0 | 211 |
| 78 | RSI Constellation Mk IV Aquila | Spicule | A | Quantum Drive | 8.1 | 0.018 | 450.0 | 274 |
| 79 | RSI Constellation Mk IV Aquila | Bolt | B | Quantum Drive | 8.1 | 0.018 | 450.0 | 232 |
| 80 | RSI Hermes | Crossfield | C | Quantum Drive | 9.4 | 0.021 | 447.6 | 203 |
| 81 | RSI Hermes | XL-1 | A | Quantum Drive | 9.4 | 0.021 | 447.6 | 264 |
| 82 | RSI Hermes | Yeager | B | Quantum Drive | 9.4 | 0.021 | 447.6 | 224 |
| 83 | RSI Apollo Medivac | Crossfield | C | Quantum Drive | 9.4 | 0.021 | 447.6 | 203 |
| 84 | RSI Apollo Medivac | XL-1 | A | Quantum Drive | 9.4 | 0.021 | 447.6 | 264 |
| 85 | RSI Apollo Medivac | Yeager | B | Quantum Drive | 9.4 | 0.021 | 447.6 | 224 |
| 86 | RSI Apollo Triage | Crossfield | C | Quantum Drive | 9.4 | 0.021 | 447.6 | 203 |
| 87 | RSI Apollo Triage | XL-1 | A | Quantum Drive | 9.4 | 0.021 | 447.6 | 264 |
| 88 | RSI Apollo Triage | Yeager | B | Quantum Drive | 9.4 | 0.021 | 447.6 | 224 |
| 89 | MISC Starlancer MAX | Yaluk | D | Quantum Drive | 8.6 | 0.02 | 430.0 | 248 |
| 90 | MISC Starlancer MAX | Bolon | C | Quantum Drive | 8.6 | 0.02 | 430.0 | 276 |
| 91 | MISC Starlancer MAX | Huracan | B | Quantum Drive | 8.6 | 0.02 | 430.0 | 304 |
| 92 | MISC Starlancer TAC | Yaluk | D | Quantum Drive | 8.6 | 0.02 | 430.0 | 248 |
| 93 | MISC Starlancer TAC | Bolon | C | Quantum Drive | 8.6 | 0.02 | 430.0 | 276 |
| 94 | MISC Starlancer TAC | Huracan | B | Quantum Drive | 8.6 | 0.02 | 430.0 | 304 |
| 95 | Anvil Asgard | Nova | C | Quantum Drive | 7.7 | 0.018 | 427.8 | 211 |
| 96 | Anvil Asgard | Spicule | A | Quantum Drive | 7.7 | 0.018 | 427.8 | 274 |
| 97 | Anvil Asgard | Bolt | B | Quantum Drive | 7.7 | 0.018 | 427.8 | 232 |
| 98 | Anvil Valkyrie | Nova | C | Quantum Drive | 7.7 | 0.018 | 427.8 | 211 |
| 99 | Anvil Valkyrie | Spicule | A | Quantum Drive | 7.7 | 0.018 | 427.8 | 274 |
| 100 | Anvil Valkyrie | Bolt | B | Quantum Drive | 7.7 | 0.018 | 427.8 | 232 |
| 101 | RSI Constellation Mk IV Taurus | Nova | C | Quantum Drive | 7.7 | 0.018 | 427.8 | 211 |
| 102 | RSI Constellation Mk IV Taurus | Spicule | A | Quantum Drive | 7.7 | 0.018 | 427.8 | 274 |
| 103 | RSI Constellation Mk IV Taurus | Bolt | B | Quantum Drive | 7.7 | 0.018 | 427.8 | 232 |
| 104 | RSI Hermes | Cascade | D | Quantum Drive | 9.4 | 0.022 | 427.3 | 237 |
| 105 | RSI Hermes | SparkFire | C | Quantum Drive | 9.4 | 0.022 | 427.3 | 301 |
| 106 | RSI Hermes | Flash | B | Quantum Drive | 9.4 | 0.022 | 427.3 | 290 |
| 107 | RSI Hermes | Hemera | A | Quantum Drive | 9.4 | 0.022 | 427.3 | 326 |
| 108 | RSI Hermes | Sojourn | B | Quantum Drive | 9.4 | 0.022 | 427.3 | 262 |
| 109 | RSI Hermes | SunFire | B | Quantum Drive | 9.4 | 0.022 | 427.3 | 331 |
| 110 | RSI Hermes | Aither | B | Quantum Drive | 9.4 | 0.022 | 427.3 | 276 |
| 111 | RSI Hermes | Torrent | C | Quantum Drive | 9.4 | 0.022 | 427.3 | 263 |
| 112 | RSI Hermes | Khaos | C | Quantum Drive | 9.4 | 0.022 | 427.3 | 251 |
| 113 | RSI Hermes | Quest | D | Quantum Drive | 9.4 | 0.022 | 427.3 | 214 |
| 114 | RSI Hermes | Odyssey ★ | C | Quantum Drive | 9.4 | 0.022 | 427.3 | 238 |
| 115 | RSI Apollo Medivac | Cascade | D | Quantum Drive | 9.4 | 0.022 | 427.3 | 237 |
| 116 | RSI Apollo Medivac | SparkFire | C | Quantum Drive | 9.4 | 0.022 | 427.3 | 301 |
| 117 | RSI Apollo Medivac | Flash | B | Quantum Drive | 9.4 | 0.022 | 427.3 | 290 |
| 118 | RSI Apollo Medivac | Hemera | A | Quantum Drive | 9.4 | 0.022 | 427.3 | 326 |
| 119 | RSI Apollo Medivac | Sojourn | B | Quantum Drive | 9.4 | 0.022 | 427.3 | 262 |
| 120 | RSI Apollo Medivac | SunFire | B | Quantum Drive | 9.4 | 0.022 | 427.3 | 331 |
| 121 | RSI Apollo Medivac | Aither | B | Quantum Drive | 9.4 | 0.022 | 427.3 | 276 |
| 122 | RSI Apollo Medivac | Torrent | C | Quantum Drive | 9.4 | 0.022 | 427.3 | 263 |
| 123 | RSI Apollo Medivac | Khaos | C | Quantum Drive | 9.4 | 0.022 | 427.3 | 251 |
| 124 | RSI Apollo Medivac | Quest | D | Quantum Drive | 9.4 | 0.022 | 427.3 | 214 |
| 125 | RSI Apollo Medivac | Odyssey ★ | C | Quantum Drive | 9.4 | 0.022 | 427.3 | 238 |
| 126 | RSI Apollo Triage | Cascade | D | Quantum Drive | 9.4 | 0.022 | 427.3 | 237 |
| 127 | RSI Apollo Triage | SparkFire | C | Quantum Drive | 9.4 | 0.022 | 427.3 | 301 |
| 128 | RSI Apollo Triage | Flash | B | Quantum Drive | 9.4 | 0.022 | 427.3 | 290 |
| 129 | RSI Apollo Triage | Hemera | A | Quantum Drive | 9.4 | 0.022 | 427.3 | 326 |
| 130 | RSI Apollo Triage | Sojourn | B | Quantum Drive | 9.4 | 0.022 | 427.3 | 262 |
| 131 | RSI Apollo Triage | SunFire | B | Quantum Drive | 9.4 | 0.022 | 427.3 | 331 |
| 132 | RSI Apollo Triage | Aither | B | Quantum Drive | 9.4 | 0.022 | 427.3 | 276 |
| 133 | RSI Apollo Triage | Torrent | C | Quantum Drive | 9.4 | 0.022 | 427.3 | 263 |
| 134 | RSI Apollo Triage | Khaos | C | Quantum Drive | 9.4 | 0.022 | 427.3 | 251 |
| 135 | RSI Apollo Triage | Quest | D | Quantum Drive | 9.4 | 0.022 | 427.3 | 214 |
| 136 | RSI Apollo Triage | Odyssey ★ | C | Quantum Drive | 9.4 | 0.022 | 427.3 | 238 |
| 137 | MISC Hull B | Yaluk | D | Quantum Drive | 8.4 | 0.02 | 420.0 | 248 |
| 138 | MISC Hull B | Bolon | C | Quantum Drive | 8.4 | 0.02 | 420.0 | 276 |
| 139 | MISC Hull B | Huracan | B | Quantum Drive | 8.4 | 0.02 | 420.0 | 304 |
| 140 | Esperia Prowler Utility | Nova ★ | C | Quantum Drive | 7.5 | 0.018 | 416.7 | 211 |
| 141 | Esperia Prowler Utility | Spicule | A | Quantum Drive | 7.5 | 0.018 | 416.7 | 274 |
| 142 | Esperia Prowler Utility | Bolt | B | Quantum Drive | 7.5 | 0.018 | 416.7 | 232 |
| 143 | MISC Starlancer MAX | Crossfield | C | Quantum Drive | 8.6 | 0.021 | 409.5 | 203 |
| 144 | MISC Starlancer MAX | XL-1 | A | Quantum Drive | 8.6 | 0.021 | 409.5 | 264 |
| 145 | MISC Starlancer MAX | Yeager | B | Quantum Drive | 8.6 | 0.021 | 409.5 | 224 |
| 146 | MISC Starlancer TAC | Crossfield | C | Quantum Drive | 8.6 | 0.021 | 409.5 | 203 |
| 147 | MISC Starlancer TAC | XL-1 | A | Quantum Drive | 8.6 | 0.021 | 409.5 | 264 |
| 148 | MISC Starlancer TAC | Yeager | B | Quantum Drive | 8.6 | 0.021 | 409.5 | 224 |
| 149 | Crusader Mercury Star Runner | Yaluk | D | Quantum Drive | 8.1 | 0.02 | 405.0 | 248 |
| 150 | Crusader Mercury Star Runner | Bolon ★ | C | Quantum Drive | 8.1 | 0.02 | 405.0 | 276 |
| 151 | Crusader Mercury Star Runner | Huracan | B | Quantum Drive | 8.1 | 0.02 | 405.0 | 304 |
| 152 | Drake Corsair | Yaluk | D | Quantum Drive | 8.1 | 0.02 | 405.0 | 248 |
| 153 | Drake Corsair | Bolon | C | Quantum Drive | 8.1 | 0.02 | 405.0 | 276 |
| 154 | Drake Corsair | Huracan | B | Quantum Drive | 8.1 | 0.02 | 405.0 | 304 |
| 155 | Origin 400i | Yaluk | D | Quantum Drive | 8.1 | 0.02 | 405.0 | 248 |
| 156 | Origin 400i | Bolon | C | Quantum Drive | 8.1 | 0.02 | 405.0 | 276 |
| 157 | Origin 400i | Huracan | B | Quantum Drive | 8.1 | 0.02 | 405.0 | 304 |
| 158 | RSI Constellation Mk IV Aquila | Yaluk | D | Quantum Drive | 8.1 | 0.02 | 405.0 | 248 |
| 159 | RSI Constellation Mk IV Aquila | Bolon ★ | C | Quantum Drive | 8.1 | 0.02 | 405.0 | 276 |
| 160 | RSI Constellation Mk IV Aquila | Huracan | B | Quantum Drive | 8.1 | 0.02 | 405.0 | 304 |
| 161 | Argo RAFT | Nova | C | Quantum Drive | 7.2 | 0.018 | 400.0 | 211 |
| 162 | Argo RAFT | Spicule | A | Quantum Drive | 7.2 | 0.018 | 400.0 | 274 |
| 163 | Argo RAFT | Bolt | B | Quantum Drive | 7.2 | 0.018 | 400.0 | 232 |
| 164 | Drake Cutlass Steel | Nova | C | Quantum Drive | 7.2 | 0.018 | 400.0 | 211 |
| 165 | Drake Cutlass Steel | Spicule | A | Quantum Drive | 7.2 | 0.018 | 400.0 | 274 |
| 166 | Drake Cutlass Steel | Bolt | B | Quantum Drive | 7.2 | 0.018 | 400.0 | 232 |
| 167 | MISC Hull B | Crossfield | C | Quantum Drive | 8.4 | 0.021 | 400.0 | 203 |
| 168 | MISC Hull B | XL-1 | A | Quantum Drive | 8.4 | 0.021 | 400.0 | 264 |
| 169 | MISC Hull B | Yeager | B | Quantum Drive | 8.4 | 0.021 | 400.0 | 224 |
| 170 | MISC Starlancer MAX | Cascade | D | Quantum Drive | 8.6 | 0.022 | 390.9 | 237 |
| 171 | MISC Starlancer MAX | SparkFire ★ | C | Quantum Drive | 8.6 | 0.022 | 390.9 | 301 |
| 172 | MISC Starlancer MAX | Flash | B | Quantum Drive | 8.6 | 0.022 | 390.9 | 290 |
| 173 | MISC Starlancer MAX | Hemera | A | Quantum Drive | 8.6 | 0.022 | 390.9 | 326 |
| 174 | MISC Starlancer MAX | Sojourn | B | Quantum Drive | 8.6 | 0.022 | 390.9 | 262 |
| 175 | MISC Starlancer MAX | SunFire | B | Quantum Drive | 8.6 | 0.022 | 390.9 | 331 |
| 176 | MISC Starlancer MAX | Aither | B | Quantum Drive | 8.6 | 0.022 | 390.9 | 276 |
| 177 | MISC Starlancer MAX | Torrent | C | Quantum Drive | 8.6 | 0.022 | 390.9 | 263 |
| 178 | MISC Starlancer MAX | Khaos | C | Quantum Drive | 8.6 | 0.022 | 390.9 | 251 |
| 179 | MISC Starlancer MAX | Quest | D | Quantum Drive | 8.6 | 0.022 | 390.9 | 214 |
| 180 | MISC Starlancer MAX | Odyssey | C | Quantum Drive | 8.6 | 0.022 | 390.9 | 238 |
| 181 | MISC Starlancer TAC | Cascade | D | Quantum Drive | 8.6 | 0.022 | 390.9 | 237 |
| 182 | MISC Starlancer TAC | SparkFire ★ | C | Quantum Drive | 8.6 | 0.022 | 390.9 | 301 |
| 183 | MISC Starlancer TAC | Flash | B | Quantum Drive | 8.6 | 0.022 | 390.9 | 290 |
| 184 | MISC Starlancer TAC | Hemera | A | Quantum Drive | 8.6 | 0.022 | 390.9 | 326 |
| 185 | MISC Starlancer TAC | Sojourn | B | Quantum Drive | 8.6 | 0.022 | 390.9 | 262 |
| 186 | MISC Starlancer TAC | SunFire | B | Quantum Drive | 8.6 | 0.022 | 390.9 | 331 |
| 187 | MISC Starlancer TAC | Aither | B | Quantum Drive | 8.6 | 0.022 | 390.9 | 276 |
| 188 | MISC Starlancer TAC | Torrent | C | Quantum Drive | 8.6 | 0.022 | 390.9 | 263 |
| 189 | MISC Starlancer TAC | Khaos | C | Quantum Drive | 8.6 | 0.022 | 390.9 | 251 |
| 190 | MISC Starlancer TAC | Quest | D | Quantum Drive | 8.6 | 0.022 | 390.9 | 214 |
| 191 | MISC Starlancer TAC | Odyssey | C | Quantum Drive | 8.6 | 0.022 | 390.9 | 238 |
| 192 | Aegis Retaliator | Nova | C | Quantum Drive | 7 | 0.018 | 388.9 | 211 |
| 193 | Aegis Retaliator | Spicule | A | Quantum Drive | 7 | 0.018 | 388.9 | 274 |
| 194 | Aegis Retaliator | Bolt | B | Quantum Drive | 7 | 0.018 | 388.9 | 232 |
| 195 | Anvil Paladin | Nova | C | Quantum Drive | 7 | 0.018 | 388.9 | 211 |
| 196 | Anvil Paladin | Spicule | A | Quantum Drive | 7 | 0.018 | 388.9 | 274 |
| 197 | Anvil Paladin | Bolt | B | Quantum Drive | 7 | 0.018 | 388.9 | 232 |
| 198 | RSI Constellation Mk IV Andromeda | Nova | C | Quantum Drive | 7 | 0.018 | 388.9 | 211 |
| 199 | RSI Constellation Mk IV Andromeda | Spicule | A | Quantum Drive | 7 | 0.018 | 388.9 | 274 |
| 200 | RSI Constellation Mk IV Andromeda | Bolt | B | Quantum Drive | 7 | 0.018 | 388.9 | 232 |
| 201 | RSI Constellation Mk IV Phoenix | Nova | C | Quantum Drive | 7 | 0.018 | 388.9 | 211 |
| 202 | RSI Constellation Mk IV Phoenix | Spicule | A | Quantum Drive | 7 | 0.018 | 388.9 | 274 |
| 203 | RSI Constellation Mk IV Phoenix | Bolt | B | Quantum Drive | 7 | 0.018 | 388.9 | 232 |
| 204 | Crusader Mercury Star Runner | Crossfield | C | Quantum Drive | 8.1 | 0.021 | 385.7 | 203 |
| 205 | Crusader Mercury Star Runner | XL-1 | A | Quantum Drive | 8.1 | 0.021 | 385.7 | 264 |
| 206 | Crusader Mercury Star Runner | Yeager | B | Quantum Drive | 8.1 | 0.021 | 385.7 | 224 |
| 207 | Drake Corsair | Crossfield | C | Quantum Drive | 8.1 | 0.021 | 385.7 | 203 |
| 208 | Drake Corsair | XL-1 | A | Quantum Drive | 8.1 | 0.021 | 385.7 | 264 |
| 209 | Drake Corsair | Yeager | B | Quantum Drive | 8.1 | 0.021 | 385.7 | 224 |
| 210 | Origin 400i | Crossfield | C | Quantum Drive | 8.1 | 0.021 | 385.7 | 203 |
| 211 | Origin 400i | XL-1 | A | Quantum Drive | 8.1 | 0.021 | 385.7 | 264 |
| 212 | Origin 400i | Yeager | B | Quantum Drive | 8.1 | 0.021 | 385.7 | 224 |
| 213 | RSI Constellation Mk IV Aquila | Crossfield | C | Quantum Drive | 8.1 | 0.021 | 385.7 | 203 |
| 214 | RSI Constellation Mk IV Aquila | XL-1 | A | Quantum Drive | 8.1 | 0.021 | 385.7 | 264 |
| 215 | RSI Constellation Mk IV Aquila | Yeager | B | Quantum Drive | 8.1 | 0.021 | 385.7 | 224 |
| 216 | Anvil Asgard | Yaluk | D | Quantum Drive | 7.7 | 0.02 | 385.0 | 248 |
| 217 | Anvil Asgard | Bolon | C | Quantum Drive | 7.7 | 0.02 | 385.0 | 276 |
| 218 | Anvil Asgard | Huracan | B | Quantum Drive | 7.7 | 0.02 | 385.0 | 304 |
| 219 | Anvil Valkyrie | Yaluk | D | Quantum Drive | 7.7 | 0.02 | 385.0 | 248 |
| 220 | Anvil Valkyrie | Bolon | C | Quantum Drive | 7.7 | 0.02 | 385.0 | 276 |
| 221 | Anvil Valkyrie | Huracan | B | Quantum Drive | 7.7 | 0.02 | 385.0 | 304 |
| 222 | RSI Constellation Mk IV Taurus | Yaluk | D | Quantum Drive | 7.7 | 0.02 | 385.0 | 248 |
| 223 | RSI Constellation Mk IV Taurus | Bolon ★ | C | Quantum Drive | 7.7 | 0.02 | 385.0 | 276 |
| 224 | RSI Constellation Mk IV Taurus | Huracan | B | Quantum Drive | 7.7 | 0.02 | 385.0 | 304 |
| 225 | MISC Hull B | Cascade | D | Quantum Drive | 8.4 | 0.022 | 381.8 | 237 |
| 226 | MISC Hull B | SparkFire ★ | C | Quantum Drive | 8.4 | 0.022 | 381.8 | 301 |
| 227 | MISC Hull B | Flash | B | Quantum Drive | 8.4 | 0.022 | 381.8 | 290 |
| 228 | MISC Hull B | Hemera | A | Quantum Drive | 8.4 | 0.022 | 381.8 | 326 |
| 229 | MISC Hull B | Sojourn | B | Quantum Drive | 8.4 | 0.022 | 381.8 | 262 |
| 230 | MISC Hull B | SunFire | B | Quantum Drive | 8.4 | 0.022 | 381.8 | 331 |
| 231 | MISC Hull B | Aither | B | Quantum Drive | 8.4 | 0.022 | 381.8 | 276 |
| 232 | MISC Hull B | Torrent | C | Quantum Drive | 8.4 | 0.022 | 381.8 | 263 |
| 233 | MISC Hull B | Khaos | C | Quantum Drive | 8.4 | 0.022 | 381.8 | 251 |
| 234 | MISC Hull B | Quest | D | Quantum Drive | 8.4 | 0.022 | 381.8 | 214 |
| 235 | MISC Hull B | Odyssey | C | Quantum Drive | 8.4 | 0.022 | 381.8 | 238 |
| 236 | Esperia Prowler Utility | Yaluk | D | Quantum Drive | 7.5 | 0.02 | 375.0 | 248 |
| 237 | Esperia Prowler Utility | Bolon | C | Quantum Drive | 7.5 | 0.02 | 375.0 | 276 |
| 238 | Esperia Prowler Utility | Huracan | B | Quantum Drive | 7.5 | 0.02 | 375.0 | 304 |
| 239 | RSI Zeus Mk II ES | Nova | C | Quantum Drive | 6.7 | 0.018 | 372.2 | 211 |
| 240 | RSI Zeus Mk II ES | Spicule | A | Quantum Drive | 6.7 | 0.018 | 372.2 | 274 |
| 241 | RSI Zeus Mk II ES | Bolt | B | Quantum Drive | 6.7 | 0.018 | 372.2 | 232 |
| 242 | MISC Freelancer DUR | Nova | C | Quantum Drive | 6.7 | 0.018 | 372.2 | 211 |
| 243 | MISC Freelancer DUR | Spicule | A | Quantum Drive | 6.7 | 0.018 | 372.2 | 274 |
| 244 | MISC Freelancer DUR | Bolt | B | Quantum Drive | 6.7 | 0.018 | 372.2 | 232 |
| 245 | Crusader Mercury Star Runner | Cascade | D | Quantum Drive | 8.1 | 0.022 | 368.2 | 237 |
| 246 | Crusader Mercury Star Runner | SparkFire | C | Quantum Drive | 8.1 | 0.022 | 368.2 | 301 |
| 247 | Crusader Mercury Star Runner | Flash | B | Quantum Drive | 8.1 | 0.022 | 368.2 | 290 |
| 248 | Crusader Mercury Star Runner | Hemera | A | Quantum Drive | 8.1 | 0.022 | 368.2 | 326 |
| 249 | Crusader Mercury Star Runner | Sojourn | B | Quantum Drive | 8.1 | 0.022 | 368.2 | 262 |
| 250 | Crusader Mercury Star Runner | SunFire | B | Quantum Drive | 8.1 | 0.022 | 368.2 | 331 |
| 251 | Crusader Mercury Star Runner | Aither | B | Quantum Drive | 8.1 | 0.022 | 368.2 | 276 |
| 252 | Crusader Mercury Star Runner | Torrent | C | Quantum Drive | 8.1 | 0.022 | 368.2 | 263 |
| 253 | Crusader Mercury Star Runner | Khaos | C | Quantum Drive | 8.1 | 0.022 | 368.2 | 251 |
| 254 | Crusader Mercury Star Runner | Quest | D | Quantum Drive | 8.1 | 0.022 | 368.2 | 214 |
| 255 | Crusader Mercury Star Runner | Odyssey | C | Quantum Drive | 8.1 | 0.022 | 368.2 | 238 |
| 256 | Drake Corsair | Cascade | D | Quantum Drive | 8.1 | 0.022 | 368.2 | 237 |
| 257 | Drake Corsair | SparkFire | C | Quantum Drive | 8.1 | 0.022 | 368.2 | 301 |
| 258 | Drake Corsair | Flash | B | Quantum Drive | 8.1 | 0.022 | 368.2 | 290 |
| 259 | Drake Corsair | Hemera | A | Quantum Drive | 8.1 | 0.022 | 368.2 | 326 |
| 260 | Drake Corsair | Sojourn | B | Quantum Drive | 8.1 | 0.022 | 368.2 | 262 |
| 261 | Drake Corsair | SunFire | B | Quantum Drive | 8.1 | 0.022 | 368.2 | 331 |
| 262 | Drake Corsair | Aither | B | Quantum Drive | 8.1 | 0.022 | 368.2 | 276 |
| 263 | Drake Corsair | Torrent ★ | C | Quantum Drive | 8.1 | 0.022 | 368.2 | 263 |
| 264 | Drake Corsair | Khaos | C | Quantum Drive | 8.1 | 0.022 | 368.2 | 251 |
| 265 | Drake Corsair | Quest | D | Quantum Drive | 8.1 | 0.022 | 368.2 | 214 |
| 266 | Drake Corsair | Odyssey | C | Quantum Drive | 8.1 | 0.022 | 368.2 | 238 |
| 267 | Origin 400i | Cascade | D | Quantum Drive | 8.1 | 0.022 | 368.2 | 237 |
| 268 | Origin 400i | SparkFire | C | Quantum Drive | 8.1 | 0.022 | 368.2 | 301 |
| 269 | Origin 400i | Flash | B | Quantum Drive | 8.1 | 0.022 | 368.2 | 290 |
| 270 | Origin 400i | Hemera | A | Quantum Drive | 8.1 | 0.022 | 368.2 | 326 |
| 271 | Origin 400i | Sojourn | B | Quantum Drive | 8.1 | 0.022 | 368.2 | 262 |
| 272 | Origin 400i | SunFire | B | Quantum Drive | 8.1 | 0.022 | 368.2 | 331 |
| 273 | Origin 400i | Aither | B | Quantum Drive | 8.1 | 0.022 | 368.2 | 276 |
| 274 | Origin 400i | Torrent ★ | C | Quantum Drive | 8.1 | 0.022 | 368.2 | 263 |
| 275 | Origin 400i | Khaos | C | Quantum Drive | 8.1 | 0.022 | 368.2 | 251 |
| 276 | Origin 400i | Quest | D | Quantum Drive | 8.1 | 0.022 | 368.2 | 214 |
| 277 | Origin 400i | Odyssey | C | Quantum Drive | 8.1 | 0.022 | 368.2 | 238 |
| 278 | RSI Constellation Mk IV Aquila | Cascade | D | Quantum Drive | 8.1 | 0.022 | 368.2 | 237 |
| 279 | RSI Constellation Mk IV Aquila | SparkFire | C | Quantum Drive | 8.1 | 0.022 | 368.2 | 301 |
| 280 | RSI Constellation Mk IV Aquila | Flash | B | Quantum Drive | 8.1 | 0.022 | 368.2 | 290 |
| 281 | RSI Constellation Mk IV Aquila | Hemera | A | Quantum Drive | 8.1 | 0.022 | 368.2 | 326 |
| 282 | RSI Constellation Mk IV Aquila | Sojourn | B | Quantum Drive | 8.1 | 0.022 | 368.2 | 262 |
| 283 | RSI Constellation Mk IV Aquila | SunFire | B | Quantum Drive | 8.1 | 0.022 | 368.2 | 331 |
| 284 | RSI Constellation Mk IV Aquila | Aither | B | Quantum Drive | 8.1 | 0.022 | 368.2 | 276 |
| 285 | RSI Constellation Mk IV Aquila | Torrent | C | Quantum Drive | 8.1 | 0.022 | 368.2 | 263 |
| 286 | RSI Constellation Mk IV Aquila | Khaos | C | Quantum Drive | 8.1 | 0.022 | 368.2 | 251 |
| 287 | RSI Constellation Mk IV Aquila | Quest | D | Quantum Drive | 8.1 | 0.022 | 368.2 | 214 |
| 288 | RSI Constellation Mk IV Aquila | Odyssey | C | Quantum Drive | 8.1 | 0.022 | 368.2 | 238 |
| 289 | Anvil Asgard | Crossfield | C | Quantum Drive | 7.7 | 0.021 | 366.7 | 203 |
| 290 | Anvil Asgard | XL-1 | A | Quantum Drive | 7.7 | 0.021 | 366.7 | 264 |
| 291 | Anvil Asgard | Yeager | B | Quantum Drive | 7.7 | 0.021 | 366.7 | 224 |
| 292 | Anvil Valkyrie | Crossfield | C | Quantum Drive | 7.7 | 0.021 | 366.7 | 203 |
| 293 | Anvil Valkyrie | XL-1 | A | Quantum Drive | 7.7 | 0.021 | 366.7 | 264 |
| 294 | Anvil Valkyrie | Yeager | B | Quantum Drive | 7.7 | 0.021 | 366.7 | 224 |
| 295 | RSI Constellation Mk IV Taurus | Crossfield | C | Quantum Drive | 7.7 | 0.021 | 366.7 | 203 |
| 296 | RSI Constellation Mk IV Taurus | XL-1 | A | Quantum Drive | 7.7 | 0.021 | 366.7 | 264 |
| 297 | RSI Constellation Mk IV Taurus | Yeager | B | Quantum Drive | 7.7 | 0.021 | 366.7 | 224 |
| 298 | Argo RAFT | Yaluk | D | Quantum Drive | 7.2 | 0.02 | 360.0 | 248 |
| 299 | Argo RAFT | Bolon ★ | C | Quantum Drive | 7.2 | 0.02 | 360.0 | 276 |
| 300 | Argo RAFT | Huracan | B | Quantum Drive | 7.2 | 0.02 | 360.0 | 304 |
| 301 | Drake Cutlass Steel | Yaluk | D | Quantum Drive | 7.2 | 0.02 | 360.0 | 248 |
| 302 | Drake Cutlass Steel | Bolon | C | Quantum Drive | 7.2 | 0.02 | 360.0 | 276 |
| 303 | Drake Cutlass Steel | Huracan | B | Quantum Drive | 7.2 | 0.02 | 360.0 | 304 |
| 304 | Esperia Prowler Utility | Crossfield | C | Quantum Drive | 7.5 | 0.021 | 357.1 | 203 |
| 305 | Esperia Prowler Utility | XL-1 | A | Quantum Drive | 7.5 | 0.021 | 357.1 | 264 |
| 306 | Esperia Prowler Utility | Yeager | B | Quantum Drive | 7.5 | 0.021 | 357.1 | 224 |
| 307 | RSI Zeus Mk II CL | Nova | C | Quantum Drive | 6.4 | 0.018 | 355.6 | 211 |
| 308 | RSI Zeus Mk II CL | Spicule | A | Quantum Drive | 6.4 | 0.018 | 355.6 | 274 |
| 309 | RSI Zeus Mk II CL | Bolt | B | Quantum Drive | 6.4 | 0.018 | 355.6 | 232 |
| 310 | Argo MOLE | Nova | C | Quantum Drive | 6.4 | 0.018 | 355.6 | 211 |
| 311 | Argo MOLE | Spicule | A | Quantum Drive | 6.4 | 0.018 | 355.6 | 274 |
| 312 | Argo MOLE | Bolt | B | Quantum Drive | 6.4 | 0.018 | 355.6 | 232 |
| 313 | Argo MOTH | Nova | C | Quantum Drive | 6.4 | 0.018 | 355.6 | 211 |
| 314 | Argo MOTH | Spicule | A | Quantum Drive | 6.4 | 0.018 | 355.6 | 274 |
| 315 | Argo MOTH | Bolt | B | Quantum Drive | 6.4 | 0.018 | 355.6 | 232 |
| 316 | Argo SRV | Nova | C | Quantum Drive | 6.4 | 0.018 | 355.6 | 211 |
| 317 | Argo SRV | Spicule | A | Quantum Drive | 6.4 | 0.018 | 355.6 | 274 |
| 318 | Argo SRV | Bolt | B | Quantum Drive | 6.4 | 0.018 | 355.6 | 232 |
| 319 | MISC Freelancer MAX | Nova | C | Quantum Drive | 6.4 | 0.018 | 355.6 | 211 |
| 320 | MISC Freelancer MAX | Spicule | A | Quantum Drive | 6.4 | 0.018 | 355.6 | 274 |
| 321 | MISC Freelancer MAX | Bolt | B | Quantum Drive | 6.4 | 0.018 | 355.6 | 232 |
| 322 | Aegis Redeemer | Nova | C | Quantum Drive | 6.3 | 0.018 | 350.0 | 211 |
| 323 | Aegis Redeemer | Spicule | A | Quantum Drive | 6.3 | 0.018 | 350.0 | 274 |
| 324 | Aegis Redeemer | Bolt | B | Quantum Drive | 6.3 | 0.018 | 350.0 | 232 |
| 325 | Aegis Retaliator | Yaluk | D | Quantum Drive | 7 | 0.02 | 350.0 | 248 |
| 326 | Aegis Retaliator | Bolon | C | Quantum Drive | 7 | 0.02 | 350.0 | 276 |
| 327 | Aegis Retaliator | Huracan | B | Quantum Drive | 7 | 0.02 | 350.0 | 304 |
| 328 | Anvil Asgard | Cascade | D | Quantum Drive | 7.7 | 0.022 | 350.0 | 237 |
| 329 | Anvil Asgard | SparkFire | C | Quantum Drive | 7.7 | 0.022 | 350.0 | 301 |
| 330 | Anvil Asgard | Flash | B | Quantum Drive | 7.7 | 0.022 | 350.0 | 290 |
| 331 | Anvil Asgard | Hemera | A | Quantum Drive | 7.7 | 0.022 | 350.0 | 326 |
| 332 | Anvil Asgard | Sojourn | B | Quantum Drive | 7.7 | 0.022 | 350.0 | 262 |
| 333 | Anvil Asgard | SunFire | B | Quantum Drive | 7.7 | 0.022 | 350.0 | 331 |
| 334 | Anvil Asgard | Aither | B | Quantum Drive | 7.7 | 0.022 | 350.0 | 276 |
| 335 | Anvil Asgard | Torrent | C | Quantum Drive | 7.7 | 0.022 | 350.0 | 263 |
| 336 | Anvil Asgard | Khaos | C | Quantum Drive | 7.7 | 0.022 | 350.0 | 251 |
| 337 | Anvil Asgard | Quest | D | Quantum Drive | 7.7 | 0.022 | 350.0 | 214 |
| 338 | Anvil Asgard | Odyssey ★ | C | Quantum Drive | 7.7 | 0.022 | 350.0 | 238 |
| 339 | Anvil Paladin | Yaluk | D | Quantum Drive | 7 | 0.02 | 350.0 | 248 |
| 340 | Anvil Paladin | Bolon | C | Quantum Drive | 7 | 0.02 | 350.0 | 276 |
| 341 | Anvil Paladin | Huracan | B | Quantum Drive | 7 | 0.02 | 350.0 | 304 |
| 342 | Anvil Valkyrie | Cascade | D | Quantum Drive | 7.7 | 0.022 | 350.0 | 237 |
| 343 | Anvil Valkyrie | SparkFire | C | Quantum Drive | 7.7 | 0.022 | 350.0 | 301 |
| 344 | Anvil Valkyrie | Flash | B | Quantum Drive | 7.7 | 0.022 | 350.0 | 290 |
| 345 | Anvil Valkyrie | Hemera | A | Quantum Drive | 7.7 | 0.022 | 350.0 | 326 |
| 346 | Anvil Valkyrie | Sojourn | B | Quantum Drive | 7.7 | 0.022 | 350.0 | 262 |
| 347 | Anvil Valkyrie | SunFire | B | Quantum Drive | 7.7 | 0.022 | 350.0 | 331 |
| 348 | Anvil Valkyrie | Aither | B | Quantum Drive | 7.7 | 0.022 | 350.0 | 276 |
| 349 | Anvil Valkyrie | Torrent | C | Quantum Drive | 7.7 | 0.022 | 350.0 | 263 |
| 350 | Anvil Valkyrie | Khaos | C | Quantum Drive | 7.7 | 0.022 | 350.0 | 251 |
| 351 | Anvil Valkyrie | Quest | D | Quantum Drive | 7.7 | 0.022 | 350.0 | 214 |
| 352 | Anvil Valkyrie | Odyssey ★ | C | Quantum Drive | 7.7 | 0.022 | 350.0 | 238 |
| 353 | RSI Constellation Mk IV Andromeda | Yaluk | D | Quantum Drive | 7 | 0.02 | 350.0 | 248 |
| 354 | RSI Constellation Mk IV Andromeda | Bolon ★ | C | Quantum Drive | 7 | 0.02 | 350.0 | 276 |
| 355 | RSI Constellation Mk IV Andromeda | Huracan | B | Quantum Drive | 7 | 0.02 | 350.0 | 304 |
| 356 | RSI Constellation Mk IV Phoenix | Yaluk | D | Quantum Drive | 7 | 0.02 | 350.0 | 248 |
| 357 | RSI Constellation Mk IV Phoenix | Bolon ★ | C | Quantum Drive | 7 | 0.02 | 350.0 | 276 |
| 358 | RSI Constellation Mk IV Phoenix | Huracan | B | Quantum Drive | 7 | 0.02 | 350.0 | 304 |
| 359 | RSI Constellation Mk IV Taurus | Cascade | D | Quantum Drive | 7.7 | 0.022 | 350.0 | 237 |
| 360 | RSI Constellation Mk IV Taurus | SparkFire | C | Quantum Drive | 7.7 | 0.022 | 350.0 | 301 |
| 361 | RSI Constellation Mk IV Taurus | Flash | B | Quantum Drive | 7.7 | 0.022 | 350.0 | 290 |
| 362 | RSI Constellation Mk IV Taurus | Hemera | A | Quantum Drive | 7.7 | 0.022 | 350.0 | 326 |
| 363 | RSI Constellation Mk IV Taurus | Sojourn | B | Quantum Drive | 7.7 | 0.022 | 350.0 | 262 |
| 364 | RSI Constellation Mk IV Taurus | SunFire | B | Quantum Drive | 7.7 | 0.022 | 350.0 | 331 |
| 365 | RSI Constellation Mk IV Taurus | Aither | B | Quantum Drive | 7.7 | 0.022 | 350.0 | 276 |
| 366 | RSI Constellation Mk IV Taurus | Torrent | C | Quantum Drive | 7.7 | 0.022 | 350.0 | 263 |
| 367 | RSI Constellation Mk IV Taurus | Khaos | C | Quantum Drive | 7.7 | 0.022 | 350.0 | 251 |
| 368 | RSI Constellation Mk IV Taurus | Quest | D | Quantum Drive | 7.7 | 0.022 | 350.0 | 214 |
| 369 | RSI Constellation Mk IV Taurus | Odyssey | C | Quantum Drive | 7.7 | 0.022 | 350.0 | 238 |
| 370 | Argo RAFT | Crossfield | C | Quantum Drive | 7.2 | 0.021 | 342.9 | 203 |
| 371 | Argo RAFT | XL-1 | A | Quantum Drive | 7.2 | 0.021 | 342.9 | 264 |
| 372 | Argo RAFT | Yeager | B | Quantum Drive | 7.2 | 0.021 | 342.9 | 224 |
| 373 | Drake Cutlass Steel | Crossfield ★ | C | Quantum Drive | 7.2 | 0.021 | 342.9 | 203 |
| 374 | Drake Cutlass Steel | XL-1 | A | Quantum Drive | 7.2 | 0.021 | 342.9 | 264 |
| 375 | Drake Cutlass Steel | Yeager | B | Quantum Drive | 7.2 | 0.021 | 342.9 | 224 |
| 376 | Esperia Prowler Utility | Cascade | D | Quantum Drive | 7.5 | 0.022 | 340.9 | 237 |
| 377 | Esperia Prowler Utility | SparkFire | C | Quantum Drive | 7.5 | 0.022 | 340.9 | 301 |
| 378 | Esperia Prowler Utility | Flash | B | Quantum Drive | 7.5 | 0.022 | 340.9 | 290 |
| 379 | Esperia Prowler Utility | Hemera | A | Quantum Drive | 7.5 | 0.022 | 340.9 | 326 |
| 380 | Esperia Prowler Utility | Sojourn | B | Quantum Drive | 7.5 | 0.022 | 340.9 | 262 |
| 381 | Esperia Prowler Utility | SunFire | B | Quantum Drive | 7.5 | 0.022 | 340.9 | 331 |
| 382 | Esperia Prowler Utility | Aither | B | Quantum Drive | 7.5 | 0.022 | 340.9 | 276 |
| 383 | Esperia Prowler Utility | Torrent | C | Quantum Drive | 7.5 | 0.022 | 340.9 | 263 |
| 384 | Esperia Prowler Utility | Khaos | C | Quantum Drive | 7.5 | 0.022 | 340.9 | 251 |
| 385 | Esperia Prowler Utility | Quest | D | Quantum Drive | 7.5 | 0.022 | 340.9 | 214 |
| 386 | Esperia Prowler Utility | Odyssey | C | Quantum Drive | 7.5 | 0.022 | 340.9 | 238 |
| 387 | RSI Zeus Mk II ES | Yaluk | D | Quantum Drive | 6.7 | 0.02 | 335.0 | 248 |
| 388 | RSI Zeus Mk II ES | Bolon | C | Quantum Drive | 6.7 | 0.02 | 335.0 | 276 |
| 389 | RSI Zeus Mk II ES | Huracan | B | Quantum Drive | 6.7 | 0.02 | 335.0 | 304 |
| 390 | MISC Freelancer DUR | Yaluk | D | Quantum Drive | 6.7 | 0.02 | 335.0 | 248 |
| 391 | MISC Freelancer DUR | Bolon | C | Quantum Drive | 6.7 | 0.02 | 335.0 | 276 |
| 392 | MISC Freelancer DUR | Huracan | B | Quantum Drive | 6.7 | 0.02 | 335.0 | 304 |
| 393 | Aegis Retaliator | Crossfield ★ | C | Quantum Drive | 7 | 0.021 | 333.3 | 203 |
| 394 | Aegis Retaliator | XL-1 | A | Quantum Drive | 7 | 0.021 | 333.3 | 264 |
| 395 | Aegis Retaliator | Yeager | B | Quantum Drive | 7 | 0.021 | 333.3 | 224 |
| 396 | Anvil Paladin | Crossfield | C | Quantum Drive | 7 | 0.021 | 333.3 | 203 |
| 397 | Anvil Paladin | XL-1 | A | Quantum Drive | 7 | 0.021 | 333.3 | 264 |
| 398 | Anvil Paladin | Yeager | B | Quantum Drive | 7 | 0.021 | 333.3 | 224 |
| 399 | RSI Constellation Mk IV Andromeda | Crossfield | C | Quantum Drive | 7 | 0.021 | 333.3 | 203 |
| 400 | RSI Constellation Mk IV Andromeda | XL-1 | A | Quantum Drive | 7 | 0.021 | 333.3 | 264 |
| 401 | RSI Constellation Mk IV Andromeda | Yeager | B | Quantum Drive | 7 | 0.021 | 333.3 | 224 |
| 402 | RSI Constellation Mk IV Phoenix | Crossfield | C | Quantum Drive | 7 | 0.021 | 333.3 | 203 |
| 403 | RSI Constellation Mk IV Phoenix | XL-1 | A | Quantum Drive | 7 | 0.021 | 333.3 | 264 |
| 404 | RSI Constellation Mk IV Phoenix | Yeager | B | Quantum Drive | 7 | 0.021 | 333.3 | 224 |
| 405 | Crusader A1 Spirit | Nova | C | Quantum Drive | 5.9 | 0.018 | 327.8 | 211 |
| 406 | Crusader A1 Spirit | Spicule | A | Quantum Drive | 5.9 | 0.018 | 327.8 | 274 |
| 407 | Crusader A1 Spirit | Bolt | B | Quantum Drive | 5.9 | 0.018 | 327.8 | 232 |
| 408 | Crusader Ares Star Fighter Inferno | Nova | C | Quantum Drive | 5.9 | 0.018 | 327.8 | 211 |
| 409 | Crusader Ares Star Fighter Inferno | Spicule | A | Quantum Drive | 5.9 | 0.018 | 327.8 | 274 |
| 410 | Crusader Ares Star Fighter Inferno | Bolt | B | Quantum Drive | 5.9 | 0.018 | 327.8 | 232 |
| 411 | Crusader Ares Star Fighter Ion | Nova | C | Quantum Drive | 5.9 | 0.018 | 327.8 | 211 |
| 412 | Crusader Ares Star Fighter Ion | Spicule | A | Quantum Drive | 5.9 | 0.018 | 327.8 | 274 |
| 413 | Crusader Ares Star Fighter Ion | Bolt | B | Quantum Drive | 5.9 | 0.018 | 327.8 | 232 |
| 414 | Crusader C1 Spirit | Nova | C | Quantum Drive | 5.9 | 0.018 | 327.8 | 211 |
| 415 | Crusader C1 Spirit | Spicule | A | Quantum Drive | 5.9 | 0.018 | 327.8 | 274 |
| 416 | Crusader C1 Spirit | Bolt | B | Quantum Drive | 5.9 | 0.018 | 327.8 | 232 |
| 417 | MISC Freelancer | Nova | C | Quantum Drive | 5.9 | 0.018 | 327.8 | 211 |
| 418 | MISC Freelancer | Spicule | A | Quantum Drive | 5.9 | 0.018 | 327.8 | 274 |
| 419 | MISC Freelancer | Bolt | B | Quantum Drive | 5.9 | 0.018 | 327.8 | 232 |
| 420 | MISC Freelancer MIS | Nova | C | Quantum Drive | 5.9 | 0.018 | 327.8 | 211 |
| 421 | MISC Freelancer MIS | Spicule | A | Quantum Drive | 5.9 | 0.018 | 327.8 | 274 |
| 422 | MISC Freelancer MIS | Bolt | B | Quantum Drive | 5.9 | 0.018 | 327.8 | 232 |
| 423 | Argo RAFT | Cascade | D | Quantum Drive | 7.2 | 0.022 | 327.3 | 237 |
| 424 | Argo RAFT | SparkFire | C | Quantum Drive | 7.2 | 0.022 | 327.3 | 301 |
| 425 | Argo RAFT | Flash | B | Quantum Drive | 7.2 | 0.022 | 327.3 | 290 |
| 426 | Argo RAFT | Hemera | A | Quantum Drive | 7.2 | 0.022 | 327.3 | 326 |
| 427 | Argo RAFT | Sojourn | B | Quantum Drive | 7.2 | 0.022 | 327.3 | 262 |
| 428 | Argo RAFT | SunFire | B | Quantum Drive | 7.2 | 0.022 | 327.3 | 331 |
| 429 | Argo RAFT | Aither | B | Quantum Drive | 7.2 | 0.022 | 327.3 | 276 |
| 430 | Argo RAFT | Torrent | C | Quantum Drive | 7.2 | 0.022 | 327.3 | 263 |
| 431 | Argo RAFT | Khaos | C | Quantum Drive | 7.2 | 0.022 | 327.3 | 251 |
| 432 | Argo RAFT | Quest | D | Quantum Drive | 7.2 | 0.022 | 327.3 | 214 |
| 433 | Argo RAFT | Odyssey | C | Quantum Drive | 7.2 | 0.022 | 327.3 | 238 |
| 434 | Drake Cutlass Steel | Cascade | D | Quantum Drive | 7.2 | 0.022 | 327.3 | 237 |
| 435 | Drake Cutlass Steel | SparkFire | C | Quantum Drive | 7.2 | 0.022 | 327.3 | 301 |
| 436 | Drake Cutlass Steel | Flash | B | Quantum Drive | 7.2 | 0.022 | 327.3 | 290 |
| 437 | Drake Cutlass Steel | Hemera | A | Quantum Drive | 7.2 | 0.022 | 327.3 | 326 |
| 438 | Drake Cutlass Steel | Sojourn | B | Quantum Drive | 7.2 | 0.022 | 327.3 | 262 |
| 439 | Drake Cutlass Steel | SunFire | B | Quantum Drive | 7.2 | 0.022 | 327.3 | 331 |
| 440 | Drake Cutlass Steel | Aither | B | Quantum Drive | 7.2 | 0.022 | 327.3 | 276 |
| 441 | Drake Cutlass Steel | Torrent | C | Quantum Drive | 7.2 | 0.022 | 327.3 | 263 |
| 442 | Drake Cutlass Steel | Khaos | C | Quantum Drive | 7.2 | 0.022 | 327.3 | 251 |
| 443 | Drake Cutlass Steel | Quest | D | Quantum Drive | 7.2 | 0.022 | 327.3 | 214 |
| 444 | Drake Cutlass Steel | Odyssey | C | Quantum Drive | 7.2 | 0.022 | 327.3 | 238 |
| 445 | RSI Zeus Mk II CL | Yaluk | D | Quantum Drive | 6.4 | 0.02 | 320.0 | 248 |
| 446 | RSI Zeus Mk II CL | Bolon | C | Quantum Drive | 6.4 | 0.02 | 320.0 | 276 |
| 447 | RSI Zeus Mk II CL | Huracan | B | Quantum Drive | 6.4 | 0.02 | 320.0 | 304 |
| 448 | Argo MOLE | Yaluk | D | Quantum Drive | 6.4 | 0.02 | 320.0 | 248 |
| 449 | Argo MOLE | Bolon | C | Quantum Drive | 6.4 | 0.02 | 320.0 | 276 |
| 450 | Argo MOLE | Huracan ★ | B | Quantum Drive | 6.4 | 0.02 | 320.0 | 304 |
| 451 | Argo MOTH | Yaluk | D | Quantum Drive | 6.4 | 0.02 | 320.0 | 248 |
| 452 | Argo MOTH | Bolon | C | Quantum Drive | 6.4 | 0.02 | 320.0 | 276 |
| 453 | Argo MOTH | Huracan ★ | B | Quantum Drive | 6.4 | 0.02 | 320.0 | 304 |
| 454 | Argo SRV | Yaluk | D | Quantum Drive | 6.4 | 0.02 | 320.0 | 248 |
| 455 | Argo SRV | Bolon | C | Quantum Drive | 6.4 | 0.02 | 320.0 | 276 |
| 456 | Argo SRV | Huracan ★ | B | Quantum Drive | 6.4 | 0.02 | 320.0 | 304 |
| 457 | MISC Freelancer MAX | Yaluk | D | Quantum Drive | 6.4 | 0.02 | 320.0 | 248 |
| 458 | MISC Freelancer MAX | Bolon | C | Quantum Drive | 6.4 | 0.02 | 320.0 | 276 |
| 459 | MISC Freelancer MAX | Huracan | B | Quantum Drive | 6.4 | 0.02 | 320.0 | 304 |
| 460 | RSI Zeus Mk II ES | Crossfield | C | Quantum Drive | 6.7 | 0.021 | 319.0 | 203 |
| 461 | RSI Zeus Mk II ES | XL-1 | A | Quantum Drive | 6.7 | 0.021 | 319.0 | 264 |
| 462 | RSI Zeus Mk II ES | Yeager | B | Quantum Drive | 6.7 | 0.021 | 319.0 | 224 |
| 463 | MISC Freelancer DUR | Crossfield | C | Quantum Drive | 6.7 | 0.021 | 319.0 | 203 |
| 464 | MISC Freelancer DUR | XL-1 | A | Quantum Drive | 6.7 | 0.021 | 319.0 | 264 |
| 465 | MISC Freelancer DUR | Yeager | B | Quantum Drive | 6.7 | 0.021 | 319.0 | 224 |
| 466 | Aegis Retaliator | Cascade | D | Quantum Drive | 7 | 0.022 | 318.2 | 237 |
| 467 | Aegis Retaliator | SparkFire | C | Quantum Drive | 7 | 0.022 | 318.2 | 301 |
| 468 | Aegis Retaliator | Flash | B | Quantum Drive | 7 | 0.022 | 318.2 | 290 |
| 469 | Aegis Retaliator | Hemera | A | Quantum Drive | 7 | 0.022 | 318.2 | 326 |
| 470 | Aegis Retaliator | Sojourn | B | Quantum Drive | 7 | 0.022 | 318.2 | 262 |
| 471 | Aegis Retaliator | SunFire | B | Quantum Drive | 7 | 0.022 | 318.2 | 331 |
| 472 | Aegis Retaliator | Aither | B | Quantum Drive | 7 | 0.022 | 318.2 | 276 |
| 473 | Aegis Retaliator | Torrent | C | Quantum Drive | 7 | 0.022 | 318.2 | 263 |
| 474 | Aegis Retaliator | Khaos | C | Quantum Drive | 7 | 0.022 | 318.2 | 251 |
| 475 | Aegis Retaliator | Quest | D | Quantum Drive | 7 | 0.022 | 318.2 | 214 |
| 476 | Aegis Retaliator | Odyssey | C | Quantum Drive | 7 | 0.022 | 318.2 | 238 |
| 477 | Anvil Paladin | Cascade | D | Quantum Drive | 7 | 0.022 | 318.2 | 237 |
| 478 | Anvil Paladin | SparkFire ★ | C | Quantum Drive | 7 | 0.022 | 318.2 | 301 |
| 479 | Anvil Paladin | Flash | B | Quantum Drive | 7 | 0.022 | 318.2 | 290 |
| 480 | Anvil Paladin | Hemera | A | Quantum Drive | 7 | 0.022 | 318.2 | 326 |
| 481 | Anvil Paladin | Sojourn | B | Quantum Drive | 7 | 0.022 | 318.2 | 262 |
| 482 | Anvil Paladin | SunFire | B | Quantum Drive | 7 | 0.022 | 318.2 | 331 |
| 483 | Anvil Paladin | Aither | B | Quantum Drive | 7 | 0.022 | 318.2 | 276 |
| 484 | Anvil Paladin | Torrent | C | Quantum Drive | 7 | 0.022 | 318.2 | 263 |
| 485 | Anvil Paladin | Khaos | C | Quantum Drive | 7 | 0.022 | 318.2 | 251 |
| 486 | Anvil Paladin | Quest | D | Quantum Drive | 7 | 0.022 | 318.2 | 214 |
| 487 | Anvil Paladin | Odyssey | C | Quantum Drive | 7 | 0.022 | 318.2 | 238 |
| 488 | RSI Constellation Mk IV Andromeda | Cascade | D | Quantum Drive | 7 | 0.022 | 318.2 | 237 |
| 489 | RSI Constellation Mk IV Andromeda | SparkFire | C | Quantum Drive | 7 | 0.022 | 318.2 | 301 |
| 490 | RSI Constellation Mk IV Andromeda | Flash | B | Quantum Drive | 7 | 0.022 | 318.2 | 290 |
| 491 | RSI Constellation Mk IV Andromeda | Hemera | A | Quantum Drive | 7 | 0.022 | 318.2 | 326 |
| 492 | RSI Constellation Mk IV Andromeda | Sojourn | B | Quantum Drive | 7 | 0.022 | 318.2 | 262 |
| 493 | RSI Constellation Mk IV Andromeda | SunFire | B | Quantum Drive | 7 | 0.022 | 318.2 | 331 |
| 494 | RSI Constellation Mk IV Andromeda | Aither | B | Quantum Drive | 7 | 0.022 | 318.2 | 276 |
| 495 | RSI Constellation Mk IV Andromeda | Torrent | C | Quantum Drive | 7 | 0.022 | 318.2 | 263 |
| 496 | RSI Constellation Mk IV Andromeda | Khaos | C | Quantum Drive | 7 | 0.022 | 318.2 | 251 |
| 497 | RSI Constellation Mk IV Andromeda | Quest | D | Quantum Drive | 7 | 0.022 | 318.2 | 214 |
| 498 | RSI Constellation Mk IV Andromeda | Odyssey | C | Quantum Drive | 7 | 0.022 | 318.2 | 238 |
| 499 | RSI Constellation Mk IV Phoenix | Cascade | D | Quantum Drive | 7 | 0.022 | 318.2 | 237 |
| 500 | RSI Constellation Mk IV Phoenix | SparkFire | C | Quantum Drive | 7 | 0.022 | 318.2 | 301 |
| 501 | RSI Constellation Mk IV Phoenix | Flash | B | Quantum Drive | 7 | 0.022 | 318.2 | 290 |
| 502 | RSI Constellation Mk IV Phoenix | Hemera | A | Quantum Drive | 7 | 0.022 | 318.2 | 326 |
| 503 | RSI Constellation Mk IV Phoenix | Sojourn | B | Quantum Drive | 7 | 0.022 | 318.2 | 262 |
| 504 | RSI Constellation Mk IV Phoenix | SunFire | B | Quantum Drive | 7 | 0.022 | 318.2 | 331 |
| 505 | RSI Constellation Mk IV Phoenix | Aither | B | Quantum Drive | 7 | 0.022 | 318.2 | 276 |
| 506 | RSI Constellation Mk IV Phoenix | Torrent | C | Quantum Drive | 7 | 0.022 | 318.2 | 263 |
| 507 | RSI Constellation Mk IV Phoenix | Khaos | C | Quantum Drive | 7 | 0.022 | 318.2 | 251 |
| 508 | RSI Constellation Mk IV Phoenix | Quest | D | Quantum Drive | 7 | 0.022 | 318.2 | 214 |
| 509 | RSI Constellation Mk IV Phoenix | Odyssey | C | Quantum Drive | 7 | 0.022 | 318.2 | 238 |
| 510 | Aegis Redeemer | Yaluk | D | Quantum Drive | 6.3 | 0.02 | 315.0 | 248 |
| 511 | Aegis Redeemer | Bolon | C | Quantum Drive | 6.3 | 0.02 | 315.0 | 276 |
| 512 | Aegis Redeemer | Huracan | B | Quantum Drive | 6.3 | 0.02 | 315.0 | 304 |
| 513 | Aegis Vanguard Harbinger | Nova | C | Quantum Drive | 5.5 | 0.018 | 305.6 | 211 |
| 514 | Aegis Vanguard Harbinger | Spicule | A | Quantum Drive | 5.5 | 0.018 | 305.6 | 274 |
| 515 | Aegis Vanguard Harbinger | Bolt | B | Quantum Drive | 5.5 | 0.018 | 305.6 | 232 |
| 516 | Aegis Vanguard Sentinel | Nova ★ | C | Quantum Drive | 5.5 | 0.018 | 305.6 | 211 |
| 517 | Aegis Vanguard Sentinel | Spicule | A | Quantum Drive | 5.5 | 0.018 | 305.6 | 274 |
| 518 | Aegis Vanguard Sentinel | Bolt | B | Quantum Drive | 5.5 | 0.018 | 305.6 | 232 |
| 519 | Aegis Vanguard Warden | Nova | C | Quantum Drive | 5.5 | 0.018 | 305.6 | 211 |
| 520 | Aegis Vanguard Warden | Spicule | A | Quantum Drive | 5.5 | 0.018 | 305.6 | 274 |
| 521 | Aegis Vanguard Warden | Bolt | B | Quantum Drive | 5.5 | 0.018 | 305.6 | 232 |
| 522 | RSI Zeus Mk II CL | Crossfield | C | Quantum Drive | 6.4 | 0.021 | 304.8 | 203 |
| 523 | RSI Zeus Mk II CL | XL-1 | A | Quantum Drive | 6.4 | 0.021 | 304.8 | 264 |
| 524 | RSI Zeus Mk II CL | Yeager | B | Quantum Drive | 6.4 | 0.021 | 304.8 | 224 |
| 525 | Argo MOLE | Crossfield | C | Quantum Drive | 6.4 | 0.021 | 304.8 | 203 |
| 526 | Argo MOLE | XL-1 | A | Quantum Drive | 6.4 | 0.021 | 304.8 | 264 |
| 527 | Argo MOLE | Yeager | B | Quantum Drive | 6.4 | 0.021 | 304.8 | 224 |
| 528 | Argo MOTH | Crossfield | C | Quantum Drive | 6.4 | 0.021 | 304.8 | 203 |
| 529 | Argo MOTH | XL-1 | A | Quantum Drive | 6.4 | 0.021 | 304.8 | 264 |
| 530 | Argo MOTH | Yeager | B | Quantum Drive | 6.4 | 0.021 | 304.8 | 224 |
| 531 | Argo SRV | Crossfield | C | Quantum Drive | 6.4 | 0.021 | 304.8 | 203 |
| 532 | Argo SRV | XL-1 | A | Quantum Drive | 6.4 | 0.021 | 304.8 | 264 |
| 533 | Argo SRV | Yeager | B | Quantum Drive | 6.4 | 0.021 | 304.8 | 224 |
| 534 | MISC Freelancer MAX | Crossfield | C | Quantum Drive | 6.4 | 0.021 | 304.8 | 203 |
| 535 | MISC Freelancer MAX | XL-1 | A | Quantum Drive | 6.4 | 0.021 | 304.8 | 264 |
| 536 | MISC Freelancer MAX | Yeager | B | Quantum Drive | 6.4 | 0.021 | 304.8 | 224 |
| 537 | RSI Zeus Mk II ES | Cascade | D | Quantum Drive | 6.7 | 0.022 | 304.5 | 237 |
| 538 | RSI Zeus Mk II ES | SparkFire | C | Quantum Drive | 6.7 | 0.022 | 304.5 | 301 |
| 539 | RSI Zeus Mk II ES | Flash | B | Quantum Drive | 6.7 | 0.022 | 304.5 | 290 |
| 540 | RSI Zeus Mk II ES | Hemera | A | Quantum Drive | 6.7 | 0.022 | 304.5 | 326 |
| 541 | RSI Zeus Mk II ES | Sojourn | B | Quantum Drive | 6.7 | 0.022 | 304.5 | 262 |
| 542 | RSI Zeus Mk II ES | SunFire | B | Quantum Drive | 6.7 | 0.022 | 304.5 | 331 |
| 543 | RSI Zeus Mk II ES | Aither | B | Quantum Drive | 6.7 | 0.022 | 304.5 | 276 |
| 544 | RSI Zeus Mk II ES | Torrent | C | Quantum Drive | 6.7 | 0.022 | 304.5 | 263 |
| 545 | RSI Zeus Mk II ES | Khaos ★ | C | Quantum Drive | 6.7 | 0.022 | 304.5 | 251 |
| 546 | RSI Zeus Mk II ES | Quest | D | Quantum Drive | 6.7 | 0.022 | 304.5 | 214 |
| 547 | RSI Zeus Mk II ES | Odyssey | C | Quantum Drive | 6.7 | 0.022 | 304.5 | 238 |
| 548 | MISC Freelancer DUR | Cascade | D | Quantum Drive | 6.7 | 0.022 | 304.5 | 237 |
| 549 | MISC Freelancer DUR | SparkFire | C | Quantum Drive | 6.7 | 0.022 | 304.5 | 301 |
| 550 | MISC Freelancer DUR | Flash | B | Quantum Drive | 6.7 | 0.022 | 304.5 | 290 |
| 551 | MISC Freelancer DUR | Hemera | A | Quantum Drive | 6.7 | 0.022 | 304.5 | 326 |
| 552 | MISC Freelancer DUR | Sojourn | B | Quantum Drive | 6.7 | 0.022 | 304.5 | 262 |
| 553 | MISC Freelancer DUR | SunFire | B | Quantum Drive | 6.7 | 0.022 | 304.5 | 331 |
| 554 | MISC Freelancer DUR | Aither | B | Quantum Drive | 6.7 | 0.022 | 304.5 | 276 |
| 555 | MISC Freelancer DUR | Torrent | C | Quantum Drive | 6.7 | 0.022 | 304.5 | 263 |
| 556 | MISC Freelancer DUR | Khaos | C | Quantum Drive | 6.7 | 0.022 | 304.5 | 251 |
| 557 | MISC Freelancer DUR | Quest | D | Quantum Drive | 6.7 | 0.022 | 304.5 | 214 |
| 558 | MISC Freelancer DUR | Odyssey ★ | C | Quantum Drive | 6.7 | 0.022 | 304.5 | 238 |
| 559 | Aegis Redeemer | Crossfield ★ | C | Quantum Drive | 6.3 | 0.021 | 300.0 | 203 |
| 560 | Aegis Redeemer | XL-1 | A | Quantum Drive | 6.3 | 0.021 | 300.0 | 264 |
| 561 | Aegis Redeemer | Yeager | B | Quantum Drive | 6.3 | 0.021 | 300.0 | 224 |
| 562 | Crusader A1 Spirit | Yaluk | D | Quantum Drive | 5.9 | 0.02 | 295.0 | 248 |
| 563 | Crusader A1 Spirit | Bolon | C | Quantum Drive | 5.9 | 0.02 | 295.0 | 276 |
| 564 | Crusader A1 Spirit | Huracan | B | Quantum Drive | 5.9 | 0.02 | 295.0 | 304 |
| 565 | Crusader Ares Star Fighter Inferno | Yaluk | D | Quantum Drive | 5.9 | 0.02 | 295.0 | 248 |
| 566 | Crusader Ares Star Fighter Inferno | Bolon | C | Quantum Drive | 5.9 | 0.02 | 295.0 | 276 |
| 567 | Crusader Ares Star Fighter Inferno | Huracan | B | Quantum Drive | 5.9 | 0.02 | 295.0 | 304 |
| 568 | Crusader Ares Star Fighter Ion | Yaluk | D | Quantum Drive | 5.9 | 0.02 | 295.0 | 248 |
| 569 | Crusader Ares Star Fighter Ion | Bolon | C | Quantum Drive | 5.9 | 0.02 | 295.0 | 276 |
| 570 | Crusader Ares Star Fighter Ion | Huracan | B | Quantum Drive | 5.9 | 0.02 | 295.0 | 304 |
| 571 | Crusader C1 Spirit | Yaluk | D | Quantum Drive | 5.9 | 0.02 | 295.0 | 248 |
| 572 | Crusader C1 Spirit | Bolon | C | Quantum Drive | 5.9 | 0.02 | 295.0 | 276 |
| 573 | Crusader C1 Spirit | Huracan | B | Quantum Drive | 5.9 | 0.02 | 295.0 | 304 |
| 574 | MISC Freelancer | Yaluk | D | Quantum Drive | 5.9 | 0.02 | 295.0 | 248 |
| 575 | MISC Freelancer | Bolon | C | Quantum Drive | 5.9 | 0.02 | 295.0 | 276 |
| 576 | MISC Freelancer | Huracan | B | Quantum Drive | 5.9 | 0.02 | 295.0 | 304 |
| 577 | MISC Freelancer MIS | Yaluk | D | Quantum Drive | 5.9 | 0.02 | 295.0 | 248 |
| 578 | MISC Freelancer MIS | Bolon | C | Quantum Drive | 5.9 | 0.02 | 295.0 | 276 |
| 579 | MISC Freelancer MIS | Huracan | B | Quantum Drive | 5.9 | 0.02 | 295.0 | 304 |
| 580 | RSI Zeus Mk II CL | Cascade | D | Quantum Drive | 6.4 | 0.022 | 290.9 | 237 |
| 581 | RSI Zeus Mk II CL | SparkFire | C | Quantum Drive | 6.4 | 0.022 | 290.9 | 301 |
| 582 | RSI Zeus Mk II CL | Flash | B | Quantum Drive | 6.4 | 0.022 | 290.9 | 290 |
| 583 | RSI Zeus Mk II CL | Hemera | A | Quantum Drive | 6.4 | 0.022 | 290.9 | 326 |
| 584 | RSI Zeus Mk II CL | Sojourn | B | Quantum Drive | 6.4 | 0.022 | 290.9 | 262 |
| 585 | RSI Zeus Mk II CL | SunFire | B | Quantum Drive | 6.4 | 0.022 | 290.9 | 331 |
| 586 | RSI Zeus Mk II CL | Aither | B | Quantum Drive | 6.4 | 0.022 | 290.9 | 276 |
| 587 | RSI Zeus Mk II CL | Torrent | C | Quantum Drive | 6.4 | 0.022 | 290.9 | 263 |
| 588 | RSI Zeus Mk II CL | Khaos ★ | C | Quantum Drive | 6.4 | 0.022 | 290.9 | 251 |
| 589 | RSI Zeus Mk II CL | Quest | D | Quantum Drive | 6.4 | 0.022 | 290.9 | 214 |
| 590 | RSI Zeus Mk II CL | Odyssey | C | Quantum Drive | 6.4 | 0.022 | 290.9 | 238 |
| 591 | Argo MOLE | Cascade | D | Quantum Drive | 6.4 | 0.022 | 290.9 | 237 |
| 592 | Argo MOLE | SparkFire | C | Quantum Drive | 6.4 | 0.022 | 290.9 | 301 |
| 593 | Argo MOLE | Flash | B | Quantum Drive | 6.4 | 0.022 | 290.9 | 290 |
| 594 | Argo MOLE | Hemera | A | Quantum Drive | 6.4 | 0.022 | 290.9 | 326 |
| 595 | Argo MOLE | Sojourn | B | Quantum Drive | 6.4 | 0.022 | 290.9 | 262 |
| 596 | Argo MOLE | SunFire | B | Quantum Drive | 6.4 | 0.022 | 290.9 | 331 |
| 597 | Argo MOLE | Aither | B | Quantum Drive | 6.4 | 0.022 | 290.9 | 276 |
| 598 | Argo MOLE | Torrent | C | Quantum Drive | 6.4 | 0.022 | 290.9 | 263 |
| 599 | Argo MOLE | Khaos | C | Quantum Drive | 6.4 | 0.022 | 290.9 | 251 |
| 600 | Argo MOLE | Quest | D | Quantum Drive | 6.4 | 0.022 | 290.9 | 214 |
| 601 | Argo MOLE | Odyssey | C | Quantum Drive | 6.4 | 0.022 | 290.9 | 238 |
| 602 | Argo MOTH | Cascade | D | Quantum Drive | 6.4 | 0.022 | 290.9 | 237 |
| 603 | Argo MOTH | SparkFire | C | Quantum Drive | 6.4 | 0.022 | 290.9 | 301 |
| 604 | Argo MOTH | Flash | B | Quantum Drive | 6.4 | 0.022 | 290.9 | 290 |
| 605 | Argo MOTH | Hemera | A | Quantum Drive | 6.4 | 0.022 | 290.9 | 326 |
| 606 | Argo MOTH | Sojourn | B | Quantum Drive | 6.4 | 0.022 | 290.9 | 262 |
| 607 | Argo MOTH | SunFire | B | Quantum Drive | 6.4 | 0.022 | 290.9 | 331 |
| 608 | Argo MOTH | Aither | B | Quantum Drive | 6.4 | 0.022 | 290.9 | 276 |
| 609 | Argo MOTH | Torrent | C | Quantum Drive | 6.4 | 0.022 | 290.9 | 263 |
| 610 | Argo MOTH | Khaos | C | Quantum Drive | 6.4 | 0.022 | 290.9 | 251 |
| 611 | Argo MOTH | Quest | D | Quantum Drive | 6.4 | 0.022 | 290.9 | 214 |
| 612 | Argo MOTH | Odyssey | C | Quantum Drive | 6.4 | 0.022 | 290.9 | 238 |
| 613 | Argo SRV | Cascade | D | Quantum Drive | 6.4 | 0.022 | 290.9 | 237 |
| 614 | Argo SRV | SparkFire | C | Quantum Drive | 6.4 | 0.022 | 290.9 | 301 |
| 615 | Argo SRV | Flash | B | Quantum Drive | 6.4 | 0.022 | 290.9 | 290 |
| 616 | Argo SRV | Hemera | A | Quantum Drive | 6.4 | 0.022 | 290.9 | 326 |
| 617 | Argo SRV | Sojourn | B | Quantum Drive | 6.4 | 0.022 | 290.9 | 262 |
| 618 | Argo SRV | SunFire | B | Quantum Drive | 6.4 | 0.022 | 290.9 | 331 |
| 619 | Argo SRV | Aither | B | Quantum Drive | 6.4 | 0.022 | 290.9 | 276 |
| 620 | Argo SRV | Torrent | C | Quantum Drive | 6.4 | 0.022 | 290.9 | 263 |
| 621 | Argo SRV | Khaos | C | Quantum Drive | 6.4 | 0.022 | 290.9 | 251 |
| 622 | Argo SRV | Quest | D | Quantum Drive | 6.4 | 0.022 | 290.9 | 214 |
| 623 | Argo SRV | Odyssey | C | Quantum Drive | 6.4 | 0.022 | 290.9 | 238 |
| 624 | MISC Freelancer MAX | Cascade | D | Quantum Drive | 6.4 | 0.022 | 290.9 | 237 |
| 625 | MISC Freelancer MAX | SparkFire | C | Quantum Drive | 6.4 | 0.022 | 290.9 | 301 |
| 626 | MISC Freelancer MAX | Flash | B | Quantum Drive | 6.4 | 0.022 | 290.9 | 290 |
| 627 | MISC Freelancer MAX | Hemera | A | Quantum Drive | 6.4 | 0.022 | 290.9 | 326 |
| 628 | MISC Freelancer MAX | Sojourn | B | Quantum Drive | 6.4 | 0.022 | 290.9 | 262 |
| 629 | MISC Freelancer MAX | SunFire | B | Quantum Drive | 6.4 | 0.022 | 290.9 | 331 |
| 630 | MISC Freelancer MAX | Aither | B | Quantum Drive | 6.4 | 0.022 | 290.9 | 276 |
| 631 | MISC Freelancer MAX | Torrent | C | Quantum Drive | 6.4 | 0.022 | 290.9 | 263 |
| 632 | MISC Freelancer MAX | Khaos | C | Quantum Drive | 6.4 | 0.022 | 290.9 | 251 |
| 633 | MISC Freelancer MAX | Quest | D | Quantum Drive | 6.4 | 0.022 | 290.9 | 214 |
| 634 | MISC Freelancer MAX | Odyssey ★ | C | Quantum Drive | 6.4 | 0.022 | 290.9 | 238 |
| 635 | Aegis Redeemer | Cascade | D | Quantum Drive | 6.3 | 0.022 | 286.4 | 237 |
| 636 | Aegis Redeemer | SparkFire | C | Quantum Drive | 6.3 | 0.022 | 286.4 | 301 |
| 637 | Aegis Redeemer | Flash | B | Quantum Drive | 6.3 | 0.022 | 286.4 | 290 |
| 638 | Aegis Redeemer | Hemera | A | Quantum Drive | 6.3 | 0.022 | 286.4 | 326 |
| 639 | Aegis Redeemer | Sojourn | B | Quantum Drive | 6.3 | 0.022 | 286.4 | 262 |
| 640 | Aegis Redeemer | SunFire | B | Quantum Drive | 6.3 | 0.022 | 286.4 | 331 |
| 641 | Aegis Redeemer | Aither | B | Quantum Drive | 6.3 | 0.022 | 286.4 | 276 |
| 642 | Aegis Redeemer | Torrent | C | Quantum Drive | 6.3 | 0.022 | 286.4 | 263 |
| 643 | Aegis Redeemer | Khaos | C | Quantum Drive | 6.3 | 0.022 | 286.4 | 251 |
| 644 | Aegis Redeemer | Quest | D | Quantum Drive | 6.3 | 0.022 | 286.4 | 214 |
| 645 | Aegis Redeemer | Odyssey | C | Quantum Drive | 6.3 | 0.022 | 286.4 | 238 |
| 646 | Aegis Vanguard Hoplite | Nova | C | Quantum Drive | 5.1 | 0.018 | 283.3 | 211 |
| 647 | Aegis Vanguard Hoplite | Spicule | A | Quantum Drive | 5.1 | 0.018 | 283.3 | 274 |
| 648 | Aegis Vanguard Hoplite | Bolt | B | Quantum Drive | 5.1 | 0.018 | 283.3 | 232 |
| 649 | Crusader A1 Spirit | Crossfield | C | Quantum Drive | 5.9 | 0.021 | 281.0 | 203 |
| 650 | Crusader A1 Spirit | XL-1 | A | Quantum Drive | 5.9 | 0.021 | 281.0 | 264 |
| 651 | Crusader A1 Spirit | Yeager ★ | B | Quantum Drive | 5.9 | 0.021 | 281.0 | 224 |
| 652 | Crusader Ares Star Fighter Inferno | Crossfield ★ | C | Quantum Drive | 5.9 | 0.021 | 281.0 | 203 |
| 653 | Crusader Ares Star Fighter Inferno | XL-1 | A | Quantum Drive | 5.9 | 0.021 | 281.0 | 264 |
| 654 | Crusader Ares Star Fighter Inferno | Yeager | B | Quantum Drive | 5.9 | 0.021 | 281.0 | 224 |
| 655 | Crusader Ares Star Fighter Ion | Crossfield ★ | C | Quantum Drive | 5.9 | 0.021 | 281.0 | 203 |
| 656 | Crusader Ares Star Fighter Ion | XL-1 | A | Quantum Drive | 5.9 | 0.021 | 281.0 | 264 |
| 657 | Crusader Ares Star Fighter Ion | Yeager | B | Quantum Drive | 5.9 | 0.021 | 281.0 | 224 |
| 658 | Crusader C1 Spirit | Crossfield | C | Quantum Drive | 5.9 | 0.021 | 281.0 | 203 |
| 659 | Crusader C1 Spirit | XL-1 | A | Quantum Drive | 5.9 | 0.021 | 281.0 | 264 |
| 660 | Crusader C1 Spirit | Yeager ★ | B | Quantum Drive | 5.9 | 0.021 | 281.0 | 224 |
| 661 | MISC Freelancer | Crossfield | C | Quantum Drive | 5.9 | 0.021 | 281.0 | 203 |
| 662 | MISC Freelancer | XL-1 | A | Quantum Drive | 5.9 | 0.021 | 281.0 | 264 |
| 663 | MISC Freelancer | Yeager | B | Quantum Drive | 5.9 | 0.021 | 281.0 | 224 |
| 664 | MISC Freelancer MIS | Crossfield ★ | C | Quantum Drive | 5.9 | 0.021 | 281.0 | 203 |
| 665 | MISC Freelancer MIS | XL-1 | A | Quantum Drive | 5.9 | 0.021 | 281.0 | 264 |
| 666 | MISC Freelancer MIS | Yeager | B | Quantum Drive | 5.9 | 0.021 | 281.0 | 224 |
| 667 | Aegis Vanguard Harbinger | Yaluk | D | Quantum Drive | 5.5 | 0.02 | 275.0 | 248 |
| 668 | Aegis Vanguard Harbinger | Bolon | C | Quantum Drive | 5.5 | 0.02 | 275.0 | 276 |
| 669 | Aegis Vanguard Harbinger | Huracan | B | Quantum Drive | 5.5 | 0.02 | 275.0 | 304 |
| 670 | Aegis Vanguard Sentinel | Yaluk | D | Quantum Drive | 5.5 | 0.02 | 275.0 | 248 |
| 671 | Aegis Vanguard Sentinel | Bolon | C | Quantum Drive | 5.5 | 0.02 | 275.0 | 276 |
| 672 | Aegis Vanguard Sentinel | Huracan | B | Quantum Drive | 5.5 | 0.02 | 275.0 | 304 |
| 673 | Aegis Vanguard Warden | Yaluk | D | Quantum Drive | 5.5 | 0.02 | 275.0 | 248 |
| 674 | Aegis Vanguard Warden | Bolon | C | Quantum Drive | 5.5 | 0.02 | 275.0 | 276 |
| 675 | Aegis Vanguard Warden | Huracan | B | Quantum Drive | 5.5 | 0.02 | 275.0 | 304 |
| 676 | Crusader A1 Spirit | Cascade | D | Quantum Drive | 5.9 | 0.022 | 268.2 | 237 |
| 677 | Crusader A1 Spirit | SparkFire | C | Quantum Drive | 5.9 | 0.022 | 268.2 | 301 |
| 678 | Crusader A1 Spirit | Flash | B | Quantum Drive | 5.9 | 0.022 | 268.2 | 290 |
| 679 | Crusader A1 Spirit | Hemera | A | Quantum Drive | 5.9 | 0.022 | 268.2 | 326 |
| 680 | Crusader A1 Spirit | Sojourn | B | Quantum Drive | 5.9 | 0.022 | 268.2 | 262 |
| 681 | Crusader A1 Spirit | SunFire | B | Quantum Drive | 5.9 | 0.022 | 268.2 | 331 |
| 682 | Crusader A1 Spirit | Aither | B | Quantum Drive | 5.9 | 0.022 | 268.2 | 276 |
| 683 | Crusader A1 Spirit | Torrent | C | Quantum Drive | 5.9 | 0.022 | 268.2 | 263 |
| 684 | Crusader A1 Spirit | Khaos | C | Quantum Drive | 5.9 | 0.022 | 268.2 | 251 |
| 685 | Crusader A1 Spirit | Quest | D | Quantum Drive | 5.9 | 0.022 | 268.2 | 214 |
| 686 | Crusader A1 Spirit | Odyssey | C | Quantum Drive | 5.9 | 0.022 | 268.2 | 238 |
| 687 | Crusader Ares Star Fighter Inferno | Cascade | D | Quantum Drive | 5.9 | 0.022 | 268.2 | 237 |
| 688 | Crusader Ares Star Fighter Inferno | SparkFire | C | Quantum Drive | 5.9 | 0.022 | 268.2 | 301 |
| 689 | Crusader Ares Star Fighter Inferno | Flash | B | Quantum Drive | 5.9 | 0.022 | 268.2 | 290 |
| 690 | Crusader Ares Star Fighter Inferno | Hemera | A | Quantum Drive | 5.9 | 0.022 | 268.2 | 326 |
| 691 | Crusader Ares Star Fighter Inferno | Sojourn | B | Quantum Drive | 5.9 | 0.022 | 268.2 | 262 |
| 692 | Crusader Ares Star Fighter Inferno | SunFire | B | Quantum Drive | 5.9 | 0.022 | 268.2 | 331 |
| 693 | Crusader Ares Star Fighter Inferno | Aither | B | Quantum Drive | 5.9 | 0.022 | 268.2 | 276 |
| 694 | Crusader Ares Star Fighter Inferno | Torrent | C | Quantum Drive | 5.9 | 0.022 | 268.2 | 263 |
| 695 | Crusader Ares Star Fighter Inferno | Khaos | C | Quantum Drive | 5.9 | 0.022 | 268.2 | 251 |
| 696 | Crusader Ares Star Fighter Inferno | Quest | D | Quantum Drive | 5.9 | 0.022 | 268.2 | 214 |
| 697 | Crusader Ares Star Fighter Inferno | Odyssey | C | Quantum Drive | 5.9 | 0.022 | 268.2 | 238 |
| 698 | Crusader Ares Star Fighter Ion | Cascade | D | Quantum Drive | 5.9 | 0.022 | 268.2 | 237 |
| 699 | Crusader Ares Star Fighter Ion | SparkFire | C | Quantum Drive | 5.9 | 0.022 | 268.2 | 301 |
| 700 | Crusader Ares Star Fighter Ion | Flash | B | Quantum Drive | 5.9 | 0.022 | 268.2 | 290 |
| 701 | Crusader Ares Star Fighter Ion | Hemera | A | Quantum Drive | 5.9 | 0.022 | 268.2 | 326 |
| 702 | Crusader Ares Star Fighter Ion | Sojourn | B | Quantum Drive | 5.9 | 0.022 | 268.2 | 262 |
| 703 | Crusader Ares Star Fighter Ion | SunFire | B | Quantum Drive | 5.9 | 0.022 | 268.2 | 331 |
| 704 | Crusader Ares Star Fighter Ion | Aither | B | Quantum Drive | 5.9 | 0.022 | 268.2 | 276 |
| 705 | Crusader Ares Star Fighter Ion | Torrent | C | Quantum Drive | 5.9 | 0.022 | 268.2 | 263 |
| 706 | Crusader Ares Star Fighter Ion | Khaos | C | Quantum Drive | 5.9 | 0.022 | 268.2 | 251 |
| 707 | Crusader Ares Star Fighter Ion | Quest | D | Quantum Drive | 5.9 | 0.022 | 268.2 | 214 |
| 708 | Crusader Ares Star Fighter Ion | Odyssey | C | Quantum Drive | 5.9 | 0.022 | 268.2 | 238 |
| 709 | Crusader C1 Spirit | Cascade | D | Quantum Drive | 5.9 | 0.022 | 268.2 | 237 |
| 710 | Crusader C1 Spirit | SparkFire | C | Quantum Drive | 5.9 | 0.022 | 268.2 | 301 |
| 711 | Crusader C1 Spirit | Flash | B | Quantum Drive | 5.9 | 0.022 | 268.2 | 290 |
| 712 | Crusader C1 Spirit | Hemera | A | Quantum Drive | 5.9 | 0.022 | 268.2 | 326 |
| 713 | Crusader C1 Spirit | Sojourn | B | Quantum Drive | 5.9 | 0.022 | 268.2 | 262 |
| 714 | Crusader C1 Spirit | SunFire | B | Quantum Drive | 5.9 | 0.022 | 268.2 | 331 |
| 715 | Crusader C1 Spirit | Aither | B | Quantum Drive | 5.9 | 0.022 | 268.2 | 276 |
| 716 | Crusader C1 Spirit | Torrent | C | Quantum Drive | 5.9 | 0.022 | 268.2 | 263 |
| 717 | Crusader C1 Spirit | Khaos | C | Quantum Drive | 5.9 | 0.022 | 268.2 | 251 |
| 718 | Crusader C1 Spirit | Quest | D | Quantum Drive | 5.9 | 0.022 | 268.2 | 214 |
| 719 | Crusader C1 Spirit | Odyssey | C | Quantum Drive | 5.9 | 0.022 | 268.2 | 238 |
| 720 | MISC Freelancer | Cascade | D | Quantum Drive | 5.9 | 0.022 | 268.2 | 237 |
| 721 | MISC Freelancer | SparkFire | C | Quantum Drive | 5.9 | 0.022 | 268.2 | 301 |
| 722 | MISC Freelancer | Flash | B | Quantum Drive | 5.9 | 0.022 | 268.2 | 290 |
| 723 | MISC Freelancer | Hemera | A | Quantum Drive | 5.9 | 0.022 | 268.2 | 326 |
| 724 | MISC Freelancer | Sojourn | B | Quantum Drive | 5.9 | 0.022 | 268.2 | 262 |
| 725 | MISC Freelancer | SunFire | B | Quantum Drive | 5.9 | 0.022 | 268.2 | 331 |
| 726 | MISC Freelancer | Aither | B | Quantum Drive | 5.9 | 0.022 | 268.2 | 276 |
| 727 | MISC Freelancer | Torrent | C | Quantum Drive | 5.9 | 0.022 | 268.2 | 263 |
| 728 | MISC Freelancer | Khaos | C | Quantum Drive | 5.9 | 0.022 | 268.2 | 251 |
| 729 | MISC Freelancer | Quest | D | Quantum Drive | 5.9 | 0.022 | 268.2 | 214 |
| 730 | MISC Freelancer | Odyssey ★ | C | Quantum Drive | 5.9 | 0.022 | 268.2 | 238 |
| 731 | MISC Freelancer MIS | Cascade | D | Quantum Drive | 5.9 | 0.022 | 268.2 | 237 |
| 732 | MISC Freelancer MIS | SparkFire | C | Quantum Drive | 5.9 | 0.022 | 268.2 | 301 |
| 733 | MISC Freelancer MIS | Flash | B | Quantum Drive | 5.9 | 0.022 | 268.2 | 290 |
| 734 | MISC Freelancer MIS | Hemera | A | Quantum Drive | 5.9 | 0.022 | 268.2 | 326 |
| 735 | MISC Freelancer MIS | Sojourn | B | Quantum Drive | 5.9 | 0.022 | 268.2 | 262 |
| 736 | MISC Freelancer MIS | SunFire | B | Quantum Drive | 5.9 | 0.022 | 268.2 | 331 |
| 737 | MISC Freelancer MIS | Aither | B | Quantum Drive | 5.9 | 0.022 | 268.2 | 276 |
| 738 | MISC Freelancer MIS | Torrent | C | Quantum Drive | 5.9 | 0.022 | 268.2 | 263 |
| 739 | MISC Freelancer MIS | Khaos | C | Quantum Drive | 5.9 | 0.022 | 268.2 | 251 |
| 740 | MISC Freelancer MIS | Quest | D | Quantum Drive | 5.9 | 0.022 | 268.2 | 214 |
| 741 | MISC Freelancer MIS | Odyssey | C | Quantum Drive | 5.9 | 0.022 | 268.2 | 238 |
| 742 | Aegis Vanguard Harbinger | Crossfield | C | Quantum Drive | 5.5 | 0.021 | 261.9 | 203 |
| 743 | Aegis Vanguard Harbinger | XL-1 | A | Quantum Drive | 5.5 | 0.021 | 261.9 | 264 |
| 744 | Aegis Vanguard Harbinger | Yeager ★ | B | Quantum Drive | 5.5 | 0.021 | 261.9 | 224 |
| 745 | Aegis Vanguard Sentinel | Crossfield | C | Quantum Drive | 5.5 | 0.021 | 261.9 | 203 |
| 746 | Aegis Vanguard Sentinel | XL-1 | A | Quantum Drive | 5.5 | 0.021 | 261.9 | 264 |
| 747 | Aegis Vanguard Sentinel | Yeager | B | Quantum Drive | 5.5 | 0.021 | 261.9 | 224 |
| 748 | Aegis Vanguard Warden | Crossfield ★ | C | Quantum Drive | 5.5 | 0.021 | 261.9 | 203 |
| 749 | Aegis Vanguard Warden | XL-1 | A | Quantum Drive | 5.5 | 0.021 | 261.9 | 264 |
| 750 | Aegis Vanguard Warden | Yeager | B | Quantum Drive | 5.5 | 0.021 | 261.9 | 224 |
| 751 | Drake Cutlass Black | Nova | C | Quantum Drive | 4.6 | 0.018 | 255.6 | 211 |
| 752 | Drake Cutlass Black | Spicule | A | Quantum Drive | 4.6 | 0.018 | 255.6 | 274 |
| 753 | Drake Cutlass Black | Bolt | B | Quantum Drive | 4.6 | 0.018 | 255.6 | 232 |
| 754 | Drake Cutlass Blue | Nova | C | Quantum Drive | 4.6 | 0.018 | 255.6 | 211 |
| 755 | Drake Cutlass Blue | Spicule | A | Quantum Drive | 4.6 | 0.018 | 255.6 | 274 |
| 756 | Drake Cutlass Blue | Bolt | B | Quantum Drive | 4.6 | 0.018 | 255.6 | 232 |
| 757 | Drake Cutlass Red | Nova | C | Quantum Drive | 4.6 | 0.018 | 255.6 | 211 |
| 758 | Drake Cutlass Red | Spicule | A | Quantum Drive | 4.6 | 0.018 | 255.6 | 274 |
| 759 | Drake Cutlass Red | Bolt | B | Quantum Drive | 4.6 | 0.018 | 255.6 | 232 |
| 760 | Esperia Stinger | Nova | C | Quantum Drive | 4.6 | 0.018 | 255.6 | 211 |
| 761 | Esperia Stinger | Spicule | A | Quantum Drive | 4.6 | 0.018 | 255.6 | 274 |
| 762 | Esperia Stinger | Bolt | B | Quantum Drive | 4.6 | 0.018 | 255.6 | 232 |
| 763 | Mirai Guardian | Nova | C | Quantum Drive | 4.6 | 0.018 | 255.6 | 211 |
| 764 | Mirai Guardian | Spicule | A | Quantum Drive | 4.6 | 0.018 | 255.6 | 274 |
| 765 | Mirai Guardian | Bolt | B | Quantum Drive | 4.6 | 0.018 | 255.6 | 232 |
| 766 | Mirai Guardian MX | Nova | C | Quantum Drive | 4.6 | 0.018 | 255.6 | 211 |
| 767 | Mirai Guardian MX | Spicule | A | Quantum Drive | 4.6 | 0.018 | 255.6 | 274 |
| 768 | Mirai Guardian MX | Bolt | B | Quantum Drive | 4.6 | 0.018 | 255.6 | 232 |
| 769 | Aegis Vanguard Hoplite | Yaluk | D | Quantum Drive | 5.1 | 0.02 | 255.0 | 248 |
| 770 | Aegis Vanguard Hoplite | Bolon | C | Quantum Drive | 5.1 | 0.02 | 255.0 | 276 |
| 771 | Aegis Vanguard Hoplite | Huracan | B | Quantum Drive | 5.1 | 0.02 | 255.0 | 304 |
| 772 | Aegis Vanguard Harbinger | Cascade | D | Quantum Drive | 5.5 | 0.022 | 250.0 | 237 |
| 773 | Aegis Vanguard Harbinger | SparkFire | C | Quantum Drive | 5.5 | 0.022 | 250.0 | 301 |
| 774 | Aegis Vanguard Harbinger | Flash | B | Quantum Drive | 5.5 | 0.022 | 250.0 | 290 |
| 775 | Aegis Vanguard Harbinger | Hemera | A | Quantum Drive | 5.5 | 0.022 | 250.0 | 326 |
| 776 | Aegis Vanguard Harbinger | Sojourn | B | Quantum Drive | 5.5 | 0.022 | 250.0 | 262 |
| 777 | Aegis Vanguard Harbinger | SunFire | B | Quantum Drive | 5.5 | 0.022 | 250.0 | 331 |
| 778 | Aegis Vanguard Harbinger | Aither | B | Quantum Drive | 5.5 | 0.022 | 250.0 | 276 |
| 779 | Aegis Vanguard Harbinger | Torrent | C | Quantum Drive | 5.5 | 0.022 | 250.0 | 263 |
| 780 | Aegis Vanguard Harbinger | Khaos | C | Quantum Drive | 5.5 | 0.022 | 250.0 | 251 |
| 781 | Aegis Vanguard Harbinger | Quest | D | Quantum Drive | 5.5 | 0.022 | 250.0 | 214 |
| 782 | Aegis Vanguard Harbinger | Odyssey | C | Quantum Drive | 5.5 | 0.022 | 250.0 | 238 |
| 783 | Aegis Vanguard Sentinel | Cascade | D | Quantum Drive | 5.5 | 0.022 | 250.0 | 237 |
| 784 | Aegis Vanguard Sentinel | SparkFire | C | Quantum Drive | 5.5 | 0.022 | 250.0 | 301 |
| 785 | Aegis Vanguard Sentinel | Flash | B | Quantum Drive | 5.5 | 0.022 | 250.0 | 290 |
| 786 | Aegis Vanguard Sentinel | Hemera | A | Quantum Drive | 5.5 | 0.022 | 250.0 | 326 |
| 787 | Aegis Vanguard Sentinel | Sojourn | B | Quantum Drive | 5.5 | 0.022 | 250.0 | 262 |
| 788 | Aegis Vanguard Sentinel | SunFire | B | Quantum Drive | 5.5 | 0.022 | 250.0 | 331 |
| 789 | Aegis Vanguard Sentinel | Aither | B | Quantum Drive | 5.5 | 0.022 | 250.0 | 276 |
| 790 | Aegis Vanguard Sentinel | Torrent | C | Quantum Drive | 5.5 | 0.022 | 250.0 | 263 |
| 791 | Aegis Vanguard Sentinel | Khaos | C | Quantum Drive | 5.5 | 0.022 | 250.0 | 251 |
| 792 | Aegis Vanguard Sentinel | Quest | D | Quantum Drive | 5.5 | 0.022 | 250.0 | 214 |
| 793 | Aegis Vanguard Sentinel | Odyssey | C | Quantum Drive | 5.5 | 0.022 | 250.0 | 238 |
| 794 | Aegis Vanguard Warden | Cascade | D | Quantum Drive | 5.5 | 0.022 | 250.0 | 237 |
| 795 | Aegis Vanguard Warden | SparkFire | C | Quantum Drive | 5.5 | 0.022 | 250.0 | 301 |
| 796 | Aegis Vanguard Warden | Flash | B | Quantum Drive | 5.5 | 0.022 | 250.0 | 290 |
| 797 | Aegis Vanguard Warden | Hemera | A | Quantum Drive | 5.5 | 0.022 | 250.0 | 326 |
| 798 | Aegis Vanguard Warden | Sojourn | B | Quantum Drive | 5.5 | 0.022 | 250.0 | 262 |
| 799 | Aegis Vanguard Warden | SunFire | B | Quantum Drive | 5.5 | 0.022 | 250.0 | 331 |
| 800 | Aegis Vanguard Warden | Aither | B | Quantum Drive | 5.5 | 0.022 | 250.0 | 276 |
| 801 | Aegis Vanguard Warden | Torrent | C | Quantum Drive | 5.5 | 0.022 | 250.0 | 263 |
| 802 | Aegis Vanguard Warden | Khaos | C | Quantum Drive | 5.5 | 0.022 | 250.0 | 251 |
| 803 | Aegis Vanguard Warden | Quest | D | Quantum Drive | 5.5 | 0.022 | 250.0 | 214 |
| 804 | Aegis Vanguard Warden | Odyssey | C | Quantum Drive | 5.5 | 0.022 | 250.0 | 238 |
| 805 | Aegis Vanguard Hoplite | Crossfield ★ | C | Quantum Drive | 5.1 | 0.021 | 242.9 | 203 |
| 806 | Aegis Vanguard Hoplite | XL-1 | A | Quantum Drive | 5.1 | 0.021 | 242.9 | 264 |
| 807 | Aegis Vanguard Hoplite | Yeager | B | Quantum Drive | 5.1 | 0.021 | 242.9 | 224 |
| 808 | Aegis Vanguard Hoplite | Cascade | D | Quantum Drive | 5.1 | 0.022 | 231.8 | 237 |
| 809 | Aegis Vanguard Hoplite | SparkFire | C | Quantum Drive | 5.1 | 0.022 | 231.8 | 301 |
| 810 | Aegis Vanguard Hoplite | Flash | B | Quantum Drive | 5.1 | 0.022 | 231.8 | 290 |
| 811 | Aegis Vanguard Hoplite | Hemera | A | Quantum Drive | 5.1 | 0.022 | 231.8 | 326 |
| 812 | Aegis Vanguard Hoplite | Sojourn | B | Quantum Drive | 5.1 | 0.022 | 231.8 | 262 |
| 813 | Aegis Vanguard Hoplite | SunFire | B | Quantum Drive | 5.1 | 0.022 | 231.8 | 331 |
| 814 | Aegis Vanguard Hoplite | Aither | B | Quantum Drive | 5.1 | 0.022 | 231.8 | 276 |
| 815 | Aegis Vanguard Hoplite | Torrent | C | Quantum Drive | 5.1 | 0.022 | 231.8 | 263 |
| 816 | Aegis Vanguard Hoplite | Khaos | C | Quantum Drive | 5.1 | 0.022 | 231.8 | 251 |
| 817 | Aegis Vanguard Hoplite | Quest | D | Quantum Drive | 5.1 | 0.022 | 231.8 | 214 |
| 818 | Aegis Vanguard Hoplite | Odyssey | C | Quantum Drive | 5.1 | 0.022 | 231.8 | 238 |
| 819 | Drake Cutlass Black | Yaluk | D | Quantum Drive | 4.6 | 0.02 | 230.0 | 248 |
| 820 | Drake Cutlass Black | Bolon | C | Quantum Drive | 4.6 | 0.02 | 230.0 | 276 |
| 821 | Drake Cutlass Black | Huracan | B | Quantum Drive | 4.6 | 0.02 | 230.0 | 304 |
| 822 | Drake Cutlass Blue | Yaluk | D | Quantum Drive | 4.6 | 0.02 | 230.0 | 248 |
| 823 | Drake Cutlass Blue | Bolon ★ | C | Quantum Drive | 4.6 | 0.02 | 230.0 | 276 |
| 824 | Drake Cutlass Blue | Huracan | B | Quantum Drive | 4.6 | 0.02 | 230.0 | 304 |
| 825 | Drake Cutlass Red | Yaluk | D | Quantum Drive | 4.6 | 0.02 | 230.0 | 248 |
| 826 | Drake Cutlass Red | Bolon ★ | C | Quantum Drive | 4.6 | 0.02 | 230.0 | 276 |
| 827 | Drake Cutlass Red | Huracan | B | Quantum Drive | 4.6 | 0.02 | 230.0 | 304 |
| 828 | Esperia Stinger | Yaluk | D | Quantum Drive | 4.6 | 0.02 | 230.0 | 248 |
| 829 | Esperia Stinger | Bolon ★ | C | Quantum Drive | 4.6 | 0.02 | 230.0 | 276 |
| 830 | Esperia Stinger | Huracan | B | Quantum Drive | 4.6 | 0.02 | 230.0 | 304 |
| 831 | Mirai Guardian | Yaluk | D | Quantum Drive | 4.6 | 0.02 | 230.0 | 248 |
| 832 | Mirai Guardian | Bolon | C | Quantum Drive | 4.6 | 0.02 | 230.0 | 276 |
| 833 | Mirai Guardian | Huracan | B | Quantum Drive | 4.6 | 0.02 | 230.0 | 304 |
| 834 | Mirai Guardian MX | Yaluk | D | Quantum Drive | 4.6 | 0.02 | 230.0 | 248 |
| 835 | Mirai Guardian MX | Bolon | C | Quantum Drive | 4.6 | 0.02 | 230.0 | 276 |
| 836 | Mirai Guardian MX | Huracan | B | Quantum Drive | 4.6 | 0.02 | 230.0 | 304 |
| 837 | Grey's Shiv | Nova | C | Quantum Drive | 4.1 | 0.018 | 227.8 | 211 |
| 838 | Grey's Shiv | Spicule | A | Quantum Drive | 4.1 | 0.018 | 227.8 | 274 |
| 839 | Grey's Shiv | Bolt | B | Quantum Drive | 4.1 | 0.018 | 227.8 | 232 |
| 840 | Drake Cutlass Black | Crossfield | C | Quantum Drive | 4.6 | 0.021 | 219.0 | 203 |
| 841 | Drake Cutlass Black | XL-1 | A | Quantum Drive | 4.6 | 0.021 | 219.0 | 264 |
| 842 | Drake Cutlass Black | Yeager | B | Quantum Drive | 4.6 | 0.021 | 219.0 | 224 |
| 843 | Drake Cutlass Blue | Crossfield | C | Quantum Drive | 4.6 | 0.021 | 219.0 | 203 |
| 844 | Drake Cutlass Blue | XL-1 | A | Quantum Drive | 4.6 | 0.021 | 219.0 | 264 |
| 845 | Drake Cutlass Blue | Yeager | B | Quantum Drive | 4.6 | 0.021 | 219.0 | 224 |
| 846 | Drake Cutlass Red | Crossfield | C | Quantum Drive | 4.6 | 0.021 | 219.0 | 203 |
| 847 | Drake Cutlass Red | XL-1 | A | Quantum Drive | 4.6 | 0.021 | 219.0 | 264 |
| 848 | Drake Cutlass Red | Yeager | B | Quantum Drive | 4.6 | 0.021 | 219.0 | 224 |
| 849 | Esperia Stinger | Crossfield | C | Quantum Drive | 4.6 | 0.021 | 219.0 | 203 |
| 850 | Esperia Stinger | XL-1 | A | Quantum Drive | 4.6 | 0.021 | 219.0 | 264 |
| 851 | Esperia Stinger | Yeager | B | Quantum Drive | 4.6 | 0.021 | 219.0 | 224 |
| 852 | Mirai Guardian | Crossfield ★ | C | Quantum Drive | 4.6 | 0.021 | 219.0 | 203 |
| 853 | Mirai Guardian | XL-1 | A | Quantum Drive | 4.6 | 0.021 | 219.0 | 264 |
| 854 | Mirai Guardian | Yeager | B | Quantum Drive | 4.6 | 0.021 | 219.0 | 224 |
| 855 | Mirai Guardian MX | Crossfield ★ | C | Quantum Drive | 4.6 | 0.021 | 219.0 | 203 |
| 856 | Mirai Guardian MX | XL-1 | A | Quantum Drive | 4.6 | 0.021 | 219.0 | 264 |
| 857 | Mirai Guardian MX | Yeager | B | Quantum Drive | 4.6 | 0.021 | 219.0 | 224 |
| 858 | Drake Cutlass Black | Cascade | D | Quantum Drive | 4.6 | 0.022 | 209.1 | 237 |
| 859 | Drake Cutlass Black | SparkFire | C | Quantum Drive | 4.6 | 0.022 | 209.1 | 301 |
| 860 | Drake Cutlass Black | Flash | B | Quantum Drive | 4.6 | 0.022 | 209.1 | 290 |
| 861 | Drake Cutlass Black | Hemera | A | Quantum Drive | 4.6 | 0.022 | 209.1 | 326 |
| 862 | Drake Cutlass Black | Sojourn | B | Quantum Drive | 4.6 | 0.022 | 209.1 | 262 |
| 863 | Drake Cutlass Black | SunFire | B | Quantum Drive | 4.6 | 0.022 | 209.1 | 331 |
| 864 | Drake Cutlass Black | Aither | B | Quantum Drive | 4.6 | 0.022 | 209.1 | 276 |
| 865 | Drake Cutlass Black | Torrent | C | Quantum Drive | 4.6 | 0.022 | 209.1 | 263 |
| 866 | Drake Cutlass Black | Khaos | C | Quantum Drive | 4.6 | 0.022 | 209.1 | 251 |
| 867 | Drake Cutlass Black | Quest | D | Quantum Drive | 4.6 | 0.022 | 209.1 | 214 |
| 868 | Drake Cutlass Black | Odyssey ★ | C | Quantum Drive | 4.6 | 0.022 | 209.1 | 238 |
| 869 | Drake Cutlass Blue | Cascade | D | Quantum Drive | 4.6 | 0.022 | 209.1 | 237 |
| 870 | Drake Cutlass Blue | SparkFire | C | Quantum Drive | 4.6 | 0.022 | 209.1 | 301 |
| 871 | Drake Cutlass Blue | Flash | B | Quantum Drive | 4.6 | 0.022 | 209.1 | 290 |
| 872 | Drake Cutlass Blue | Hemera | A | Quantum Drive | 4.6 | 0.022 | 209.1 | 326 |
| 873 | Drake Cutlass Blue | Sojourn | B | Quantum Drive | 4.6 | 0.022 | 209.1 | 262 |
| 874 | Drake Cutlass Blue | SunFire | B | Quantum Drive | 4.6 | 0.022 | 209.1 | 331 |
| 875 | Drake Cutlass Blue | Aither | B | Quantum Drive | 4.6 | 0.022 | 209.1 | 276 |
| 876 | Drake Cutlass Blue | Torrent | C | Quantum Drive | 4.6 | 0.022 | 209.1 | 263 |
| 877 | Drake Cutlass Blue | Khaos | C | Quantum Drive | 4.6 | 0.022 | 209.1 | 251 |
| 878 | Drake Cutlass Blue | Quest | D | Quantum Drive | 4.6 | 0.022 | 209.1 | 214 |
| 879 | Drake Cutlass Blue | Odyssey | C | Quantum Drive | 4.6 | 0.022 | 209.1 | 238 |
| 880 | Drake Cutlass Red | Cascade | D | Quantum Drive | 4.6 | 0.022 | 209.1 | 237 |
| 881 | Drake Cutlass Red | SparkFire | C | Quantum Drive | 4.6 | 0.022 | 209.1 | 301 |
| 882 | Drake Cutlass Red | Flash | B | Quantum Drive | 4.6 | 0.022 | 209.1 | 290 |
| 883 | Drake Cutlass Red | Hemera | A | Quantum Drive | 4.6 | 0.022 | 209.1 | 326 |
| 884 | Drake Cutlass Red | Sojourn | B | Quantum Drive | 4.6 | 0.022 | 209.1 | 262 |
| 885 | Drake Cutlass Red | SunFire | B | Quantum Drive | 4.6 | 0.022 | 209.1 | 331 |
| 886 | Drake Cutlass Red | Aither | B | Quantum Drive | 4.6 | 0.022 | 209.1 | 276 |
| 887 | Drake Cutlass Red | Torrent | C | Quantum Drive | 4.6 | 0.022 | 209.1 | 263 |
| 888 | Drake Cutlass Red | Khaos | C | Quantum Drive | 4.6 | 0.022 | 209.1 | 251 |
| 889 | Drake Cutlass Red | Quest | D | Quantum Drive | 4.6 | 0.022 | 209.1 | 214 |
| 890 | Drake Cutlass Red | Odyssey | C | Quantum Drive | 4.6 | 0.022 | 209.1 | 238 |
| 891 | Esperia Stinger | Cascade | D | Quantum Drive | 4.6 | 0.022 | 209.1 | 237 |
| 892 | Esperia Stinger | SparkFire | C | Quantum Drive | 4.6 | 0.022 | 209.1 | 301 |
| 893 | Esperia Stinger | Flash | B | Quantum Drive | 4.6 | 0.022 | 209.1 | 290 |
| 894 | Esperia Stinger | Hemera | A | Quantum Drive | 4.6 | 0.022 | 209.1 | 326 |
| 895 | Esperia Stinger | Sojourn | B | Quantum Drive | 4.6 | 0.022 | 209.1 | 262 |
| 896 | Esperia Stinger | SunFire | B | Quantum Drive | 4.6 | 0.022 | 209.1 | 331 |
| 897 | Esperia Stinger | Aither | B | Quantum Drive | 4.6 | 0.022 | 209.1 | 276 |
| 898 | Esperia Stinger | Torrent | C | Quantum Drive | 4.6 | 0.022 | 209.1 | 263 |
| 899 | Esperia Stinger | Khaos | C | Quantum Drive | 4.6 | 0.022 | 209.1 | 251 |
| 900 | Esperia Stinger | Quest | D | Quantum Drive | 4.6 | 0.022 | 209.1 | 214 |
| 901 | Esperia Stinger | Odyssey | C | Quantum Drive | 4.6 | 0.022 | 209.1 | 238 |
| 902 | Mirai Guardian | Cascade | D | Quantum Drive | 4.6 | 0.022 | 209.1 | 237 |
| 903 | Mirai Guardian | SparkFire | C | Quantum Drive | 4.6 | 0.022 | 209.1 | 301 |
| 904 | Mirai Guardian | Flash | B | Quantum Drive | 4.6 | 0.022 | 209.1 | 290 |
| 905 | Mirai Guardian | Hemera | A | Quantum Drive | 4.6 | 0.022 | 209.1 | 326 |
| 906 | Mirai Guardian | Sojourn | B | Quantum Drive | 4.6 | 0.022 | 209.1 | 262 |
| 907 | Mirai Guardian | SunFire | B | Quantum Drive | 4.6 | 0.022 | 209.1 | 331 |
| 908 | Mirai Guardian | Aither | B | Quantum Drive | 4.6 | 0.022 | 209.1 | 276 |
| 909 | Mirai Guardian | Torrent | C | Quantum Drive | 4.6 | 0.022 | 209.1 | 263 |
| 910 | Mirai Guardian | Khaos | C | Quantum Drive | 4.6 | 0.022 | 209.1 | 251 |
| 911 | Mirai Guardian | Quest | D | Quantum Drive | 4.6 | 0.022 | 209.1 | 214 |
| 912 | Mirai Guardian | Odyssey | C | Quantum Drive | 4.6 | 0.022 | 209.1 | 238 |
| 913 | Mirai Guardian MX | Cascade | D | Quantum Drive | 4.6 | 0.022 | 209.1 | 237 |
| 914 | Mirai Guardian MX | SparkFire | C | Quantum Drive | 4.6 | 0.022 | 209.1 | 301 |
| 915 | Mirai Guardian MX | Flash | B | Quantum Drive | 4.6 | 0.022 | 209.1 | 290 |
| 916 | Mirai Guardian MX | Hemera | A | Quantum Drive | 4.6 | 0.022 | 209.1 | 326 |
| 917 | Mirai Guardian MX | Sojourn | B | Quantum Drive | 4.6 | 0.022 | 209.1 | 262 |
| 918 | Mirai Guardian MX | SunFire | B | Quantum Drive | 4.6 | 0.022 | 209.1 | 331 |
| 919 | Mirai Guardian MX | Aither | B | Quantum Drive | 4.6 | 0.022 | 209.1 | 276 |
| 920 | Mirai Guardian MX | Torrent | C | Quantum Drive | 4.6 | 0.022 | 209.1 | 263 |
| 921 | Mirai Guardian MX | Khaos | C | Quantum Drive | 4.6 | 0.022 | 209.1 | 251 |
| 922 | Mirai Guardian MX | Quest | D | Quantum Drive | 4.6 | 0.022 | 209.1 | 214 |
| 923 | Mirai Guardian MX | Odyssey | C | Quantum Drive | 4.6 | 0.022 | 209.1 | 238 |
| 924 | Grey's Shiv | Yaluk | D | Quantum Drive | 4.1 | 0.02 | 205.0 | 248 |
| 925 | Grey's Shiv | Bolon | C | Quantum Drive | 4.1 | 0.02 | 205.0 | 276 |
| 926 | Grey's Shiv | Huracan | B | Quantum Drive | 4.1 | 0.02 | 205.0 | 304 |
| 927 | Grey's Shiv | Crossfield | C | Quantum Drive | 4.1 | 0.021 | 195.2 | 203 |
| 928 | Grey's Shiv | XL-1 | A | Quantum Drive | 4.1 | 0.021 | 195.2 | 264 |
| 929 | Grey's Shiv | Yeager | B | Quantum Drive | 4.1 | 0.021 | 195.2 | 224 |
| 930 | Grey's Shiv | Cascade | D | Quantum Drive | 4.1 | 0.022 | 186.4 | 237 |
| 931 | Grey's Shiv | SparkFire | C | Quantum Drive | 4.1 | 0.022 | 186.4 | 301 |
| 932 | Grey's Shiv | Flash | B | Quantum Drive | 4.1 | 0.022 | 186.4 | 290 |
| 933 | Grey's Shiv | Hemera | A | Quantum Drive | 4.1 | 0.022 | 186.4 | 326 |
| 934 | Grey's Shiv | Sojourn | B | Quantum Drive | 4.1 | 0.022 | 186.4 | 262 |
| 935 | Grey's Shiv | SunFire | B | Quantum Drive | 4.1 | 0.022 | 186.4 | 331 |
| 936 | Grey's Shiv | Aither | B | Quantum Drive | 4.1 | 0.022 | 186.4 | 276 |
| 937 | Grey's Shiv | Torrent | C | Quantum Drive | 4.1 | 0.022 | 186.4 | 263 |
| 938 | Grey's Shiv | Khaos | C | Quantum Drive | 4.1 | 0.022 | 186.4 | 251 |
| 939 | Grey's Shiv | Quest | D | Quantum Drive | 4.1 | 0.022 | 186.4 | 214 |
| 940 | Grey's Shiv | Odyssey ★ | C | Quantum Drive | 4.1 | 0.022 | 186.4 | 238 |

## Quantum drive size 3 (10 ships, 150 combinations)

| # | Ship | Quantum drive | Grade | Class | Tank SCU | SCU/Gm | Range Gm | Speed Mm/s |
|--|--|--|--|--|--|--|--|--|
| 1 | Aegis Reclaimer | Agni | B | Quantum Drive | 21.8 | 0.036 | 605.6 | 586 |
| 2 | Aegis Reclaimer | Vesta | D | Quantum Drive | 21.8 | 0.036 | 605.6 | 479 |
| 3 | Aegis Reclaimer | Kama ★ | C | Quantum Drive | 21.8 | 0.036 | 605.6 | 532 |
| 4 | Anvil Carrack | Agni | B | Quantum Drive | 20.9 | 0.036 | 580.6 | 586 |
| 5 | Anvil Carrack | Vesta | D | Quantum Drive | 20.9 | 0.036 | 580.6 | 479 |
| 6 | Anvil Carrack | Kama ★ | C | Quantum Drive | 20.9 | 0.036 | 580.6 | 532 |
| 7 | Crusader A2 Hercules Starlifter | Agni | B | Quantum Drive | 20.9 | 0.036 | 580.6 | 586 |
| 8 | Crusader A2 Hercules Starlifter | Vesta | D | Quantum Drive | 20.9 | 0.036 | 580.6 | 479 |
| 9 | Crusader A2 Hercules Starlifter | Kama | C | Quantum Drive | 20.9 | 0.036 | 580.6 | 532 |
| 10 | Crusader C2 Hercules Starlifter | Agni | B | Quantum Drive | 20.9 | 0.036 | 580.6 | 586 |
| 11 | Crusader C2 Hercules Starlifter | Vesta | D | Quantum Drive | 20.9 | 0.036 | 580.6 | 479 |
| 12 | Crusader C2 Hercules Starlifter | Kama ★ | C | Quantum Drive | 20.9 | 0.036 | 580.6 | 532 |
| 13 | Crusader M2 Hercules Starlifter | Agni | B | Quantum Drive | 20.9 | 0.036 | 580.6 | 586 |
| 14 | Crusader M2 Hercules Starlifter | Vesta | D | Quantum Drive | 20.9 | 0.036 | 580.6 | 479 |
| 15 | Crusader M2 Hercules Starlifter | Kama | C | Quantum Drive | 20.9 | 0.036 | 580.6 | 532 |
| 16 | Aegis Reclaimer | Pontes | C | Quantum Drive | 21.8 | 0.038 | 573.7 | 392 |
| 17 | Aegis Reclaimer | TS-2 | A | Quantum Drive | 21.8 | 0.038 | 573.7 | 510 |
| 18 | Aegis Reclaimer | Balandin | B | Quantum Drive | 21.8 | 0.038 | 573.7 | 431 |
| 19 | Aegis Reclaimer | Ranger | B | Quantum Drive | 21.8 | 0.039 | 559.0 | 506 |
| 20 | Aegis Reclaimer | Drifter | D | Quantum Drive | 21.8 | 0.039 | 559.0 | 414 |
| 21 | Aegis Reclaimer | Metis | C | Quantum Drive | 21.8 | 0.039 | 559.0 | 484 |
| 22 | Aegis Reclaimer | Wanderer | C | Quantum Drive | 21.8 | 0.039 | 559.0 | 460 |
| 23 | Aegis Reclaimer | Erebos | A | Quantum Drive | 21.8 | 0.039 | 559.0 | 629 |
| 24 | Aegis Reclaimer | Echo | D | Quantum Drive | 21.8 | 0.039 | 559.0 | 457 |
| 25 | Aegis Reclaimer | Fissure | C | Quantum Drive | 21.8 | 0.039 | 559.0 | 508 |
| 26 | Aegis Reclaimer | Tyche | B | Quantum Drive | 21.8 | 0.039 | 559.0 | 532 |
| 27 | Aegis Reclaimer | Impulse | B | Quantum Drive | 21.8 | 0.039 | 559.0 | 559 |
| 28 | RSI Perseus | Agni | B | Quantum Drive | 19.8 | 0.036 | 550.0 | 586 |
| 29 | RSI Perseus | Vesta | D | Quantum Drive | 19.8 | 0.036 | 550.0 | 479 |
| 30 | RSI Perseus | Kama | C | Quantum Drive | 19.8 | 0.036 | 550.0 | 532 |
| 31 | Anvil Carrack | Pontes | C | Quantum Drive | 20.9 | 0.038 | 550.0 | 392 |
| 32 | Anvil Carrack | TS-2 | A | Quantum Drive | 20.9 | 0.038 | 550.0 | 510 |
| 33 | Anvil Carrack | Balandin | B | Quantum Drive | 20.9 | 0.038 | 550.0 | 431 |
| 34 | Crusader A2 Hercules Starlifter | Pontes ★ | C | Quantum Drive | 20.9 | 0.038 | 550.0 | 392 |
| 35 | Crusader A2 Hercules Starlifter | TS-2 | A | Quantum Drive | 20.9 | 0.038 | 550.0 | 510 |
| 36 | Crusader A2 Hercules Starlifter | Balandin | B | Quantum Drive | 20.9 | 0.038 | 550.0 | 431 |
| 37 | Crusader C2 Hercules Starlifter | Pontes | C | Quantum Drive | 20.9 | 0.038 | 550.0 | 392 |
| 38 | Crusader C2 Hercules Starlifter | TS-2 | A | Quantum Drive | 20.9 | 0.038 | 550.0 | 510 |
| 39 | Crusader C2 Hercules Starlifter | Balandin | B | Quantum Drive | 20.9 | 0.038 | 550.0 | 431 |
| 40 | Crusader M2 Hercules Starlifter | Pontes ★ | C | Quantum Drive | 20.9 | 0.038 | 550.0 | 392 |
| 41 | Crusader M2 Hercules Starlifter | TS-2 | A | Quantum Drive | 20.9 | 0.038 | 550.0 | 510 |
| 42 | Crusader M2 Hercules Starlifter | Balandin | B | Quantum Drive | 20.9 | 0.038 | 550.0 | 431 |
| 43 | Anvil Carrack | Ranger | B | Quantum Drive | 20.9 | 0.039 | 535.9 | 506 |
| 44 | Anvil Carrack | Drifter | D | Quantum Drive | 20.9 | 0.039 | 535.9 | 414 |
| 45 | Anvil Carrack | Metis | C | Quantum Drive | 20.9 | 0.039 | 535.9 | 484 |
| 46 | Anvil Carrack | Wanderer | C | Quantum Drive | 20.9 | 0.039 | 535.9 | 460 |
| 47 | Anvil Carrack | Erebos | A | Quantum Drive | 20.9 | 0.039 | 535.9 | 629 |
| 48 | Anvil Carrack | Echo | D | Quantum Drive | 20.9 | 0.039 | 535.9 | 457 |
| 49 | Anvil Carrack | Fissure | C | Quantum Drive | 20.9 | 0.039 | 535.9 | 508 |
| 50 | Anvil Carrack | Tyche | B | Quantum Drive | 20.9 | 0.039 | 535.9 | 532 |
| 51 | Anvil Carrack | Impulse | B | Quantum Drive | 20.9 | 0.039 | 535.9 | 559 |
| 52 | Crusader A2 Hercules Starlifter | Ranger | B | Quantum Drive | 20.9 | 0.039 | 535.9 | 506 |
| 53 | Crusader A2 Hercules Starlifter | Drifter | D | Quantum Drive | 20.9 | 0.039 | 535.9 | 414 |
| 54 | Crusader A2 Hercules Starlifter | Metis | C | Quantum Drive | 20.9 | 0.039 | 535.9 | 484 |
| 55 | Crusader A2 Hercules Starlifter | Wanderer | C | Quantum Drive | 20.9 | 0.039 | 535.9 | 460 |
| 56 | Crusader A2 Hercules Starlifter | Erebos | A | Quantum Drive | 20.9 | 0.039 | 535.9 | 629 |
| 57 | Crusader A2 Hercules Starlifter | Echo | D | Quantum Drive | 20.9 | 0.039 | 535.9 | 457 |
| 58 | Crusader A2 Hercules Starlifter | Fissure | C | Quantum Drive | 20.9 | 0.039 | 535.9 | 508 |
| 59 | Crusader A2 Hercules Starlifter | Tyche | B | Quantum Drive | 20.9 | 0.039 | 535.9 | 532 |
| 60 | Crusader A2 Hercules Starlifter | Impulse | B | Quantum Drive | 20.9 | 0.039 | 535.9 | 559 |
| 61 | Crusader C2 Hercules Starlifter | Ranger | B | Quantum Drive | 20.9 | 0.039 | 535.9 | 506 |
| 62 | Crusader C2 Hercules Starlifter | Drifter | D | Quantum Drive | 20.9 | 0.039 | 535.9 | 414 |
| 63 | Crusader C2 Hercules Starlifter | Metis | C | Quantum Drive | 20.9 | 0.039 | 535.9 | 484 |
| 64 | Crusader C2 Hercules Starlifter | Wanderer | C | Quantum Drive | 20.9 | 0.039 | 535.9 | 460 |
| 65 | Crusader C2 Hercules Starlifter | Erebos | A | Quantum Drive | 20.9 | 0.039 | 535.9 | 629 |
| 66 | Crusader C2 Hercules Starlifter | Echo | D | Quantum Drive | 20.9 | 0.039 | 535.9 | 457 |
| 67 | Crusader C2 Hercules Starlifter | Fissure | C | Quantum Drive | 20.9 | 0.039 | 535.9 | 508 |
| 68 | Crusader C2 Hercules Starlifter | Tyche | B | Quantum Drive | 20.9 | 0.039 | 535.9 | 532 |
| 69 | Crusader C2 Hercules Starlifter | Impulse | B | Quantum Drive | 20.9 | 0.039 | 535.9 | 559 |
| 70 | Crusader M2 Hercules Starlifter | Ranger | B | Quantum Drive | 20.9 | 0.039 | 535.9 | 506 |
| 71 | Crusader M2 Hercules Starlifter | Drifter | D | Quantum Drive | 20.9 | 0.039 | 535.9 | 414 |
| 72 | Crusader M2 Hercules Starlifter | Metis | C | Quantum Drive | 20.9 | 0.039 | 535.9 | 484 |
| 73 | Crusader M2 Hercules Starlifter | Wanderer | C | Quantum Drive | 20.9 | 0.039 | 535.9 | 460 |
| 74 | Crusader M2 Hercules Starlifter | Erebos | A | Quantum Drive | 20.9 | 0.039 | 535.9 | 629 |
| 75 | Crusader M2 Hercules Starlifter | Echo | D | Quantum Drive | 20.9 | 0.039 | 535.9 | 457 |
| 76 | Crusader M2 Hercules Starlifter | Fissure | C | Quantum Drive | 20.9 | 0.039 | 535.9 | 508 |
| 77 | Crusader M2 Hercules Starlifter | Tyche | B | Quantum Drive | 20.9 | 0.039 | 535.9 | 532 |
| 78 | Crusader M2 Hercules Starlifter | Impulse | B | Quantum Drive | 20.9 | 0.039 | 535.9 | 559 |
| 79 | Aegis Hammerhead | Agni | B | Quantum Drive | 19 | 0.036 | 527.8 | 586 |
| 80 | Aegis Hammerhead | Vesta | D | Quantum Drive | 19 | 0.036 | 527.8 | 479 |
| 81 | Aegis Hammerhead | Kama ★ | C | Quantum Drive | 19 | 0.036 | 527.8 | 532 |
| 82 | MISC Starfarer | Agni | B | Quantum Drive | 19 | 0.036 | 527.8 | 586 |
| 83 | MISC Starfarer | Vesta | D | Quantum Drive | 19 | 0.036 | 527.8 | 479 |
| 84 | MISC Starfarer | Kama ★ | C | Quantum Drive | 19 | 0.036 | 527.8 | 532 |
| 85 | MISC Starfarer Gemini | Agni | B | Quantum Drive | 19 | 0.036 | 527.8 | 586 |
| 86 | MISC Starfarer Gemini | Vesta | D | Quantum Drive | 19 | 0.036 | 527.8 | 479 |
| 87 | MISC Starfarer Gemini | Kama | C | Quantum Drive | 19 | 0.036 | 527.8 | 532 |
| 88 | Drake Caterpillar | Agni | B | Quantum Drive | 18.8 | 0.036 | 522.2 | 586 |
| 89 | Drake Caterpillar | Vesta | D | Quantum Drive | 18.8 | 0.036 | 522.2 | 479 |
| 90 | Drake Caterpillar | Kama | C | Quantum Drive | 18.8 | 0.036 | 522.2 | 532 |
| 91 | RSI Perseus | Pontes ★ | C | Quantum Drive | 19.8 | 0.038 | 521.1 | 392 |
| 92 | RSI Perseus | TS-2 | A | Quantum Drive | 19.8 | 0.038 | 521.1 | 510 |
| 93 | RSI Perseus | Balandin | B | Quantum Drive | 19.8 | 0.038 | 521.1 | 431 |
| 94 | RSI Perseus | Ranger | B | Quantum Drive | 19.8 | 0.039 | 507.7 | 506 |
| 95 | RSI Perseus | Drifter | D | Quantum Drive | 19.8 | 0.039 | 507.7 | 414 |
| 96 | RSI Perseus | Metis | C | Quantum Drive | 19.8 | 0.039 | 507.7 | 484 |
| 97 | RSI Perseus | Wanderer | C | Quantum Drive | 19.8 | 0.039 | 507.7 | 460 |
| 98 | RSI Perseus | Erebos | A | Quantum Drive | 19.8 | 0.039 | 507.7 | 629 |
| 99 | RSI Perseus | Echo | D | Quantum Drive | 19.8 | 0.039 | 507.7 | 457 |
| 100 | RSI Perseus | Fissure | C | Quantum Drive | 19.8 | 0.039 | 507.7 | 508 |
| 101 | RSI Perseus | Tyche | B | Quantum Drive | 19.8 | 0.039 | 507.7 | 532 |
| 102 | RSI Perseus | Impulse | B | Quantum Drive | 19.8 | 0.039 | 507.7 | 559 |
| 103 | Aegis Hammerhead | Pontes | C | Quantum Drive | 19 | 0.038 | 500.0 | 392 |
| 104 | Aegis Hammerhead | TS-2 | A | Quantum Drive | 19 | 0.038 | 500.0 | 510 |
| 105 | Aegis Hammerhead | Balandin | B | Quantum Drive | 19 | 0.038 | 500.0 | 431 |
| 106 | MISC Starfarer | Pontes | C | Quantum Drive | 19 | 0.038 | 500.0 | 392 |
| 107 | MISC Starfarer | TS-2 | A | Quantum Drive | 19 | 0.038 | 500.0 | 510 |
| 108 | MISC Starfarer | Balandin | B | Quantum Drive | 19 | 0.038 | 500.0 | 431 |
| 109 | MISC Starfarer Gemini | Pontes ★ | C | Quantum Drive | 19 | 0.038 | 500.0 | 392 |
| 110 | MISC Starfarer Gemini | TS-2 | A | Quantum Drive | 19 | 0.038 | 500.0 | 510 |
| 111 | MISC Starfarer Gemini | Balandin | B | Quantum Drive | 19 | 0.038 | 500.0 | 431 |
| 112 | Drake Caterpillar | Pontes ★ | C | Quantum Drive | 18.8 | 0.038 | 494.7 | 392 |
| 113 | Drake Caterpillar | TS-2 | A | Quantum Drive | 18.8 | 0.038 | 494.7 | 510 |
| 114 | Drake Caterpillar | Balandin | B | Quantum Drive | 18.8 | 0.038 | 494.7 | 431 |
| 115 | Aegis Hammerhead | Ranger | B | Quantum Drive | 19 | 0.039 | 487.2 | 506 |
| 116 | Aegis Hammerhead | Drifter | D | Quantum Drive | 19 | 0.039 | 487.2 | 414 |
| 117 | Aegis Hammerhead | Metis | C | Quantum Drive | 19 | 0.039 | 487.2 | 484 |
| 118 | Aegis Hammerhead | Wanderer | C | Quantum Drive | 19 | 0.039 | 487.2 | 460 |
| 119 | Aegis Hammerhead | Erebos | A | Quantum Drive | 19 | 0.039 | 487.2 | 629 |
| 120 | Aegis Hammerhead | Echo | D | Quantum Drive | 19 | 0.039 | 487.2 | 457 |
| 121 | Aegis Hammerhead | Fissure | C | Quantum Drive | 19 | 0.039 | 487.2 | 508 |
| 122 | Aegis Hammerhead | Tyche | B | Quantum Drive | 19 | 0.039 | 487.2 | 532 |
| 123 | Aegis Hammerhead | Impulse | B | Quantum Drive | 19 | 0.039 | 487.2 | 559 |
| 124 | MISC Starfarer | Ranger | B | Quantum Drive | 19 | 0.039 | 487.2 | 506 |
| 125 | MISC Starfarer | Drifter | D | Quantum Drive | 19 | 0.039 | 487.2 | 414 |
| 126 | MISC Starfarer | Metis | C | Quantum Drive | 19 | 0.039 | 487.2 | 484 |
| 127 | MISC Starfarer | Wanderer | C | Quantum Drive | 19 | 0.039 | 487.2 | 460 |
| 128 | MISC Starfarer | Erebos | A | Quantum Drive | 19 | 0.039 | 487.2 | 629 |
| 129 | MISC Starfarer | Echo | D | Quantum Drive | 19 | 0.039 | 487.2 | 457 |
| 130 | MISC Starfarer | Fissure | C | Quantum Drive | 19 | 0.039 | 487.2 | 508 |
| 131 | MISC Starfarer | Tyche | B | Quantum Drive | 19 | 0.039 | 487.2 | 532 |
| 132 | MISC Starfarer | Impulse | B | Quantum Drive | 19 | 0.039 | 487.2 | 559 |
| 133 | MISC Starfarer Gemini | Ranger | B | Quantum Drive | 19 | 0.039 | 487.2 | 506 |
| 134 | MISC Starfarer Gemini | Drifter | D | Quantum Drive | 19 | 0.039 | 487.2 | 414 |
| 135 | MISC Starfarer Gemini | Metis | C | Quantum Drive | 19 | 0.039 | 487.2 | 484 |
| 136 | MISC Starfarer Gemini | Wanderer | C | Quantum Drive | 19 | 0.039 | 487.2 | 460 |
| 137 | MISC Starfarer Gemini | Erebos | A | Quantum Drive | 19 | 0.039 | 487.2 | 629 |
| 138 | MISC Starfarer Gemini | Echo | D | Quantum Drive | 19 | 0.039 | 487.2 | 457 |
| 139 | MISC Starfarer Gemini | Fissure | C | Quantum Drive | 19 | 0.039 | 487.2 | 508 |
| 140 | MISC Starfarer Gemini | Tyche | B | Quantum Drive | 19 | 0.039 | 487.2 | 532 |
| 141 | MISC Starfarer Gemini | Impulse | B | Quantum Drive | 19 | 0.039 | 487.2 | 559 |
| 142 | Drake Caterpillar | Ranger | B | Quantum Drive | 18.8 | 0.039 | 482.1 | 506 |
| 143 | Drake Caterpillar | Drifter | D | Quantum Drive | 18.8 | 0.039 | 482.1 | 414 |
| 144 | Drake Caterpillar | Metis | C | Quantum Drive | 18.8 | 0.039 | 482.1 | 484 |
| 145 | Drake Caterpillar | Wanderer | C | Quantum Drive | 18.8 | 0.039 | 482.1 | 460 |
| 146 | Drake Caterpillar | Erebos | A | Quantum Drive | 18.8 | 0.039 | 482.1 | 629 |
| 147 | Drake Caterpillar | Echo | D | Quantum Drive | 18.8 | 0.039 | 482.1 | 457 |
| 148 | Drake Caterpillar | Fissure | C | Quantum Drive | 18.8 | 0.039 | 482.1 | 508 |
| 149 | Drake Caterpillar | Tyche | B | Quantum Drive | 18.8 | 0.039 | 482.1 | 532 |
| 150 | Drake Caterpillar | Impulse | B | Quantum Drive | 18.8 | 0.039 | 482.1 | 559 |

## Quantum drive size 4 (1 ships, 2 combinations)

| # | Ship | Quantum drive | Grade | Class | Tank SCU | SCU/Gm | Range Gm | Speed Mm/s |
|--|--|--|--|--|--|--|--|--|
| 1 | Origin 890 Jump | Frontline | A | Quantum Drive | 33.1 | 0.053 | 624.5 | 974 |
| 2 | Origin 890 Jump | Allegro ★ | A | Quantum Drive | 33.1 | 0.055 | 601.8 | 1263 |
