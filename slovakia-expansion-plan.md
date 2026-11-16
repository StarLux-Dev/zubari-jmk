# Dentalmap — rozšírenie na Slovensko (plán a stav)

Postup: skill **dental-coverage-map** + recept `claude/sk-kraj-recipe.md` + skripty `claude/scripts/`. Hotové 4 z 8 SK krajov + **spojená mapa ČR+SR**.

## Spojená mapa ČR + SR (16. 11. 2026) — `zubari-cesko-slovensko.html` → GitHub `index.html`
- Prepínač vlajok 🇨🇿/🇸🇰; každá krajina **vlastný overený renderer** (Praha 22 obvodov + Brno 29 MČ zachované; neaktívna krajina šedý obrys).
- **Opravený bug** pôvodnej českej mapy: pražské obvody zdieľajú kód obce → popup každého obvodu vypisoval všetkých 1 200 zubárov. Teraz párovanie podľa mestskej časti (Praha 1 = 106 ✓).
- Filtre: kraj, špecializácia (plní sa z dát), poisťovňa (len SK), pokrytie obce, **ekonomika okresu**. Prefarbujú mapu aj bočný panel.
- **Ekonomika okresov SK (oficiálne):** ÚPSVR mesačná štatistika, Tab. 2 „Poradie území podľa PDU“ — podiel disponibilných uchádzačov o zamestnanie, 09/2026, všetkých 79 okresov, priemer SR 4,02 %. Úrovne: vysoká ≤2,7 · nadpriemerná ≤3,3 · priemerná ≤4,4 · mierne podpriemerná ≤5,6 · podpriemerná >5,6. ČR: pôvodná kúpna sila/ceny bytov per okres. (Získané cez prehliadač: XLSX rozparsované SheetJS priamo v stránke ÚPSVR.)
- **Príležitosti na založenie ambulancie:** skóre = obyvatelia × váha ekonomiky okresu × miera nedostatku (0 ordinácií = 1; inak (4−per10k)/4), obce ≥1 500 (ČR) / ≥1 000 (SR) ob. Top 15 v paneli, klik = zoom.
- **Excel export** (SheetJS): „filter“ = aktuálne prefiltrované, „všetko“ = celá krajina; 2 hárky: Zubári (názov, adresa, odbor, telefón, email/web ČR, poisťovne SR, GPS, odkazy) + Obce-pokrytie (obyv., počet, /10 tis., ekonomika, PDU).
- Leaflet/MarkerCluster CSS vložené do súboru (artefaktový viewer blokuje externé CSS). JS z cdnjs. Esri podklad bez kľúča.
- Overené: node --check, smoke test (obe krajiny, všetky filtre, export: SK 1 499 / CZ 6 065 ordinácií; obce „všetko“ SK 1 358 / CZ 6 307).
- **GitHub:** commit `f822608` pripravený v klone `StarLux-Dev/zubari-jmk` (index.html = spojená mapa, + zubari-cesko-kompletni.html, 4 SK kraje, README). **Push čaká na prepojenie GitHub účtu** (claude.ai → Settings → Connectors).

## Zdroj zubárov SK = e-VÚC + obohatenie detailov
Zoznam cez `fetch` + stránkovanie (**safe crawler**: overenie každej strany + pauzy + jeden okres/volanie — inak throtlovanie ticho podpočíta); detaily → GPS, telefón, poisťovne. Populácia SODB 2021 (mertel), hranice drakh.

## Hotové SK kraje (správne)
| Kraj | Obce/okr | Obyv. | Amb. | /10 tis. |
|---|---|---|---|---|
| Žilinský | 315/11 | 691 509 | 487 | 7,04 |
| Trenčiansky | 276/9 | 583 946 | 359 | 6,15 |
| Trnavský | 251/7 | 565 604 | 317 | 5,60 |
| Banskobystrický | 516/13 | 645 276 | 336 | 5,21 |
Spolu 1 499 ordinácií, 2 486 335 obyv., 100 % GPS.

## Roadmapa
Prešovský (psk) → Košický (ksk, MČ) → Nitriansky (nsk) → Bratislavský (bsk, MČ); po každom kraji znovu postaviť spojenú mapu (`build_combined.py` v scratchpade — pri novej relácii obnoviť z tohto popisu). Fáza 2: izochróny, „zubár pri mne“.
