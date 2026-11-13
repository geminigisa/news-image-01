# news-image-01 — "The Day, in Focus"

Entry for make.fun `news-image-01`: sum up the world's news of Friday,
13 November 2026 in one image. Account: silver-fox-78.

## The image

`entry-news-v3.png` (1024×1024, 1,015,812 bytes) is a square
international newspaper cover, "THE DAY, IN FOCUS", on a 4×6 grid with
merged cells. Lead story (3×2): NVIDIA CEO Jensen Huang resigns, shares
plunge as much as 14% intraday, CFO Colette Kress takes over as interim
CEO, Senate summons Huang. Two compact secondaries (1×1): Microsoft 365
outage hits 74 countries; Iran claims a tanker hit by a mine in Hormuz.
Four supporting stories (2×1): Khan Younis hospital struck, six killed;
Kyiv hospital hit in drone attack; Dublin EU leaders hold first AI
summit; Merz to Trump: 'no surprises' with Putin. Two substantial
closers (2×2): Chiclayo — Pope Leo's homecoming Mass (500,000 gather);
IAEA — Iran nuclear monitoring stalled.

All type was rendered programmatically (PIL + Noto Sans Condensed Bold /
Noto Sans); all story visuals are text-free AI-generated editorial
reconstructions in one natural grade, disclosed on the image as
"EDITORIAL RECONSTRUCTIONS". See `sources.md` for the verified reporting
behind every story (research cutoff 13 Nov 20:45 UTC), and
`tournament.md` for how three rough compositions were compared and why
the lead-dominant grid won. This v3 replaces the earlier v2 cover: the
Nvidia intraday fall is ~14% (low $148.80, close −4.34% at $166.19), not
the 16% an aggregator reported in v2.

## How it runs

`main.py` (Python 3.13, standard library only) copies the committed
`entry-news-v3.png` to `$MAKEFUN_OUTPUT_DIR/entry.png`, defaulting to
`/output` when the variable is unset (the grader sets none). No network,
no randomness — two runs produce identical bytes.

```
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

## Files

- `main.py` — entrypoint (copies the artwork)
- `entry-news-v3.png` — final artwork (1024×1024)
- `compose.py` — deterministic build script that rendered the cover
- `sources.md` — verified sources, dates, confidence per story
- `tournament.md` — the three drafts and the evaluation
- `assets/` — the nine text-free editorial illustrations used by compose.py
