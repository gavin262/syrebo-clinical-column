"""Draw 1080px clinical-column posters.

Chinese posters use brand blue #0050A0 as the only accent.
Section chips and result chips center their text on the chip rectangle.
"""

from __future__ import annotations

import re
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

W = 1080
MARGIN = 48
CONTENT_W = W - MARGIN * 2
BLUE = (0, 80, 160)  # #0050A0
NAVY = (0, 53, 107)  # #00356B
TEXT = (28, 40, 54)
MUTED = (82, 100, 120)
WHITE = (255, 255, 255)
PALE = (232, 242, 251)  # #E8F2FB
CHIP_BG = (228, 238, 248)  # #E4EEF8
LIGHT = (213, 228, 247)
LINE = (211, 222, 236)
BAR_2 = (159, 184, 206)  # blue tint, not a second hue
FOOT = (90, 108, 128)

FONT_PATH = "/usr/share/fonts/truetype/wqy/wqy-microhei.ttc"
LATIN_WORD = re.compile(r"[A-Za-z]{2,}")
# Tokens allowed outside the citation block on a Chinese poster.
ZH_ALLOW = re.compile(
    r"^(?:SYREBO|Syrebo|syrebo|com|SY|HR|FMA|UE|BBT|ARAT|FIM|DOI)$"
)


def font(size: int) -> ImageFont.FreeTypeFont:
    return ImageFont.truetype(FONT_PATH, size)


def wrap(draw: ImageDraw.ImageDraw, text: str, fnt, max_w: int) -> list[str]:
    lines: list[str] = []
    line = ""
    for ch in text:
        trial = line + ch
        if draw.textlength(trial, font=fnt) > max_w and line and ch not in "，。；：、！？）】》％":
            lines.append(line)
            line = ch
        else:
            line = trial
    if line:
        lines.append(line)
    return lines


def _ink_box(draw, text, fnt):
    return draw.textbbox((0, 0), text, font=fnt)


def draw_block_centered(draw, rect, lines, fnt, fill, gap=4):
    """Center a stack of lines inside rect, each line centered horizontally."""
    x0, y0, x1, y1 = rect
    metrics = []
    for ln in lines:
        b = _ink_box(draw, ln, fnt)
        metrics.append((ln, b, b[2] - b[0], b[3] - b[1]))
    total = sum(m[3] for m in metrics) + gap * (len(metrics) - 1)
    y = y0 + ((y1 - y0) - total) / 2
    for ln, b, w, h in metrics:
        x = x0 + ((x1 - x0) - w) / 2 - b[0]
        draw.text((x, y - b[1]), ln, font=fnt, fill=fill)
        y += h + gap


def draw_line_in_rect(draw, rect, text, fnt, fill, align="left", pad=18):
    """Place one line so its ink box is vertically centered in rect."""
    x0, y0, x1, y1 = rect
    b = _ink_box(draw, text, fnt)
    tw, th = b[2] - b[0], b[3] - b[1]
    y = y0 + ((y1 - y0) - th) / 2 - b[1]
    if align == "center":
        x = x0 + ((x1 - x0) - tw) / 2 - b[0]
    elif align == "right":
        x = x1 - pad - tw - b[0]
    else:
        x = x0 + pad - b[0]
    draw.text((x, y), text, font=fnt, fill=fill)


def rounded(im, box, radius, fill, outline=None, width=1):
    layer = Image.new("RGBA", im.size, (0, 0, 0, 0))
    d = ImageDraw.Draw(layer)
    d.rounded_rectangle(box, radius=radius, fill=fill, outline=outline, width=width)
    base = im.convert("RGBA")
    out = Image.alpha_composite(base, layer)
    return out.convert("RGB")


def cover(src: Image.Image, w: int, h: int) -> Image.Image:
    sw, sh = src.size
    scale = max(w / sw, h / sh)
    nw, nh = round(sw * scale), round(sh * scale)
    resized = src.resize((nw, nh), Image.Resampling.LANCZOS)
    left = (nw - w) // 2
    top = (nh - h) // 2
    return resized.crop((left, top, left + w, top + h))


def paste_round(base: Image.Image, photo: Image.Image, box, radius=18):
    x0, y0, x1, y1 = box
    w, h = x1 - x0, y1 - y0
    img = cover(photo.convert("RGB"), w, h)
    mask = Image.new("L", (w, h), 0)
    ImageDraw.Draw(mask).rounded_rectangle((0, 0, w - 1, h - 1), radius=radius, fill=255)
    base.paste(img, (x0, y0), mask)
    return rounded(base, box, radius, fill=None, outline=LINE, width=2) if False else _stroke(base, box, radius)


def _stroke(base, box, radius):
    d = ImageDraw.Draw(base)
    d.rounded_rectangle(box, radius=radius, outline=LINE, width=2)
    return base


def chip_deviation(im: Image.Image, rect, bg, ink) -> float:
    """Return how far the ink centroid sits from the rectangle center, in px."""
    x0, y0, x1, y1 = [int(v) for v in rect]
    crop = im.crop((x0, y0, x1, y1))
    px = crop.load()
    w, h = crop.size
    minx = miny = 10**9
    maxx = maxy = -1
    n = 0
    for y in range(h):
        for x in range(w):
            r, g, b = px[x, y][:3]
            # Ink is the brand blue; skip the pale chip fill and antialiased edge.
            if b > r + 40 and b > 90 and r < 80:
                n += 1
                minx = min(minx, x)
                miny = min(miny, y)
                maxx = max(maxx, x)
                maxy = max(maxy, y)
    if n < 8:
        return 0.0
    cx = (minx + maxx) / 2
    cy = (miny + maxy) / 2
    return max(abs(cx - w / 2), abs(cy - h / 2))


def assert_zh_copy(parts: list[str]) -> None:
    """Designed Chinese-poster text may not carry English words."""
    blob = "\n".join(parts)
    bad = []
    for word in LATIN_WORD.findall(blob):
        if ZH_ALLOW.match(word):
            continue
        # Split compounds already handled; flag the token.
        bad.append(word)
    if bad:
        raise SystemExit("Chinese poster contains English words: " + ", ".join(sorted(set(bad))))


def render(spec: dict, photo: Image.Image | None, logo: Image.Image) -> Image.Image:
    """spec keys: lang, chip, cat, title, sub, caption, diagram, stats,
    design_label, key_label, result, note, boundary, source, footer.
    Draws on a tall canvas and crops to the footer.
    """
    probe = ImageDraw.Draw(Image.new("RGB", (10, 10), WHITE))
    f_title = font(46)
    title_lines = wrap(probe, spec["title"], f_title, CONTENT_W)
    if len(title_lines) > 3:
        f_title = font(40)
        title_lines = wrap(probe, spec["title"], f_title, CONTENT_W)
    f_sub = font(24)
    sub_lines = wrap(probe, spec["sub"], f_sub, CONTENT_W) if spec.get("sub") else []
    header_h = 112
    band_h = 36 + 28 + len(title_lines) * 58 + 8 + max(1, len(sub_lines)) * 34 + 28
    visual_h = 430 if photo is not None else 280
    cap_lines = wrap(probe, spec["caption"], font(20), CONTENT_W) if spec.get("caption") else []
    f_note = font(22)
    note_lines = wrap(probe, spec["note"], f_note, CONTENT_W - 48)
    bound_lines = wrap(probe, spec["boundary"], f_note, CONTENT_W - 64)
    src_font = font(20)
    src_wrapped = []
    for line in spec["source"]:
        src_wrapped.extend(wrap(probe, line, src_font, CONTENT_W - 48))

    im = Image.new("RGB", (W, 4600), WHITE)
    # Header.
    logo_h = 54
    logo_w = round(logo.width * logo_h / logo.height)
    logo_r = logo.resize((logo_w, logo_h), Image.Resampling.LANCZOS)
    im.paste(logo_r, (MARGIN, (header_h - logo_h) // 2), logo_r)
    d = ImageDraw.Draw(im)
    chip = spec["chip"]
    f_chip = font(22)
    cb = _ink_box(d, chip, f_chip)
    chip_w = (cb[2] - cb[0]) + 36
    chip_h = 44
    chip_x = W - MARGIN - chip_w
    chip_y = (header_h - chip_h) // 2
    chip_rect = (chip_x, chip_y, chip_x + chip_w, chip_y + chip_h)
    im = rounded(im, chip_rect, 6, PALE)
    d = ImageDraw.Draw(im)
    draw_block_centered(d, chip_rect, [chip], f_chip, BLUE)
    # Blue title band.
    band = (0, header_h, W, header_h + band_h)
    d.rectangle(band, fill=BLUE)
    cat_f = font(20)
    cy = header_h + 26
    d.text((MARGIN, cy), spec["cat"], font=cat_f, fill=LIGHT)
    ty = cy + 40
    for ln in title_lines:
        d.text((MARGIN, ty), ln, font=f_title, fill=WHITE)
        ty += 58
    sy = ty + 4
    for ln in sub_lines:
        d.text((MARGIN, sy), ln, font=f_sub, fill=(225, 238, 249))
        sy += 34

    y = header_h + band_h + 28
    vis = (MARGIN, y, MARGIN + CONTENT_W, y + visual_h)
    if photo is not None:
        im = paste_round(im, photo, vis, radius=16)
        d = ImageDraw.Draw(im)
    else:
        im = rounded(im, vis, 16, PALE, outline=LINE, width=2)
        d = ImageDraw.Draw(im)
        d.rectangle((vis[0], vis[1], vis[0] + 8, vis[3]), fill=BLUE)
        diagram = spec["diagram"]
        num_f = font(42)
        draw_line_in_rect(
            d,
            (vis[2] - 140, vis[3] - 78, vis[2] - 24, vis[3] - 18),
            diagram["number"],
            num_f,
            BLUE,
            align="right",
            pad=0,
        )
        title_f = font(36)
        lines = wrap(d, diagram["title"], title_f, CONTENT_W - 180)
        block_h = len(lines) * 48
        top = vis[1] + (visual_h - block_h - 40) // 2
        for i, ln in enumerate(lines):
            d.text((vis[0] + 40, top + i * 48), ln, font=title_f, fill=NAVY)
        sub_f = font(22)
        d.text((vis[0] + 40, top + block_h + 8), diagram["sub"], font=sub_f, fill=MUTED)
    y = vis[3]
    if cap_lines:
        y += 14
        for ln in cap_lines:
            d.text((MARGIN, y), ln, font=font(20), fill=MUTED)
            y += 28
        y += 8

    def section_pill(label, top):
        nonlocal im
        fnt = font(22)
        b = _ink_box(ImageDraw.Draw(im), label, fnt)
        pw = (b[2] - b[0]) + 36
        ph = 44
        rect = (MARGIN, top, MARGIN + pw, top + ph)
        im2 = rounded(im, rect, 5, BLUE)
        draw_block_centered(ImageDraw.Draw(im2), rect, [label], fnt, WHITE)
        return im2, top + ph, rect

    y += 26
    im, y, _ = section_pill(spec["design_label"], y)
    d = ImageDraw.Draw(im)
    y += 16
    stats = spec["stats"]
    gap = 18
    card_w = (CONTENT_W - gap * 2) // 3
    card_h = 156
    for i, (big, small) in enumerate(stats):
        x = MARGIN + i * (card_w + gap)
        rect = (x, y, x + card_w, y + card_h)
        im = rounded(im, rect, 10, WHITE, outline=LINE, width=2)
        d = ImageDraw.Draw(im)
        d.rectangle((x, y, x + card_w, y + 6), fill=BLUE)
        # Number + label centered as a group inside the card.
        bf = font(34)
        sf = font(20)
        small_lines = wrap(d, small, sf, card_w - 28)
        bb = _ink_box(d, big, bf)
        sh = sum((_ink_box(d, ln, sf)[3] - _ink_box(d, ln, sf)[1]) for ln in small_lines)
        sh += 4 * (len(small_lines) - 1)
        bh = bb[3] - bb[1]
        group = bh + 12 + sh
        gy = y + 6 + ((card_h - 6) - group) / 2
        draw_line_in_rect(d, (x, gy, x + card_w, gy + bh), big, bf, BLUE, align="left", pad=16)
        # The helper centers vertically in the given rect; pass a tight rect.
        ly = gy + bh + 12
        for ln in small_lines:
            lb = _ink_box(d, ln, sf)
            lh = lb[3] - lb[1]
            d.text((x + 16 - lb[0], ly - lb[1]), ln, font=sf, fill=MUTED)
            ly += lh + 4
    y += card_h + 28
    im, y, _ = section_pill(spec["key_label"], y)
    d = ImageDraw.Draw(im)
    y += 18

    deviations = []
    result = spec["result"]
    if result["type"] == "bars":
        max_v = max(result["values"])
        bar_max = 460
        row_h = 72
        vf = font(32)
        lf = font(22)
        for i, (label, value, text) in enumerate(zip(result["labels"], result["values"], result["texts"])):
            ry = y + i * row_h
            draw_line_in_rect(d, (MARGIN, ry, MARGIN + 210, ry + 48), label, lf, NAVY, align="left", pad=0)
            bw = max(24, round(bar_max * (value / max_v)))
            by = ry + 12
            d.rounded_rectangle((MARGIN + 220, by, MARGIN + 220 + bw, by + 26), radius=4, fill=BLUE if i == 0 else BAR_2)
            draw_line_in_rect(d, (W - MARGIN - 280, ry, W - MARGIN, ry + 48), text, vf, NAVY, align="right", pad=0)
        axis = result.get("axis")
        if axis:
            d.text((MARGIN + 220, y + row_h * 2 - 4), axis, font=font(18), fill=MUTED)
        y += row_h * len(result["labels"]) + 24
    elif result["type"] == "matrix":
        cells = result["cells"]
        cw = (CONTENT_W - 16) // 2
        ch = 86
        for i, (big, small) in enumerate(cells):
            col, row = i % 2, i // 2
            x = MARGIN + col * (cw + 16)
            ry = y + row * (ch + 12)
            rect = (x, ry, x + cw, ry + ch)
            im = rounded(im, rect, 8, PALE)
            d = ImageDraw.Draw(im)
            # Big value and label share the row and are each vertically centered.
            draw_line_in_rect(d, (x, ry, x + 210, ry + ch), big, font(30), BLUE, align="left", pad=16)
            draw_line_in_rect(d, (x + 220, ry, x + cw, ry + ch), small, font(20), MUTED, align="left", pad=8)
        rows = (len(cells) + 1) // 2
        y += rows * (ch + 12)
    elif result["type"] == "cards":
        cards = result["cards"]
        cw = (CONTENT_W - 18) // 2
        ch = 150
        for i, (big, small) in enumerate(cards):
            x = MARGIN + i * (cw + 18)
            rect = (x, y, x + cw, y + ch)
            im = rounded(im, rect, 10, PALE)
            d = ImageDraw.Draw(im)
            draw_block_centered(
                d,
                (x + 16, y + 12, x + cw - 16, y + ch - 12),
                [big, small],
                font(30),
                NAVY,
                gap=12,
            )
            # Recolor is unnecessary; both lines navy/blue via a second pass for the value.
            draw_line_in_rect(d, (x, y + 18, x + cw, y + 78), big, font(32), BLUE, align="center")
            small_lines = wrap(d, small, font(20), cw - 36)
            draw_block_centered(d, (x + 12, y + 78, x + cw - 12, y + ch - 10), small_lines, font(20), NAVY, gap=2)
        y += ch
    else:
        head_lines = wrap(d, result["headline"], font(36), CONTENT_W)
        for ln in head_lines:
            d.text((MARGIN, y), ln, font=font(36), fill=NAVY)
            y += 48
        y += 14
        chips = result["chips"]
        n = len(chips)
        gap = 14
        cw = (CONTENT_W - gap * (n - 1)) // n
        ch = 56
        fnt = font(20)
        # Shrink if any label does not fit.
        for label in chips:
            while fnt.size > 15 and _ink_box(d, label, fnt)[2] > cw - 20:
                fnt = font(fnt.size - 1)
        for i, label in enumerate(chips):
            x = MARGIN + i * (cw + gap)
            rect = (x, y, x + cw, y + ch)
            im = rounded(im, rect, 6, CHIP_BG)
            d = ImageDraw.Draw(im)
            lines = wrap(d, label, fnt, cw - 16)
            if len(lines) > 1:
                draw_block_centered(d, rect, lines, fnt, BLUE, gap=2)
            else:
                draw_block_centered(d, rect, [label], fnt, BLUE)
            deviations.append(chip_deviation(im, rect, CHIP_BG, BLUE))
        y += ch

    y += 22
    note_h = 24 + len(note_lines) * 34 + 20
    note_rect = (MARGIN, y, MARGIN + CONTENT_W, y + note_h)
    im = rounded(im, note_rect, 10, WHITE, outline=LINE, width=2)
    d = ImageDraw.Draw(im)
    ny = y + 16
    for ln in note_lines:
        d.text((MARGIN + 22, ny), ln, font=f_note, fill=TEXT)
        ny += 34
    y += note_h + 16
    bound_h = 20 + len(bound_lines) * 34 + 20
    bound_rect = (MARGIN, y, MARGIN + CONTENT_W, y + bound_h)
    im = rounded(im, bound_rect, 10, PALE)
    d = ImageDraw.Draw(im)
    d.rectangle((MARGIN, y, MARGIN + 8, y + bound_h), fill=BLUE)
    by = y + 16
    for ln in bound_lines:
        d.text((MARGIN + 26, by), ln, font=f_note, fill=TEXT)
        by += 34
    y += bound_h + 16
    src_h = 16 + len(src_wrapped) * 30 + 16
    src_rect = (MARGIN, y, MARGIN + CONTENT_W, y + src_h)
    im = rounded(im, src_rect, 8, PALE)
    d = ImageDraw.Draw(im)
    d.rectangle((MARGIN, y, MARGIN + 6, y + src_h), fill=BLUE)
    sy = y + 14
    for ln in src_wrapped:
        d.text((MARGIN + 22, sy), ln, font=src_font, fill=MUTED)
        sy += 30
    y += src_h + 22
    foot = spec["footer"]
    ff = font(18)
    fw = d.textlength(foot, font=ff)
    d.text(((W - fw) / 2, y), foot, font=ff, fill=FOOT)
    foot_box = _ink_box(d, foot, ff)
    bottom = int(y + (foot_box[3] - foot_box[1]) + 36)
    im = im.crop((0, 0, W, min(im.height, bottom)))

    if deviations:
        worst = max(deviations)
        if worst > 8:
            raise SystemExit(f"Chip text is off-center by {worst:.1f}px ({spec.get('chip')})")
        spec["_chip_dev"] = round(worst, 2)
    return im
