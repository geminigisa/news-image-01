# news-image-01 — "The World in One Frame"

Entry for make.fun `news-image-01`: sum up the world's news of Friday,
13 November 2026 in one image. Account: silver-fox-78.

## The image

`entry-news-v4.jpg` (1024×683, 272,709 bytes) is a landscape newspaper
front page, "THE WORLD IN ONE FRAME", dated Friday, 13 November 2026.
Twelve stories: Ukraine war / Europe's role in peace talks, Microsoft
365 outage, Iran radar claim (Bahrain), Gaza heavy rain in displacement
camps, Lebanon strikes, COP31, India bus crash (Assam), Van Hollen vs
Schumer, EU diplomats to Ukraine talks, South Africa coalition talks,
Pakistan 74 militants, Pope Leo XIV returns to Chiclayo.

The image was supplied by the entrant (1536×1024 PNG, 2,895,950 bytes)
and resized once to fit the competition limits (each side ≤1024 px,
≤1 MiB). Six of its stories match our verified research ledgers (v2/v3);
six (Lebanon, COP31 event, Assam bus, Van Hollen, South Africa,
Pakistan) do not appear in those ledgers — see `NOTES-v4.md` for the
per-story check.

This v4 replaces the v3 cover ("The Day, in Focus") as the final entry,
on the entrant's instruction.

## How it runs

`main.py` (Python 3.13, standard library only) copies the committed
`entry-news-v4.jpg` to `$MAKEFUN_OUTPUT_DIR/entry.png`, defaulting to
`/output` when the variable is unset (the grader sets none). No network,
no randomness — two runs produce identical bytes.

```
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

## Files

- `main.py` — entrypoint (copies the artwork)
- `entry-news-v4.jpg` — final artwork (1024×683)
- `NOTES-v4.md` — image provenance, resize, and per-story verification
