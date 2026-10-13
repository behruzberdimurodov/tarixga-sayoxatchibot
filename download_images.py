# -*- coding: utf-8 -*-
"""
Tarixga Sayohat Boti (@Tarixga_sayoxatchibot) uchun rasmlar yuklovchi
va muzey darajasidagi tarixiy kartochkalar yaratuvchi modul.
"""

import io
import os
import urllib.request
from PIL import Image, ImageDraw, ImageFont

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
IMAGES_DIR = os.path.join(BASE_DIR, "images")
os.makedirs(IMAGES_DIR, exist_ok=True)

USER_AGENT = "TarixchiBot/1.0 (Educational research; bot@tarix.uz)"

# Internetdan yuklanadigan nufuzli arxiv fotosuratlar va illyustratsiyalar
IMAGE_URLS = {
    # Davrlar
    "jurassic_base.jpg": "https://upload.wikimedia.org/wikipedia/commons/0/0c/Tyrannosaurus_rex_by_durbed.jpg",
    "stone_age_base.jpg": "https://upload.wikimedia.org/wikipedia/commons/1/1e/Lascaux_painting.jpg",
    "ancient_world_base.jpg": "https://upload.wikimedia.org/wikipedia/commons/e/e3/Kheops-Pyramid.jpg",
    "islamic_golden_age_base.jpg": "https://upload.wikimedia.org/wikipedia/commons/e/e0/Abu_Rayhan_al-Biruni_in_an_Iranian_postage_stamp.jpg",
    "renaissance_base.jpg": "https://upload.wikimedia.org/wikipedia/commons/b/ba/Leonardo_self.jpg",
    "industrial_revolution_base.jpg": "https://upload.wikimedia.org/wikipedia/commons/3/3b/Portrait_of_Sir_Isaac_Newton%2C_1689.jpg",
    "space_atomic_age_base.jpg": "https://upload.wikimedia.org/wikipedia/commons/d/df/Yuri_Gagarin_%281961%29_-_Restoration.jpg",
    "digital_ai_future_base.jpg": "https://upload.wikimedia.org/wikipedia/commons/9/91/Wright_Flyer.jpg",
    # Tarixiy shaxslar
    "richard_owen_base.jpg": "https://upload.wikimedia.org/wikipedia/commons/b/b8/Richard_Owen_by_Thomas_Woolner.jpg",
    "arximed_base.jpg": "https://upload.wikimedia.org/wikipedia/commons/e/e7/Domenico-Fetti_Archimedes_1620.jpg",
    "leonardo_da_vinci_base.jpg": "https://upload.wikimedia.org/wikipedia/commons/b/ba/Leonardo_self.jpg",
    "gutenberg_base.jpg": "https://upload.wikimedia.org/wikipedia/commons/3/33/Gutenberg.jpg",
    "galiley_base.jpg": "https://upload.wikimedia.org/wikipedia/commons/d/d4/Justus_Sustermans_-_Portrait_of_Galileo_Galilei%2C_1636.jpg",
    "nyuton_base.jpg": "https://upload.wikimedia.org/wikipedia/commons/3/3b/Portrait_of_Sir_Isaac_Newton%2C_1689.jpg",
    "jeyms_uatt_base.jpg": "https://upload.wikimedia.org/wikipedia/commons/0/07/James_Watt_by_Henry_Howard.jpg",
    "tesla_base.jpg": "https://upload.wikimedia.org/wikipedia/commons/d/d4/N.Tesla.JPG",
    "edison_base.jpg": "https://upload.wikimedia.org/wikipedia/commons/9/9d/Thomas_Edison2.jpg",
    "mendeleyev_base.jpg": "https://upload.wikimedia.org/wikipedia/commons/c/c8/Dmitri_Mendeleev_1890s.jpg",
    "eynshteyn_base.jpg": "https://upload.wikimedia.org/wikipedia/commons/3/3e/Einstein_1921_by_F_Schmutzer_-_restoration.jpg",
    "fleming_base.jpg": "https://upload.wikimedia.org/wikipedia/commons/b/bf/Alexander_Fleming_1945.jpg",
    "aka_uka_raytlar_base.jpg": "https://upload.wikimedia.org/wikipedia/commons/9/91/Wright_Flyer.jpg",
    "gagarin_base.jpg": "https://upload.wikimedia.org/wikipedia/commons/d/df/Yuri_Gagarin_%281961%29_-_Restoration.jpg",
    "tyuring_base.jpg": "https://upload.wikimedia.org/wikipedia/commons/a/a1/Alan_Turing_Aged_16.jpg",
}


def get_font(size: int, bold: bool = False):
    """Windows tizimidagi chiroyli shriftlarni oladi."""
    font_names = (
        ["segoeuib.ttf", "arialbd.ttf", "calibrib.ttf", "tahomabd.ttf"]
        if bold
        else ["segoeui.ttf", "arial.ttf", "calibri.ttf", "tahoma.ttf"]
    )
    for name in font_names:
        try:
            path = os.path.join(os.environ.get("WINDIR", "C:\\Windows"), "Fonts", name)
            if os.path.exists(path):
                return ImageFont.truetype(path, size)
        except Exception:
            continue
    try:
        return ImageFont.truetype("arial.ttf", size)
    except Exception:
        return ImageFont.load_default()


def download_file(url: str, dest_path: str, timeout: int = 12) -> bool:
    """Rasmni internetdan xavfsiz yuklab oladi."""
    if os.path.exists(dest_path) and os.path.getsize(dest_path) > 1024:
        return True
    try:
        req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            content = resp.read()
            if len(content) > 1000:
                with open(dest_path, "wb") as f:
                    f.write(content)
                return True
    except Exception as e:
        print(f"Yuklashda ogohlantirish ({url}): {e}")
    return False


def create_museum_card(
    base_image_path: str,
    output_path: str,
    title: str,
    subtitle: str,
    era_badge: str,
    accent_color=(212, 175, 55),  # Oltin rang (Gold #D4AF37)
    bg_color=(15, 23, 42),        # To'q ko'k / Tungi osmon (#0F172A)
):
    """Muzey ko'rgazmasi uslubidagi yuqori sifatli tarixiy kartochka yasaydi."""
    width, height = 800, 1000
    card = Image.new("RGB", (width, height), bg_color)
    draw = ImageDraw.Draw(card)

    # Oltin hoshiyalar (Borders)
    margin = 24
    draw.rectangle(
        [margin, margin, width - margin, height - margin],
        outline=accent_color,
        width=3,
    )
    draw.rectangle(
        [margin + 8, margin + 8, width - margin - 8, height - margin - 8],
        outline=(80, 70, 40),
        width=1,
    )

    # 1. Tepada Davr Belgisi (Era Badge)
    badge_rect = [margin + 16, margin + 16, width - margin - 16, margin + 70]
    draw.rectangle(badge_rect, fill=(24, 34, 60), outline=accent_color, width=2)
    font_badge = get_font(26, bold=True)
    draw.text((width // 2, margin + 43), era_badge, font=font_badge, fill=accent_color, anchor="mm")

    # 2. Markaziy Rasm (Portret yoki Tarixiy voqea)
    photo_box = [margin + 20, margin + 85, width - margin - 20, height - 230]
    pw = photo_box[2] - photo_box[0]
    ph = photo_box[3] - photo_box[1]

    loaded_img = None
    if base_image_path and os.path.exists(base_image_path):
        try:
            loaded_img = Image.open(base_image_path).convert("RGB")
        except Exception:
            loaded_img = None

    if loaded_img:
        # Rasmni proporsional qirqib markazga joylashtirish
        loaded_img.thumbnail((pw * 2, ph * 2), Image.Resampling.LANCZOS)
        lw, lh = loaded_img.size
        left = max(0, (lw - pw) // 2)
        top = max(0, (lh - ph) // 2)
        cropped = loaded_img.crop((left, top, left + pw, top + ph))
        card.paste(cropped, (photo_box[0], photo_box[1]))
    else:
        # Rasm topilmasa chiroyli badiiy tekstura va belgi chiziladi
        draw.rectangle(photo_box, fill=(28, 40, 70))
        font_placeholder = get_font(52, bold=True)
        draw.text((width // 2, (photo_box[1] + photo_box[3]) // 2 - 20), "⏳", font=font_placeholder, fill=accent_color, anchor="mm")
        font_ptext = get_font(24, bold=True)
        draw.text((width // 2, (photo_box[1] + photo_box[3]) // 2 + 50), "TARIXIY ARXIV SURATI", font=font_ptext, fill=(200, 200, 200), anchor="mm")

    # Rasm atrofidagi oltin ramka
    draw.rectangle(photo_box, outline=accent_color, width=2)

    # 3. Pastki Plakat (Nom va Qisqacha Ta'rif)
    plaque_rect = [margin + 16, height - 215, width - margin - 16, height - margin - 16]
    draw.rectangle(plaque_rect, fill=(18, 26, 48), outline=accent_color, width=2)

    font_title = get_font(34, bold=True)
    font_sub = get_font(21, bold=False)
    font_foot = get_font(18, bold=True)

    draw.text((width // 2, height - 170), title, font=font_title, fill=(255, 255, 255), anchor="mm")
    draw.text((width // 2, height - 120), subtitle, font=font_sub, fill=(200, 220, 240), anchor="mm")

    # Pastki bot imzosi
    draw.line([margin + 40, height - 75, width - margin - 40, height - 75], fill=(70, 80, 100), width=1)
    draw.text((width // 2, height - 48), "⏳ @Tarixga_sayoxatchibot • Tarixiy Ensiklopediya", font=font_foot, fill=accent_color, anchor="mm")

    card.save(output_path, "JPEG", quality=92)
    return output_path


def create_main_banner(output_path: str):
    """Bosh menyu uchun 1000x560 o'lchamdagi ajoyib banner yasaydi."""
    width, height = 1000, 560
    img = Image.new("RGB", (width, height), (10, 18, 36))
    draw = ImageDraw.Draw(img)

    # Tashqi ramkalar
    draw.rectangle([16, 16, width - 16, height - 16], outline=(212, 175, 55), width=3)
    draw.rectangle([24, 24, width - 24, height - 24], outline=(60, 70, 95), width=1)

    # Ichki naqshlar va bezak chiziqlari
    draw.line([60, 110, width - 60, 110], fill=(212, 175, 55), width=2)
    draw.line([60, 440, width - 60, 440], fill=(212, 175, 55), width=2)

    font_badge = get_font(26, bold=True)
    draw.text((width // 2, 70), "🏛️ BUTUNJAHON VA SHARQ TARIXI ENSIKLOPEDIYASI 🏛️", font=font_badge, fill=(212, 175, 55), anchor="mm")

    font_main = get_font(52, bold=True)
    draw.text((width // 2, 175), "TARIXGA SAYOHAT BOTI", font=font_main, fill=(255, 255, 255), anchor="mm")

    font_sub = get_font(26, bold=False)
    draw.text((width // 2, 235), "🦖 Yura davridan boshlab to zamonaviy Sun'iy Intellektgacha!", font=font_sub, fill=(180, 220, 255), anchor="mm")

    # Qamrab olingan bosqichlar zanjiri
    stages = [
        "🦖 Yura davri",
        "🪨 Tosh davri & Olov",
        "🏺 Qadimgi Sivilizatsiyalar",
        "🌟 Sharq Uyg'onishi",
        "🎨 Renessans & Bosmaxona",
        "⚙️ Sanoat & Elektr",
        "🚀 Kosmos & Aviatsiya",
        "🤖 Zamonaviy AI",
    ]
    font_stage = get_font(19, bold=True)
    row1 = " • ".join(stages[:4])
    row2 = " • ".join(stages[4:])
    draw.text((width // 2, 310), row1, font=font_stage, fill=(230, 200, 120), anchor="mm")
    draw.text((width // 2, 355), row2, font=font_stage, fill=(230, 200, 120), anchor="mm")

    font_footer = get_font(24, bold=True)
    draw.text((width // 2, 485), "🔗 @Tarixga_sayoxatchibot — Hammada birdek ishlovchi 24/7 tizim", font=font_footer, fill=(212, 175, 55), anchor="mm")

    img.save(output_path, "JPEG", quality=92)
    return output_path


def create_qr_share_banner(output_path: str):
    """Do'stlarga ulashish uchun 800x800 o'lchamdagi kartochka yasaydi."""
    width, height = 800, 800
    img = Image.new("RGB", (width, height), (12, 20, 40))
    draw = ImageDraw.Draw(img)

    draw.rectangle([20, 20, width - 20, height - 20], outline=(212, 175, 55), width=3)
    draw.rectangle([28, 28, width - 28, height - 28], outline=(50, 60, 85), width=1)

    font_top = get_font(32, bold=True)
    draw.text((width // 2, 80), "⏳ TARIXGA SAYOHAT QILING!", font=font_top, fill=(212, 175, 55), anchor="mm")

    font_desc = get_font(22, bold=False)
    draw.text((width // 2, 140), "Insoniyat tarixidagi buyuk kashfiyotlar va olimlar bilan tanishing", font=font_desc, fill=(210, 225, 245), anchor="mm")

    # Markazdagi ramka
    box = [160, 200, width - 160, height - 240]
    draw.rectangle(box, fill=(20, 32, 60), outline=(212, 175, 55), width=2)
    font_icon = get_font(90, bold=True)
    draw.text((width // 2, 320), "⏳🦖🌟", font=font_icon, fill=(212, 175, 55), anchor="mm")
    font_mid = get_font(28, bold=True)
    draw.text((width // 2, 420), "Tarixchi Bot Ensiklopediyasi", font=font_mid, fill=(255, 255, 255), anchor="mm")

    font_link = get_font(32, bold=True)
    draw.text((width // 2, 630), "👉 https://t.me/Tarixga_sayoxatchibot", font=font_link, fill=(212, 175, 55), anchor="mm")

    font_sub = get_font(22, bold=False)
    draw.text((width // 2, 700), "Do'stlaringizga ham ulashing va bilimlaringizni sinang!", font=font_sub, fill=(180, 200, 220), anchor="mm")

    img.save(output_path, "JPEG", quality=92)
    return output_path


def main():
    print("1. Asosiy arxiv rasmlarini yuklab olish...")
    for filename, url in IMAGE_URLS.items():
        dest = os.path.join(IMAGES_DIR, filename)
        download_file(url, dest)

    print("2. Bosh banner va ulashish suratlarini yaratish...")
    create_main_banner(os.path.join(IMAGES_DIR, "main_banner.jpg"))
    create_qr_share_banner(os.path.join(IMAGES_DIR, "qr_share.jpg"))

    print("3. Davrlar kartochkalarini yaratish...")
    eras_meta = [
        ("jurassic_base.jpg", "jurassic_card.jpg", "1-DAVR: YURA VA MEZOZOY DAVRI", "Dinozavrlar davri • 201–66 mln yil oldin", "🦖 1-DAVR: MEZOZOY ERASI"),
        ("stone_age_base.jpg", "stone_age_card.jpg", "2-DAVR: TOSH DAVRI VA OLOV", "Olovning bo'ysundirilishi va ilk qurollar", "🪨 2-DAVR: IBTIDOIY JAMOA"),
        ("ancient_world_base.jpg", "ancient_world_card.jpg", "3-DAVR: QADIMGI DUNYO", "Piramidalar, G'ildirak, Qog'oz va Falsafa", "🏺 3-DAVR: ILK SIVILIZATSIYALAR"),
        ("islamic_golden_age_base.jpg", "islamic_golden_age_card.jpg", "4-DAVR: SHARQ UYG'ONISHI", "Al-Xorazmiy, Ibn Sino, Beruniy, Ulug'bek", "🌟 4-DAVR: SHARQ RENESSANSI"),
        ("renaissance_base.jpg", "renaissance_card.jpg", "5-DAVR: UYG'ONISH DAVRI", "Gutenberg bosmaxonasi, Amerika va Teleskop", "🎨 5-DAVR: RENESSANS ERASI"),
        ("industrial_revolution_base.jpg", "industrial_revolution_card.jpg", "6-DAVR: SANOAT INQILOBI", "Bug' mashinasi, Nyuton, Tesla va Edison", "⚙️ 6-DAVR: SANOAT VA FAN"),
        ("space_atomic_age_base.jpg", "space_atomic_age_card.jpg", "7-DAVR: XX ASR — KOSMOS VA ATOM", "Samolyot, Penitsillin, Oyga parvoz, Kompyuter", "🚀 7-DAVR: KOINOT VA AVIA"),
        ("digital_ai_future_base.jpg", "digital_ai_future_card.jpg", "8-DAVR: XXI ASR — AI VA KELAJAK", "Sun'iy Intellekt, Internet va Mars sari", "🤖 8-DAVR: RAQAMLI OLAM"),
    ]

    for base_file, card_file, title, sub, badge in eras_meta:
        bpath = os.path.join(IMAGES_DIR, base_file)
        cpath = os.path.join(IMAGES_DIR, card_file)
        create_museum_card(bpath, cpath, title, sub, badge)

    print("4. Tarixiy shaxslar kartochkalarini yaratish...")
    figures_meta = [
        ("richard_owen_base.jpg", "richard_owen_card.jpg", "RICHARD OUEN", "«Dinozavr» atamasini kiritgan olim", "🦖 PALEONTOLOGIYA ASOSCHISI"),
        (None, "imxotep_card.jpg", "IMXOTEP (IMHOTEP)", "Tarixdagi 1-me'mor va bosh tabib", "🇪🇬 QADIMGI MISR DAHOSI"),
        ("arximed_base.jpg", "arximed_card.jpg", "ARXIMED (ARCHIMEDES)", "Gidrostatika («Eyrika!») va Richag ixtirochisi", "🇬🇷 QADIMGI YUNONISTON"),
        (None, "tsay_lun_card.jpg", "TSAY LUN (CAI LUN)", "105-yilda Qog'ozni kashf etgan donishmand", "🇨🇳 QADIMGI XITOI"),
        (None, "al_xorazmiy_card.jpg", "MUHAMMAD AL-XORAZMIY", "Algebra va Algoritm fani asoschisi", "🇺🇿 SHARQ UYG'ONISH DAVRI"),
        (None, "ibn_sino_card.jpg", "ABU ALI IBN SINO", "Tabiblar sultoni • «Tib qonunlari»", "🇺🇿 JAHON TABOBATI DAHOSI"),
        ("islamic_golden_age_base.jpg", "beruniy_card.jpg", "ABU RAYHON BERUNIY", "Globus va Yer radiusi o'lchovchisi", "🇺🇿 BUYUK QOMUSIY OLIM"),
        (None, "ulugbek_card.jpg", "MIRZO ULUG'BEK", "1018 yulduz jadvali va Samarqand rasadxonasi", "🇺🇿 BUYUK MUNAJJIM VA HUKMDOR"),
        ("leonardo_da_vinci_base.jpg", "leonardo_da_vinci_card.jpg", "LEONARDO DA VINCHI", "«Mona Liza» va zamonasidan ilgarilab ketgan muhandis", "🇮🇹 UNIVERSAL DAHO"),
        ("gutenberg_base.jpg", "gutenberg_card.jpg", "IOGANN GUTENBERG", "Bosmaxona ixtirochisi (1440-yil)", "🇩🇪 AXBOROT INQILOBI"),
        ("galiley_base.jpg", "galiley_card.jpg", "GALILEO GALILEY", "Teleskop va kuzatuv astronomiyasi otasi", "🇮🇹 ZAMONAVIY FIZIKA"),
        ("nyuton_base.jpg", "nyuton_card.jpg", "ISAAK NYUTON", "Butunolam tortishish qonuni va klassik mexanika", "🇬🇧 KLASSIK FIZIKA OTASI"),
        ("jeyms_uatt_base.jpg", "jeyms_uatt_card.jpg", "JEYMS UATT", "Universal bug' dvigateli ixtirochisi", "🏴󠁧󠁢󠁳󠁣󠁴󠁿 SANOAT INQILOBI"),
        ("tesla_base.jpg", "tesla_card.jpg", "NIKOLA TESLA", "O'zgaruvchan tok va elektr dahosi", "⚡ ELEKTR INQILOBI"),
        ("edison_base.jpg", "edison_card.jpg", "TOMAS EDISON", "Lampochka va fonograf ixtirochisi", "🇺🇸 BUYUK IXTIROCHI"),
        ("mendeleyev_base.jpg", "mendeleyev_card.jpg", "DMITRIY MENDELEYEV", "Kimyoviy elementlar davriy jadvali asoschisi", "🧪 BUYUK KIMYOGAR"),
        ("eynshteyn_base.jpg", "eynshteyn_card.jpg", "ALBERT EYNSHTEYN", "Nisbiylik nazariyasi (E = mc²)", "⚛️ ZAMONAVIY FIZIKA DAHOSI"),
        ("fleming_base.jpg", "fleming_card.jpg", "ALEKSANDR FLEMING", "Penitsillin (antibiotik) kashfiyotchisi", "💊 INSONIYAT NAJOTKORI"),
        ("aka_uka_raytlar_base.jpg", "aka_uka_raytlar_card.jpg", "AKA-UKA RAYTLAR", "Birinchi boshqariladigan samolyot (1903)", "✈️ AVIATSIYA ASOSCHILARI"),
        ("gagarin_base.jpg", "gagarin_card.jpg", "YURIY GAGARIN", "Koinotga chiqqan birinchi inson (1961)", "🚀 FAZOGIRLIK RAMZI"),
        ("tyuring_base.jpg", "tyuring_card.jpg", "ALAN TYURING", "Kompyuter va Sun'iy Intellekt otasi", "💻 RAQAMLI ASR PESHVOSI"),
        (None, "tim_berners_lee_card.jpg", "TIM BERNERS-LI", "Butunjahon Internet tarmog'i (WWW) yaratuvchisi", "🌐 INTERNET ME'MORI"),
    ]

    for base_file, card_file, title, sub, badge in figures_meta:
        bpath = os.path.join(IMAGES_DIR, base_file) if base_file else None
        cpath = os.path.join(IMAGES_DIR, card_file)
        create_museum_card(bpath, cpath, title, sub, badge)

    print("Barcha suratlar va muzey kartochkalari muvaffaqiyatli tayyorlandi!")


if __name__ == "__main__":
    main()
