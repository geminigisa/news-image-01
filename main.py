#!/usr/bin/env python3
"""news-image-01 entry: write the pre-rendered 13 Nov 2026 front page to /output/entry.png.

The artwork is a committed PNG in this repository (entry-news-v2.png):
a 1024x1024 editorial cover summarising the world's news of Friday,
13 November 2026. This program only copies it into the output
directory, so the run is deterministic and needs no network.
"""

import os
import shutil
from pathlib import Path


def main():
    asset = Path(__file__).resolve().parent / "entry-news-v2.png"
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(asset, out_dir / "entry.png")


if __name__ == "__main__":
    main()
