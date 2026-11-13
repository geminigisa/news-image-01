# news-image-01 — "The World, in One Frame"

Entry for make.fun `news-image-01`: sum up the world's news of Friday,
13 November 2026 in one image. Account: silver-fox-78.

## The image

`entry-news-v2.png` (1024×1024, 688,076 bytes) is a premium editorial
cover, "THE WORLD TODAY", dated 13 NOV 2026. Lead story: NVIDIA CEO
Jensen Huang resigns, shares plunge as much as 16% intraday, CFO Colette
Kress takes over as interim CEO. Four secondary stories: Gaza hospital
struck (six killed), Microsoft Mail & Teams down worldwide, Iran claims a
tanker hit by a mine in Hormuz (US denies the radar-strike claim), and
Europe to join the Ukraine talks (biggest prisoner swap planned).

All type was rendered programmatically (PIL + DejaVu); all story visuals
are text-free editorial illustrations in one palette (ink navy, warm
ivory, vermilion). See `source-ledger.md` for the verified reporting
behind every story, and `tournament.md` for how three draft concepts
were compared and why this cover won.

## How it runs

`main.py` (Python 3.13, standard library only) copies the committed
`entry-news-v2.png` to `$MAKEFUN_OUTPUT_DIR/entry.png`. No network, no
randomness — two runs produce identical bytes.

```
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

## Files

- `main.py` — entrypoint (copies the artwork)
- `entry-news-v2.png` — final artwork (1024×1024)
- `compose.py` — deterministic build script that rendered the cover
- `source-ledger.md` — verified sources, dates, confidence per story
- `tournament.md` — the three drafts and the pairwise tournament
- `assets/` — the six text-free editorial illustrations used by compose.py
