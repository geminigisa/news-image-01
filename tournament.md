# tournament.md — news-image-01 v3 "THE DAY, IN FOCUS"

## The three rough compositions

All three share: 1024×1024, black header bar ("FRIDAY 13 NOVEMBER 2026" /
"THE DAY'S WORLD NEWS", Noto Sans Bold, 3 px vermilion rule), black footer
disclosure ("EDITORIAL RECONSTRUCTIONS — IMAGES ARE AI-GENERATED
ILLUSTRATIONS OF REPORTED EVENTS"), warm-white headline banners, bold
condensed uppercase headlines (Noto Sans Condensed Bold, auto-fit),
4 px dark gutters, all text typeset programmatically with PIL (no
image-generated text). All 9 photos viewed individually before composing.

### Draft A — lead-dominant grid (the brief's suggested layout)
- Lead 3×2 top-left (Nvidia, image 767×205 + banner 103, headline 44 px,
  subline 1 line). Upper-right: Microsoft 1×1 + Hormuz 1×1 (image 92 px +
  banner 60, headline ≤20 px, 2 lines). Middle: 4× 2×1 side panels
  (Gaza, Kyiv, EU-AI, Merz — image 200 px left, banner 310 px right,
  headline ≤24 px, 3 lines, 3 px vermilion edge). Bottom: 2× 2×2
  (Pope, IAEA — image 205 px + banner 103, headline ≤34 px + subline).
- 9 stories. File: drafts/draft-a.png (sha256 329c947d…).

### Draft B — balanced mosaic
- Lead 2×2 top-left (Nvidia, headline 40 px). Top-right: Microsoft 1×1 +
  Hormuz 1×1, Gaza 2×1 side below them. Middle: 5× 2×1 side panels
  (Kyiv, EU-AI, Merz, IAEA + Gaza). Bottom: Pope as a full-width 1024×308
  band (image 640 px left, banner 384 px right, headline 40 px + subline).
- 9 stories. File: drafts/draft-b.png (sha256 8228e09b…).

### Draft C — reduced story, larger text
- Lead 3×2 + Microsoft 1×1 + Hormuz 1×1 (same top as A). Middle: Gaza 2×2
  + Kyiv 2×2 as large top-image panels (headline 36 px). Bottom: Pope 2×2
  + IAEA 2×2.
- 7 stories — EU-AI summit and Merz quote dropped. File:
  drafts/draft-c.png (sha256 0931c5c9…).

## Evaluation (viewed directly, full size + 512 px preview for A)

| Criterion | A | B | C |
|---|---|---|---|
| Accuracy (headlines vs ledger) | all 9 exact | all 9 exact | 7 exact, 2 cut |
| Same-day relevance | 9 verified 13 Nov stories | 9 verified | 7 verified |
| Coverage | full (markets, tech, 2 wars, diplomacy, faith, nuclear) | full | thin — loses the Dublin diplomacy thread entirely |
| Comprehension | clear top→bottom read; uniform middle rows scan fast | good, but lead less dominant; 5 side panels in a row get monotonous | clear, but the two big hospital panels dominate the middle and the day feels narrower |
| Headline readability | all fit; lead subline on ONE line | lead subline wraps to 2 lines, banner has dead space below | largest text; but Gaza/Kyiv banners have ~30 px empty space (no subline) |
| Hierarchy | strongest: 3×2 lead, compact secondaries, 2×2 closers | flatter lead; the bottom band is the single most striking element | strong, but hierarchy serves 7 stories, not the day |
| Originality | faithful to brief; red edge on side panels + red rule | the full-width Pope band is the most distinctive single move | the paired big hospital panels are powerful |

## Weaknesses found while viewing (all drafts)
- EU-AI side image is flag-heavy at 200 px (the summit hall's EU-flag row
  reads as a blue band). Acceptable: the flags are the real setting, not a
  decorative cliché, and delegates are visible from behind. Left as is —
  shifting the crop focus risks a worse frame.
- Gaza side image crops the two rescue workers at the waist — normal
  photojournalistic foreground cropping, kept.
- Nvidia lead image: the red falling-arrow chart is a symbolic drawn arrow,
  not a data chart with numbers — it is not presented as sourced market
  data; the 14% figure lives only in the typeset subline. Kept.
- B's lead subline wrapping ("…Senate summons / Huang") and C's empty
  banner space are real readability costs of those layouts.

## Choice: Draft A

A is the strongest communicator, not the busiest: it carries all 9 verified
stories, the clearest hierarchy (3×2 lead → compact secondaries → 2×1
middle → 2×2 closers), single-line sublines, and the cleanest overall read
at both 1024 px and 512 px. B's band is beautiful but its lead is weaker
and its subline wraps; C buys larger text by dropping two verified,
distinctive stories (first-ever EU AI summit + the day's best diplomacy
quote), which costs more coverage than it gains in readability.

## Final asset
- entry-news-v3.png — Draft A, 1024×1024 PNG, 1,015,812 bytes (0.969 MiB),
  sha256 329c947d63b6293fb9ce5d842e5d29ae35d571bc102a0a1d3429774b14901b4f.
- entry-news-v3-512.png — 512×512 preview, viewed, hierarchy holds.
- compose.py — deterministic builder (PIL only, no network); re-run
  reproduces all three drafts byte-identically (verified: two runs,
  identical sha256 for a/b/c).
- sources.md — research ledger, cutoff 2026-11-13 20:45 UTC.

## Selected stories (9) / discarded
Selected: 1 Nvidia CEO resigns (+ Senate summons subline) · 2 Microsoft
outage 74 countries · 3 Iran claims tanker hit by mine · 4 Khan Younis
hospital struck, six killed · 5 Kyiv hospital hit in drone attack ·
6 Dublin EU first AI summit · 7 Merz to Trump "no surprises" ·
8 IAEA Iran monitoring stalled · 9 Pope Leo homecoming Mass, Chiclayo.
Verified but cut (space/overlap): Europe joins Ukraine talks + prisoner
swap (folded into Dublin thread) · DOJ/Binance $1.2B seizure (12 Nov
follow-up) · COP31 talks continue (no discrete 13 Nov event) · Gaza
winter-storm tent deaths (same location/day as hospital strike).
Not verified, not used (from the grid reference): Taiwan 100+ ships ·
Pakistan 74 militants · Kenya building collapse · US PPI +6.5% ·
Salvadoran robots · MSF Ebola funds · Moscow car bomb · Mossad chief in
Washington · Japan beats Korea 9-5 · Iran downed US drone · Shuttle
Endeavour · Mexico Buen Fin · "1,200 drones" (Russian claim is 1,198).
Correction vs v2 ledger: Nvidia intraday fall is ~14% (low $148.80,
close −4.34% at $166.19), NOT 16% — v3 uses 14%.
