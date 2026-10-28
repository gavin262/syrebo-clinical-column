#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Build issue 12 and supplementary studies 01–08 into the clinical column."""

from __future__ import annotations

import html
import re
import shutil
import subprocess
import sys
from pathlib import Path

from PIL import Image, ImageFilter

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))

from rmt_content import STUDIES as A  # noqa: E402
from rmt_content2 import MORE as B  # noqa: E402
from rmt_content3 import MORE as C  # noqa: E402
from rmt_depth import apply_depth  # noqa: E402
from rmt_draw import assert_zh_copy, render  # noqa: E402

STUDIES = A + B + C
apply_depth(STUDIES)
ASSETS = ROOT / "assets"
SRC_IMG = Path("/tmp/rmt-img")
LOCALES = ["fr", "es", "pt", "nl", "it", "ro", "tr", "hr", "ru", "lt", "id", "ko", "th", "hi"]

PHOTOS = {
    "hr08": "scene_hr08.jpg",
    "hr03a": "scene_hr03a.jpg",
    "hr06": "scene_hr06.jpg",
    "hr03b": "scene_hr03b.jpg",
}
PHOTO_SRC = {
    "hr08": "hr08.jpg",
    "hr03a": "hr03a.jpg",
    "hr06": "hr06.jpg",
    "hr03b": "hr03b.jpg",
}

CSS = r"""
body{font-family:-apple-system,'Noto Sans SC','PingFang SC','Microsoft YaHei',Arial,sans-serif;margin:0;background:#f4f7fb;color:#1c2836}
.header{background:#fff;border-bottom:4px solid #0050a0;padding:18px 24px;display:flex;align-items:center;gap:16px}
.header img{height:44px}
.header .col{font-size:20px;font-weight:700;color:#00356b}
.header .sub{font-size:13px;color:#5a6c80}
.nav{background:#00356b;color:#fff;padding:10px 24px;font-size:14px}
.nav a{color:#d5e4f7;text-decoration:none;margin-right:14px}
.wrap{max-width:780px;margin:0 auto;padding:28px 22px 60px;background:#fff}
.issue{color:#0050a0;font-weight:700;letter-spacing:1px}
h1{color:#00356b;font-size:30px;line-height:1.35;margin:10px 0 6px}
h1.en{font-size:28px}
h2{color:#00356b;font-size:21px;border-left:5px solid #0050a0;padding-left:10px;margin:28px 0 10px}
p{font-size:17px;line-height:1.85;margin:12px 0}
img.cover,img.product{width:100%;border-radius:10px;margin:14px 0}
.cap{font-size:13px;color:#5a6c80;margin:-6px 0 18px}
.source{background:#e8f2fb;border-left:5px solid #00356b;padding:14px 16px;font-size:15px;line-height:1.7;margin:26px 0}
.tip{background:#fdf6ec;border:1px solid #f0d9a8;padding:14px 16px;font-size:15px;line-height:1.7;border-radius:8px}
.footer{border-top:1px solid #d3deec;margin-top:40px;padding-top:16px;font-size:13px;color:#5a6c80;text-align:center}
.poster{width:100%;max-width:720px;display:block;margin:18px auto;border-radius:10px;box-shadow:0 4px 24px rgba(0,0,0,.12)}
.btn{display:inline-block;background:#00356b;color:#fff;padding:10px 18px;border-radius:8px;text-decoration:none;margin-right:10px}
p.limit{font-size:13.5px;color:#526478;line-height:1.65}
.source a{color:#0050a0;font-weight:600}
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
p.scan{margin:18px 0 0}span.tag{display:inline-block;background:#0050a0;color:#fff;font-size:13px;font-weight:700;line-height:1.2;padding:6px 12px;border-radius:4px}
"""

POSTER_CSS = CSS  # same chrome; poster pages simply do not use the paper rules


def esc(text: str) -> str:
    return html.escape(text, quote=True)


def paras(items) -> str:
    return "\n".join(f"<p>{esc(p)}</p>" for p in items)


def nav_links(lang: str) -> str:
    days = "".join(f'<a href="day{n:02d}.html">{n:02d}</a>' for n in range(1, 13))
    if lang == "zh":
        sups = "".join(f'<a href="sup{n:02d}.html">补{n:02d}</a>' for n in range(1, 9))
        home = '<a href="../index.html">专栏首页</a>'
    else:
        sups = "".join(f'<a href="sup{n:02d}.html">S{n:02d}</a>' for n in range(1, 9))
        home = '<a href="../index.html">Column home</a>'
    return f'<div class="nav">{home}{days}{sups}</div>'


def doi_link(doi: str) -> str:
    return f'<a href="https://doi.org/{esc(doi)}" rel="noopener noreferrer">{esc(doi)}</a>'


def trial_html(lang: str, trial: str | None) -> str:
    if not trial:
        return ""
    url = f"https://trialsearch.who.int/Trial2.aspx?TrialID={trial}"
    link = f'<a href="{url}" rel="noopener noreferrer">{esc(trial)}</a>'
    if lang == "zh":
        return f"临床试验注册：{link}。"
    return f" Trial registration: {link}."


def article(study: dict, lang: str) -> str:
    d = study[lang]
    zh = lang == "zh"
    if zh:
        head_col, head_sub = "Syrebo 临床研究专栏", "循证 · 康复机器人手套临床研究解读"
        h2_bg, h2_ov, h2_mean, h2_src = "研究背景", "研究概述", "研究意义", "文章来源"
        t_design, t_sample, t_result, t_limit = "研究设计", "样本与周期", "核心结果", "研究边界"
        pk, view, pending = "文献摘录", "查看出处", "论文图片：待确认授权，本页不转载。"
        tip = "温馨提示：康复效果因人而异，具体训练方案请在医生或治疗师指导下制定。"
        foot = "syrebo.com · Syrebo 临床研究专栏<br>本文内容基于已发表研究整理，仅供康复科普参考，不构成医疗建议。"
        src_lead = "研究出处："
        h1_class = ""
        html_lang = "zh-CN"
    else:
        head_col, head_sub = "Syrebo Clinical Research Column", "Evidence-based reads on robotic glove rehabilitation research"
        h2_bg, h2_ov, h2_mean, h2_src = "Background", "Study overview", "What this study adds", "Source"
        t_design, t_sample, t_result, t_limit = "Study design", "Sample and schedule", "Main findings", "Limits"
        pk, view, pending = "From the paper", "View source", "Paper figures: reuse not confirmed; none are reproduced on this page."
        tip = "Note: Rehabilitation outcomes vary by individual. Please follow the training plan prescribed by your physician or therapist."
        foot = "syrebo.com · Syrebo Clinical Research Column<br>This content is compiled from published studies for rehabilitation education only and does not constitute medical advice."
        src_lead = "Source: "
        h1_class = ' class="en"'
        html_lang = "en"

    pending_html = ""
    figure_html = ""
    if study["pending"]:
        pending_html = f'<p class="pi">{esc(pending)}</p>'
    elif study.get("figure"):
        fig = "excerpt_day12_qian_fig1.jpg" if study["figure"] == "qian" else "excerpt_sup08_kuv_fig1.jpg"
        figure_html = (
            f'<figure><img src="../assets/{fig}" alt="{esc(d["fig_alt"])}">'
            f'<figcaption>{esc(d["fig_cap"])} {doi_link(study["doi"])}</figcaption></figure>'
        )
    photo_html = ""
    if study.get("photo"):
        src = PHOTOS[study["photo"]]
        if zh:
            red = src.replace(".jpg", "_zh.jpg")
            if (ASSETS / red).exists():
                src = red
        photo_html = (
            f'<img class="product" src="../assets/{src}" alt="{esc(d["photo_alt"])}">\n'
            f'<div class="cap">{esc(d["photo_cap"])}</div>'
        )
    source_body = (
        f'<div class="source">{src_lead}{esc(d["source"])} DOI: {doi_link(study["doi"])}。'
        if zh
        else f'<div class="source">{src_lead}{esc(d["source"])} DOI: {doi_link(study["doi"])}.'
    )
    source_body += trial_html(lang, study.get("trial")) + "</div>"
    related = related_html(study, lang)
    return f"""<!DOCTYPE html>
<html lang="{html_lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{esc(d["title"])}</title>
<meta name="description" content="{esc(d["desc"])}">
<meta name="keywords" content="{esc(d["keywords"])}">
<style>{CSS}</style>
</head>
<body>
<div class="header"><img src="../assets/logo_official.png" alt="Syrebo"><div><div class="col">{head_col}</div><div class="sub">{head_sub}</div></div></div>
{nav_links(lang)}
<div class="wrap">
<div class="issue">{esc(d["issue"])}</div>
<h1{h1_class}>{esc(d["h1"])}</h1>
<section class="paper"><p class="pk">{pk}</p><div class="pm"><p class="pt">{esc(d["paper_title"])}</p><p class="pa">{esc(d["paper_authors"])}</p><p class="pv">{esc(d["paper_venue"])}</p><p class="pi">{esc(d["paper_meta"])}</p><p class="pi"><a href="https://doi.org/{esc(study["doi"])}" rel="noopener noreferrer">{view}</a></p>{pending_html}</div>{figure_html}</section>
{photo_html}
{paras(d["lead"])}
<h2>{h2_bg}</h2>
{paras(d["background"])}
<h2>{h2_ov}</h2>
{paras(d["overview"])}
<p class="scan"><span class="tag">{t_design}</span></p>
<p>{esc(d["design"])}</p>
<p class="scan"><span class="tag">{t_sample}</span></p>
<p>{esc(d["sample"])}</p>
<p class="scan"><span class="tag">{t_result}</span></p>
<p>{esc(d["results"])}</p>
<h2>{h2_mean}</h2>
{paras(d["meaning"])}
<h2>{h2_src}</h2>
<p class="limit"><span class="tag">{t_limit}</span> {esc(d["limits"])}</p>
{source_body}
{related}
<div class="tip">{tip}</div>
<div class="footer">{foot}</div>
</div>
</body>
</html>
"""


def related_html(study: dict, lang: str) -> str:
    items = study.get("related") or []
    if not items:
        return ""
    heading = "相关阅读" if lang == "zh" else "Related reading"
    rows = []
    for href, zh_label, en_label in items:
        label = zh_label if lang == "zh" else en_label
        rows.append(f'<li><a href="{esc(href)}">{esc(label)}</a></li>')
    return f'<h2>{heading}</h2>\n<ul class="related">\n' + "\n".join(rows) + "\n</ul>"


def poster_page(study: dict, lang: str) -> str:
    d = study[lang]
    slug = study["slug"]
    zh = lang == "zh"
    img = f"{slug}_poster.jpg" if zh else f"{slug}_poster_en.jpg"
    img_src = f"../assets/{img}" if zh else f"../../assets/{img}"
    logo = "../assets/logo_official.png" if zh else "../../assets/logo_official.png"
    if zh:
        head_col, head_sub = "Syrebo 临床研究专栏", f"图片版海报 · {d['issue']}"
        issue = f"{d['issue']} · 图片版"
        # /poster/ has image pages for 01–09 and these new pieces. Issues 10 and 11 have no image page.
        days = "".join(f'<a href="day{n:02d}.html">{n:02d}</a>' for n in list(range(1, 10)) + [12])
        sups = "".join(f'<a href="sup{n:02d}.html">补{n:02d}</a>' for n in range(1, 9))
        nav = f'<div class="nav"><a href="../index.html">专栏首页</a>{days}{sups}</div>'
        src_lead, tip_label = "研究出处：", "研究边界："
        read = f'<a class="btn" href="../zh/{slug}.html">阅读中文全文</a><a class="btn" href="../en/{slug}.html">Read in English</a>'
        tip = "温馨提示：康复效果因人而异，具体训练方案请在医生或治疗师指导下制定。"
        foot = "syrebo.com · Syrebo 临床研究专栏<br>本文内容基于已发表研究整理，仅供康复科普参考，不构成医疗建议。"
        html_lang = "zh-CN"
        title = f"{d['h1']} | Syrebo 临床研究专栏 · {d['issue']}（图片版）"
    else:
        head_col, head_sub = "Syrebo Clinical Research Column", f"Image version · {d['issue']}"
        issue = f"{d['issue']} · Image version"
        nav = nav_links("en")
        src_lead, tip_label = "Source: ", "Limits: "
        read = f'<a class="btn" href="../{slug}.html">Read the article</a><a class="btn" href="../../zh/{slug}.html">Chinese version</a>'
        tip = "Note: Rehabilitation outcomes vary by individual. Please follow the training plan prescribed by your physician or therapist."
        foot = "syrebo.com · Syrebo Clinical Research Column<br>This content is compiled from published studies for rehabilitation education only and does not constitute medical advice."
        html_lang = "en"
        title = f"{d['h1']} | Syrebo Clinical Research Column · {d['issue']} (Image version)"
    end = "。" if zh else "."
    source = f'<div class="source">{src_lead}{esc(d["source"])} DOI: {doi_link(study["doi"])}{end}{trial_html(lang, study.get("trial"))}</div>'
    limit = f'<div class="tip">{tip_label}{esc(d["limits"])}</div>'
    return f"""<!DOCTYPE html>
<html lang="{html_lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{esc(title)}</title>
<meta name="description" content="{esc(d["desc"])}">
<style>{POSTER_CSS}</style>
</head>
<body>
<div class="header"><img src="{logo}" alt="Syrebo"><div><div class="col">{head_col}</div><div class="sub">{head_sub}</div></div></div>
{nav}
<div class="wrap">
<div class="issue">{esc(issue)}</div>
<h1>{esc(d["h1"])}</h1>
<img class="poster" src="{img_src}" alt="{esc(d['h1'])}">
{source}
{limit}
<div class="tip">{tip}</div>
<p>{read}</p>
<div class="footer">{foot}</div>
</div>
</body>
</html>
"""


def designed_zh(spec: dict) -> list[str]:
    parts = [
        spec["chip"], spec["cat"], spec["title"], spec.get("sub") or "",
        spec.get("caption") or "", spec["design_label"], spec["key_label"],
        spec["note"], spec["boundary"], spec["footer"],
    ]
    for big, small in spec["stats"]:
        parts.extend([big, small])
    if spec.get("diagram"):
        parts.extend([spec["diagram"]["title"], spec["diagram"]["sub"], spec["diagram"]["number"]])
    result = spec["result"]
    if result["type"] == "chips":
        parts.append(result["headline"])
        parts.extend(result["chips"])
    elif result["type"] == "bars":
        parts.extend(result["labels"])
        parts.extend(result["texts"])
        parts.append(result.get("axis") or "")
    elif result["type"] == "matrix":
        for big, small in result["cells"]:
            parts.extend([big, small])
    return parts


UI_WORD = re.compile(
    r"function|train|repetit|patient|score|mode|start|stop|clinical|evidence|active|passive",
    re.I,
)


def redact_ui(src: Image.Image) -> Image.Image:
    """Blur English interface words on a brand-scene photo used in a Chinese poster."""
    im = src.convert("RGB")
    tmp = Path("/tmp/ui_ocr.png")
    im.save(tmp)
    out = subprocess.check_output(
        ["tesseract", str(tmp), "stdout", "-l", "eng", "--psm", "6", "tsv"],
        text=True,
        stderr=subprocess.DEVNULL,
    )
    boxes = []
    for line in out.splitlines()[1:]:
        cols = line.split("\t")
        if len(cols) < 12:
            continue
        text = cols[11].strip()
        try:
            conf = float(cols[10])
        except ValueError:
            continue
        if conf < 15 or not UI_WORD.search(text):
            continue
        left, top, width, height = map(int, cols[6:10])
        boxes.append((left, top, width, height))
    if not boxes:
        return im
    for left, top, width, height in boxes:
        pad = 10
        x0 = max(0, left - pad)
        y0 = max(0, top - pad)
        x1 = min(im.width, left + width + pad)
        y1 = min(im.height, top + height + pad)
        crop = im.crop((x0, y0, x1, y1)).filter(ImageFilter.GaussianBlur(radius=7))
        im.paste(crop, (x0, y0))
    return im


def copy_images() -> None:
    for key, name in PHOTOS.items():
        src = SRC_IMG / PHOTO_SRC[key]
        dest = ASSETS / name
        if src.exists():
            shutil.copyfile(src, dest)
        elif not dest.exists():
            raise SystemExit(f"missing photo {src}")
    pairs = [
        (SRC_IMG / "qian_fig1.jpg", ASSETS / "excerpt_day12_qian_fig1.jpg"),
        (SRC_IMG / "kuv_fig1.jpg", ASSETS / "excerpt_sup08_kuv_fig1.jpg"),
    ]
    for src, dest in pairs:
        if src.exists():
            shutil.copyfile(src, dest)
        elif not dest.exists():
            raise SystemExit(f"missing figure {src}")


def render_posters() -> None:
    logo = Image.open(ASSETS / "logo_official.png").convert("RGBA")
    redacted: dict[str, Image.Image] = {}
    for study in STUDIES:
        raw = None
        if study.get("photo"):
            raw = Image.open(ASSETS / PHOTOS[study["photo"]]).convert("RGB")
            if study["photo"] not in redacted:
                cleaned = redact_ui(raw)
                redacted[study["photo"]] = cleaned
                if cleaned.tobytes() != raw.tobytes():
                    cleaned.save(ASSETS / PHOTOS[study["photo"]].replace(".jpg", "_zh.jpg"), quality=88, optimize=True)
        for lang, suffix in (("zh", ""), ("en", "_en")):
            spec = dict(study["poster"][lang])
            if lang == "zh":
                assert_zh_copy(designed_zh(spec))
            photo = None if raw is None else (redacted[study["photo"]] if lang == "zh" else raw)
            im = render(spec, photo, logo)
            out = ASSETS / f"{study['slug']}_poster{suffix}.jpg"
            im.save(out, quality=88, optimize=True)
            dev = spec.get("_chip_dev")
            print(f"{out.name} {im.size} chip_dev={dev}")


def write_pages() -> None:
    for study in STUDIES:
        slug = study["slug"]
        (ROOT / "zh" / f"{slug}.html").write_text(article(study, "zh"), encoding="utf-8")
        (ROOT / "en" / f"{slug}.html").write_text(article(study, "en"), encoding="utf-8")
        (ROOT / "poster" / f"{slug}.html").write_text(poster_page(study, "zh"), encoding="utf-8")
        (ROOT / "en" / "poster" / f"{slug}.html").write_text(poster_page(study, "en"), encoding="utf-8")
        print("page", slug)


def zh_index_block() -> str:
    lines = []
    for study in STUDIES:
        slug = study["slug"]
        lines.append(f'<h2>{esc(study["zh_index"])}</h2>')
        if slug == "sup01":
            # series intro sits once, before the first supplement heading is wrong.
            pass
        lines.append(
            f'<p><a class="btn" href="{slug}.html">中文版</a>'
            f'<a class="btn" href="../poster/{slug}.html">图片版海报</a></p>'
        )
    # Insert a series heading before supplement 01.
    html_bits = []
    for study in STUDIES:
        slug = study["slug"]
        if slug == "sup01":
            html_bits.append("<h2>补充研究系列</h2>")
            html_bits.append("<p>以下 8 篇与前面各期使用同一专栏结构。型号未在全文核对的，正文里写明，不把它们计成已确认的设备实验。</p>")
        html_bits.append(f'<h2>{esc(study["zh_index"])}</h2>')
        html_bits.append(
            f'<p><a class="btn" href="{slug}.html">中文版</a>'
            f'<a class="btn" href="../poster/{slug}.html">图片版海报</a></p>'
        )
    return "\n".join(html_bits) + "\n"


def en_index_block() -> str:
    bits = []
    for study in STUDIES:
        slug = study["slug"]
        if slug == "sup01":
            bits.append('<h2 id="supplement">Supplementary research series</h2>')
            bits.append("<p>Eight further reads use the same column structure. Where the full text did not confirm a model, the page says so and does not count the paper as a confirmed device experiment.</p>")
        bits.append(f'<h2>{esc(study["en_index"])}</h2>')
        bits.append(
            f'<p><a class="btn" href="{slug}.html">English</a>'
            f'<a class="btn" href="poster/{slug}.html">Poster version</a></p>'
        )
    return "\n".join(bits) + "\n"


def root_index_block() -> str:
    bits = []
    for study in STUDIES:
        slug = study["slug"]
        if slug == "sup01":
            bits.append("<h2>补充研究系列 · Supplementary research series</h2>")
            bits.append("<p>Eight supplementary reads. Chinese and English. Papers without a confirmed device model are marked in the article.</p>")
        bits.append(f'<h2>{esc(study["zh_index"])}</h2>')
        bits.append(f'<p>{esc(study["root_en"])}</p>')
        bits.append(
            f'<p><a class="btn" href="zh/{slug}.html">中文版</a>'
            f'<a class="btn" href="en/{slug}.html">English</a>'
            f'<a class="btn" href="poster/{slug}.html">图片版海报</a></p>'
        )
    return "\n".join(bits) + "\n"


def insert_before_footer(path: Path, block: str, marker: str) -> None:
    text = path.read_text(encoding="utf-8")
    if marker in text:
        print("skip insert", path)
        return
    token = '<div class="footer">'
    if token not in text:
        raise SystemExit(f"no footer in {path}")
    path.write_text(text.replace(token, block + token, 1), encoding="utf-8")
    print("insert", path)


def patch_indexes() -> None:
    zh = ROOT / "zh" / "index.html"
    en = ROOT / "en" / "index.html"
    root = ROOT / "index.html"
    for path, old, new in [
        (zh, "11 篇临床研究解读", "12 期与补充研究 8 篇"),
        (zh, "临床研究专栏 · 全部 11 期", "临床研究专栏 · 12 期与补充研究"),
        (en, "11 Clinical Study Summaries", "12 issues and 8 supplementary studies"),
        (en, "11 clinical study summaries", "12 issues and 8 supplementary studies"),
        (en, "Clinical Research Column · All 11 Issues", "Clinical Research Column · 12 issues and a supplement"),
        (root, "11 篇临床研究解读", "12 期与补充研究 8 篇"),
        (root, "临床研究专栏 · 全部 11 期", "临床研究专栏 · 12 期与补充研究"),
    ]:
        text = path.read_text(encoding="utf-8")
        if old in text:
            path.write_text(text.replace(old, new), encoding="utf-8")
    insert_before_footer(zh, zh_index_block(), "sup01.html")
    insert_before_footer(en, en_index_block(), 'id="supplement"')
    insert_before_footer(root, root_index_block(), "zh/day12.html")
    other = """<h2>Issue 12 and supplementary studies 01–08</h2>
<p>These nine reads are published in Chinese and English.</p>
<p><a class="btn" href="../en/day12.html">Issue 12 · English</a><a class="btn" href="../en/index.html#supplement">Supplementary series · English</a></p>
"""
    for loc in LOCALES:
        insert_before_footer(ROOT / loc / "index.html", other, "../en/day12.html")


def patch_nav() -> None:
    zh_extra = "".join(f'<a href="sup{n:02d}.html">补{n:02d}</a>' for n in range(1, 9))
    en_extra = "".join(f'<a href="sup{n:02d}.html">S{n:02d}</a>' for n in range(1, 9))
    zh_new = f'<a href="day11.html">11</a><a href="day12.html">12</a>{zh_extra}</div>'
    en_new = f'<a href="day11.html">11</a><a href="day12.html">12</a>{en_extra}</div>'
    poster_new = f'<a href="day09.html">09</a><a href="day12.html">12</a>{zh_extra}</div>'
    for path in (ROOT / "zh").glob("*.html"):
        text = path.read_text(encoding="utf-8")
        old = '<a href="day11.html">11</a></div>'
        if old in text and "day12.html" not in text:
            path.write_text(text.replace(old, zh_new, 1), encoding="utf-8")
            print("nav", path.relative_to(ROOT))
    for path in (ROOT / "en").rglob("*.html"):
        text = path.read_text(encoding="utf-8")
        old = '<a href="day11.html">11</a></div>'
        if old in text and "day12.html" not in text:
            path.write_text(text.replace(old, en_new, 1), encoding="utf-8")
            print("nav", path.relative_to(ROOT))
    for path in (ROOT / "poster").glob("*.html"):
        text = path.read_text(encoding="utf-8")
        old = '<a href="day09.html">09</a></div>'
        if old in text and "day12.html" not in text:
            path.write_text(text.replace(old, poster_new, 1), encoding="utf-8")
            print("nav", path.relative_to(ROOT))


def write_licenses() -> None:
    path = ASSETS / "excerpt_licenses.txt"
    text = path.read_text(encoding="utf-8")
    marker = "excerpt_day12_qian_fig1.jpg"
    if marker in text:
        print("licenses already recorded")
        return
    addition = """
excerpt_day12_qian_fig1.jpg
  Paper: Qian J, Liang C, Liu R, Yu J, Yang T, Bai D. Frontiers in Neurology, 2025;16:1602896.
  DOI: 10.3389/fneur.2025.1602896
  License: CC BY 4.0 (Frontiers).
  Use: Figure 1, the three intervention panels, on the issue 12 excerpt card.
  Attribution is in the figure caption.

excerpt_sup08_kuv_fig1.jpg
  Paper: Kuvijitsuwan P, et al. Scientific Reports, 2024;14:20113.
  DOI: 10.1038/s41598-024-71094-y
  License: CC BY 4.0 (Scientific Reports / Nature).
  Use: Figure 1 of the university-built air-guitar. Not a SYREBO device.
  Attribution is in the figure caption.

Not embedded, and why (待确认授权):
  sup01 Li 2023, Springer LNCS 14267 — publisher copyright, full text not obtained.
  sup02 Zhang 2024, 亚太传统医药 — reuse terms not stated.
  sup03 Rehman 2026, Hong Kong Physiotherapy Journal — license not confirmed from the abstract in hand.
  sup04 Abd-Eltwab 2026, Egyptian Journal of Hospital Medicine — license not confirmed.
  sup05 Liu 2024, IEEE TNSRE — publisher copyright.
  sup06 Sgambato 2026, IEEE BioRob — publisher copyright.
  sup07 Heo 2026, Soft Robotics — publisher copyright.

Brand-scene photographs (scene_hr08.jpg, scene_hr03a.jpg, scene_hr06.jpg, scene_hr03b.jpg)
  are SYREBO marketing scenes, not paper figures. Every use is captioned as not a
  photograph of the study device. They are not literature excerpts.
"""
    path.write_text(text.rstrip() + "\n" + addition, encoding="utf-8")
    print("licenses updated")


def check_pages() -> None:
    banned = ["510(k)", "510k", "FDA cleared", "FDA approved", "FDA批准", "如果你患", "您的病"]
    required_zh = ["研究背景", "研究概述", "研究意义", "文章来源", "研究设计", "样本与周期", "核心结果", "研究边界", "文献摘录"]
    required_en = ["Background", "Study overview", "What this study adds", "Source", "Study design", "Sample and schedule", "Main findings", "Limits", "From the paper"]
    for study in STUDIES:
        for lang, needed in (("zh", required_zh), ("en", required_en)):
            path = ROOT / lang / f"{study['slug']}.html"
            text = path.read_text(encoding="utf-8")
            for token in needed:
                if token not in text:
                    raise SystemExit(f"{path} missing {token}")
            rel = "相关阅读" if lang == "zh" else "Related reading"
            if rel not in text:
                raise SystemExit(f"{path} missing {rel}")
            for token in banned:
                if token in text:
                    raise SystemExit(f"{path} contains {token}")
            if study["pending"] and ("待确认授权" not in text and "reuse not confirmed" not in text):
                raise SystemExit(f"{path} missing pending-license mark")
        # English article body should not grow a Chinese paragraph. The excerpt card may
        # keep an original Chinese title (Zhang 2024), matching issue 11's Japanese title.
        en = (ROOT / "en" / f"{study['slug']}.html").read_text(encoding="utf-8")
        if study["slug"] != "sup02" and any("\u4e00" <= ch <= "\u9fff" for ch in en):
            raise SystemExit(f"Chinese characters in {study['slug']} English page")
    print("page checks ok", len(STUDIES))


def main() -> None:
    if len(STUDIES) != 9:
        raise SystemExit(f"expected 9 studies, got {len(STUDIES)}")
    pages_only = "--pages" in sys.argv
    if not pages_only:
        copy_images()
        render_posters()
    write_pages()
    if not pages_only:
        patch_indexes()
        patch_nav()
        write_licenses()
    check_pages()


if __name__ == "__main__":
    main()
