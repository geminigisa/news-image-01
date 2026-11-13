# news-image-01 v2 — Tournament notes (FASE 2–5)

Final asset: `entry-news-v2.png` (winner: Draft A, after one fix).
All type rendered programmatically with PIL + DejaVu (Serif Bold headlines,
Sans sublines). All story visuals are text-free editorial illustrations
generated in a single coherent language (ink navy / warm ivory / vermilion).
Date "13 NOV 2026" visible on every draft. No fake logos, no vague labels,
no "pick me" text, no gore.

## FASE 2 — Three concepts (all 1024×1024, 5 stories)

| | A — "THE WORLD, IN ONE FRAME" | B — "THE DAY IN FIVE FRAMES" | C — "WHERE IT HAPPENED" |
|---|---|---|---|
| Layout | Newspaper cover: masthead, giant lead headline + wide lead image, 4 secondary panels in a row | Banded digest: lead band (text left, image right, double height) + 4 numbered horizontal bands | World map hero with 4 numbered pins + 5 callout rows |
| Lead | NVIDIA photo-illustration, full width | NVIDIA, half width | Map (no photo) |
| File | drafts/draft-a-cover.png | drafts/draft-b-bands.png | drafts/draft-c-map.png |

6-criteria comparison (1 = best):
- **Accuracy / specificity:** A 1, B 1, C 2 — A/B attach exact headlines to matching
  visuals; C's map pins were misplaced (see below).
- **Breadth (5 stories):** all equal (same 5 stories).
- **Immediate comprehension:** A 1 (cover reading path is instant), B 2 (bands read
  top-down), C 3 (map must be decoded, then list read).
- **Legibility:** B 1 (single-line 26 px headlines), A 2 (2-line 17–20 px in 226 px
  panels), C 2 (24 px list headlines).
- **Hierarchy / coherence:** A 1 (classic cover hierarchy), B 2, C 3 (400 px map
  + dead space at bottom).
- **Originality / restraint:** C 1 (most original), B 2, A 3 — but C's originality
  costs accuracy and comprehension.

**Choice: Draft A.** Highest comprehension + hierarchy, the two things a
pairwise vision judge rewards fastest; zero factual errors.

## FASE 5 — Pairwise tournament (A/B and B/A)

- **A vs B:** A wins. Full-width lead image (chip + falling arrow) reads in one
  glance; B's lead band has two dangling widow words ("…Kress takes / over",
  "…successor search / begins") and its lead image wastes ~25% on a dark desk
  band. B's single-line secondary headlines are more legible, but that does not
  outweigh A's lead strength.
- **A vs C:** A wins clearly. Photos beat a map for emotional immediacy; C's
  markers 1 and 4 are geographically WRONG (see critique); C leaves ~100 px
  dead ivory at the bottom.
- **B vs C:** B wins. Clean numbered list, no geographic errors, all headlines
  legible.

## 8-question picture-editor critique

### Draft A (winner)
1. Lead identifiable in 3 s? YES — "NVIDIA CEO RESIGNS" at 64 px + chip/arrow.
2. Each secondary explainable from image alone? YES — hospital+ambulances,
   dark office+blue screens, tanker+smoke, handshake+documents; headlines
   confirm each.
3. Specific to 13 Nov 2026? YES — date top-right + "FRIDAY • WORLD NEWS";
   all five stories are dated 12–13 Nov in the ledger.
4. Visual + headline match sources? YES — chip+fall = NVDA plunge (intraday
   −16%); hospital = Nasser strike; office = Microsoft 365 outage; tanker+smoke
   = Hormuz mine claim (headline says CLAIMS); handshake = talks.
5. World news, not one country? YES — US, Gaza, global (Microsoft), Hormuz,
   Europe/Ukraine.
6. Anything attractive but uninformative? NO — every element carries a story.
7. Any text too small? Secondary sublines (14 px) are small but readable at
   1024; headlines carry the meaning. Footer credit (13 px) is a credit only.
8. One coherent image? YES — single palette, single illustration language,
   one grid.

### Draft B
1–6: same as A (pass). 7: lead sublines have widow words ("over", "begins")
— typographic flaw. 8: reads slightly like a list/slide deck, less "one
designed image". Verdict: strong second, not revised (only the winner is).

### Draft C
1. Lead? The MAP is the lead — no story lead; weaker.
2. Secondaries explainable? Only via the list; the map alone explains nothing.
3. Specific to 13 Nov? YES (date + list).
4. Visual+headline match? PARTIAL — **marker 1 (Santa Clara/Nvidia) lands in
   the central USA, not California; marker 4 (Dublin) lands over the North
   Sea/Scandinavia, not Ireland.** My linear lat/lon→pixel mapping was off for
   this stylized projection. Markers 2 (Gaza) and 3 (Hormuz) are approximately
   right. This is a factual/geographic error and the main reason C lost.
5. World news? YES. 6. Map is attractive but carries little story information.
7. List text fine. 8. Bottom ~100 px dead ivory — loose.
Verdict: weakest; would need marker re-calibration by eye + tighter layout
to compete. Not pursued — A already wins.

## Fix applied to the winner (Draft A)
Weakest substantive issue found: the Hormuz headline wrapped to **3 lines**
("IRAN CLAIMS / TANKER HIT BY / MINE"), pushing its subline below the other
panels' baselines. Fix: auto-fit one headline size (tried 20→19→18→17 px)
so every secondary headline wraps to at most 2 lines; all four now use the
same size and all sublines share a baseline. Re-rendered and re-viewed —
fixed. No other change.

## 512 px preview (Draft A)
`drafts/draft-a-cover-512.png` viewed: hierarchy holds — masthead, date,
lead headline, subline, lead image and all four secondary headlines remain
readable at 512 px. Secondary sublines get small (expected); headlines carry
the stories. Footer credit is tiny at 512 (credit only, fine).

## Validation — final asset
- File: `v2-work/entry-news-v2.png`
- Decode: OK (PIL open + verify)
- Dimensions: 1024 × 1024 px
- Size: 688,076 bytes (≤ 1 MiB ✓)
- SHA-256: 7e34cf92f396146dd82bd6a7ad60c1787a9a29e6dea66f50213486ce2aa11569
- Text: all exact, none clipped (verified by direct viewing of the render)
- Determinism: re-running compose.py produces a byte-identical draft A
- 512 px preview: viewed, hierarchy holds

## Notes for PHASE 6 (parent)
- Final asset is a committed PNG in v2-work; the entrypoint (parent) only
  needs to copy it to /output/entry.png (no network, no fonts needed at
  runtime — the asset is pre-rendered).
- v1 asset (`../entry-news.jpg`) was NOT overwritten; it remains the fallback
  candidate. The v1 prep cron (03:05 WIB) is independent of this v2 work.
- The user said at 03:02 WIB they are preparing their own prompt — if it
  arrives before submit, the image can be swapped; this v2 asset is the
  current best candidate.
