#!/usr/bin/env python3
"""Build the gta6-meme-x-01 meme (1024x1024). v2 — fixed layout (v1 overflowed
the ticket: punchline clipped, footer + barcode missing, stamp covered text).

Concept: VICE CITY PARKING AUTHORITY ticket — a fake official Leonida
document (the winning top-5 pattern: official Leonida document + absurd
GTA 6 detail + "paid by my AI agent on make.fun"), in our own variant.
No top-5 title is copied (no Mart, no Steam invoice, no library notice,
no hurricane warning, no bail certificate).

All text is drawn here with PIL so every letter is crisp — no
AI-generated text anywhere. The make.fun ghost is the OFFICIAL press-kit
mark (mark-1024.png), pasted as the issuing officer's badge and in the
footer next to the make.fun name.
"""
import random
from PIL import Image, ImageDraw, ImageFont

BASE = "/home/hatch/workspace/makefun/gta6-meme-x-01"
MARK = BASE + "/press-kit/make-fun-press-kit/mark-1024.png"
OUT = BASE + "/meme.png"

W, H = 1024, 1024

MAGENTA = (196, 28, 131)      # make.fun #C41C83
MAGENTA_DK = (140, 12, 90)
NAVY = (22, 16, 48)
PURPLE = (59, 15, 79)
CREAM = (247, 241, 222)
INK = (24, 22, 30)
GREY = (96, 90, 84)
RED = (178, 34, 34)
PINK_BG = (255, 214, 232)

BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
REG = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
MONO_B = "/usr/share/fonts/truetype/dejavu/DejaVuSansMono-Bold.ttf"
MONO = "/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


def center_text(d, y, text, fnt, fill, x0, x1):
    d.text(((x0 + x1) / 2, y), text, font=fnt, fill=fill, anchor="ma")


def main():
    # ---- background: Vice City night gradient + stars + glow ----
    img = Image.new("RGB", (W, H), NAVY)
    d = ImageDraw.Draw(img, "RGBA")
    for y in range(H):
        t = y / H
        r = round(NAVY[0] + (PURPLE[0] - NAVY[0]) * t)
        g = round(NAVY[1] + (PURPLE[1] - NAVY[1]) * t)
        b = round(NAVY[2] + (PURPLE[2] - NAVY[2]) * t)
        d.line([(0, y), (W, y)], fill=(r, g, b))
    for i in range(260):
        a = int(70 * (1 - i / 260))
        d.ellipse([-260, H - 200 + i * 0.4, W + 260, H + 260 - i * 0.2],
                  fill=(MAGENTA[0], MAGENTA[1], MAGENTA[2], a))
    random.seed(77)
    for _ in range(90):
        x, y = random.randint(0, W), random.randint(0, 420)
        r = random.choice([1, 1, 2])
        d.ellipse([x, y, x + r, y + r], fill=(255, 255, 255, random.randint(90, 200)))

    # ---- ticket card (drawn flat, then rotated -2 deg) ----
    TW, TH = 880, 900
    ticket = Image.new("RGBA", (TW, TH), (0, 0, 0, 0))
    td = ImageDraw.Draw(ticket)
    td.rounded_rectangle([0, 0, TW - 1, TH - 1], radius=18, fill=CREAM,
                         outline=(190, 178, 150), width=2)
    for y in range(14, TH - 10, 22):  # perforation
        td.line([(52, y), (52, y + 12)], fill=(170, 158, 128), width=2)
    td.ellipse([-16, 300, 16, 332], fill=NAVY)
    td.ellipse([-16, 560, 16, 592], fill=NAVY)

    x0, x1 = 84, TW - 36
    y = 30
    center_text(td, y, "S T A T E   O F   L E O N I D A", font(BOLD, 22), GREY, x0, x1)
    y += 32
    center_text(td, y, "CITY OF VICE CITY", font(BOLD, 50), NAVY, x0, x1)
    y += 58
    center_text(td, y, "★  PARKING AUTHORITY  ★", font(BOLD, 29), MAGENTA, x0, x1)
    y += 44
    td.line([(x0, y), (x1, y)], fill=INK, width=3)
    y += 14
    center_text(td, y, "PARKING VIOLATION NOTICE", font(BOLD, 29), INK, x0, x1)
    y += 42
    td.text((x0, y), "Ticket No. 0613-2026", font=font(MONO, 23), fill=GREY)
    tw = td.textlength("NOV 19, 2026  •  11:59 PM", font=font(MONO, 23))
    td.text((x1 - tw, y), "NOV 19, 2026  •  11:59 PM", font=font(MONO, 23), fill=GREY)
    y += 36
    for x in range(x0, x1, 16):  # dashed divider
        td.line([(x, y), (x + 9, y)], fill=(170, 158, 128), width=2)
    y += 20

    # ---- fields: one line each (label + value) ----
    fields = [
        ("VEHICLE:  ", "STOLEN SUPERCAR (HOT PINK)"),
        ("LOCATION: ", "VICE CITY BEACH, LEONIDA"),
        ("VIOLATION:", "ILLEGAL PARKING ON THE BEACH"),
        ("DURATION: ", "13 YEARS — SINCE GTA V (2013)"),
    ]
    for label, value in fields:
        td.text((x0, y), label, font=font(MONO_B, 27), fill=GREY)
        lw = td.textlength(label, font=font(MONO_B, 27))
        td.text((x0 + lw, y), value, font=font(MONO_B, 27), fill=INK)
        y += 46
    # officer row with the ghost badge
    td.text((x0, y), "OFFICER:  ", font=font(MONO_B, 27), fill=GREY)
    ghost = Image.open(MARK).convert("RGBA").resize((52, 52), Image.LANCZOS)
    ticket.alpha_composite(ghost, (x0 + 168, y - 6))
    td.text((x0 + 232, y), "GHOST-77", font=font(MONO_B, 27), fill=INK)
    y += 62

    # ---- fine box (right side kept empty for the stamp) ----
    td.rounded_rectangle([x0, y, x1, y + 108], radius=12,
                         outline=MAGENTA, width=4, fill=PINK_BG)
    td.text((x0 + 24, y + 12), "FINE DUE", font=font(BOLD, 25), fill=MAGENTA_DK)
    td.text((x0 + 24, y + 42), "$250.00", font=font(BOLD, 58), fill=MAGENTA)
    fine_y, fine_h = y, 108
    y += 130

    # ---- punchline: one line ----
    center_text(td, y, "PAID BY MY AI AGENT ON make.fun",
                font(BOLD, 33), RED, x0, x1)
    y += 52

    # ---- footer: ghost + make.fun + pitch ----
    ghost2 = Image.open(MARK).convert("RGBA").resize((84, 84), Image.LANCZOS)
    fx = (TW - 84 - 296) // 2
    ticket.alpha_composite(ghost2, (fx, y))
    td.text((fx + 100, y + 6), "make.fun", font=font(BOLD, 48), fill=INK)
    td.text((fx + 100, y + 56), "agents win real money here", font=font(REG, 21), fill=GREY)
    y += 100
    # barcode strip
    bx = x0
    random.seed(613)
    while bx < x1 - 8:
        bw = random.choice([2, 3, 4, 6])
        if random.random() < 0.62:
            td.rectangle([bx, y, bx + bw, y + 30], fill=INK)
        bx += bw + 3
    center_text(td, y + 38, "06132026  •  PAY AT MAKE.FUN  •  NO EXCUSES ACCEPTED",
                font(MONO, 18), GREY, x0, x1)

    # ---- paste ticket rotated, with shadow ----
    rot = ticket.rotate(2, expand=True, resample=Image.BICUBIC)
    shadow = Image.new("RGBA", rot.size, (0, 0, 0, 0))
    sd = ImageDraw.Draw(shadow)
    sd.rounded_rectangle([14, 18, rot.width - 2, rot.height - 2], radius=20,
                         fill=(0, 0, 0, 140))
    px = (W - rot.width) // 2
    py = (H - rot.height) // 2 + 6
    img.paste(Image.alpha_composite(shadow, rot), (px, py),
              Image.alpha_composite(shadow, rot))

    # ---- PAID stamp: over the EMPTY right half of the fine box ----
    # (kept clear of the punchline line below the box)
    stamp = Image.new("RGBA", (370, 165), (0, 0, 0, 0))
    sdd = ImageDraw.Draw(stamp)
    sdd.rounded_rectangle([6, 6, 363, 158], radius=16, outline=RED, width=8)
    sdd.rounded_rectangle([16, 16, 353, 148], radius=12, outline=RED, width=3)
    sdd.text((185, 76), "PAID", font=font(BOLD, 88), fill=RED, anchor="mm")
    stamp = stamp.rotate(-14, expand=True, resample=Image.BICUBIC)
    # fine box top in canvas coords: py + fine_y (ticket coords, pre-rotation approx)
    sx = px + rot.width - 400
    sy = py + 425
    img.paste(stamp, (sx, sy), stamp)

    img.save(OUT, "PNG", optimize=True)
    import os
    print("wrote", OUT, os.path.getsize(OUT), "bytes")


if __name__ == "__main__":
    main()
