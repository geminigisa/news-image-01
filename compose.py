#!/usr/bin/env python3
"""Compose 3 editorial drafts for news-image-01 v2 (1024x1024, PIL + DejaVu).
All type is rendered programmatically; generated images carry no text.
Assets: v2-work/assets/*.webp (1920x1280, 3:2, text-free editorial illustrations).
Output: v2-work/drafts/draft-{a,b,c}.png
"""
import os
from PIL import Image, ImageDraw, ImageFont

BASE = os.path.dirname(os.path.abspath(__file__))
ASSETS = os.path.join(BASE, "assets")
OUT = os.path.join(BASE, "drafts")
os.makedirs(OUT, exist_ok=True)

IVORY = (245, 239, 227)
NAVY = (27, 42, 74)
VERMILION = (192, 57, 43)
SLATE = (74, 84, 106)
WHITE = (255, 255, 255)
PAPER = (250, 246, 236)

SERIF_B = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
SANS_B = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
SANS = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


def cover(im, w, h, focus=(0.5, 0.5)):
    """Center-crop (with focus point) + resize to w x h."""
    iw, ih = im.size
    target = w / h
    src = iw / ih
    if src > target:  # too wide -> crop width
        nw = int(ih * target)
        x0 = int((iw - nw) * focus[0])
        box = (x0, 0, x0 + nw, ih)
    else:  # too tall -> crop height
        nh = int(iw / target)
        y0 = int((ih - nh) * focus[1])
        box = (0, y0, iw, y0 + nh)
    return im.crop(box).resize((w, h), Image.LANCZOS)


def wrap(draw, text, fnt, max_w):
    words = text.split()
    lines, cur = [], ""
    for w in words:
        t = (cur + " " + w).strip()
        if draw.textlength(t, font=fnt) <= max_w:
            cur = t
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def draw_lines(draw, x, y, lines, fnt, fill, align="left", width=None, spacing=4):
    """Draw wrapped lines; returns y after last line."""
    for ln in lines:
        if align == "center":
            lx = x + (width - draw.textlength(ln, font=fnt)) / 2
        else:
            lx = x
        draw.text((lx, y), ln, font=fnt, fill=fill)
        y += fnt.size + spacing
    return y


def hline(draw, x0, x1, y, fill=NAVY, w=2):
    draw.line([(x0, y), (x1, y)], fill=fill, width=w)


def num_badge(draw, cx, cy, n, r=14, fill=VERMILION):
    draw.ellipse([cx - r, cy - r, cx + r, cy + r], fill=fill, outline=WHITE, width=2)
    f = font(SANS_B, 16)
    t = str(n)
    tw = draw.textlength(t, font=f)
    th = f.size
    draw.text((cx - tw / 2, cy - th / 2 - 1), t, font=f, fill=WHITE)


def load(name):
    return Image.open(os.path.join(ASSETS, name)).convert("RGB")


IMG = {
    "nvidia": load("media-generation-v2-nvidia-0-e95fea83-a672-43ab-85df-7bb7c5dfa142.webp"),
    "gaza": load("media-generation-v2-gaza-0-812f5d6d-8ec2-4477-aef2-649e86b3a36d.webp"),
    "microsoft": load("media-generation-v2-microsoft-0-a597afdd-fc57-4a3c-af31-2bdc197e2cbe.webp"),
    "hormuz": load("media-generation-v2-hormuz-0-4d847e79-d53f-4d0b-b3ea-dde414db2824.webp"),
    "ukraine": load("media-generation-v2-ukraine-0-6de85018-b15c-49d4-aa7b-6c87c38fc5f2.webp"),
    "map": load("media-generation-v2-map-0-93156f93-82b2-458f-9870-d18fbe3549f5.webp"),
}

SECONDARIES = [
    ("gaza", "GAZA HOSPITAL STRUCK", "Six killed in overnight strike"),
    ("microsoft", "MICROSOFT MAIL & TEAMS DOWN", "Outage hits 74 countries"),
    ("hormuz", "IRAN CLAIMS TANKER HIT BY MINE", "US denies radar strike claim"),
    ("ukraine", "EUROPE TO JOIN UKRAINE TALKS", "Biggest prisoner swap planned"),
]

M = 36
W = 1024 - 2 * M  # 952


def masthead(d, y=28, size=44, date_right=None):
    f = font(SERIF_B, size)
    d.text((M, y), "THE WORLD TODAY", font=f, fill=NAVY)
    if date_right:
        f2 = font(SANS_B, 18)
        t = date_right
        d.text((1024 - M - d.textlength(t, font=f2), y + 14), t, font=f2, fill=VERMILION)
    return y + size + 12


# ---------------------------------------------------------------- DRAFT A: cover
def draft_a():
    im = Image.new("RGB", (1024, 1024), IVORY)
    d = ImageDraw.Draw(im)
    y = masthead(d, date_right="13 NOV 2026")
    hline(d, M, 1024 - M, y, NAVY, 2)
    y += 10
    f = font(SANS_B, 15)
    t = "FRIDAY  •  WORLD NEWS"
    d.text(((1024 - d.textlength(t, font=f)) / 2, y), t, font=f, fill=SLATE)
    y += 28
    # Lead headline
    f = font(SERIF_B, 64)
    t = "NVIDIA CEO RESIGNS"
    d.text(((1024 - d.textlength(t, font=f)) / 2, y), t, font=f, fill=NAVY)
    y += 76
    f = font(SANS, 22)
    t = "Shares plunge as much as 16% — Kress takes over"
    d.text(((1024 - d.textlength(t, font=f)) / 2, y), t, font=f, fill=SLATE)
    y += 36
    # Lead image 952 x 420
    im.paste(cover(IMG["nvidia"], W, 420, focus=(0.5, 0.45)), (M, y))
    y += 420 + 14
    hline(d, M, 1024 - M, y, VERMILION, 3)
    y += 12
    f = font(SANS_B, 15)
    t = "TODAY'S OTHER DEVELOPMENTS"
    d.text(((1024 - d.textlength(t, font=f)) / 2, y), t, font=f, fill=NAVY)
    y += 28
    # Secondary row: 4 panels. Auto-fit ONE headline size so every headline
    # wraps to at most 2 lines and all sublines share a baseline.
    pw, gap = 226, 16
    best = 17
    for size in (20, 19, 18, 17):
        fh = font(SERIF_B, size)
        if all(len(wrap(d, head, fh, pw)) <= 2 for _, head, _ in SECONDARIES):
            best = size
            break
    for i, (key, head, sub) in enumerate(SECONDARIES):
        x = M + i * (pw + gap)
        im.paste(cover(IMG[key], pw, 150), (x, y))
        yy = y + 150 + 8
        fh = font(SERIF_B, best)
        lines = wrap(d, head, fh, pw)
        yy = draw_lines(d, x, yy, lines, fh, NAVY, align="center", width=pw, spacing=2)
        yy += 2
        fs = font(SANS, 14)
        lines = wrap(d, sub, fs, pw)
        draw_lines(d, x, yy, lines, fs, SLATE, align="center", width=pw, spacing=2)
    # Footer
    hline(d, M, 1024 - M, 990, NAVY, 1)
    f = font(SANS, 13)
    t = "Sources: Nvidia, AP, Reuters, BBC, Microsoft, US Dept. of Justice"
    d.text(((1024 - d.textlength(t, font=f)) / 2, 996), t, font=f, fill=SLATE)
    im.save(os.path.join(OUT, "draft-a-cover.png"))
    print("draft A saved")


# ---------------------------------------------------------------- DRAFT B: bands
def draft_b():
    im = Image.new("RGB", (1024, 1024), IVORY)
    d = ImageDraw.Draw(im)
    y = masthead(d, date_right="13 NOV 2026")
    hline(d, M, 1024 - M, y, VERMILION, 3)
    y += 14
    # Lead band (300 tall): text left, image right
    band_y = y
    tx = M
    tw = 500
    num_badge(d, tx + 14, band_y + 16, 1, r=14)
    fh = font(SERIF_B, 52)
    lines = wrap(d, "NVIDIA CEO RESIGNS", fh, tw)
    yy = draw_lines(d, tx, band_y + 40, lines, fh, NAVY, spacing=2)
    yy += 6
    fs = font(SANS, 20)
    lines = wrap(d, "Shares plunge as much as 16% — Kress takes over", fs, tw)
    yy = draw_lines(d, tx, yy, lines, fs, SLATE, spacing=4)
    yy += 4
    fs2 = font(SANS, 20)
    lines = wrap(d, "Chip stocks slide worldwide; successor search begins", fs2, tw)
    draw_lines(d, tx, yy, lines, fs2, SLATE, spacing=4)
    im.paste(cover(IMG["nvidia"], 428, 300, focus=(0.5, 0.45)), (1024 - M - 428, band_y))
    y = band_y + 300 + 16
    hline(d, M, 1024 - M, y, NAVY, 2)
    y += 12
    # 4 secondary bands, 132 tall each
    for i, (key, head, sub) in enumerate(SECONDARIES):
        by = y + i * 140
        num_badge(d, M + 14, by + 60, i + 2, r=14)
        im.paste(cover(IMG[key], 180, 120), (M + 42, by))
        fh = font(SERIF_B, 26)
        d.text((M + 238, by + 18), head, font=fh, fill=NAVY)
        fs = font(SANS, 18)
        d.text((M + 238, by + 62), sub, font=fs, fill=SLATE)
        if i < 3:
            hline(d, M, 1024 - M, by + 132, NAVY, 1)
    hline(d, M, 1024 - M, 990, NAVY, 1)
    f = font(SANS, 13)
    t = "Sources: Nvidia, AP, Reuters, BBC, Microsoft, US Dept. of Justice"
    d.text(((1024 - d.textlength(t, font=f)) / 2, 996), t, font=f, fill=SLATE)
    im.save(os.path.join(OUT, "draft-b-bands.png"))
    print("draft B saved")


# ---------------------------------------------------------------- DRAFT C: map
def draft_c():
    im = Image.new("RGB", (1024, 1024), IVORY)
    d = ImageDraw.Draw(im)
    y = masthead(d, size=36, date_right="13 NOV 2026")
    hline(d, M, 1024 - M, y, NAVY, 2)
    y += 10
    f = font(SANS_B, 15)
    t = "WHERE IT HAPPENED"
    d.text(((1024 - d.textlength(t, font=f)) / 2, y), t, font=f, fill=NAVY)
    y += 26
    # Map: crop top 75% of the 1920x1280 asset (drops Antarctica), place 952x400
    m = IMG["map"].crop((0, 100, 1920, 900)).resize((W, 400), Image.LANCZOS)
    im.paste(m, (M, y))
    map_y0 = y

    def to_map(lon, lat):
        # rough linear mapping on the ORIGINAL 1920x1280 frame, then to placed crop
        x0 = 50 + (lon + 180) * (1830 / 360)
        y0 = 130 + (75 - lat) * (1100 / 135)
        x = M + (x0 / 1920) * W
        yy = map_y0 + ((y0 - 100) / 800) * 400
        return x, yy

    markers = [
        (1, -121.95, 37.35),   # Santa Clara (Nvidia)
        (2, 34.45, 31.5),      # Gaza
        (3, 56.25, 26.6),      # Hormuz
        (4, -6.26, 53.35),     # Dublin (Ukraine talks)
    ]
    for n, lon, lat in markers:
        x, yy = to_map(lon, lat)
        num_badge(d, x, yy, n, r=15)
    y = map_y0 + 400 + 16
    hline(d, M, 1024 - M, y, VERMILION, 3)
    y += 12
    rows = [
        (1, "NVIDIA CEO RESIGNS", "Shares plunge as much as 16% — Kress takes over"),
        (2, "GAZA HOSPITAL STRUCK", "Six killed in overnight strike"),
        (3, "IRAN CLAIMS TANKER HIT BY MINE", "US denies radar strike claim"),
        (4, "EUROPE TO JOIN UKRAINE TALKS", "Biggest prisoner swap planned"),
        (5, "MICROSOFT MAIL & TEAMS DOWN", "Outage hits 74 countries — worldwide"),
    ]
    for n, head, sub in rows:
        num_badge(d, M + 14, y + 22, n, r=14)
        fh = font(SERIF_B, 24)
        d.text((M + 42, y), head, font=fh, fill=NAVY)
        fs = font(SANS, 17)
        d.text((M + 42, y + 34), sub, font=fs, fill=SLATE)
        y += 66
        if n < 5:
            hline(d, M, 1024 - M, y - 8, NAVY, 1)
    hline(d, M, 1024 - M, 990, NAVY, 1)
    f = font(SANS, 13)
    t = "Sources: Nvidia, AP, Reuters, BBC, Microsoft, US Dept. of Justice"
    d.text(((1024 - d.textlength(t, font=f)) / 2, 996), t, font=f, fill=SLATE)
    im.save(os.path.join(OUT, "draft-c-map.png"))
    print("draft C saved")


if __name__ == "__main__":
    draft_a()
    draft_b()
    draft_c()
