# sc-quantum – Quantum-Range- und Flugzeit-Auswertung (Star Citizen 4.10.2-LIVE)

Arbeitsverzeichnis für ein Ranking der Schiffe nach Quantum Range, gruppiert nach Quantum-Drive-Size,
und für eine Flugzeit-Simulation. Alle Daten stammen aus der Star Citizen Wiki API und liegen lokal,
damit die API nicht erneut abgefragt werden muss.

## Inhalt

| Pfad | Beschreibung |
|---|---|
| `ships/p1..p12.json` | Schiffsdatensätze der API (310 Einträge, Version 4.10.2-LIVE.12881860), seitenweise gespeichert |
| `drives/<uuid>.json` | 59 Quantum-Drive-Module (alle `QuantumDrive`-Items der API) |
| `combos.json` | Alle Kombinationen Schiff × Drive passender Size (2532) mit Range und Speed |
| `ranking.md` | Ranking als Markdown, je Size sortiert nach Range |
| `flighttime.py` | Flugzeit-Simulation (Modul und Kommandozeile) |
| `flighttime.json` | Ergebnis der Simulation für die vorgegebenen Vergleichskombinationen, inkl. Einzelphasen |
| `build_web.py` | Erzeugt `web/data.js` aus den lokalen Daten |
| `web/index.html` | Sortierbare Tabelle, lokal per Doppelklick im Browser öffnen (offline, ohne Abhängigkeiten) |
| `web/data.js` | Daten für die Tabelle (wird von `build_web.py` erzeugt, nicht von Hand ändern) |

## Datenquellen

- Schiffe: <https://api.star-citizen.wiki/api/v2/vehicles> (30 pro Seite, Parameter `page[number]`)
- Quantum Drives: <https://api.star-citizen.wiki/api/v2/items?filter[type]=QuantumDrive&page[size]=100>
  (Detailseite je Item über das Feld `link`)
- Version: <https://api.star-citizen.wiki/api/v2/game-versions> (aktuell 4.10.2-LIVE.12881860, 09.10.2026)
- Preise: Feld `uex_prices.purchase` der API (Daten von UEX, <https://uexcorp.space>), Community-Daten.

Die API verlangt einen Browser-User-Agent (sonst HTTP 403 bei `/api/items/...`).
Die Daten werden nicht automatisch aktualisiert. Für neue Patches `ships/` und `drives/` neu laden.

## Berechnungen

### Quantum Range

```
Range (Gm) = Tank (SCU) / fuel_consumption_scu_per_gm
```

- Tank: `quantum.quantum_fuel_capacity` des Schiffs (Stock-Loadout).
- `fuel_consumption_scu_per_gm`: Feld des Drives (`quantum_drive.fuel_consumption_scu_per_gm`).
- Die Formel reproduziert das Minimum der SPViewer-Spanne (geprüft an Cutlass Black, Cutter Rambler, Starlancer MAX).
  Das SPViewer-Maximum (ca. 20–25 % höher) ist ungeklärt und wird nicht verwendet.
- Das Feld ist in der API auf 3 Nachkommastellen gerundet. Bei Size 1 (0,004/0,005) ist der Fehler groß.
  Beim Taurus weicht der Wert deshalb von SPViewer ab (385 statt 350 Gm).
- Das früher verwendete Feld `quantum.quantum_range` des Schiffs (basiert auf `quantum_fuel_requirement`) passt nicht zu SPViewer und wird nicht genutzt.

### Kombinationen

- Nur Schiffe mit Stock-Quantum-Drive, Tankgröße und mindestens einem aUEC-Kaufpreis (130 Schiffe).
  Nicht kaufbare Schiffe (z. B. Wikelo-Specials, Idris, Javelin) sind ausgeschlossen.
- Die Size des Drives wird vom Stock-Loadout übernommen. Es werden nur Drives dieser Size kombiniert.
- Ausgeschlossen: Platzhalter-Drive und Mauler-Drive.
- Bei mehreren Datensätzen gleichen Namens wird der niedrigste Kaufpreis über alle Datensätze genommen.

### Flugzeit-Simulation (`flighttime.py`)

Strecke:

1. Abdocken, 5 km im SCM (aus dem Stand, ohne Bremsen)
2. 10 km im NAV bis zum Quantum-Punkt (von SCM-Speed auf Max, ohne Bremsen)
3. Quantum-Sprung 60 Gm, Ziel in 30 km
4. Abstand gewinnen (10 km NAV aus dem Stand), Quantum-Sprung 3 Gm, Ziel in 30 km
5. Abstand gewinnen (10 km NAV aus dem Stand), Quantum-Sprung 30 Gm, Ziel in 30 km

Annahmen:

- Beschleunigung SCM = `scm / zero_to_scm`, NAV = `max / zero_to_max`, Bremsen = `max / max_to_zero`.
  Das sind die API-Felder `speed.*`. Konstante Beschleunigung.
- Der NAV-Modus wird mit `speed.max` angenommen.
- QT: Stufe 1 bis `engage_speed` mit `stage_one_accel_rate`, Stufe 2 bis `drive_speed` mit `stage_two_accel_rate`.
  Das Abbremsen wird symmetrisch zum Beschleunigen angesetzt (die API nennt keine Werte).
  Reicht die Strecke nicht für die Höchstgeschwindigkeit, wird die Spitzengeschwindigkeit berechnet.
- Die Spool-Zeit des Drives (`spool_up_time`) zählt vor jedem Sprung vollständig.
  Parallel zum Anflug wäre sie im Spiel teils überlappend, das Ergebnis ist also eher konservativ.
- Cooldown des Drives: Es wird nur die Wartezeit gezählt, die nach Anflug und Abstand gewinnen noch übrig bleibt.
- Die 10 km für "Abstand gewinnen" sind eine Annahme, du hast keinen Wert vorgegeben (`GAIN_M`).
- Nicht berücksichtigt: Ausrichtung, Kalibrierung, Boost, Masse- und Lasteffekte, Kollisionen, Wartezeiten im Spiel.
- Die Gesamtzeit ist eine Modellrechnung, keine im Spiel gemessene Zeit.

Konstanten (`UNDOCK_SCM_M`, `NAV_TO_QT_M`, `QT1_M`, `QT_SHORT_M`, `QT2_M`, `ARRIVAL_M`, `GAIN_M`) stehen am Anfang von `flighttime.py`.

Aufruf:

```
cd sc-quantum
python3 flighttime.py        # Vergleichsliste, sortiert nach Gesamtzeit, schreibt flighttime.json
```

Vergleichskombinationen stehen in `COMBOS` (Corsair, C2, 315p, Cutlass Black, C1 Spirit, Constellation-Varianten).

#### Ergebnis (Sekunden, Stand 4.10.2)

| # | Schiff + Drive | Gesamt |
|---|---|---|
| 1 | Origin 315p + FoxFire | 572,7 |
| 2 | Crusader C1 Spirit + SunFire | 608,6 |
| 3 | Constellation Mk IV Andromeda + SunFire | 648,9 |
| 4 | Constellation Mk IV Phoenix + SunFire | 649,3 |
| 5 | Constellation Mk IV Phoenix Emerald + SunFire | 650,9 |
| 6 | Constellation Mk V Centaurus + SunFire | 655,3 |
| 7 | Constellation Mk IV Taurus + SunFire | 657,3 |
| 8 | Constellation Mk IV Aquila + SunFire | 657,3 |
| 9 | Drake Corsair + SunFire | 657,5 |
| 10 | Drake Cutlass Black + SunFire | 699,4 |
| 11 | Crusader C2 Hercules Starlifter + Erebos | 867,4 |

Details je Phase (SCM, NAV, Spool, QT, Anflug, Abstand, Cooldown-Wartezeit) stehen in `flighttime.json`.

## Browser-Tabelle (`web/index.html`)

Neu erzeugen nach Datenänderungen:

```
cd sc-quantum
python3 build_web.py
```

Danach `web/index.html` im Browser öffnen (Reload genügt).

Funktionen:

- Sticky Header.
- Sortieren per Klick auf die Spaltenköpfe, erneuter Klick wechselt die Richtung.
  Mit **Shift+Klick** weitere Spalten als nächste Sortierkriterien hinzufügen. Die Zahl am Kopf zeigt die Reihenfolge.
- Filter: Suche (Schiff/Drive), QD-Size, minimaler Cargo, nur Stock-Drive, nur mit Preis.
- Leere Werte stehen beim Sortieren immer am Ende.

Spalten (in dieser Reihenfolge):

| Spalten | Inhalt |
|---|---|
| Schiff, QD-Size, Quantum Drive, Grade, Stock | Kombination, Stock = Drive ist der Stock-Drive des Schiffs |
| Tank SCU, SCU/Gm, Range Gm | Range-Berechnung |
| Speed Mm/s, Cooldown s, Spool s | Drive-Werte |
| Cargo SCU, Masse t, SCM m/s | Schiffswerte (Masse mit Loadout) |
| Schiff aUEC, Drive aUEC, Summe aUEC | niedrigste UEX-Kaufpreise |
| **Flug gesamt s** | Gesamtzeit der Strecke oben |
| **QT 60 Gm s**, **QT 3 Gm s**, **QT 30 Gm s** | reine Quantum-Flugzeit je Sprung |
| **Spool+Wartezeit s** | 3 × Spool plus Cooldown-Wartezeit |
| **Nahflug s** | SCM, NAV, 3 × Anflug und 2 × Abstand gewinnen |

Die Flugzeit-Spalten sind für alle Kombinationen berechnet. Bei Schiffen ohne vollständige Flugdaten in der API
(Aopoa Khartu-al, Aopoa San'tok.yāi, Drake Herald, Esperia Prowler Utility) sind sie leer.

## Bekannte Einschränkungen

- Community-Daten (Wiki-API, UEX), nicht offiziell. Preise und Werte ändern sich mit Patches.
- Kein Abgleich mit Erkul oder SPViewer außer den vier Referenzschiffen. Das SPViewer-Maximum der Range ist nicht erklärt.
  SPViewer-API (`data.spviewer.eu/spvapi`) verlangt ein Token und wird nicht genutzt.
- Avenger Stalker hat laut API 0 SCU Cargo (nur 0,71 SCU Fahrzeuginventar), nicht geprüft.
- Schiffsgröße (QD-Size) kommt aus dem Stock-Loadout. Ob ein Schiff andere Sizes aufnehmen kann, wird nicht geprüft.
