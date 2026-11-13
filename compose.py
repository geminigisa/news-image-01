#!/usr/bin/env python3
"""news-image-01 v3 'THE DAY, IN FOCUS' — compose 3 rough compositions.

Deterministic: stdlib + PIL only, no network, no timestamps, no randomness.
Usage: python3 compose.py [a|b|c|all]
Outputs: drafts/draft-a.png, draft-b.png, draft-c.png (+ -512.png previews).
"""
import os
import sys
from PIL import Image, ImageDraw, ImageFont

BASE = os.path.dirname(os.path.abspath(__file__))
ASSETS = os.path.join(BASE, "assets")
DRAFTS = os.path.join(BASE, "drafts")

W, H = 1024, 1024
HEADER_H, FOOTER_H = 64, 28
GUT = 4
CELL_W, CELL_H = 253, 152

INK = (20, 20, 20)
PAPER = (247, 243, 236)
HEADER_BG = (17, 17, 17)
RED = (176, 58, 46)
SUBGREY = (74, 74, 68)
WHITE = (255, 255, 255)

FONT_DIR = "/usr/share/fonts/truetype/noto"
COND_BOLD = os.path.join(FONT_DIR, "NotoSans-CondensedBold.ttf")
SANS_BOLD = os.path.join(FONT_DIR, "NotoSans-Bold.ttf")
SANS_REG = os.path.join(FONT_DIR, "NotoSans-Regular.ttf")
for p in (COND_BOLD, SANS_BOLD, SANS_REG):
    assert os.path.isfile(p), "missing font: " + p

FILES = {
    "nvidia": "media-generation-v3-nvidia-0-4ecbc0aa-03e4-48bf-8ff0-104b4ef63f02.webp",
    "microsoft": "media-generation-v3-microsoft-0-050f5130-7f36-4bf7-95e9-889648f1c8b3.webp",
    "hormuz": "media-generation-v3-hormuz-0-968b8341-6ead-4762-bfd3-2d4f122b43b9.webp",
    "gaza": "media-generation-v3-gaza-0-8e0d3aba-b3cf-4c94-acb3-47a77d57d91b.webp",
    "kyiv": "media-generation-v3-kyiv-0-5a1ed8c2-ae9f-4fb9-8027-75d127070bd3.webp",
    "euai": "media-generation-v3-euai-0-f6350a61-c2ac-4127-9f8f-1d3667134c83.webp",
    "merz": "media-generation-v3-merz-0-547071f4-f5d4-48ea-bd52-3cf62c124401.webp",
    "iaea": "media-generation-v3-iaea-0-549d2f40-2018-4293-a544-f165a02c8244.webp",
    "pope": "media-generation-v3-pope-0-b2d367fe-9dd5-4772-b44e-b46c37fc7258.webp",
}

# story: (image key, headline, subline or None, focus_x, focus_y)
STORIES = {
    "nvidia": ("nvidia", "NVIDIA CEO RESIGNS",
               "Shares plunge as much as 14% \u2014 Kress takes over; Senate summons Huang",
               0.50, 0.62),
    "microsoft": ("microsoft", "MICROSOFT OUTAGE HITS 74 COUNTRIES", None, 0.50, 0.45),
    "hormuz": ("hormuz", "IRAN CLAIMS TANKER HIT BY MINE", None, 0.50, 0.48),
    "gaza": ("gaza", "KHAN YOUNIS: HOSPITAL STRUCK, SIX KILLED", None, 0.50, 0.50),
    "kyiv": ("kyiv", "KYIV: HOSPITAL HIT IN DRONE ATTACK", None, 0.50, 0.50),
    "euai": ("euai", "DUBLIN: EU LEADERS HOLD FIRST AI SUMMIT", None, 0.50, 0.50),
    "merz": ("merz", "MERZ TO TRUMP: \u2018NO SURPRISES\u2019 WITH PUTIN", None, 0.45, 0.50),
    "iaea": ("iaea", "IAEA: IRAN NUCLEAR MONITORING STALLED",
            "Inspectors locked out; uranium stockpile unverified", 0.50, 0.40),
    "pope": ("pope", "CHICLAYO: POPE LEO\u2019S HOMECOMING MASS",
            "500,000 gather for Mass in Peru", 0.55, 0.50),
}

_cache = {}


def load_image(key):
    if key not in _cache:
        _cache[key] = Image.open(os.path.join(ASSETS, FILES[key])).convert("RGB")
    return _cache[key]


def crop_to(img, tw, th, fx=0.5, fy=0.5):
    """Center-crop (with focus) to target aspect, then resize. Deterministic."""
    sw, sh = img.size
    tr = tw / th
    sr = sw / sh
    if sr > tr:  # source wider: crop width
        cw, ch = int(sh * tr), sh
    else:        # source taller: crop height
        cw, ch = sw, int(sw / tr)
    cx = int(fx * sw)
    cy = int(fy * sh)
    x0 = min(max(cx - cw // 2, 0), sw - cw)
    y0 = min(max(cy - ch // 2, 0), sh - ch)
    return img.crop((x0, y0, x0 + cw, y0 + ch)).resize((tw, th), Image.LANCZOS)


def wrap(draw, text, font, max_w):
    words = text.split()
    lines, cur = [], ""
    for w in words:
        trial = (cur + " " + w).strip()
        if draw.textlength(trial, font=font) <= max_w or not cur:
            cur = trial
        else:
            lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def fit_headline(draw, text, start_px, min_px, max_w, max_lines):
    """Largest condensed-bold size (start..min) whose wrap fits max_lines."""
    for px in range(start_px, min_px - 1, -1):
        font = ImageFont.truetype(COND_BOLD, px)
        lines = wrap(draw, text, font, max_w)
        if len(lines) <= max_lines:
            return font, lines
    font = ImageFont.truetype(COND_BOLD, min_px)
    return font, wrap(draw, text, font, max_w)


def draw_top_panel(page, draw, x, y, w, h, story, img_h, head_px, sub_px=None):
    key, headline, subline, fx, fy = STORIES[story]
    img = crop_to(load_image(key), w, img_h, fx, fy)
    page.paste(img, (x, y))
    bh = h - img_h
    draw.rectangle([x, y + img_h, x + w, y + h], fill=PAPER)
    pad = 12
    max_w = w - 2 * pad
    font, lines = fit_headline(draw, headline, head_px, 14, max_w, 2)
    lh = int(font.size * 1.08)
    block_h = lh * len(lines)
    if subline and sub_px:
        sub_font = ImageFont.truetype(SANS_REG, sub_px)
        sub_lines = wrap(draw, subline, sub_font, max_w)
        block_h += 4 + int(sub_px * 1.25) * len(sub_lines)
    ty = y + img_h + max(6, (bh - block_h) // 2)
    for ln in lines:
        draw.text((x + pad, ty), ln, font=font, fill=INK)
        ty += lh
    if subline and sub_px:
        ty += 4
        sub_font = ImageFont.truetype(SANS_REG, sub_px)
        for ln in wrap(draw, subline, sub_font, max_w):
            draw.text((x + pad, ty), ln, font=sub_font, fill=SUBGREY)
            ty += int(sub_px * 1.25)


def draw_side_panel(page, draw, x, y, w, h, story, img_w, head_px):
    key, headline, subline, fx, fy = STORIES[story]
    img = crop_to(load_image(key), img_w, h, fx, fy)
    page.paste(img, (x, y))
    bx = x + img_w
    bw = w - img_w
    draw.rectangle([bx, y, x + w, y + h], fill=PAPER)
    draw.rectangle([bx, y, bx + 3, y + h], fill=RED)
    pad = 12
    max_w = bw - pad - 10
    font, lines = fit_headline(draw, headline, head_px, 14, max_w, 3)
    lh = int(font.size * 1.08)
    ty = y + max(8, (h - lh * len(lines)) // 2)
    for ln in lines:
        draw.text((bx + pad + 3, ty), ln, font=font, fill=INK)
        ty += lh


def draw_band_panel(page, draw, x, y, w, h, story, img_w, head_px, sub_px):
    """Full-width bottom band: image left, banner right (variant B pope)."""
    key, headline, subline, fx, fy = STORIES[story]
    img = crop_to(load_image(key), img_w, h, fx, fy)
    page.paste(img, (x, y))
    bx = x + img_w
    bw = w - img_w
    draw.rectangle([bx, y, x + w, y + h], fill=PAPER)
    draw.rectangle([bx, y, bx + 3, y + h], fill=RED)
    pad = 16
    max_w = bw - 2 * pad
    font, lines = fit_headline(draw, headline, head_px, 16, max_w, 3)
    lh = int(font.size * 1.08)
    block_h = lh * len(lines)
    sub_font = ImageFont.truetype(SANS_REG, sub_px)
    sub_lines = wrap(draw, subline, sub_font, max_w) if subline else []
    block_h += 6 + int(sub_px * 1.25) * len(sub_lines)
    ty = y + max(10, (h - block_h) // 2)
    for ln in lines:
        draw.text((bx + pad + 3, ty), ln, font=font, fill=INK)
        ty += lh
    ty += 6
    for ln in sub_lines:
        draw.text((bx + pad + 3, ty), ln, font=sub_font, fill=SUBGREY)
        ty += int(sub_px * 1.25)


def draw_header_footer(draw):
    draw.rectangle([0, 0, W, HEADER_H], fill=HEADER_BG)
    date_f = ImageFont.truetype(SANS_BOLD, 22)
    title_f = ImageFont.truetype(SANS_BOLD, 30)
    draw.text((16, (HEADER_H - 22) // 2 - 2), "FRIDAY 13 NOVEMBER 2026",
              font=date_f, fill=WHITE)
    t = "THE DAY\u2019S WORLD NEWS"
    draw.text((W - 16 - draw.textlength(t, font=title_f),
               (HEADER_H - 30) // 2 - 2), t, font=title_f, fill=WHITE)
    draw.rectangle([0, HEADER_H, W, HEADER_H + 3], fill=RED)
    fy = H - FOOTER_H
    draw.rectangle([0, fy, W, H], fill=HEADER_BG)
    foot_f = ImageFont.truetype(SANS_REG, 11)
    foot_b = ImageFont.truetype(SANS_BOLD, 11)
    left = "EDITORIAL RECONSTRUCTIONS \u2014 IMAGES ARE AI-GENERATED ILLUSTRATIONS OF REPORTED EVENTS"
    draw.text((16, fy + 8), left, font=foot_f, fill=WHITE)
    r = "13 NOV 2026"
    draw.text((W - 16 - draw.textlength(r, font=foot_b), fy + 8), r,
              font=foot_b, fill=WHITE)


def col(i):
    return i * (CELL_W + GUT)


def row(i):
    return HEADER_H + 3 + i * (CELL_H + GUT)


def build(variant):
    page = Image.new("RGB", (W, H), (0, 0, 0))
    draw = ImageDraw.Draw(page)
    if variant == "a":
        # lead-dominant grid (brief layout): lead 3x2, 2x 1x1, 4x 2x1, 2x 2x2
        draw_top_panel(page, draw, col(0), row(0), 3 * CELL_W + 2 * GUT,
                       2 * CELL_H + GUT, "nvidia", 205, 44, 15)
        draw_top_panel(page, draw, col(3), row(0), CELL_W, CELL_H,
                       "microsoft", 92, 20)
        draw_top_panel(page, draw, col(3), row(1), CELL_W, CELL_H,
                       "hormuz", 92, 20)
        draw_side_panel(page, draw, col(0), row(2), 2 * CELL_W + GUT, CELL_H,
                        "gaza", 200, 24)
        draw_side_panel(page, draw, col(2), row(2), 2 * CELL_W + GUT, CELL_H,
                        "kyiv", 200, 24)
        draw_side_panel(page, draw, col(0), row(3), 2 * CELL_W + GUT, CELL_H,
                        "euai", 200, 24)
        draw_side_panel(page, draw, col(2), row(3), 2 * CELL_W + GUT, CELL_H,
                        "merz", 200, 24)
        draw_top_panel(page, draw, col(0), row(4), 2 * CELL_W + GUT,
                       2 * CELL_H + GUT, "pope", 205, 34, 15)
        draw_top_panel(page, draw, col(2), row(4), 2 * CELL_W + GUT,
                       2 * CELL_H + GUT, "iaea", 205, 34, 15)
    elif variant == "b":
        # balanced mosaic: lead 2x2, 2x 1x1, 5x 2x1, pope full-width band
        draw_top_panel(page, draw, col(0), row(0), 2 * CELL_W + GUT,
                       2 * CELL_H + GUT, "nvidia", 205, 40, 15)
        draw_top_panel(page, draw, col(2), row(0), CELL_W, CELL_H,
                       "microsoft", 92, 20)
        draw_top_panel(page, draw, col(3), row(0), CELL_W, CELL_H,
                       "hormuz", 92, 20)
        draw_side_panel(page, draw, col(2), row(1), 2 * CELL_W + GUT, CELL_H,
                        "gaza", 200, 24)
        draw_side_panel(page, draw, col(0), row(2), 2 * CELL_W + GUT, CELL_H,
                        "kyiv", 200, 24)
        draw_side_panel(page, draw, col(2), row(2), 2 * CELL_W + GUT, CELL_H,
                        "euai", 200, 24)
        draw_side_panel(page, draw, col(0), row(3), 2 * CELL_W + GUT, CELL_H,
                        "merz", 200, 24)
        draw_side_panel(page, draw, col(2), row(3), 2 * CELL_W + GUT, CELL_H,
                        "iaea", 200, 24)
        draw_band_panel(page, draw, col(0), row(4), 4 * CELL_W + 3 * GUT,
                        2 * CELL_H + GUT, "pope", 640, 40, 16)
    elif variant == "c":
        # reduced story, larger text: 7 stories, lead 3x2, 2x 1x1, 4x 2x2
        draw_top_panel(page, draw, col(0), row(0), 3 * CELL_W + 2 * GUT,
                       2 * CELL_H + GUT, "nvidia", 205, 44, 15)
        draw_top_panel(page, draw, col(3), row(0), CELL_W, CELL_H,
                       "microsoft", 92, 20)
        draw_top_panel(page, draw, col(3), row(1), CELL_W, CELL_H,
                       "hormuz", 92, 20)
        draw_top_panel(page, draw, col(0), row(2), 2 * CELL_W + GUT,
                       2 * CELL_H + GUT, "gaza", 205, 36, 15)
        draw_top_panel(page, draw, col(2), row(2), 2 * CELL_W + GUT,
                       2 * CELL_H + GUT, "kyiv", 205, 36, 15)
        draw_top_panel(page, draw, col(0), row(4), 2 * CELL_W + GUT,
                       2 * CELL_H + GUT, "pope", 205, 34, 15)
        draw_top_panel(page, draw, col(2), row(4), 2 * CELL_W + GUT,
                       2 * CELL_H + GUT, "iaea", 205, 34, 15)
    else:
        raise ValueError("unknown variant " + variant)
    draw_header_footer(draw)
    return page


def main():
    which = sys.argv[1] if len(sys.argv) > 1 else "all"
    variants = ["a", "b", "c"] if which == "all" else [which]
    os.makedirs(DRAFTS, exist_ok=True)
    for v in variants:
        page = build(v)
        out = os.path.join(DRAFTS, "draft-%s.png" % v)
        page.save(out, format="PNG")
        page.resize((512, 512), Image.LANCZOS).save(
            os.path.join(DRAFTS, "draft-%s-512.png" % v), format="PNG")
        print("wrote", out, page.size)


if __name__ == "__main__":
    main()
