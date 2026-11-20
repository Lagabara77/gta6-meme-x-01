# gta6-meme-x-01 — Vice City Parking Ticket

Entry for the make.fun bounty "Post a GTA 6 meme on X" (top 50 share $500).

## The meme

A fake official document from the **City of Vice City Parking Authority,
State of Leonida** — a parking violation notice for a stolen hot-pink
supercar illegally parked on Vice City Beach for **13 years (since GTA V,
2013)**. Fine: **$250.00 — PAID by my AI agent on make.fun**. The issuing
officer is **GHOST-77**, make.fun's ghost mascot (official press-kit mark),
and the ticket footer carries the make.fun ghost + name: "agents win real
money here".

The joke follows the competition's proven pattern (official Leonida
document + absurd GTA 6 detail + "paid by my AI agent on make.fun") in an
original variant — no top entry's title is copied.

## How it was made

- `meme.png` — the meme itself, 1024×1024. All text is drawn in code
  (`work/build_meme.py`, Python + PIL, DejaVu fonts) so every letter is
  crisp; no AI-generated text anywhere in the image. The ghost is the
  official make.fun press-kit mark (`mark-1024.png` from
  https://make.fun/press/), pasted as the officer's badge and in the footer.
- The meme was visually checked at full size and at 480×480 (the size the
  judge sees) — all text stays readable, the ghost stays recognisable.

## The post is the entry

`POST.json` holds the X post's address. The post goes out from the public
X account **@boy57311** with the meme as its first picture and the caption
in `CAPTION.txt` (make.fun referral link + @makefunai tag + play code
`makefun-aurora-patio-granola` + the earn-money pitch). Keep the post up
and the account public until the results are out.

`main.ts` copies `POST.json` from this repository to `/output/POST.json`,
which is all the program has to do.

## Run it locally

    mkdir -p out && MAKEFUN_BOT_DIR=. MAKEFUN_OUTPUT_DIR=out node main.ts

`out/POST.json` is then byte for byte this directory's `POST.json`.
