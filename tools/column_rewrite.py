#!/usr/bin/env python3
"""Rewrite day articles into the WeChat-style narrative, all 16 locales.

Keeps the literature-excerpt card, images, and the existing citation links.
Inserts scan labels inside the narrative. Does not touch poster images.
"""

from __future__ import annotations

import html
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LANGS = [
    "zh", "en", "fr", "es", "pt", "nl", "it", "ro", "tr", "hr",
    "ru", "lt", "id", "ko", "th", "hi",
]

HEADS = {
    "zh": dict(bg="研究背景", ov="研究概述", sig="研究意义", src="文章来源",
               design="研究设计", sample="样本与周期", result="核心结果", limit="研究边界"),
    "en": dict(bg="Background", ov="Study overview", sig="What this study adds", src="Source",
               design="Study design", sample="Sample and schedule", result="Main findings", limit="Limits"),
    "fr": dict(bg="Contexte", ov="Aperçu de l'étude", sig="Ce que l'étude apporte", src="Source",
               design="Conception de l'étude", sample="Échantillon et rythme", result="Résultats principaux", limit="Limites"),
    "es": dict(bg="Antecedentes", ov="Resumen del estudio", sig="Qué aporta este estudio", src="Fuente",
               design="Diseño del estudio", sample="Muestra y pauta", result="Resultados principales", limit="Límites"),
    "pt": dict(bg="Contexto", ov="Visão geral do estudo", sig="O que o estudo acrescenta", src="Fonte",
               design="Desenho do estudo", sample="Amostra e esquema", result="Resultados principais", limit="Limites"),
    "nl": dict(bg="Achtergrond", ov="Overzicht van de studie", sig="Wat deze studie toevoegt", src="Bron",
               design="Opzet", sample="Steekproef en schema", result="Belangrijkste bevindingen", limit="Grenzen"),
    "it": dict(bg="Contesto", ov="Panoramica dello studio", sig="Cosa aggiunge questo studio", src="Fonte",
               design="Disegno dello studio", sample="Campione e calendario", result="Risultati principali", limit="Limiti"),
    "ro": dict(bg="Context", ov="Prezentarea studiului", sig="Ce aduce acest studiu", src="Sursă",
               design="Designul studiului", sample="Eșantion și program", result="Rezultate principale", limit="Limite"),
    "tr": dict(bg="Arka plan", ov="Çalışmanın özeti", sig="Bu çalışmanın eklediği", src="Kaynak",
               design="Çalışma tasarımı", sample="Örneklem ve program", result="Ana bulgular", limit="Sınırlar"),
    "hr": dict(bg="Pozadina", ov="Pregled studije", sig="Što ova studija dodaje", src="Izvor",
               design="Dizajn studije", sample="Uzorak i raspored", result="Glavni nalazi", limit="Ograničenja"),
    "ru": dict(bg="Контекст", ov="Обзор исследования", sig="Что добавляет это исследование", src="Источник",
               design="Дизайн исследования", sample="Выборка и режим", result="Основные результаты", limit="Границы"),
    "lt": dict(bg="Kontekstas", ov="Tyrimo apžvalga", sig="Ką šis tyrimas prideda", src="Šaltinis",
               design="Tyrimo planas", sample="Imtis ir tvarka", result="Pagrindiniai radiniai", limit="Ribos"),
    "id": dict(bg="Latar belakang", ov="Ikhtisar studi", sig="Apa yang ditambahkan studi ini", src="Sumber",
               design="Desain studi", sample="Sampel dan jadwal", result="Temuan utama", limit="Batasan"),
    "ko": dict(bg="연구 배경", ov="연구 개요", sig="이 연구가 더하는 것", src="출처",
               design="연구 설계", sample="표본과 주기", result="핵심 결과", limit="연구 경계"),
    "th": dict(bg="ที่มา", ov="ภาพรวมของการศึกษา", sig="สิ่งที่การศึกษานี้เพิ่ม", src="แหล่งที่มา",
               design="รูปแบบการศึกษา", sample="กลุ่มตัวอย่างและระยะเวลา", result="ผลหลัก", limit="ข้อจำกัด"),
    "hi": dict(bg="पृष्ठभूमि", ov="अध्ययन का अवलोकन", sig="यह अध्ययन क्या जोड़ता है", src="स्रोत",
               design="अध्ययन डिज़ाइन", sample="नमूना और अनुसूची", result="मुख्य परिणाम", limit="सीमाएँ"),
}

TAG_CSS = (
    "p.scan{margin:18px 0 0}"
    "span.tag{display:inline-block;background:#0050a0;color:#fff;font-size:13px;"
    "font-weight:700;line-height:1.2;padding:6px 12px;border-radius:4px}"
)


def esc_attr(text: str) -> str:
    return html.escape(text, quote=True)


def tx(text: str) -> str:
    """Escape copy for HTML text. Scores such as p<0.001 must not become tags."""
    return html.escape(text, quote=False)


def render_body(lang: str, article: dict) -> str:
    h = HEADS[lang]
    parts = [f"<p>{tx(article['lead'])}</p>", f"<h2>{tx(h['bg'])}</h2>"]
    for para in article["bg"]:
        parts.append(f"<p>{tx(para)}</p>")
    parts.append(f"<h2>{tx(h['ov'])}</h2>")
    if article.get("device"):
        parts.append(f"<p>{tx(article['device'])}</p>")
    parts.append(f'<p class="scan"><span class="tag">{tx(h["design"])}</span></p>')
    parts.append(f"<p>{tx(article['design'])}</p>")
    parts.append(f'<p class="scan"><span class="tag">{tx(h["sample"])}</span></p>')
    parts.append(f"<p>{tx(article['sample'])}</p>")
    parts.append(f'<p class="scan"><span class="tag">{tx(h["result"])}</span></p>')
    parts.append(f"<p>{tx(article['result'])}</p>")
    parts.append(f"<h2>{tx(h['sig'])}</h2>")
    for para in article["sig"]:
        parts.append(f"<p>{tx(para)}</p>")
    parts.append(f"<h2>{tx(h['src'])}</h2>")
    parts.append(
        f'<p class="limit"><span class="tag">{tx(h["limit"])}</span> {tx(article["limit"])}</p>'
    )
    return "\n".join(parts)


def ensure_css(text: str) -> str:
    if "span.tag{" in text:
        return text
    return text.replace("</style>", TAG_CSS + "\n</style>", 1)


def rewrite_file(path: Path, lang: str, article: dict) -> str:
    text = path.read_text()
    old_h1 = re.search(r"<h1[^>]*>(.*?)</h1>", text, re.S).group(1)
    text = ensure_css(text)
    text = re.sub(
        r"<title>.*?</title>",
        f"<title>{esc_attr(article['title'])}</title>",
        text,
        count=1,
        flags=re.S,
    )
    text = re.sub(
        r'<meta name="description" content=".*?">',
        f'<meta name="description" content="{esc_attr(article["desc"])}">',
        text,
        count=1,
        flags=re.S,
    )
    text = re.sub(
        r"(<h1[^>]*>).*?(</h1>)",
        lambda m: m.group(1) + esc_attr(article["title"]) + m.group(2),
        text,
        count=1,
        flags=re.S,
    )
    body = render_body(lang, article)
    new_text, n = re.subn(
        r"(<div class=\"cap\">.*?</div>\n).*?(<div class=\"source\">)",
        lambda m: m.group(1) + body + "\n" + m.group(2),
        text,
        count=1,
        flags=re.S,
    )
    if n != 1:
        raise SystemExit(f"splice failed: {path}")
    # Day 10 pages carry a tip that frames a product comparison. Use the
    # same individual-variation note as day 01 in that language.
    if path.name == "day10.html":
        tip = re.search(
            r'<div class="tip">.*?</div>',
            (ROOT / lang / "day01.html").read_text(),
            re.S,
        )
        # day01 may already be rewritten; the tip itself is unchanged.
        if tip:
            new_text = re.sub(
                r'<div class="tip">.*?</div>',
                tip.group(0),
                new_text,
                count=1,
                flags=re.S,
            )
    path.write_text(new_text)
    index = ROOT / lang / "index.html"
    if index.exists() and old_h1:
        idx = index.read_text()
        if old_h1 in idx:
            idx = idx.replace(old_h1, esc_attr(article["title"]))
            index.write_text(idx)
    return old_h1


def main() -> None:
    sys.path.insert(0, str(Path(__file__).resolve().parent))
    from column_copy import ARTICLES  # noqa: WPS433

    missing = []
    for n, pack in ARTICLES.items():
        for lang in LANGS:
            if lang not in pack:
                missing.append(f"{n}:{lang}")
    if missing:
        raise SystemExit("missing copy: " + ", ".join(missing[:20]))
    for n in range(1, 12):
        for lang in LANGS:
            path = ROOT / lang / f"day{n:02d}.html"
            rewrite_file(path, lang, ARTICLES[n][lang])
            print(f"rewrote {lang}/day{n:02d}.html")


if __name__ == "__main__":
    main()
