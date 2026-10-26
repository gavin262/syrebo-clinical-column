#!/usr/bin/env python3
"""Repair the Syrebo clinical column: citation links, cover fallback, posters.

Cover fallback
    Chinese pages keep assets/dayNN_cover.jpg.
    Every other locale uses assets/dayNN_cover_en.jpg when that file exists.
    Chinese is used only when it is the only cover for that issue.

Citation links
    DOI  -> https://doi.org/{doi}
    PMID -> https://pubmed.ncbi.nlm.nih.gov/{pmid}/
    PMCID -> https://pmc.ncbi.nlm.nih.gov/articles/{pmcid}/
    NCT -> https://clinicaltrials.gov/study/{nct}
    ChiCTR -> WHO ICTRP record for that registry id

    Issues that have no DOI on the page:
      06 Meng 2022 — journal abstract (no DOI assigned):
         http://hnzyydxxb.hnucm.edu.cn/hnzyydxxb/ch/reader/view_abstract.aspx?file_no=20220307
      09 Prabhu 2025 — journal article page. A DOI sometimes quoted
         (10.54839/ijprcp.v4i2.24.26) does not resolve and is not added.
         https://ijprcp.com/articles/rehabilitation-of-left-sided-hemiparesis-post-mca-infarction-using-faradic-electrical-stimulation-and-robotic-hand-rehabilitation-a-case-report
      11 Furudate 2023 — the page omitted the DOI; it is 10.7210/jrsj.41.331
         (J-STAGE). That DOI is inserted and linked. No search fallback.

Posters
    Non-English posters for issues 01–09 keep their type, drop the issue-number
    tag in the top banner (English posters already have none), and rebuild the
    photo band from the full product image so the device is not cropped.
    Issue 11's English poster photo is Sharma 2024 Figure 2 (CC BY 4.0).
"""

from __future__ import annotations

import re
import subprocess
import sys
from pathlib import Path

from PIL import Image, ImageDraw, ImageFilter, ImageFont

ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / "assets"

BRAND_BLUE = "#0050a0"
OLD_ACCENT = "#00b4a0"
OLD_NAV_LINK = "#bfe3de"
NEW_NAV_LINK = "#d5e4f7"

DOI_11 = "10.7210/jrsj.41.331"
MENG_URL = (
    "http://hnzyydxxb.hnucm.edu.cn/hnzyydxxb/ch/reader/view_abstract.aspx?file_no=20220307"
)
PRABHU_URL = (
    "https://ijprcp.com/articles/rehabilitation-of-left-sided-hemiparesis-post-mca-infarction-"
    "using-faradic-electrical-stimulation-and-robotic-hand-rehabilitation-a-case-report"
)
SHARMA_DOI = "10.7759/cureus.59314"
SHARMA_FIG = ASSETS / "day11_sharma2024_fig2.jpg"

SOURCE_PAGE = {
    "zh": "原文页面",
    "en": "Source page",
    "fr": "Page source",
    "es": "Página de la fuente",
    "pt": "Página da fonte",
    "nl": "Bronpagina",
    "it": "Pagina della fonte",
    "ro": "Pagina sursă",
    "tr": "Kaynak sayfası",
    "hr": "Izvorna stranica",
    "ru": "Страница источника",
    "lt": "Šaltinio puslapis",
    "id": "Halaman sumber",
    "ko": "원문 페이지",
    "th": "หน้าแหล่งที่มา",
    "hi": "स्रोत पृष्ठ",
}

DAY11_CAPTION = {
    "zh": "Sharma 等，Cureus 2024，图2：Syrebo 软体康复手套与主机（CC BY 4.0）。此图来自该病例报告，不是日本机器人学会综述的配图；综述未刊出手套照片。",
    "en": "Sharma et al., Cureus 2024, Figure 2: Syrebo soft robotic glove and console (CC BY 4.0). From that case report, not a figure in the Japanese review, which does not show the glove.",
    "fr": "Sharma et al., Cureus 2024, figure 2 : gant robotique souple Syrebo et console (CC BY 4.0). Photo issue de ce cas clinique, et non de la revue japonaise, qui ne montre pas le gant.",
    "es": "Sharma et al., Cureus 2024, figura 2: guante robótico blando Syrebo y consola (CC BY 4.0). Procede de ese informe de caso, no de la revisión japonesa, que no muestra el guante.",
    "pt": "Sharma et al., Cureus 2024, figura 2: luva robótica macia Syrebo e consola (CC BY 4.0). Imagem desse relato de caso, não da revisão japonesa, que não mostra a luva.",
    "nl": "Sharma et al., Cureus 2024, figuur 2: zachte robotische Syrebo-handschoen en console (CC BY 4.0). Uit dat casusverslag, niet uit de Japanse review, die de handschoen niet toont.",
    "it": "Sharma et al., Cureus 2024, figura 2: guanto robotico morbido Syrebo e console (CC BY 4.0). Da quel caso clinico, non dalla rassegna giapponese, che non mostra il guanto.",
    "ro": "Sharma et al., Cureus 2024, figura 2: mănușă robotică moale Syrebo și consolă (CC BY 4.0). Din acel raport de caz, nu din revista japoneză, care nu arată mănușa.",
    "tr": "Sharma et al., Cureus 2024, Şekil 2: Syrebo yumuşak robotik eldiven ve konsol (CC BY 4.0). Bu olgu sunumundan alınmıştır; eldiveni göstermeyen Japon derlemesinden değildir.",
    "hr": "Sharma et al., Cureus 2024, slika 2: meka robotska rukavica Syrebo i konzola (CC BY 4.0). Iz tog prikaza slučaja, a ne iz japanskog pregleda, koji ne prikazuje rukavicu.",
    "ru": "Sharma и соавт., Cureus, 2024, рис. 2: мягкая роботизированная перчатка Syrebo и консоль (CC BY 4.0). Из этого клинического случая, а не из японского обзора, где перчатка не показана.",
    "lt": "Sharma ir kt., Cureus, 2024, 2 pav.: minkšta robotinė Syrebo pirštinė ir pultas (CC BY 4.0). Iš to atvejo aprašymo, o ne iš japonų apžvalgos, kurioje pirštinė neparodyta.",
    "id": "Sharma dkk., Cureus 2024, Gambar 2: sarung tangan robotik lunak Syrebo dan konsol (CC BY 4.0). Dari laporan kasus itu, bukan dari tinjauan Jepang, yang tidak menampilkan sarung tangan.",
    "ko": "Sharma 등, Cureus 2024, 그림 2: Syrebo 소프트 로봇 장갑과 본체(CC BY 4.0). 이 증례 보고의 사진이며, 장갑을 보여 주지 않는 일본 학회 종설의 그림이 아닙니다.",
    "th": "Sharma และคณะ, Cureus 2024, รูปที่ 2: ถุงมือหุ่นยนต์แบบนิ่ม Syrebo และคอนโซล (CC BY 4.0) ภาพจากรายงานผู้ป่วยรายนี้ ไม่ใช่รูปจากบทความทบทวนของญี่ปุ่น ซึ่งไม่ได้แสดงถุงมือ",
    "hi": "Sharma et al., Cureus 2024, चित्र 2: Syrebo सॉफ्ट रोबोटिक दस्ताना और कंसोल (CC BY 4.0)। यह उस केस रिपोर्ट से है, जापानी समीक्षा से नहीं, जिसमें दस्ताना नहीं दिखाया गया है।",
}

POSTER_CAPTION = (
    "Syrebo glove and console — Sharma et al., Cureus 2024, Fig. 2 (CC BY 4.0).\n"
    "Not a figure from the Japanese review; that paper does not show the glove."
)

LATIN_FONT = "/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf"


def lang_of(path: Path) -> str:
    rel = path.relative_to(ROOT)
    if rel.parts[0] == "poster":
        return "zh"
    if len(rel.parts) > 1 and rel.parts[0] != "assets":
        return rel.parts[0]
    return "zh"


def html_escape(text: str) -> str:
    return (
        text.replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
        .replace('"', "&quot;")
    )


def link_token(prefix: str, label: str, href: str) -> str:
    return (
        f'{prefix}<a href="{href}" rel="noopener noreferrer">{html_escape(label)}</a>'
    )


def strip_tail(token: str) -> tuple[str, str]:
    m = re.match(r"^(.*?)([。.)），,;；、]+)$", token)
    if m:
        return m.group(1), m.group(2)
    return token, ""


# DOI suffix stops before CJK punctuation such as （ so a following PMID is not swallowed.
DOI_BODY = r"10\.\d{4,9}/[A-Za-z0-9.\-_()/:]+"


def sub_outside_tags(text: str, pattern: str, repl, flags: int = 0) -> str:
    """Apply repl only to text nodes so new anchors are not nested or rewritten."""
    parts = re.split(r"(<[^>]+>)", text)
    return "".join(
        part if part.startswith("<") else re.sub(pattern, repl, part, flags=flags)
        for part in parts
    )


def linkify_plain(text: str) -> str:
    def doi(m: re.Match) -> str:
        core, tail = strip_tail(m.group(2))
        return link_token(m.group(1), core, f"https://doi.org/{core}") + tail

    def pmid(m: re.Match) -> str:
        return link_token(m.group(1), m.group(2), f"https://pubmed.ncbi.nlm.nih.gov/{m.group(2)}/")

    def pmcid(m: re.Match) -> str:
        return link_token(
            m.group(1), m.group(2), f"https://pmc.ncbi.nlm.nih.gov/articles/{m.group(2)}/"
        )

    def nct(m: re.Match) -> str:
        return link_token("", m.group(1), f"https://clinicaltrials.gov/study/{m.group(1)}")

    def chictr(m: re.Match) -> str:
        return link_token(
            "",
            m.group(1),
            f"https://trialsearch.who.int/Trial2.aspx?TrialID={m.group(1)}",
        )

    text = sub_outside_tags(text, rf"(DOI\s*[:：]\s*)({DOI_BODY})", doi, flags=re.I)
    text = sub_outside_tags(text, r"(PMID\s*[:：]\s*)(\d{5,9})", pmid)
    text = sub_outside_tags(text, r"(PMCID\s*[:：]\s*)(PMC\d+)", pmcid)
    text = sub_outside_tags(text, r"\b(NCT\d{8})\b", nct)
    text = sub_outside_tags(text, r"\b(ChiCTR\d+)\b", chictr)
    return text


def linkify_html_fragment(fragment: str) -> str:
    return linkify_plain(fragment)


def ensure_issue11_doi(inner: str) -> str:
    if DOI_11 in inner:
        return inner
    inner = inner.rstrip()
    if not inner.endswith((".", "。", ")", "）")):
        inner += "."
    return inner + f" DOI: {DOI_11}."


def fallback_link(lang: str, url: str) -> str:
    label = SOURCE_PAGE.get(lang, SOURCE_PAGE["en"])
    return f' <a href="{url}" rel="noopener noreferrer">{html_escape(label)}</a>'


def process_html(path: Path) -> bool:
    original = path.read_text(encoding="utf-8")
    html = original
    lang = lang_of(path)
    issue = None
    m = re.search(r"day(\d{2})\.html$", path.name)
    if m:
        issue = m.group(1)

    def rewrite_source(match: re.Match) -> str:
        inner = match.group(1)
        if issue == "11":
            inner = ensure_issue11_doi(inner)
        inner = linkify_html_fragment(inner)
        if "doi.org" not in inner and "http" not in inner.lower():
            if issue == "06":
                inner = inner.rstrip() + fallback_link(lang, MENG_URL)
            elif issue == "09":
                inner = inner.rstrip() + fallback_link(lang, PRABHU_URL)
        return f'<div class="source">{inner}</div>'

    html = re.sub(
        r'<div class="source">(.*?)</div>',
        rewrite_source,
        html,
        flags=re.S,
    )

    if lang != "zh":
        html = re.sub(r"day(\d{2})_cover\.jpg", lambda m: (
            f"day{m.group(1)}_cover_en.jpg"
            if (ASSETS / f"day{m.group(1)}_cover_en.jpg").exists()
            else m.group(0)
        ), html)

    html = re.sub(r"C[\-‐‑–—]12", "C12", html)

    if issue == "11" and "day11_product.jpg" in html and lang in DAY11_CAPTION:
        caption = DAY11_CAPTION[lang]
        alt = html_escape(caption)
        visible = html_escape(caption) + (
            f' <a href="https://doi.org/{SHARMA_DOI}" rel="noopener noreferrer">{SHARMA_DOI}</a>'
        )
        # depth: lang/day11.html -> ../assets ; anything else unexpected keeps relative
        prefix = "../" if path.parent != ROOT else ""
        html = re.sub(
            r'<img class="product" src="[^"]*day11_product\.jpg" alt="[^"]*">\s*<div class="cap">.*?</div>',
            (
                f'<img class="product" src="{prefix}assets/day11_sharma2024_fig2.jpg" alt="{alt}">\n'
                f'<div class="cap">{visible}</div>'
            ),
            html,
            count=1,
            flags=re.S,
        )

    sibling_10 = path.parent / "day10.html"
    if sibling_10.exists() and 'href="day10.html"' not in html:
        html = html.replace(
            'day09.html">09</a>',
            'day09.html">09</a><a href="day10.html">10</a><a href="day11.html">11</a>',
            1,
        )

    html = html.replace(OLD_ACCENT, BRAND_BLUE).replace(OLD_NAV_LINK, NEW_NAV_LINK)

    if "p.limit{" not in html and "</style>" in html:
        html = html.replace(
            "</style>",
            "p.limit{font-size:13.5px;color:#5c6b70;line-height:1.65}\n"
            ".source a{color:#0050a0;font-weight:600}\n"
            "</style>",
            1,
        )
    # Limitation note: drop a heading that sits immediately above it, and
    # set the note itself in small type. [^<] keeps this from swallowing
    # earlier sections.
    html = re.sub(
        r"<h2>[^<]*</h2>\s*<p>([^<]*)</p>(\s*)<div class=\"source\">",
        r'<p class="limit">\1</p>\2<div class="source">',
        html,
        count=1,
    )
    html = re.sub(
        r"<p>([^<]*)</p>(\s*)<div class=\"source\">",
        r'<p class="limit">\1</p>\2<div class="source">',
        html,
        count=1,
    )

    if html != original:
        path.write_text(html, encoding="utf-8")
        return True
    return False


def row_fractions(im: Image.Image, y: int) -> tuple[float, float]:
    w, _ = im.size
    px = im.load()
    white = teal = n = 0
    for x in range(0, w, 2):
        r, g, b = px[x, y]
        n += 1
        if r > 245 and g > 245 and b > 245:
            white += 1
        if r < 50 and 40 < g < 130 and 60 < b < 140:
            teal += 1
    return white / n, teal / n


def find_photo_span(im: Image.Image) -> tuple[int, int] | None:
    """Photo band between the teal title and the white body copy.

    Body text is mostly white but not a solid 0.97, and some photos contain a
    bright screen, so the end is the first sustained rise in smoothed whiteness
    after a non-white photo — not the last near-white row on the page.
    """
    _, h = im.size
    whites: list[float] = []
    teals: list[float] = []
    for y in range(h):
        white, teal = row_fractions(im, y)
        whites.append(white)
        teals.append(teal)
    teal_end = None
    seen = False
    for y in range(80, min(h - 1, 900)):
        if teals[y] > 0.4:
            seen = True
            teal_end = y
        elif seen and teal_end is not None and y > teal_end + 15:
            break
    if teal_end is None:
        return None
    y = teal_end + 1
    while y < h - 40 and whites[y] > 0.9:
        y += 1
    photo_start = y

    def smooth(i: int) -> float:
        window = whites[i:i + 8]
        return sum(window) / len(window)

    run = 0
    photo_end = None
    for y in range(photo_start + 50, h - 8):
        if smooth(y) > 0.82:
            run += 1
            if run >= 8:
                photo_end = y - 8
                break
        else:
            run = 0
    if photo_end is None:
        return None
    height = photo_end - photo_start
    if not (200 < photo_start < 750 and 120 < height < 980):
        return None
    if photo_end > h - 60:
        return None
    return photo_start, photo_end


def contain(product: Image.Image, slot_w: int, slot_h: int) -> Image.Image:
    if product.mode == "RGBA":
        base = Image.new("RGB", product.size, (255, 255, 255))
        base.paste(product, mask=product.split()[-1])
        product = base
    else:
        product = product.convert("RGB")
    canvas = Image.new("RGB", (slot_w, slot_h), (255, 255, 255))
    scale = min(slot_w / product.width, slot_h / product.height)
    nw, nh = max(1, int(product.width * scale)), max(1, int(product.height * scale))
    resized = product.resize((nw, nh), Image.Resampling.LANCZOS)
    canvas.paste(resized, ((slot_w - nw) // 2, (slot_h - nh) // 2))
    return canvas


def clear_issue_tag(im: Image.Image) -> int:
    """Whiten the top-banner issue tag. The logo sits at x<340 and is kept."""
    px = im.load()
    w, _ = im.size
    hits = []
    for y in range(28, 118):
        for x in range(360, w - 4):
            r, g, b = px[x, y]
            if r < 165 and g < 185 and b < 205:
                hits.append((x, y))
    if len(hits) < 40:
        return 0
    xs = [p[0] for p in hits]
    ys = [p[1] for p in hits]
    x0, x1 = max(360, min(xs) - 3), min(w - 2, max(xs) + 3)
    y0, y1 = max(20, min(ys) - 3), min(125, max(ys) + 3)
    cleared = 0
    for y in range(y0, y1 + 1):
        for x in range(x0, x1 + 1):
            r, g, b = px[x, y]
            if r < 230 or g < 230 or b < 230:
                px[x, y] = (255, 255, 255)
                cleared += 1
    return cleared


def product_for(day: str) -> Path | None:
    for ext in (".jpg", ".png", ".jpeg"):
        p = ASSETS / f"day{day}_product{ext}"
        if p.exists():
            return p
    return None


def rebuild_poster(path: Path, day: str) -> str:
    im = Image.open(path).convert("RGB")
    cleared = clear_issue_tag(im)
    span = find_photo_span(im)
    if span is None:
        if cleared:
            im.save(path, quality=92, optimize=True)
            return f"tag-only ({cleared}px)"
        return "SKIP no photo span"
    photo_start, photo_end = span
    prod_path = product_for(day)
    if prod_path is None:
        return "SKIP no product"
    product = Image.open(prod_path)
    aspect_h = round(im.width * product.height / product.width)
    # At least as tall as the English poster photo, and tall enough to show
    # the whole product without cropping.
    en_path = ASSETS / f"day{day}_poster_en.jpg"
    en_h = 0
    if en_path.exists() and en_path.resolve() != path.resolve():
        en_span = find_photo_span(Image.open(en_path).convert("RGB"))
        if en_span:
            en_h = en_span[1] - en_span[0]
    target_h = max(aspect_h, en_h, photo_end - photo_start)
    slot = contain(product, im.width, target_h)
    top = im.crop((0, 0, im.width, photo_start))
    bottom = im.crop((0, photo_end, im.width, im.height))
    out = Image.new("RGB", (im.width, top.height + target_h + bottom.height), (255, 255, 255))
    out.paste(top, (0, 0))
    out.paste(slot, (0, photo_start))
    out.paste(bottom, (0, photo_start + target_h))
    if day == "09":
        out = fix_c12_title(out)
    out.save(path, quality=92, optimize=True)
    return (
        f"photo {photo_end-photo_start}px -> {target_h}px, "
        f"canvas {im.height} -> {out.height}, tag {cleared}"
    )


def ocr_tsv(im: Image.Image) -> str:
    tmp = Path("/tmp/poster_ocr.png")
    im.save(tmp)
    proc = subprocess.run(
        ["tesseract", str(tmp), "stdout", "-l", "eng+chi_sim", "--psm", "6", "tsv"],
        capture_output=True,
        text=True,
    )
    return proc.stdout


def fix_c12_title(im: Image.Image) -> Image.Image:
    """Turn a burned-in C-12 title into C12 by deleting the hyphen stroke."""
    w, _ = im.size
    band = im.crop((0, 100, w, 460))
    tsv = ocr_tsv(band)
    im = im.copy()
    px = im.load()
    for line in tsv.splitlines()[1:]:
        cols = line.split("\t")
        if len(cols) < 12:
            continue
        text = cols[11]
        if not re.search(r"C[\-–—]12", text):
            continue
        left, top, width, height = map(int, cols[6:10])
        # band offset
        left += 0
        top += 100
        box = (max(0, left - 4), max(0, top - 4), min(w, left + width + 12), top + height + 8)
        crop = im.crop(box)
        fixed = _collapse_hyphen(crop)
        if fixed is not None:
            im.paste(fixed, box[:2])
    return im


def _collapse_hyphen(crop: Image.Image) -> Image.Image | None:
    crop = crop.convert("RGB")
    px = crop.load()
    W, H = crop.size
    # Decide polarity from the median of non-extreme pixels.
    sample = [px[x, y] for y in range(0, H, 2) for x in range(0, W, 3)]
    lum = sorted((r + g + b) / 3 for r, g, b in sample)
    mid = lum[len(lum) // 2]
    light_text = mid < 140  # teal background, white glyphs

    def is_ink(rgb: tuple[int, int, int]) -> bool:
        r, g, b = rgb
        if light_text:
            return (r + g + b) > 580
        return (r + g + b) < 280 and max(r, g, b) < 140

    cols = []
    for x in range(W):
        n = sum(1 for y in range(H) if is_ink(px[x, y]))
        cols.append(n)
    clusters = []
    inb = False
    for i, n in enumerate(cols):
        if n > 0 and not inb:
            s = i
            inb = True
            mx = n
        elif n > 0 and inb:
            mx = max(mx, n)
        elif n == 0 and inb:
            clusters.append((s, i - 1, mx))
            inb = False
    if inb:
        clusters.append((s, W - 1, mx))
    hy_i = None
    for i, cl in enumerate(clusters[1:], start=1):
        if cl[2] <= max(8, H // 6) and (cl[1] - cl[0]) < 22:
            hy_i = i
            break
    if hy_i is None or hy_i + 1 >= len(clusters):
        return None
    if light_text:
        bg = (15, 74, 90)
        for y in range(H):
            for x in range(W):
                r, g, b = px[x, y]
                if r < 45 and 50 < g < 110 and 70 < b < 120:
                    bg = (r, g, b)
                    break
            else:
                continue
            break
    else:
        bg = (255, 255, 255)
    src = clusters[hy_i + 1][0]
    dst = clusters[0][1] + 2
    if src <= dst:
        return None
    new = Image.new("RGB", (W, H), bg)
    new.paste(crop.crop((0, 0, dst, H)), (0, 0))
    new.paste(crop.crop((src, 0, W, H)), (dst, 0))
    return new


def rewrite_day11_poster(path: Path) -> str:
    im = Image.open(path).convert("RGB")
    span = find_photo_span(im)
    if span is None:
        return "SKIP no photo span"
    photo_start, photo_end = span
    product = Image.open(SHARMA_FIG)
    target_h = max(720, photo_end - photo_start)
    slot = contain(product, im.width, target_h)
    top = im.crop((0, 0, im.width, photo_start))
    bottom = im.crop((0, photo_end, im.width, im.height))
    out = Image.new("RGB", (im.width, top.height + target_h + bottom.height), (255, 255, 255))
    out.paste(top, (0, 0))
    out.paste(slot, (0, photo_start))
    caption_top = photo_start + target_h
    out.paste(bottom, (0, caption_top))
    _repaint_day11_caption(out, caption_top)
    out.save(path, quality=92, optimize=True)
    return f"sharma fig2 into {target_h}px slot, canvas {out.height}"


def _repaint_day11_caption(im: Image.Image, caption_top: int) -> None:
    """Cover the old mirror-scene caption and write an accurate one."""
    w, _ = im.size
    band_h = 210
    band = im.crop((0, caption_top, w, min(im.height, caption_top + band_h)))
    tsv = ocr_tsv(band)
    draw = ImageDraw.Draw(im)
    boxes = []
    for line in tsv.splitlines()[1:]:
        cols = line.split("\t")
        if len(cols) < 12:
            continue
        text = cols[11].strip()
        if not text or float(cols[10]) < 0:
            continue
        if re.search(r"mirror|glove|home|training|setup|scene", text, re.I):
            left, top, width, height = map(int, cols[6:10])
            boxes.append((left, caption_top + top, left + width, caption_top + top + height))
    if boxes:
        x0 = min(b[0] for b in boxes) - 8
        y0 = min(b[1] for b in boxes) - 6
        x1 = max(b[2] for b in boxes) + 8
        y1 = max(b[3] for b in boxes) + 10
    else:
        # Caption sits in the first text block under the photo; cover a safe band.
        x0, y0, x1, y1 = 40, caption_top + 8, w - 40, caption_top + 120
    draw.rectangle((max(0, x0), max(0, y0), min(w, x1), y1), fill=(255, 255, 255))
    font = ImageFont.truetype(LATIN_FONT, 26)
    color = (90, 104, 110)
    y = y0 + 8
    for line in POSTER_CAPTION.split("\n"):
        draw.text((56, y), line, font=font, fill=color)
        y += 36


def poster_paths() -> list[tuple[Path, str]]:
    found = []
    for path in sorted(ASSETS.glob("day??_poster*.jpg")):
        m = re.match(r"day(\d{2})_poster(?:_([a-z]{2}))?\.jpg$", path.name)
        if not m:
            continue
        day, lang = m.group(1), m.group(2) or "zh"
        found.append((path, day, lang))
    return found


def main() -> None:
    check = "--check" in sys.argv
    do_html = "--html" in sys.argv or "--all" in sys.argv
    do_posters = "--posters" in sys.argv or "--all" in sys.argv
    if not check and not do_html and not do_posters:
        print("usage: fix_clinical_column.py --html | --posters | --all | --check")
        print("--posters is not idempotent; it was applied once to enlarge photo bands.")
        return
    html_changed = 0
    if do_html and not check:
        for path in sorted(ROOT.rglob("*.html")):
            if process_html(path):
                html_changed += 1
        print(f"html updated: {html_changed}")

    if not do_posters and not check:
        return

    for path, day, lang in poster_paths():
        if day == "11" and lang == "en":
            if check:
                im = Image.open(path).convert("RGB")
                print(f"CHECK {path.name} span={find_photo_span(im)}")
                continue
            print(f"{path.name}: {rewrite_day11_poster(path)}")
            continue
        if lang == "en":
            # English posters already omit the issue tag and show the product.
            # Still repair a burned-in C-12 in the title.
            if day == "09" and not check:
                im = fix_c12_title(Image.open(path).convert("RGB"))
                im.save(path, quality=92, optimize=True)
                print(f"{path.name}: C12 title")
            elif check and day == "09":
                print(f"CHECK {path.name} c12-only")
            continue
        if day not in {f"{n:02d}" for n in range(1, 10)}:
            continue
        if check:
            im = Image.open(path).convert("RGB")
            print(f"CHECK {path.name} span={find_photo_span(im)}")
            continue
        print(f"{path.name}: {rebuild_poster(path, day)}")

    if do_posters and not check:
        for cover in sorted(ASSETS.glob("day09_cover*.jpg")):
            im = fix_c12_title(Image.open(cover).convert("RGB"))
            im.save(cover, quality=92, optimize=True)
            print(f"{cover.name}: C12 title")
        old = ASSETS / "day11_product.jpg"
        if old.exists():
            old.unlink()
            print("removed day11_product.jpg")


if __name__ == "__main__":
    main()
