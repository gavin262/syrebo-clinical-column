#!/usr/bin/env python3
"""Round 3: realign poster label pills, drop foreign subtitles, add excerpts.

Pill labels are baked into poster JPEGs. The blue chip sits above the glyphs.
This recenters each left-hand chip on its glyphs. Non-English posters and the
Chinese covers also carry an English subtitle on the blue title band; that line
is painted out. Article pages gain a bibliographic excerpt card. Figures are
embedded only when the paper's license allows commercial reuse (CC BY).
"""

from __future__ import annotations

import html
import re
import subprocess
from pathlib import Path

import numpy as np
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / "assets"
BLUE = np.array([0, 80, 160], dtype=np.int16)
BLUE_T = (0, 80, 160)
FONT_CJK = "/usr/share/fonts/truetype/wqy/wqy-microhei.ttc"
FUNC = {
    "a", "an", "the", "in", "of", "for", "and", "from", "with", "on", "to",
    "among", "after", "new", "versus", "vs", "by", "into", "over",
}

LANGS = [
    "zh", "en", "fr", "es", "pt", "nl", "it", "ro", "tr", "hr",
    "ru", "lt", "id", "ko", "th", "hi",
]

KICKER = {
    "zh": "文献摘录",
    "en": "From the paper",
    "fr": "Extrait de l'article",
    "es": "Del artículo",
    "pt": "Do artigo",
    "nl": "Uit het artikel",
    "it": "Dal articolo",
    "ro": "Din articol",
    "tr": "Makaleden",
    "hr": "Iz članka",
    "ru": "Из статьи",
    "lt": "Iš straipsnio",
    "id": "Dari artikel",
    "ko": "논문 원문",
    "th": "จากบทความ",
    "hi": "लेख से",
}
CAP_PAGE = {
    "zh": "论文首页题录截图，取自开放获取版本（{lic}）。",
    "en": "Bibliographic crop of the open-access first page ({lic}).",
    "fr": "Extrait bibliographique de la première page en accès ouvert ({lic}).",
    "es": "Recorte bibliográfico de la primera página en acceso abierto ({lic}).",
    "pt": "Recorte bibliográfico da primeira página em acesso aberto ({lic}).",
    "nl": "Bibliografische uitsnede van de open-access eerste pagina ({lic}).",
    "it": "Ritaglio bibliografico della prima pagina ad accesso aperto ({lic}).",
    "ro": "Decupaj bibliografic al primei pagini cu acces deschis ({lic}).",
    "tr": "Açık erişimli ilk sayfanın bibliyografik kırpımı ({lic}).",
    "hr": "Bibliografski isječak naslovnice iz otvorenog pristupa ({lic}).",
    "ru": "Библиографический фрагмент первой страницы открытой статьи ({lic}).",
    "lt": "Atvirosios prieigos pirmo puslapio bibliografinis fragmentas ({lic}).",
    "id": "Potongan bibliografi halaman pertama akses terbuka ({lic}).",
    "ko": "오픈액세스 논문 첫 페이지의 서지 영역 ({lic}).",
    "th": "ส่วนบรรณานุกรมจากหน้าแรกของบทความแบบเปิด ({lic}).",
    "hi": "ओपन-एक्सेस प्रथम पृष्ठ का ग्रंथपरक अंश ({lic}).",
}
CAP_FIG = {
    "zh": "论文图2：软体康复手套与主机。取自开放获取病例报告（{lic}），画面未改。",
    "en": "Figure 2 from the case report: soft rehabilitation glove and console. Reproduced unchanged from the open-access article ({lic}).",
    "fr": "Figure 2 du cas clinique : gant de rééducation souple et console. Reproduite sans modification depuis l'article en accès ouvert ({lic}).",
    "es": "Figura 2 del caso clínico: guante de rehabilitación blando y consola. Reproducida sin cambios desde el artículo en acceso abierto ({lic}).",
    "pt": "Figura 2 do relato de caso: luva de reabilitação macia e consola. Reproduzida sem alterações a partir do artigo em acesso aberto ({lic}).",
    "nl": "Figuur 2 uit het casusverslag: zachte revalidatiehandschoen en console. Ongewijzigd overgenomen uit het open-access artikel ({lic}).",
    "it": "Figura 2 del caso clinico: guanto morbido e console. Riprodotta senza modifiche dall'articolo ad accesso aperto ({lic}).",
    "ro": "Figura 2 din raportul de caz: mănușă moale de reabilitare și consolă. Reprodusă neschimbată din articolul cu acces deschis ({lic}).",
    "tr": "Olgu raporunun Şekil 2'si: yumuşak rehabilitasyon eldiveni ve konsol. Açık erişimli makaleden değiştirilmeden alınmıştır ({lic}).",
    "hr": "Slika 2 iz prikaza slučaja: meka rehabilitacijska rukavica i konzola. Preneseno bez izmjena iz članka u otvorenom pristupu ({lic}).",
    "ru": "Рис. 2 из описания случая: мягкая реабилитационная перчатка и консоль. Воспроизведено без изменений из статьи открытого доступа ({lic}).",
    "lt": "2 pav. iš atvejo aprašymo: minkšta reabilitacijos pirštinė ir pultas. Perkelta nepakeista iš atvirosios prieigos straipsnio ({lic}).",
    "id": "Gambar 2 dari laporan kasus: sarung tangan rehabilitasi lunak dan konsol. Diproduksi ulang tanpa perubahan dari artikel akses terbuka ({lic}).",
    "ko": "증례 보고의 그림 2: 소프트 재활 장갑과 본체. 오픈액세스 논문에서 수정 없이 옮김 ({lic}).",
    "th": "รูปที่ 2 จากรายงานผู้ป่วย: ถุงมือฟื้นฟูแบบนิ่มและคอนโซล นำมาจากบทความแบบเปิดโดยไม่ดัดแปลง ({lic}).",
    "hi": "केस रिपोर्ट की आकृति 2: सॉफ्ट पुनर्वास दस्ताना और कंसोल। ओपन-एक्सेस लेख से बिना बदलाव के ({lic}).",
}
LINK = {
    "zh": "查看出处",
    "en": "View source",
    "fr": "Voir la source",
    "es": "Ver la fuente",
    "pt": "Ver a fonte",
    "nl": "Bekijk de bron",
    "it": "Vedi la fonte",
    "ro": "Vezi sursa",
    "tr": "Kaynağı gör",
    "hr": "Vidi izvor",
    "ru": "Открыть источник",
    "lt": "Atidaryti šaltinį",
    "id": "Lihat sumber",
    "ko": "출처 보기",
    "th": "ดูแหล่งที่มา",
    "hi": "स्रोत देखें",
}
ALT_COVER = {
    "zh": "封面", "en": "Cover", "fr": "Couverture", "es": "Portada", "pt": "Capa",
    "nl": "Omslag", "it": "Copertina", "ro": "Copertă", "tr": "Kapak",
    "hr": "Naslovnica", "ru": "Обложка", "lt": "Viršelis", "id": "Sampul",
    "ko": "표지", "th": "หน้าปก", "hi": "कवर",
}
ALT_POSTER = {
    "zh": "海报", "en": "Poster", "fr": "Affiche", "es": "Póster", "pt": "Pôster",
    "nl": "Poster", "it": "Poster", "ro": "Afiș", "tr": "Poster",
    "hr": "Poster", "ru": "Постер", "lt": "Plakatas", "id": "Poster",
    "ko": "포스터", "th": "โปสเตอร์", "hi": "पोस्टर",
}
FIG_ALT = {
    "zh": "论文图：软体康复手套与主机",
    "en": "Paper figure: soft rehabilitation glove and console",
    "fr": "Figure de l'article : gant souple et console",
    "es": "Figura del artículo: guante blando y consola",
    "pt": "Figura do artigo: luva macia e consola",
    "nl": "Figuur uit het artikel: zachte handschoen en console",
    "it": "Figura dell'articolo: guanto morbido e console",
    "ro": "Figura din articol: mănușă moale și consolă",
    "tr": "Makale şekli: yumuşak eldiven ve konsol",
    "hr": "Slika iz članka: meka rukavica i konzola",
    "ru": "Рисунок из статьи: мягкая перчатка и консоль",
    "lt": "Paveikslas iš straipsnio: minkšta pirštinė ir pultas",
    "id": "Gambar artikel: sarung tangan lunak dan konsol",
    "ko": "논문 그림: 소프트 장갑과 본체",
    "th": "รูปจากบทความ: ถุงมือนิ่มและคอนโซล",
    "hi": "लेख की आकृति: सॉफ्ट दस्ताना और कंसोल",
}

# image: path relative to assets/, or None. license shown to readers when an image is embedded.
PAPERS = [
    {
        "n": 1,
        "authors": "Sunnetci MA, Menek B",
        "title": "Effects of robotic hand-assisted rehabilitation on motor function and daily living activities in acute stroke: a randomized controlled trial",
        "venue": "Scientific Reports, 2026",
        "href": "https://doi.org/10.1038/s41598-025-32258-6",
        "ids": "DOI: 10.1038/s41598-025-32258-6 · NCT06805955",
        "image": None,
        "why": "CC BY-NC-ND 4.0. A commercial column cannot reuse the figure.",
    },
    {
        "n": 2,
        "authors": "Abdelraouf OR, et al.",
        "title": "Soft robotic gloves versus mirror therapy: a long-term comparative study on hand function and motor recovery in post-stroke rehabilitation",
        "venue": "Journal of Rehabilitation Medicine, 2025",
        "href": "https://doi.org/10.2340/jrm.v57.43482",
        "ids": "DOI: 10.2340/jrm.v57.43482 · PMID: 40874348 · NCT05898971",
        "image": "excerpt_day02_jrm.jpg",
        "lic": "CC BY 4.0",
        "kind": "page",
        "why": "CC BY 4.0. First-page header crop (title and authors).",
    },
    {
        "n": 3,
        "authors": "Woo JJ, Kwon JS",
        "title": "Effects of Robotic Mirroring Training and Mirror Therapy with Robot on Unilateral Neglect, Depression, and Activities of Daily Living Among Patients with Subacute Stroke",
        "venue": "NeuroRehabilitation, 2025",
        "href": "https://doi.org/10.1177/10538135251382902",
        "ids": "DOI: 10.1177/10538135251382902 · PMID: 41092018",
        "image": None,
        "why": "Closed access (Unpaywall). Text only; 待确认授权 for any figure.",
    },
    {
        "n": 4,
        "authors": "Abd Elhady AS, Ahmed GM, Hassan A, Ibrahim SM, Abdelmageed SM",
        "title": "Efficacy of robotic training gloves in improving hand function and movement in stroke patients",
        "venue": "SPORT TK-EuroAmerican Journal of Sport Sciences, 2025, 14, Article 40",
        "href": "https://doi.org/10.6018/sportk.660321",
        "ids": "DOI: 10.6018/sportk.660321",
        "image": None,
        "why": "CC BY-NC-ND 4.0. Figure not embedded.",
    },
    {
        "n": 5,
        "authors": "Lin Y, Wang C, Yin G, et al.",
        "title": "Feasibility and preliminary efficacy of a soft robotic glove for hand rehabilitation in early subacute stroke: a pilot investigation",
        "venue": "BioMedical Engineering OnLine, 2026",
        "href": "https://doi.org/10.1186/s12938-026-01614-6",
        "ids": "DOI: 10.1186/s12938-026-01614-6 · ChiCTR2000034614",
        "image": None,
        "why": "CC BY 4.0 confirmed, but the publisher PDF is behind a bot challenge here, so no crop was saved.",
    },
    {
        "n": 6,
        "authors": "孟灵、杨松、钟青华、王瑞安、林伟弟、尹刚刚、常小荣、蒋学余",
        "title": "康复机器人手套结合电针治疗痰瘀阻络型脑卒中手功能障碍患者的临床研究",
        "venue": "湖南中医药大学学报, 2022, 42(3): 387-392",
        "href": "http://hnzyydxxb.hnucm.edu.cn/hnzyydxxb/ch/reader/view_abstract.aspx?file_no=20220307",
        "ids": "湖南中医药大学学报, 2022",
        "image": None,
        "why": "Abstract page only. License not stated. 待确认授权.",
    },
    {
        "n": 7,
        "authors": "Sharma VS, Sharath HV, Sasun AR",
        "title": "Effectiveness of Syrebo's Glove Rehabilitation Program in a Patient With Middle Cerebral Artery Infarct: A Case Report",
        "venue": "Cureus, 2024, 16(4): e59314",
        "href": "https://doi.org/10.7759/cureus.59314",
        "ids": "DOI: 10.7759/cureus.59314 · PMID: 38817453 · PMC11136872",
        "image": "day11_sharma2024_fig2.jpg",
        "lic": "CC BY 4.0",
        "kind": "fig",
        "why": "CC BY 4.0. Existing Figure 2 (glove and console), already in the repo.",
    },
    {
        "n": 8,
        "authors": "陈涛、刘沙鑫、陈雪莲、毛磊、李德波、甘林玉",
        "title": "创新式镜像疗法对脑卒中患者上肢功能障碍的康复效果",
        "venue": "新医学, 2024, 55(6): 397-402",
        "href": "https://cjournal.hep.com.cn/0253-9802/CN/1207256030272373518",
        "ids": "DOI: 10.3969/j.issn.0253-9802.2024.06.001",
        "image": None,
        "why": "Chinese journal page. Reuse terms not stated. 待确认授权.",
    },
    {
        "n": 9,
        "authors": "Prabhu C, Mohan P, Sajjana D",
        "title": "Rehabilitation of Left-Sided Hemiparesis Post-MCA Infarction Using Faradic Electrical Stimulation and Robotic Hand Rehabilitation: A Case Report",
        "venue": "International Journal of Physiotherapy Research and Clinical Practice, 2025, 4(2): 27-30",
        "href": "https://ijprcp.com/articles/rehabilitation-of-left-sided-hemiparesis-post-mca-infarction-using-faradic-electrical-stimulation-and-robotic-hand-rehabilitation-a-case-report",
        "ids": "IJPRCP, 2025, 4(2): 27-30",
        "image": None,
        "why": "Journal page does not state a reuse license. 待确认授权.",
    },
    {
        "n": 10,
        "authors": "Ledoux ED, Barth EJ",
        "title": "Design, modeling, and preliminary evaluation of a 3D-printed wrist-hand grasping orthosis for stroke survivors",
        "venue": "Wearable Technologies, 2024; 5: e12",
        "href": "https://doi.org/10.1017/wtc.2024.18",
        "ids": "DOI: 10.1017/wtc.2024.18 · PMID: 39575325 · PMC11579884",
        "image": "excerpt_day10_ledoux.jpg",
        "lic": "CC BY 4.0",
        "kind": "page",
        "why": "CC BY 4.0. First-page header only; the comparison table is not shown.",
    },
    {
        "n": 11,
        "authors": "古館裕大、千葉馨、石田裕二、三上貞芳",
        "title": "在宅利用を想定した片麻痺手指リハビリロボットにおける医療者との連携と開発",
        "venue": "日本ロボット学会誌, 2023; 41(4)",
        "href": "https://doi.org/10.7210/jrsj.41.331",
        "ids": "DOI: 10.7210/jrsj.41.331",
        "image": None,
        "why": "J-STAGE bronze PDF. Society copyright, license not a CC grant. 待确认授权.",
    },
]

PAPER_CSS = """
.paper{border:1px solid #d3deec;border-radius:12px;overflow:hidden;margin:14px 0 18px;background:#fff}
.paper .pk{margin:0;background:#0050a0;color:#fff;font-size:14px;letter-spacing:.04em;padding:9px 16px;font-weight:700}
.paper .pm{padding:14px 16px 12px}
.paper .pt{font-size:17px;line-height:1.45;color:#00356b;font-weight:700;margin:0 0 8px}
.paper .pa{font-size:14.5px;line-height:1.55;color:#1c2836;margin:0}
.paper .pv{font-size:14px;color:#5a6c80;margin:4px 0 0}
.paper .pi{font-size:13px;color:#5a6c80;margin:4px 0 0}
.paper figure{margin:0 16px 14px}
.paper figure img{width:100%;height:auto;border-radius:8px;border:1px solid #d3deec;display:block}
.paper figcaption{font-size:13px;color:#5a6c80;line-height:1.55;margin-top:6px}
.paper figcaption a,.paper .pi a{color:#0050a0;font-weight:600}
"""


def is_blue(arr: np.ndarray) -> np.ndarray:
    r = arr[:, :, 0].astype(np.int16)
    g = arr[:, :, 1].astype(np.int16)
    b = arr[:, :, 2].astype(np.int16)
    return (b > 120) & (b > r + 40) & (b > g + 15) & (r < 90) & (g < 150)


def find_pills(im: np.ndarray) -> list[tuple[int, int, int, int]]:
    blue = is_blue(im)
    h, w = blue.shape
    col = blue[:, 30:260].mean(axis=1)
    runs = []
    in_run = False
    start = 0
    for y, v in enumerate(col):
        if v > 0.08 and not in_run:
            start = y
            in_run = True
        elif v <= 0.08 and in_run:
            runs.append((start, y - 1))
            in_run = False
    if in_run:
        runs.append((start, h - 1))
    pills = []
    for y0, y1 in runs:
        height = y1 - y0 + 1
        if height < 20 or height > 58:
            continue
        if y0 < 420:
            continue
        xs = np.where(blue[y0 : y1 + 1].any(axis=0))[0]
        if len(xs) == 0:
            continue
        x0, x1 = int(xs[0]), int(xs[-1])
        width = x1 - x0
        if x0 > 130 or width < 70 or width > 450:
            continue
        region = blue[y0 : y1 + 1, x0 : x1 + 1]
        if region.mean() < 0.35:
            continue
        pills.append((y0, y1, x0, x1))
    return pills


def glyph_mask(im: np.ndarray, y0: int, y1: int, x0: int, x1: int):
    """Non-blue, non-page ink of the label, including the part hanging below the chip."""
    h, w = im.shape[:2]
    # stop at the first clear row under the chip so body copy is not swallowed
    ye = min(h - 1, y1 + 16)
    for y in range(y1 + 1, min(h, y1 + 18)):
        row = im[y, x0 + 6 : x1 - 6]
        if row.size and row.mean() > 246:
            # allow one hanging row that is not pure white; stop at a white gap
            ye = y - 1
            break
    else:
        ye = min(h - 1, y1 + 12)
    if ye <= y0:
        return None
    patch = im[y0 : ye + 1, x0 : x1 + 1].astype(np.int16)
    dist = np.abs(patch - BLUE).sum(axis=2)
    lum = patch.mean(axis=2)
    white = lum > 242
    flat = dist < 70
    g = (~white) & (~flat)
    yy, xx = np.where(g)
    if len(yy) == 0:
        return None
    abs_y = yy + y0
    abs_x = xx + x0
    side = ((abs_x <= x0 + 4) | (abs_x >= x1 - 4)) & (abs_y <= y1 + 1)
    top = abs_y <= y0 + 6
    keep = ~(side | top)
    if keep.sum() < 20:
        return None
    mask = np.zeros(g.shape, dtype=bool)
    mask[yy[keep], xx[keep]] = True
    return mask, y0, x0, ye


def realign_pills(path: Path, write: bool, im: np.ndarray | None = None) -> tuple[int, np.ndarray]:
    if im is None:
        im = np.array(Image.open(path).convert("RGB"))
    else:
        im = im.copy()
    src = im.copy()
    pills = find_pills(im)
    fixed = 0
    notes = []
    for y0, y1, x0, x1 in pills:
        found = glyph_mask(im, y0, y1, x0, x1)
        if not found:
            notes.append(f"  skip no-glyph {y0}-{y1}")
            continue
        g, ys, xs, ye = found
        yy, xx = np.where(g)
        gy0, gy1 = int(yy.min() + ys), int(yy.max() + ys)
        gx0, gx1 = int(xx.min() + xs), int(xx.max() + xs)
        gh = gy1 - gy0 + 1
        gw = gx1 - gx0 + 1
        gcy = (gy0 + gy1) / 2
        gcx = (gx0 + gx1) / 2
        pcy = (y0 + y1) / 2
        pcx = (x0 + x1) / 2
        dy = gcy - pcy
        dx = gcx - pcx
        if abs(dy) < 3 and abs(dx) < 4:
            notes.append(f"  ok dy={dy:.1f} {y0}-{y1}")
            continue
        pad_y, pad_x = 8, 14
        need_h = max(y1 - y0, gh + 2 * pad_y)
        need_w = max(x1 - x0, gw + 2 * pad_x)
        ny0 = int(round(gcy - need_h / 2))
        ny1 = ny0 + need_h
        nx0 = int(round(gcx - need_w / 2))
        nx1 = nx0 + need_w
        nx0 = max(20, nx0)
        # keep at least 4px of chip under the glyphs, and 8px before the next ink
        ny1 = max(ny1, gy1 + 4)
        ny0 = min(ny0, gy0 - 4)
        for y in range(gy1 + 1, min(im.shape[0] - 1, gy1 + 36)):
            row = src[y, nx0 : nx1 + 1]
            if row.size == 0:
                break
            if row.mean() > 246:
                continue
            # next content (body or the following chip)
            if ny1 > y - 8:
                ny1 = max(gy1 + 3, y - 8)
            break
        if ny1 - ny0 < gh + 4:
            ny0 = max(0, gy1 - (gh + 6))
        # clear old chip and its near-blue halo
        y_a, y_b = max(0, y0 - 2), min(im.shape[0], y1 + 3)
        x_a, x_b = max(0, x0 - 2), min(im.shape[1], x1 + 3)
        halo = im[y_a:y_b, x_a:x_b]
        near = np.abs(halo.astype(np.int16) - BLUE).sum(2) < 140
        im[y_a:y_b, x_a:x_b][near] = 255
        im[y0 : y1 + 1, x0 : x1 + 1] = 255
        # clear hanging ink that will be restored
        im[ys : ye + 1, xs : xs + g.shape[1]][g] = 255
        # new chip
        chip = Image.new("RGB", (nx1 - nx0 + 1, ny1 - ny0 + 1), (255, 255, 255))
        draw = ImageDraw.Draw(chip)
        draw.rounded_rectangle(
            [0, 0, nx1 - nx0, ny1 - ny0], radius=6, fill=BLUE_T
        )
        chip_np = np.array(chip)
        im[ny0 : ny1 + 1, nx0 : nx1 + 1] = chip_np
        # restore glyphs on top
        region = im[ys : ye + 1, xs : xs + g.shape[1]]
        region[g] = src[ys : ye + 1, xs : xs + g.shape[1]][g]
        im[ys : ye + 1, xs : xs + g.shape[1]] = region
        fixed += 1
        notes.append(
            f"  fix dy={dy:.1f} dx={dx:.1f} {y0}-{y1} -> {ny0}-{ny1} x {nx0}-{nx1}"
        )
    print(f"{path.name}: pills {len(pills)} fixed {fixed}")
    for line in notes:
        print(line)
    if write:
        Image.fromarray(im).save(path, quality=95, subsampling=0)
    return fixed, im


def header_band(im: np.ndarray) -> tuple[int, int]:
    """Blue title panel. The right edge stays blue even where the title is drawn."""
    blue = is_blue(im)
    right = blue[:, -70:].mean(1)
    ys = np.where(right > 0.75)[0]
    ys = ys[(ys > 100) & (ys < 520)]
    if len(ys) == 0:
        return 140, 380
    return int(ys[0]), int(ys[-1])


def ocr_tsv(image_path: Path) -> list[dict]:
    proc = subprocess.run(
        ["tesseract", str(image_path), "stdout", "tsv", "-l", "eng", "--psm", "6"],
        capture_output=True,
        text=True,
        check=False,
    )
    rows = []
    for line in proc.stdout.splitlines()[1:]:
        parts = line.split("\t")
        if len(parts) < 12:
            continue
        text = parts[11].strip()
        if not text:
            continue
        try:
            conf = float(parts[10])
            left, top, width, height = map(int, parts[6:10])
        except ValueError:
            continue
        rows.append(
            {"t": text, "c": conf, "x": left, "y": top, "w": width, "h": height}
        )
    return rows


def _latin_token(token: str) -> str | None:
    token = token.strip().strip(":;,.!|")
    if not token or not re.search(r"[A-Za-z]", token):
        return None
    if re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9'’\-]*", token):
        return token
    return None


def english_lines(words: list[dict], cover: bool = False) -> list[tuple[int, int, int, int, str]]:
    max_h = 32 if cover else 26
    latin = []
    for w in words:
        token = _latin_token(w["t"])
        if token is None or w["c"] < 80 or not (10 <= w["h"] <= max_h):
            continue
        w = dict(w)
        w["t"] = token
        latin.append(w)
    if not latin:
        return []
    latin.sort(key=lambda w: (w["y"], w["x"]))
    lines: list[list[dict]] = []
    for w in latin:
        if lines and abs(w["y"] - lines[-1][0]["y"]) <= 8:
            lines[-1].append(w)
        else:
            lines.append([w])
    out = []
    for line in lines:
        if len(line) < 4:
            continue
        words_l = [w["t"].lower().strip("-'") for w in line]
        heights = sorted(w["h"] for w in line)
        median_h = heights[len(heights) // 2]
        has_func = any(t in FUNC for t in words_l)
        # A short Latin line under the localized title is the English subtitle,
        # including titles that OCR splits around digits ("200-Patient").
        if not has_func and not (len(line) >= 5 and median_h <= 24):
            continue
        x0 = min(w["x"] for w in line)
        y0 = min(w["y"] for w in line)
        x1 = max(w["x"] + w["w"] for w in line)
        y1 = max(w["y"] + w["h"] for w in line)
        if x1 - x0 < 180:
            continue
        out.append((x0, y0, x1, y1, " ".join(w["t"] for w in line)))
    return out


def paint_lines(im: np.ndarray, boxes: list[tuple[int, int, int, int]], origin: tuple[int, int]) -> int:
    ox, oy = origin
    painted = 0
    for x0, y0, x1, y1, _text in boxes:
        ax0, ay0 = x0 + ox - 4, y0 + oy - 3
        ax1, ay1 = x1 + ox + 4, y1 + oy + 3
        ax0 = max(0, ax0)
        ay0 = max(0, ay0)
        ax1 = min(im.shape[1] - 1, ax1)
        ay1 = min(im.shape[0] - 1, ay1)
        # sample blue above the line; bail if that strip is not blue
        sy = max(0, ay0 - 8)
        sample = im[sy : max(sy + 1, ay0 - 2), ax0:ax1]
        if sample.size == 0 or not is_blue(sample).mean() > 0.45:
            # try inside the line's own blue pixels
            sample = im[ay0 : ay1 + 1, ax0 : ax1 + 1]
            sel = is_blue(sample)
            if sel.mean() < 0.25:
                continue
            color = np.median(sample[sel], axis=0).astype(np.uint8)
        else:
            sel = is_blue(sample)
            color = np.median(sample[sel], axis=0).astype(np.uint8) if sel.any() else BLUE_T
        im[ay0 : ay1 + 1, ax0 : ax1 + 1] = color
        painted += 1
    return painted


def erase_english_subtitle(
    path: Path, write: bool, cover: bool = False, im: np.ndarray | None = None
) -> tuple[list[str], np.ndarray]:
    if im is None:
        im = np.array(Image.open(path).convert("RGB"))
    else:
        im = im.copy()
    if cover:
        # English subtitle sits in the lower half of the Chinese left panel.
        y0, x0, x1 = 300, 20, 650
        origin = (x0, y0)
    else:
        _hs, he = header_band(im)
        y0 = max(80, he - 170)
        x0, x1 = 24, im.shape[1] - 24
        origin = (x0, y0)
    y1 = min(im.shape[0] - 1, (560 if cover else he + 12))
    crop = im[y0:y1, x0:x1]
    tmp = Path("/tmp/ocr_band.png")
    Image.fromarray(crop).save(tmp)
    boxes = english_lines(ocr_tsv(tmp), cover=cover)
    n = paint_lines(im, boxes, origin)
    texts = [b[4] for b in boxes]
    if n and write:
        Image.fromarray(im).save(path, quality=95, subsampling=0)
    print(f"{path.name}: english-lines {n} :: {texts}")
    return (texts if n else []), im


def zh_issue_cover(n: int, title: str, write: bool) -> None:
    src = ASSETS / f"day{n:02d}_cover_en.jpg"
    dest = ASSETS / f"day{n:02d}_cover.jpg"
    im = Image.open(src).convert("RGB")
    arr = np.array(im)
    sample = arr[430:500, 80:240]
    color = tuple(int(x) for x in np.median(sample.reshape(-1, 3), axis=0))
    draw = ImageDraw.Draw(im)
    draw.rectangle([28, 155, 630, 555], fill=color)
    font_k = ImageFont.truetype(FONT_CJK, 22)
    font = ImageFont.truetype(FONT_CJK, 34)
    kicker = f"临床研究专栏  ·  第 {n:02d} 期"
    draw.text((48, 175), kicker, font=font_k, fill=(255, 255, 255))
    # wrap title
    max_w = 560
    lines: list[str] = []
    buf = ""
    for ch in title:
        trial = buf + ch
        if draw.textlength(trial, font=font) <= max_w:
            buf = trial
        else:
            if buf:
                lines.append(buf)
            buf = ch
    if buf:
        lines.append(buf)
    y = 230
    for line in lines:
        draw.text((48, y), line, font=font, fill=(255, 255, 255))
        y += 48
    if write:
        im.save(dest, quality=95, subsampling=0)
    print(f"zh cover day{n:02d} -> {dest.name} ({len(lines)} lines)")


def save_excerpt_images(write: bool) -> None:
    """Crops prepared earlier in /tmp/papers; copy into assets when present."""
    mapping = {
        "/tmp/papers/jrm_headcrop.png": ASSETS / "excerpt_day02_jrm.jpg",
        "/tmp/papers/ledoux_headcrop.png": ASSETS / "excerpt_day10_ledoux.jpg",
    }
    for src, dest in mapping.items():
        if not Path(src).exists():
            print("missing crop", src)
            continue
        im = Image.open(src).convert("RGB")
        if write:
            im.save(dest, quality=90, subsampling=0)
        print("excerpt", dest.name, im.size, "write" if write else "preview")


def paper_html(lang: str, paper: dict) -> str:
    title = html.escape(paper["title"])
    authors = html.escape(paper["authors"])
    venue = html.escape(paper["venue"])
    ids = html.escape(paper["ids"])
    href = html.escape(paper["href"], quote=True)
    bits = [
        '<section class="paper">',
        f'<p class="pk">{html.escape(KICKER[lang])}</p>',
        '<div class="pm">',
        f'<p class="pt">{title}</p>',
        f'<p class="pa">{authors}</p>',
        f'<p class="pv">{venue}</p>',
        f'<p class="pi">{ids}</p>',
    ]
    if paper.get("image"):
        bits.append("</div>")
        lic = paper["lic"]
        cap_src = CAP_FIG if paper.get("kind") == "fig" else CAP_PAGE
        cap = html.escape(cap_src[lang].format(lic=lic))
        alt = html.escape(FIG_ALT[lang] if paper.get("kind") == "fig" else title)
        src = html.escape(f"../assets/{paper['image']}", quote=True)
        link = html.escape(LINK[lang])
        bits.append(
            "<figure>"
            f'<img src="{src}" alt="{alt}">'
            f'<figcaption>{cap} <a href="{href}" rel="noopener noreferrer">{link}</a></figcaption>'
            "</figure>"
        )
    else:
        bits.append(
            f'<p class="pi"><a href="{href}" rel="noopener noreferrer">{html.escape(LINK[lang])}</a></p>'
        )
        bits.append("</div>")
    bits.append("</section>")
    return "".join(bits)


def insert_excerpts() -> int:
    n_done = 0
    by_n = {p["n"]: p for p in PAPERS}
    for lang in LANGS:
        folder = ROOT / lang
        for n in range(1, 12):
            path = folder / f"day{n:02d}.html"
            text = path.read_text()
            if 'class="paper"' not in text:
                block = paper_html(lang, by_n[n])
                if "</h1>" not in text:
                    raise SystemExit(f"no h1 in {path}")
                text = text.replace("</h1>", "</h1>\n" + block, 1)
                n_done += 1
            if ".paper .pk" not in text:
                text = text.replace("</style>", PAPER_CSS + "</style>", 1)
            # localized alts
            text = text.replace('alt="cover"', f'alt="{ALT_COVER[lang]}"', 1)
            path.write_text(text)
        # poster pages live under lang/poster and, for zh, also /poster
    # root Chinese posters
    for path in (ROOT / "poster").glob("day*.html"):
        text = path.read_text()
        text = text.replace('alt="poster"', f'alt="{ALT_POSTER["zh"]}"')
        path.write_text(text)
    for lang in LANGS:
        poster_dir = ROOT / lang / "poster"
        if not poster_dir.exists():
            continue
        for path in poster_dir.glob("day*.html"):
            text = path.read_text()
            text = text.replace('alt="poster"', f'alt="{ALT_POSTER[lang]}"')
            text = text.replace('alt="cover"', f'alt="{ALT_COVER[lang]}"')
            path.write_text(text)
    # point zh day10/11 at the Chinese covers
    for n in (10, 11):
        path = ROOT / "zh" / f"day{n:02d}.html"
        text = path.read_text()
        text = text.replace(
            f"../assets/day{n:02d}_cover_en.jpg",
            f"../assets/day{n:02d}_cover.jpg",
        )
        path.write_text(text)
    return n_done


def poster_paths() -> list[tuple[Path, str]]:
    out = []
    for path in sorted(ASSETS.glob("day*_poster*.jpg")):
        m = re.match(r"day\d+_poster(?:_([a-z]+))?\.jpg$", path.name)
        if not m:
            continue
        lang = m.group(1) or "zh"
        out.append((path, lang))
    return out


def main() -> None:
    import sys

    write = "--write" in sys.argv
    do_img = "--images" in sys.argv or "--write" in sys.argv
    do_html = "--html" in sys.argv or "--write" in sys.argv
    if do_img:
        save_excerpt_images(write)
        total = 0
        for path, lang in poster_paths():
            fixed, im = realign_pills(path, write=False)
            total += fixed
            changed = fixed > 0
            if lang != "en":
                texts, im = erase_english_subtitle(path, write=False, cover=False, im=im)
                if texts:
                    changed = True
            if write and changed:
                Image.fromarray(im).save(path, quality=95, subsampling=0)
        for n in range(1, 10):
            erase_english_subtitle(ASSETS / f"day{n:02d}_cover.jpg", write, cover=True)
        for n, title in (
            (10, "第三方横向评价：Syrebo 软体结构被评为同类动力手康复设备中最轻薄、最轻"),
            (11, "日本学会综述中的认可：Syrebo 被列为全球少数实现家庭实用化的手指康复机器人产品"),
        ):
            zh_issue_cover(n, title, write)
        print("pills fixed", total)
    if do_html:
        print("excerpt pages", insert_excerpts())


if __name__ == "__main__":
    main()
