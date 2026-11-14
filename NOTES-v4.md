# news-image-01 v4 — "THE WORLD IN ONE FRAME" (gambar dari user, round 3)

## Sumber gambar
- Gambar dipasok user langsung (upload 14 Nov 2026 ~09:39 WIB, file
  `workspace/user/media_library/image/image-33.png`): 1536x1024 PNG,
  2.895.950 byte — MELEBIHI batas kompetisi (tiap sisi <=1024 px, <=1 MiB).
- Diresize sekali (PIL LANCZOS, pertahankan rasio) menjadi `entry-news-v4.jpg`:
  1024x683 JPEG, 272.709 byte, sha256
  54e79812433620b7642e718b5edf6a4b112886501f12d6ea0e358176bc6fed55.
  Program (main.py) hanya menyalin file ini ke /output/entry.png, jadi
  run tetap deterministik dan tanpa network.

## Isi gambar
Halaman depan koran lanskap "THE WORLD IN ONE FRAME", header
"FRIDAY, 13 NOVEMBER 2026". 12 cerita: Ukraine war / Europe peace talks,
Microsoft 365 outage, Iran radar claim (Bahrain), Gaza heavy rain,
Lebanon strikes, COP31, India bus crash (Assam), Van Hollen vs Schumer,
EU diplomats to Ukraine talks, South Africa coalition talks,
Pakistan 74 militants, Pope Leo XIV returns to Chiclayo.

## Verifikasi cerita (disilangkan dengan ledger v2 + sources.md v3)
TERVERIFIKASI di riset kami (v2/v3):
- Ukraine drone attacks + Europe's role in peace talks — v3 (Europe joins
  Ukraine talks; Dublin AI summit thread).
- Microsoft 365 outage (74 countries) — v2 + v3.
- Iran claims radar strike / tanker hit — v2 + v3 (klaim, damage unverified).
- Gaza heavy rain in displacement camps — v3 (badai musim dingin Gaza).
- EU to send diplomats to Ukraine peace talks — v3.
- Pope Leo XIV returns to Chiclayo — v3 (misa 500.000 orang).

TIDAK ADA di ledger terverifikasi kami (v2/v3) — tampil di gambar apa adanya,
bukan klaim dari riset sesi ini:
- Lebanon "deadly strikes test ceasefire".
- COP31 "UN chief urges rapid emissions cuts" (v3: COP31 Antalya terverifikasi
  ada, tapi tanpa event diskrit 13 Nov).
- India "bus and truck collision in Assam kills at least 24".
- US "Van Hollen to challenge Schumer for Senate Democratic leadership".
- South Africa "parties enter high-stakes coalition talks".
- Pakistan "military reports 74 militants killed in border-region raids"
  (v3 secara eksplisit menandai klaim ini BELUM terverifikasi).

## Status
- v4 MENGGANTIKAN v3 ("The Day, in Focus", round 2, 01a1d6ac) sebagai entry
  final bila round 3 ini disubmit — atas instruksi user "submit gambar ini"
  (14 Nov 2026 09:39 WIB).
- Deadline kompetisi: 15 Nov 2026 03:00 WIB.
