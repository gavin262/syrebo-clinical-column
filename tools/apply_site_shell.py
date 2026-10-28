#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Shared column chrome: syrebo.com look, SEO, and the research invitation."""

from __future__ import annotations

import html
import json
import os
import re
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SITE = "https://gavin262.github.io/syrebo-clinical-column"
CONTACT = "https://www.syrebo.com/contact-us"
CONTACT_ZH = "https://cn.syrebo.com/contact-us"
HOME = "https://www.syrebo.com/"
MAIL = "mailto:info@syrebo.com"
TODAY = date.today().isoformat()

LOCALES = {
    "zh": "zh-CN",
    "en": "en",
    "fr": "fr",
    "es": "es",
    "pt": "pt",
    "nl": "nl",
    "it": "it",
    "ro": "ro",
    "tr": "tr",
    "hr": "hr",
    "ru": "ru",
    "lt": "lt",
    "id": "id",
    "ko": "ko",
    "th": "th",
    "hi": "hi",
}

CSS = r"""/* column-shell */
body{font-family:"Source Sans 3","Noto Sans SC","PingFang SC","Microsoft YaHei","WenQuanYi Micro Hei",Arial,sans-serif;margin:0;background:#f7f8fa;color:#1c2836}
.header{background:#fff;border-bottom:3px solid #0050A0;padding:16px 24px;display:flex;align-items:center;gap:16px}
.header .brand{display:flex;line-height:0}
.header img{height:42px}
.header .col{font-size:20px;font-weight:700;color:#0a2540}
.header .sub{font-size:13px;color:#5a6c80}
.official{margin-left:auto;color:#0050A0;font-weight:700;text-decoration:none;font-size:14px;white-space:nowrap}
.official:hover{text-decoration:underline}
.nav{background:#fff;color:#17324a;padding:10px 24px;font-size:14px;display:flex;flex-wrap:wrap;gap:8px 14px;align-items:center;border-bottom:1px solid #e2e8f0}
.nav a{color:#17324a;text-decoration:none;margin:0}
.nav a:hover{color:#0050A0}
.wrap{max-width:800px;margin:0 auto;padding:28px 22px 48px;background:#fff;box-shadow:0 8px 28px rgba(10,37,64,.06)}
.issue{color:#0050A0;font-weight:700;letter-spacing:.04em;font-size:13px}
h1{color:#0a2540;font-size:30px;line-height:1.35;margin:10px 0 6px}
h1.en{font-size:28px}
h2{color:#0a2540;font-size:21px;border-left:5px solid #0050A0;padding-left:10px;margin:28px 0 10px}
p{font-size:17px;line-height:1.85;margin:12px 0}
img.cover,img.product{width:100%;border-radius:10px;margin:14px 0}
.cap{font-size:13px;color:#5a6c80;margin:-6px 0 18px}
.source{background:#eef6fc;border-left:5px solid #0050A0;padding:14px 16px;font-size:15px;line-height:1.7;margin:26px 0}
.tip{background:#f7f8fa;border:1px solid #e2e8f0;padding:14px 16px;font-size:15px;line-height:1.7;border-radius:12px}
.footer{border-top:1px solid #e2e8f0;margin-top:36px;padding-top:16px;font-size:13px;color:#5a6c80;text-align:center;line-height:1.7}
.footer a{color:#0050A0;text-decoration:none;font-weight:600}
.footer a:hover{text-decoration:underline}
.poster{width:100%;max-width:720px;display:block;margin:18px auto;border-radius:10px;box-shadow:0 4px 24px rgba(10,37,64,.12)}
.btn{display:inline-block;background:#0050A0;color:#fff;padding:10px 20px;border-radius:999px;text-decoration:none;margin:6px 8px 6px 0;font-weight:600;font-size:15px;line-height:1.2;border:1px solid #0050A0}
.btn:hover{background:#00356b;border-color:#00356b;color:#fff}
.btn-line{background:#fff;color:#0050A0}
.btn-line:hover{background:#eef6fc;color:#0050A0}
.hero{max-width:1206px;margin:0 auto}
.hero img{width:100%;display:block}
p.limit{font-size:13.5px;color:#526478;line-height:1.65}
.source a,.related a{color:#0050A0;font-weight:600}
.paper{border:1px solid #d3deec;border-radius:12px;overflow:hidden;margin:14px 0 18px;background:#fff}
.paper .pk{margin:0;background:#0050A0;color:#fff;font-size:14px;letter-spacing:.04em;padding:9px 16px;font-weight:700}
.paper .pm{padding:14px 16px 12px}
.paper .pt{font-size:17px;line-height:1.45;color:#0a2540;font-weight:700;margin:0 0 8px}
.paper .pa{font-size:14.5px;line-height:1.55;color:#1c2836;margin:0}
.paper .pv{font-size:14px;color:#5a6c80;margin:4px 0 0}
.paper .pi{font-size:13px;color:#5a6c80;margin:4px 0 0}
.paper figure{margin:0 16px 14px}
.paper figure img{width:100%;height:auto;border-radius:8px;border:1px solid #d3deec;display:block}
.paper figcaption{font-size:13px;color:#5a6c80;line-height:1.55;margin-top:6px}
.paper figcaption a,.paper .pi a{color:#0050A0;font-weight:600}
p.scan{margin:18px 0 0}span.tag{display:inline-block;background:#0050A0;color:#fff;font-size:13px;font-weight:700;line-height:1.2;padding:6px 12px;border-radius:4px;vertical-align:middle}
.cta{background:#eef6fc;border:1px solid #c9dcec;border-radius:16px;padding:8px 20px 16px;margin:28px 0}
.cta h2{margin-top:16px}
ul.related{margin:8px 0 18px;padding-left:1.2em}
ul.related li{margin:6px 0;line-height:1.6}
.who{margin:8px 0 16px;padding-left:1.2em}
.who li{margin:4px 0}
"""

# Short, compliant invitation. Who / what is offered / what is not promised.
COPY = {
    "zh": {
        "logo": "司羿智能",
        "official": "官网",
        "nav": "合作",
        "foot_contact": "官网联系页",
        "foot_join": "参与临床研究合作",
        "cta_h": "参与临床研究合作",
        "cta_p": [
            "本专栏面向康复治疗师、康复门诊和医院康复科。可以讨论的是：按书面安排提供评估设备，以及协助把临床问题整理成研究方案要点。研究是否开展，以伦理审查和双方协议为准。",
            "某一篇论文里的分数不是产品效果，本页也不比较其他品牌。",
        ],
        "cta_more": "查看合作说明",
        "poster_suffix": "本页为图片版海报，正文在文章页。",
    },
    "en": {
        "logo": "Syrebo",
        "official": "syrebo.com",
        "nav": "Research",
        "foot_contact": "Contact page",
        "foot_join": "Join our clinical research",
        "cta_h": "Join our clinical research",
        "cta_p": [
            "This column is for rehabilitation therapists, clinics, and hospital departments. What can be discussed is an evaluation unit by written arrangement, and help turning a clinical question into the outline of a study protocol. Whether a study proceeds depends on ethics review and an agreement between the parties.",
            "A score in one paper is not a product effect, and this page does not rank other brands.",
        ],
        "cta_more": "How to take part",
        "poster_suffix": "This page is the image version. The article is linked below.",
    },
    "fr": {
        "logo": "Syrebo",
        "official": "syrebo.com",
        "nav": "Recherche",
        "foot_contact": "Contact",
        "foot_join": "Recherche clinique",
        "cta_h": "Rejoindre la recherche clinique",
        "cta_p": [
            "Cette colonne s’adresse aux thérapeutes en rééducation, aux cliniques et aux services hospitaliers. On peut discuter, selon un accord écrit, d’un appareil d’évaluation et d’une aide pour formuler les points d’un protocole. Le démarrage dépend de l’avis d’éthique et de l’accord des parties.",
            "Un score publié n’est pas un effet produit, et cette page ne classe pas d’autres marques.",
        ],
        "cta_more": "Lire en anglais",
        "poster_suffix": "Version image. L’article en anglais est lié plus bas.",
    },
    "es": {
        "logo": "Syrebo",
        "official": "syrebo.com",
        "nav": "Investigación",
        "foot_contact": "Contacto",
        "foot_join": "Investigación clínica",
        "cta_h": "Participar en la investigación clínica",
        "cta_p": [
            "Esta columna se dirige a terapeutas de rehabilitación, clínicas y servicios hospitalarios. Se puede hablar, mediante un acuerdo por escrito, de un equipo de evaluación y de apoyo para redactar los puntos de un protocolo. El inicio depende de la revisión ética y del acuerdo de las partes.",
            "Una puntuación publicada no es un efecto del producto, y esta página no compara otras marcas.",
        ],
        "cta_more": "Leer en inglés",
        "poster_suffix": "Versión en imagen. El artículo en inglés está enlazado debajo.",
    },
    "pt": {
        "logo": "Syrebo",
        "official": "syrebo.com",
        "nav": "Pesquisa",
        "foot_contact": "Contacto",
        "foot_join": "Pesquisa clínica",
        "cta_h": "Participar da pesquisa clínica",
        "cta_p": [
            "Esta coluna dirige-se a terapeutas de reabilitação, clínicas e serviços hospitalares. É possível falar, por acordo escrito, de um equipamento de avaliação e de apoio para redigir os pontos de um protocolo. O início depende da revisão ética e do acordo entre as partes.",
            "Uma pontuação publicada não é um efeito do produto, e esta página não compara outras marcas.",
        ],
        "cta_more": "Ler em inglês",
        "poster_suffix": "Versão em imagem. O artigo em inglês está ligado abaixo.",
    },
    "nl": {
        "logo": "Syrebo",
        "official": "syrebo.com",
        "nav": "Onderzoek",
        "foot_contact": "Contact",
        "foot_join": "Klinisch onderzoek",
        "cta_h": "Meedoen aan klinisch onderzoek",
        "cta_p": [
            "Deze kolom is bedoeld voor revalidatietherapeuten, klinieken en ziekenhuisafdelingen. Besproken kan worden, op basis van een schriftelijke afspraak, een evaluatieapparaat en hulp bij de opzet van een studieprotocol. Starten hangt af van ethische toetsing en overeenstemming.",
            "Een gepubliceerde score is geen producteffect, en deze pagina rangschikt geen andere merken.",
        ],
        "cta_more": "Lees in het Engels",
        "poster_suffix": "Beeldversie. Het Engelse artikel staat hieronder.",
    },
    "it": {
        "logo": "Syrebo",
        "official": "syrebo.com",
        "nav": "Ricerca",
        "foot_contact": "Contatto",
        "foot_join": "Ricerca clinica",
        "cta_h": "Partecipare alla ricerca clinica",
        "cta_p": [
            "Questa colonna si rivolge a terapisti della riabilitazione, cliniche e servizi ospedalieri. Si può discutere, con un accordo scritto, di un’unità di valutazione e di un supporto per i punti di un protocollo. L’avvio dipende dalla revisione etica e dall’accordo tra le parti.",
            "Un punteggio pubblicato non è un effetto del prodotto, e questa pagina non confronta altri marchi.",
        ],
        "cta_more": "Leggi in inglese",
        "poster_suffix": "Versione immagine. L’articolo in inglese è collegato sotto.",
    },
    "ro": {
        "logo": "Syrebo",
        "official": "syrebo.com",
        "nav": "Cercetare",
        "foot_contact": "Contact",
        "foot_join": "Cercetare clinică",
        "cta_h": "Participați la cercetarea clinică",
        "cta_p": [
            "Coloana se adresează terapeuților de recuperare, clinicilor și secțiilor de spital. Se poate discuta, prin acord scris, un echipament de evaluare și sprijin pentru punctele unui protocol. Începerea depinde de avizul de etică și de acordul părților.",
            "Un scor publicat nu este un efect al produsului, iar pagina nu compară alte mărci.",
        ],
        "cta_more": "Citiți în engleză",
        "poster_suffix": "Versiune imagine. Articolul în engleză este mai jos.",
    },
    "tr": {
        "logo": "Syrebo",
        "official": "syrebo.com",
        "nav": "Araştırma",
        "foot_contact": "İletişim",
        "foot_join": "Klinik araştırma",
        "cta_h": "Klinik araştırmaya katılın",
        "cta_p": [
            "Bu dizi rehabilitasyon terapistlerine, kliniklere ve hastane birimlerine yöneliktir. Yazılı anlaşmayla bir değerlendirme cihazı ve bir çalışma protokolünün maddelerini hazırlama desteği konuşulabilir. Başlamak etik kuruluna ve tarafların anlaşmasına bağlıdır.",
            "Yayımlanmış bir puan ürün etkisi değildir ve bu sayfa başka markaları sıralamaz.",
        ],
        "cta_more": "İngilizce okuyun",
        "poster_suffix": "Görsel sürüm. İngilizce yazı aşağıda bağlantılıdır.",
    },
    "hr": {
        "logo": "Syrebo",
        "official": "syrebo.com",
        "nav": "Istraživanje",
        "foot_contact": "Kontakt",
        "foot_join": "Kliničko istraživanje",
        "cta_h": "Pridružite se kliničkom istraživanju",
        "cta_p": [
            "Ovaj stupac namijenjen je rehabilitacijskim terapeutima, klinikama i bolničkim odjelima. Pisanim dogovorom može se razgovarati o uređaju za procjenu i o podršci za točke protokola. Početak ovisi o etičkom odobrenju i dogovoru strana.",
            "Objavljeni rezultat nije učinak proizvoda, a ova stranica ne uspoređuje druge marke.",
        ],
        "cta_more": "Pročitajte na engleskom",
        "poster_suffix": "Slikovna inačica. Engleski članak je povezan ispod.",
    },
    "ru": {
        "logo": "Syrebo",
        "official": "syrebo.com",
        "nav": "Исследования",
        "foot_contact": "Контакты",
        "foot_join": "Клинические исследования",
        "cta_h": "Участие в клинических исследованиях",
        "cta_p": [
            "Колонка адресована реабилитационным терапевтам, клиникам и больничным отделениям. По письменному соглашению можно обсудить устройство для оценки и помощь в формулировке пунктов протокола. Начало работы зависит от этического заключения и соглашения сторон.",
            "Опубликованный балл не является эффектом изделия, и эта страница не сравнивает другие марки.",
        ],
        "cta_more": "Читать на английском",
        "poster_suffix": "Версия-изображение. Английская статья указана ниже.",
    },
    "lt": {
        "logo": "Syrebo",
        "official": "syrebo.com",
        "nav": "Tyrimai",
        "foot_contact": "Kontaktai",
        "foot_join": "Klinikiniai tyrimai",
        "cta_h": "Prisijunkite prie klinikinių tyrimų",
        "cta_p": [
            "Skiltis skirta reabilitacijos terapeutams, klinikoms ir ligoninių skyriams. Raštišku susitarimu galima aptarti vertinimo įrangą ir pagalbą suformuluojant protokolo punktus. Pradžia priklauso nuo etikos peržiūros ir šalių susitarimo.",
            "Paskelbtas balas nėra gaminio poveikis, ir šis puslapis nelygina kitų prekių ženklų.",
        ],
        "cta_more": "Skaityti angliškai",
        "poster_suffix": "Vaizdo versija. Angliškas straipsnis susietas žemiau.",
    },
    "id": {
        "logo": "Syrebo",
        "official": "syrebo.com",
        "nav": "Riset",
        "foot_contact": "Kontak",
        "foot_join": "Riset klinis",
        "cta_h": "Bergabung dalam penelitian klinis",
        "cta_p": [
            "Kolom ini ditujukan kepada terapis rehabilitasi, klinik, dan bagian rumah sakit. Melalui perjanjian tertulis dapat dibahas perangkat evaluasi dan bantuan menyusun pokok protokol. Dimulainya penelitian bergantung pada tinjauan etik dan kesepakatan para pihak.",
            "Skor yang diterbitkan bukan efek produk, dan halaman ini tidak membandingkan merek lain.",
        ],
        "cta_more": "Baca dalam bahasa Inggris",
        "poster_suffix": "Versi gambar. Artikel bahasa Inggris ditautkan di bawah.",
    },
    "ko": {
        "logo": "Syrebo",
        "official": "syrebo.com",
        "nav": "연구",
        "foot_contact": "문의",
        "foot_join": "임상 연구",
        "cta_h": "임상 연구에 참여하기",
        "cta_p": [
            "이 칼럼은 재활 치료사, 클리닉, 병원 재활부서를 위한 글입니다. 서면 합의에 따라 평가 장비와 연구 계획서 요점 정리를 논의할 수 있습니다. 연구 시작은 윤리 심사와 당사자 합의에 따릅니다.",
            "논문의 점수는 제품 효과가 아니며, 이 페이지는 다른 브랜드를 비교하지 않습니다.",
        ],
        "cta_more": "영어로 읽기",
        "poster_suffix": "이미지 버전입니다. 영어 글은 아래에 연결되어 있습니다.",
    },
    "th": {
        "logo": "Syrebo",
        "official": "syrebo.com",
        "nav": "วิจัย",
        "foot_contact": "ติดต่อ",
        "foot_join": "งานวิจัยคลินิก",
        "cta_h": "ร่วมงานวิจัยทางคลินิก",
        "cta_p": [
            "คอลัมน์นี้เขียนถึงนักกิจกรรมบำบัด นักกายภาพบำบัด คลินิก และหน่วยงานในโรงพยาบาล สามารถหารือตามข้อตกลงเป็นลายลักษณ์อักษรเรื่องอุปกรณ์ประเมินผล และการช่วยจัดประเด็นของโครงร่างวิจัย การเริ่มศึกษาขึ้นกับจริยธรรมการวิจัยและข้อตกลงของคู่กรณี",
            "คะแนนในบทความที่เผยแพร่ไม่ใช่ผลของผลิตภัณฑ์ และหน้านี้ไม่จัดอันดับแบรนด์อื่น",
        ],
        "cta_more": "อ่านภาษาอังกฤษ",
        "poster_suffix": "หน้านี้เป็นภาพโปสเตอร์ บทความภาษาอังกฤษอยู่ด้านล่าง",
    },
    "hi": {
        "logo": "Syrebo",
        "official": "syrebo.com",
        "nav": "अनुसंधान",
        "foot_contact": "संपर्क",
        "foot_join": "नैदानिक अनुसंधान",
        "cta_h": "नैदानिक अनुसंधान में शामिल हों",
        "cta_p": [
            "यह स्तंभ पुनर्वास चिकित्सकों, क्लीनिकों और अस्पताल इकाइयों के लिए है। लिखित व्यवस्था पर मूल्यांकन उपकरण और अध्ययन रूपरेखा के बिंदुओं पर सहायता की चर्चा हो सकती है। अध्ययन की शुरुआत नैतिक समीक्षा और पक्षों के समझौते पर निर्भर है।",
            "किसी प्रकाशित अंक को उत्पाद का प्रभाव नहीं माना जाता, और यह पृष्ठ अन्य ब्रांडों की तुलना नहीं करता।",
        ],
        "cta_more": "अंग्रेज़ी में पढ़ें",
        "poster_suffix": "यह चित्र संस्करण है। अंग्रेज़ी लेख नीचे जुड़ा है।",
    },
}

RECIPROCAL = {
    "day02.html": ["day12.html", "sup03.html"],
    "day05.html": ["day12.html", "sup01.html"],
    "day08.html": ["sup01.html"],
}


def esc(text: str) -> str:
    return html.escape(text, quote=True)


def pages() -> list[Path]:
    found = []
    for path in ROOT.rglob("*.html"):
        if "tools" in path.parts or path.name.startswith("."):
            continue
        found.append(path)
    return sorted(found)


def locale_of(path: Path) -> str:
    rel = path.relative_to(ROOT)
    if rel.parts[0] == "poster":
        return "zh"
    if rel.parts[0] in LOCALES:
        return rel.parts[0]
    return "zh"


def group_key(path: Path) -> tuple[str, str] | None:
    rel = path.relative_to(ROOT)
    parts = rel.parts
    if path.name == "join.html" and parts[0] in ("zh", "en"):
        return ("join", "join.html")
    if path.name == "index.html" and len(parts) == 1:
        return None
    if path.name == "index.html" and parts[0] in LOCALES:
        return ("index", "index.html")
    if parts[0] == "poster":
        return ("poster", path.name)
    if len(parts) >= 3 and parts[1] == "poster" and parts[0] in LOCALES:
        return ("poster", path.name)
    if parts[0] in LOCALES and path.suffix == ".html":
        return ("article", path.name)
    return None


def public_url(path: Path) -> str:
    rel = path.relative_to(ROOT).as_posix()
    if rel == "index.html":
        return SITE + "/"
    return SITE + "/" + rel


def abs_src(path: Path, src: str) -> str:
    if src.startswith("http://") or src.startswith("https://"):
        return src
    target = (path.parent / src).resolve()
    rel = target.relative_to(ROOT).as_posix()
    return SITE + "/" + rel


def rel_href(path: Path, target: Path) -> str:
    href = os.path.relpath(target, path.parent)
    return href.replace(os.sep, "/")


def h1_text(path: Path) -> str:
    text = path.read_text(encoding="utf-8")
    match = re.search(r"<h1[^>]*>(.*?)</h1>", text, re.S)
    if not match:
        return path.stem
    return re.sub(r"<[^>]+>", "", match.group(1)).strip()


INDEX_BLURB = {
    "root": "Syrebo 临床研究专栏入口：12 期与 8 篇补充研究，可进入中文、英文和其他语言版本。",
    "zh": "中文临床研究专栏目录，收录 12 期与 8 篇补充研究，并链到文章页和图片版海报。",
    "en": "English index of the Syrebo Clinical Research Column: 12 issues and 8 supplementary studies, with links to articles and posters.",
    "fr": "Sommaire français de la colonne de recherche clinique Syrebo, avec les 11 premiers numéros et un lien vers les lectures 12 et suppléments en anglais.",
    "es": "Índice en español de la columna de investigación clínica Syrebo, con los 11 primeros números y un enlace a la lectura 12 y los suplementos en inglés.",
    "pt": "Índice em português da coluna de pesquisa clínica Syrebo, com os 11 primeiros números e uma ligação à leitura 12 e aos suplementos em inglês.",
    "nl": "Nederlandse index van de Syrebo-kolom voor klinisch onderzoek, met de eerste 11 nummers en een link naar nummer 12 en de supplementen in het Engels.",
    "it": "Indice italiano della colonna di ricerca clinica Syrebo, con i primi 11 numeri e un collegamento alla lettura 12 e ai supplementi in inglese.",
    "ro": "Index în română al coloanei de cercetare clinică Syrebo, cu primele 11 numere și o legătură către numărul 12 și suplimentele în engleză.",
    "tr": "Syrebo klinik araştırma sütununun Türkçe dizini: ilk 11 sayı ve İngilizce 12. sayı ile ek okumalara bağlantı.",
    "hr": "Hrvatsko kazalo kliničkog stupca Syrebo, s prvih 11 brojeva i poveznicom na 12. broj i dodatke na engleskom.",
    "ru": "Русский указатель клинической колонки Syrebo: первые 11 выпусков и ссылка на 12-й выпуск и дополнения на английском.",
    "lt": "Lietuviška Syrebo klinikinės skilties rodyklė: pirmi 11 numerių ir nuoroda į 12 numerį bei papildymus anglų kalba.",
    "id": "Indeks bahasa Indonesia kolom penelitian klinis Syrebo: 11 edisi pertama dan tautan ke edisi 12 serta suplemen dalam bahasa Inggris.",
    "ko": "Syrebo 임상 연구 칼럼 한국어 색인. 1–11호와 영어판 12호·보충 연구로 연결됩니다.",
    "th": "สารบัญภาษาไทยของคอลัมน์งานวิจัยคลินิก Syrebo มี 11 ฉบับแรก และลิงก์ไปฉบับที่ 12 กับบทความเสริมภาษาอังกฤษ",
    "hi": "Syrebo नैदानिक अनुसंधान स्तंभ की हिंदी अनुक्रमणिका: पहले 11 अंक और अंग्रेज़ी अंक 12 तथा पूरक अध्ययनों की कड़ी।",
}


def description_of(text: str, path: Path, copy: dict) -> str:
    rel = path.relative_to(ROOT)
    if path.name == "index.html":
        key = "root" if rel.as_posix() == "index.html" else locale_of(path)
        return INDEX_BLURB[key]
    match = re.search(r'<meta name="description" content="([^"]*)"', text)
    if match:
        desc = html.unescape(match.group(1)).strip()
    else:
        title = re.search(r"<title>(.*?)</title>", text, re.S)
        desc = re.sub(r"\s+", " ", title.group(1)).strip() if title else path.stem
    poster = "poster" in path.relative_to(ROOT).parts
    if poster and copy["poster_suffix"] not in desc:
        desc = desc.rstrip(".") + ". " + copy["poster_suffix"]
    return re.sub(r"\s+", " ", desc).strip()


def title_of(text: str) -> str:
    match = re.search(r"<title>(.*?)</title>", text, re.S)
    raw = match.group(1) if match else ""
    return re.sub(r"\s+", " ", html.unescape(raw)).strip()


def set_description(text: str, desc: str) -> str:
    tag = f'<meta name="description" content="{esc(desc)}">'
    if re.search(r'<meta name="description" content="[^"]*">', text):
        return re.sub(r'<meta name="description" content="[^"]*">', tag, text, count=1)
    return text.replace("</title>", "</title>\n" + tag, 1)


def seo_block(path: Path, text: str, desc: str, alternates: list[tuple[str, str]]) -> str:
    title = title_of(text)
    url = public_url(path)
    lang = locale_of(path)
    image = SITE + "/assets/logo_official.png"
    for src in re.findall(r'<img[^>]+src="([^"]+)"', text):
        if "logo_" in src:
            continue
        image = abs_src(path, src)
        break
    lines = [
        "<!-- seo:start -->",
        f'<link rel="canonical" href="{esc(url)}">',
        '<meta name="robots" content="index,follow">',
        f'<meta property="og:type" content="{"website" if path.name == "index.html" else "article"}">',
        f'<meta property="og:site_name" content="Syrebo Clinical Research Column">',
        f'<meta property="og:title" content="{esc(title)}">',
        f'<meta property="og:description" content="{esc(desc)}">',
        f'<meta property="og:url" content="{esc(url)}">',
        f'<meta property="og:image" content="{esc(image)}">',
        f'<meta property="og:locale" content="{LOCALES[lang].replace("-", "_")}">',
        '<meta name="twitter:card" content="summary_large_image">',
        f'<meta name="twitter:title" content="{esc(title)}">',
        f'<meta name="twitter:description" content="{esc(desc)}">',
        f'<meta name="twitter:image" content="{esc(image)}">',
    ]
    for code, href in alternates:
        lines.append(f'<link rel="alternate" hreflang="{code}" href="{esc(href)}">')
    doi = re.search(r"https://doi\.org/([0-9.]+/[^\s\"<]+)", text)
    if doi:
        identifier = doi.group(1).rstrip(").,;")
        paper = ""
        pt = re.search(r'<p class="pt">(.*?)</p>', text, re.S)
        if pt:
            paper = re.sub(r"<[^>]+>", "", pt.group(1)).strip()
        graph = {
            "@context": "https://schema.org",
            "@type": "MedicalWebPage",
            "headline": title,
            "description": desc,
            "inLanguage": LOCALES[lang],
            "url": url,
            "image": image,
            "isBasedOn": {
                "@type": "ScholarlyArticle",
                "identifier": identifier,
                "url": "https://doi.org/" + identifier,
                "name": paper or title,
            },
            "publisher": {
                "@type": "Organization",
                "name": "Syrebo",
                "url": HOME,
                "email": "info@syrebo.com",
            },
            "about": {
                "@type": "ScholarlyArticle",
                "identifier": identifier,
                "sameAs": "https://doi.org/" + identifier,
            },
        }
        lines.append('<script type="application/ld+json">')
        lines.append(json.dumps(graph, ensure_ascii=False, separators=(",", ":")))
        lines.append("</script>")
    else:
        graph = {
            "@context": "https://schema.org",
            "@type": "WebPage",
            "headline": title,
            "description": desc,
            "inLanguage": LOCALES[lang],
            "url": url,
            "publisher": {"@type": "Organization", "name": "Syrebo", "url": HOME, "email": "info@syrebo.com"},
        }
        lines.append('<script type="application/ld+json">')
        lines.append(json.dumps(graph, ensure_ascii=False, separators=(",", ":")))
        lines.append("</script>")
    lines.append("<!-- seo:end -->")
    return "\n".join(lines)


def upsert_seo(text: str, block: str) -> str:
    if "<!-- seo:start -->" in text:
        return re.sub(r"<!-- seo:start -->.*?<!-- seo:end -->", block, text, count=1, flags=re.S)
    return text.replace("</head>", block + "\n</head>", 1)


def cta_html(path: Path, copy: dict, lang: str) -> str:
    if path.name == "index.html" and path.parent == ROOT:
        return (
            '<aside class="cta" id="join-research">'
            "<h2>参与临床研究合作</h2>"
            "<p>面向康复治疗师、康复门诊和医院康复科。可按书面安排讨论评估设备，以及把临床问题整理成方案要点。已发表的分数不是产品承诺，这里也不比较其他品牌。</p>"
            '<p><a class="btn" href="zh/join.html">中文说明</a>'
            '<a class="btn" href="en/join.html">English</a>'
            f'<a class="btn btn-line" href="{CONTACT}">官网联系页</a>'
            f'<a class="btn btn-line" href="{MAIL}">info@syrebo.com</a></p>'
            "</aside>\n"
        )
    join = ROOT / ("en" if lang != "zh" else "zh") / "join.html"
    if lang == "zh":
        join = ROOT / "zh" / "join.html"
    href = rel_href(path, join)
    paras = "".join(f"<p>{esc(p)}</p>" for p in copy["cta_p"])
    return (
        f'<aside class="cta" id="join-research"><h2>{esc(copy["cta_h"])}</h2>'
        f"{paras}"
        f'<p><a class="btn" href="{esc(href)}">{esc(copy["cta_more"])}</a>'
        f'<a class="btn btn-line" href="{CONTACT}">{esc(copy["foot_contact"])}</a>'
        f'<a class="btn btn-line" href="{MAIL}">info@syrebo.com</a></p></aside>\n'
    )


def insert_cta(text: str, block: str) -> str:
    if 'id="join-research"' in text:
        return text
    if '<div class="tip">' in text:
        return text.replace('<div class="tip">', block + '<div class="tip">', 1)
    return text.replace('<div class="footer">', block + '<div class="footer">', 1)


def related_block(path: Path, lang: str) -> str:
    names = RECIPROCAL.get(path.name)
    if not names or lang not in ("zh", "en") or "poster" in path.relative_to(ROOT).parts:
        return ""
    if 'class="related"' in path.read_text(encoding="utf-8"):
        return ""
    heading = "相关阅读" if lang == "zh" else "Related reading"
    items = []
    for name in names:
        target = path.parent / name
        if not target.exists():
            continue
        items.append(f'<li><a href="{esc(name)}">{esc(h1_text(target))}</a></li>')
    if not items:
        return ""
    return f"<h2>{heading}</h2>\n<ul class=\"related\">\n" + "\n".join(items) + "\n</ul>\n"


def write_join_pages() -> None:
    zh_nav = re.search(r'<div class="nav">.*?</div>', (ROOT / "zh" / "day12.html").read_text(encoding="utf-8")).group(0)
    en_nav = re.search(r'<div class="nav">.*?</div>', (ROOT / "en" / "day12.html").read_text(encoding="utf-8")).group(0)
    zh = f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>参与临床研究合作 · Syrebo 临床研究专栏</title>
<meta name="description" content="面向康复治疗师、康复门诊和医院康复科。可按书面安排讨论评估设备和研究方案要点。联系方式与官网联系页一致。">
<style>{CSS}</style>
</head>
<body>
<div class="header"><img src="../assets/logo_official.png" alt="司羿智能"><div><div class="col">Syrebo 临床研究专栏</div><div class="sub">参与临床研究合作</div></div></div>
{zh_nav}
<div class="wrap">
<h1>参与临床研究合作</h1>
<p>本专栏把已发表的研究按同一结构读出来，方便康复治疗师核对设计、样本、结局和边界。专栏同时邀请临床团队把尚未回答的问题做成下一项可以注册、可以审查的研究。已发表的分数留在论文里，不写成产品承诺。</p>
<h2>我们希望联系的人</h2>
<ul class="who">
<li>康复治疗师</li>
<li>康复门诊和诊所</li>
<li>医院康复科</li>
</ul>
<h2>可以讨论的支持</h2>
<p>两项都以后续书面安排为准，不是对训练结果的承诺。</p>
<ul class="who">
<li>按约定提供评估用设备</li>
<li>研究方案上的支持：把临床问题整理成可以讨论的方案要点</li>
</ul>
<h2>不在合作说明里承诺的事</h2>
<p>不把某一篇论文的分数写成产品效果，不把先导研究写成已经确证。不比较、不排名其他品牌。研究是否能够开展，取决于伦理审查和双方协议，不在本页预先决定。</p>
<h2>联系方式</h2>
<p>以下路径与官网公开的联系页一致。</p>
<p><a class="btn" href="{CONTACT_ZH}">中文联系页</a><a class="btn" href="{CONTACT}">英文联系页</a><a class="btn btn-line" href="{MAIL}">info@syrebo.com</a></p>
<p>官网联系页公开的电话为 +86 173 1798 3724。来信请注明所在机构、角色，以及希望讨论的临床问题。请不要在第一封信里附带可识别个人的病历。</p>
<p><a href="index.html">返回专栏目录</a> · <a href="day12.html">第 12 期</a> · <a href="../en/join.html">英文说明</a></p>
<div class="footer">syrebo.com · Syrebo 临床研究专栏<br>本文说明合作意向，不构成医疗建议。</div>
</div>
</body>
</html>
"""
    en = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Join our clinical research · Syrebo Clinical Research Column</title>
<meta name="description" content="For rehabilitation therapists, clinics, and hospitals. An evaluation unit by written arrangement and support for a study-protocol outline. Contact paths match the official Syrebo contact page.">
<style>{CSS}</style>
</head>
<body>
<div class="header"><img src="../assets/logo_official.png" alt="Syrebo"><div><div class="col">Syrebo Clinical Research Column</div><div class="sub">Join our clinical research</div></div></div>
{en_nav}
<div class="wrap">
<h1 class="en">Join our clinical research</h1>
<p>The column reads published studies in one structure, so a rehabilitation therapist can check design, sample, outcomes, and limits. It also invites clinical teams to turn an unanswered question into a study that can be registered and reviewed. Scores stay inside the papers. They are not rewritten as product claims.</p>
<h2>Who we hope to hear from</h2>
<ul class="who">
<li>Rehabilitation therapists</li>
<li>Rehabilitation clinics</li>
<li>Hospital rehabilitation departments</li>
</ul>
<h2>What can be discussed</h2>
<p>Both items depend on a later written arrangement. They are not a promise about training results.</p>
<ul class="who">
<li>An evaluation unit, by arrangement</li>
<li>Support for a study protocol: turning a clinical question into an outline that can be discussed</li>
</ul>
<h2>What this page does not promise</h2>
<p>A score in one paper is not a product effect, and a pilot is not a confirmatory result. This page does not compare or rank other brands. Whether a study can start depends on ethics review and an agreement. It is not decided here.</p>
<h2>Contact</h2>
<p>These paths match the contact page published on the official site.</p>
<p><a class="btn" href="{CONTACT}">Contact page</a><a class="btn btn-line" href="{MAIL}">info@syrebo.com</a></p>
<p>The contact page lists the telephone number +86 173 1798 3724. Please name your institution, your role, and the clinical question you want to discuss. Please do not attach identifiable clinical records in a first message.</p>
<p><a href="index.html">Column index</a> · <a href="day12.html">Issue 12</a> · <a href="../zh/join.html">中文</a></p>
<div class="footer">syrebo.com · Syrebo Clinical Research Column<br>This page describes a research invitation. It is not medical advice.</div>
</div>
</body>
</html>
"""
    (ROOT / "zh" / "join.html").write_text(zh, encoding="utf-8")
    (ROOT / "en" / "join.html").write_text(en, encoding="utf-8")


def alternates_for(path: Path, groups: dict[tuple[str, str], list[Path]]) -> list[tuple[str, str]]:
    key = group_key(path)
    if not key or key not in groups:
        return []
    members = groups[key]
    if len(members) < 2 and path.name != "join.html":
        return []
    rows = []
    en_url = None
    for member in members:
        lang = locale_of(member)
        url = public_url(member)
        rows.append((LOCALES[lang], url))
        if lang == "en":
            en_url = url
    if en_url:
        rows.append(("x-default", en_url))
    elif rows:
        rows.append(("x-default", rows[0][1]))
    return rows


def apply_one(path: Path, groups: dict, seen_desc: dict[str, int]) -> None:
    lang = locale_of(path)
    copy = COPY[lang]
    text = path.read_text(encoding="utf-8")
    text = re.sub(r"<style>.*?</style>", "<style>\n" + CSS + "\n</style>", text, count=1, flags=re.S)
    if 'class="brand"' not in text:
        text = re.sub(
            r'<div class="header"><img src="([^"]+)" alt="[^"]*">',
            lambda m: (
                f'<div class="header"><a class="brand" href="{HOME}" rel="noopener noreferrer">'
                f'<img src="{m.group(1)}" alt="{esc(copy["logo"])}"></a>'
            ),
            text,
            count=1,
        )
    if 'class="official"' not in text and 'class="nav"' in text:
        label = esc(copy["official"])
        official = (
            f'</div><a class="official" href="{HOME}" rel="noopener noreferrer">{label}</a></div>\n'
            '<div class="nav">'
        )
        text, count = re.subn(r"</div></div>\s*<div class=\"nav\">", official, text, count=1)
        if count != 1:
            raise SystemExit(f"header pattern missing in {path}")
    nav = re.search(r'<div class="nav">.*?</div>', text, re.S)
    if nav and "join.html" not in nav.group(0):
        href = rel_href(path, ROOT / ("zh" if lang == "zh" else "en") / "join.html")
        addition = f'<a href="{esc(href)}">{esc(copy["nav"])}</a>'
        text = text.replace(nav.group(0), nav.group(0)[:-6] + addition + "</div>", 1)
    extra = related_block(path, lang)
    if extra and 'class="related"' not in text:
        if '<div class="tip">' in text:
            text = text.replace('<div class="tip">', extra + '<div class="tip">', 1)
        else:
            text = text.replace('<div class="footer">', extra + '<div class="footer">', 1)
    if path.name != "join.html":
        text = insert_cta(text, cta_html(path, copy, lang))
    if 'alt="封面"' in text:
        label = h1_text_from(text)
        text = text.replace('alt="封面"', f'alt="{esc(label)}"', 1)
    if lang == "zh":
        text = rewrite_english_alts(text)
    desc = description_of(text, path, copy)
    seen_desc[desc] = seen_desc.get(desc, 0) + 1
    if seen_desc[desc] > 1:
        desc = f"{desc} [{path.relative_to(ROOT).as_posix()}]"
    text = set_description(text, desc)
    text = upsert_seo(text, seo_block(path, text, desc, alternates_for(path, groups)))
    text = link_footer(text, path, copy, lang)
    path.write_text(text, encoding="utf-8")


def h1_text_from(text: str) -> str:
    match = re.search(r"<h1[^>]*>(.*?)</h1>", text, re.S)
    if not match:
        return "Syrebo"
    return re.sub(r"<[^>]+>", "", match.group(1)).strip()


def rewrite_english_alts(text: str) -> str:
    def repl(match: re.Match) -> str:
        alt = match.group(1)
        letters = sum(ch.isascii() and ch.isalpha() for ch in alt)
        if len(alt) > 40 and letters / max(len(alt), 1) > 0.55:
            return match.group(0).replace(alt, "文献摘录配图，原文题名见上方文献卡片")
        return match.group(0)

    return re.sub(r'alt="([^"]*)"', repl, text)


def link_footer(text: str, path: Path, copy: dict, lang: str) -> str:
    match = re.search(r'<div class="footer">(.*?)</div>', text, re.S)
    if not match or "contact-us" in match.group(0):
        return text
    inner = match.group(1)
    if "syrebo.com" in inner and "<a " not in inner.split("syrebo.com", 1)[0][-40:]:
        inner = inner.replace("syrebo.com", f'<a href="{HOME}">syrebo.com</a>', 1)
    join = rel_href(path, ROOT / ("zh" if lang == "zh" else "en") / "join.html")
    contact_href = CONTACT_ZH if lang == "zh" else CONTACT
    links = (
        f'<p class="footlinks"><a href="{contact_href}">{esc(copy["foot_contact"])}</a>'
        f' · <a href="{MAIL}">info@syrebo.com</a>'
        f' · <a href="{esc(join)}">{esc(copy["foot_join"])}</a></p>'
    )
    return text[: match.start()] + f'<div class="footer">{inner}{links}</div>' + text[match.end() :]


def write_sitemap(all_pages: list[Path]) -> None:
    rows = ['<?xml version="1.0" encoding="UTF-8"?>', '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for path in all_pages:
        rows.append("  <url>")
        rows.append(f"    <loc>{esc(public_url(path))}</loc>")
        rows.append(f"    <lastmod>{TODAY}</lastmod>")
        rows.append("  </url>")
    rows.append("</urlset>\n")
    (ROOT / "sitemap.xml").write_text("\n".join(rows), encoding="utf-8")
    (ROOT / "robots.txt").write_text(
        "User-agent: *\nAllow: /\n\nSitemap: " + SITE + "/sitemap.xml\n",
        encoding="utf-8",
    )


def main() -> None:
    write_join_pages()
    all_pages = pages()
    groups: dict[tuple[str, str], list[Path]] = {}
    for path in all_pages:
        key = group_key(path)
        if key:
            groups.setdefault(key, []).append(path)
    seen: dict[str, int] = {}
    for path in all_pages:
        apply_one(path, groups, seen)
    write_sitemap(pages())
    missing = []
    for path in pages():
        text = path.read_text(encoding="utf-8")
        if 'rel="canonical"' not in text:
            missing.append(str(path))
        if path.name != "join.html" and 'id="join-research"' not in text:
            missing.append("cta " + str(path))
        if "510(k)" in text or "510k" in text:
            missing.append("510 " + str(path))
    if missing:
        raise SystemExit("shell check failed:\n" + "\n".join(missing[:30]))
    print("shell ok", len(pages()))


if __name__ == "__main__":
    main()
