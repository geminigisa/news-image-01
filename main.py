#!/usr/bin/env python3
"""news-image-01 entry: write the pre-rendered 13 Nov 2026 front page to /output/entry.png.

The artwork is a committed JPEG in this repository (entry-news-v4.jpg):
a 1024x683 landscape front page, "THE WORLD IN ONE FRAME", summarising
the world's news of Friday, 13 November 2026. The image was supplied by
the entrant and resized once to fit the competition limits (each side
<=1024 px, <=1 MiB). This program only copies it into the output
directory, so the run is deterministic and needs no network. The output
file is JPEG data by magic bytes, which the competition accepts alongside PNG.
"""

import os
import shutil
from pathlib import Path


def main():
    asset = Path(__file__).resolve().parent / "entry-news-v4.jpg"
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(asset, out_dir / "entry.png")


if __name__ == "__main__":
    main()
