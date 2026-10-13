# -*- coding: utf-8 -*-
"""
Tarixga Sayohat Boti (@Tarixga_sayoxatchibot)
Mukammal, 24/7 uzluksiz ishlovchi, ko'p foydalanuvchili (multi-user),
Yura davridan to zamonaviy Sun'iy Intellektgacha bo'lgan tarixiy ensiklopediya,
kashfiyotchilar, ixtirolar va interaktiv viktorina Telegram boti.
"""

import base64
import io
import json
import logging
import os
import random
import socket
import sqlite3
import sys
import threading
import time
import urllib.parse
from datetime import datetime

import requests
import telebot
from telebot import types

from tarix_data import (
    BOT_LINK,
    BOT_NAME,
    BOT_USERNAME,
    DEFAULT_TOKEN,
    ERA_ORDER,
    ERAS,
    HISTORICAL_FIGURES,
    INVENTIONS,
    QUIZ_QUESTIONS,
    SHARE_LINK,
)

# ---------------------------------------------------------------------------
# SOZLAMALAR VA LOGGING
# ---------------------------------------------------------------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
IMAGES_DIR = os.path.join(BASE_DIR, "images")
DB_PATH = os.path.join(BASE_DIR, "tarix_storage.db")
LOG_PATH = os.path.join(BASE_DIR, "bot.log")
CACHE_FILE = os.path.join(BASE_DIR, "telegram_file_ids.json")

_handlers = [logging.FileHandler(LOG_PATH, encoding="utf-8")]
if sys.stderr is not None:
    try:
        sys.stderr.reconfigure(encoding="utf-8", errors="replace")
        _handlers.append(logging.StreamHandler(sys.stderr))
    except Exception:
        pass

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=_handlers,
)
logger = logging.getLogger("TarixchiBot")

TOKEN = os.environ.get("BOT_TOKEN", DEFAULT_TOKEN)

# Barqaror ulanish parametrlari
telebot.apihelper.SESSION_TIME_TO_LIVE = 45
telebot.apihelper.RETRY_ON_ERROR = True
telebot.apihelper.MAX_RETRIES = 4
telebot.apihelper.RETRY_TIMEOUT = 0.5

# Ko'p foydalanuvchili 16 oqimli bot
bot = telebot.TeleBot(TOKEN, parse_mode="HTML", threaded=True, num_threads=16)

# ---------------------------------------------------------------------------
# MA'LUMOTLAR BAZASI (SQLite Concurrency Safe)
# ---------------------------------------------------------------------------
DB_LOCK = threading.Lock()


def get_db():
    conn = sqlite3.connect(DB_PATH, check_same_thread=False, timeout=20.0)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    with DB_LOCK:
        conn = get_db()
        cur = conn.cursor()
        cur.execute(
            """
            CREATE TABLE IF NOT EXISTS users (
                user_id INTEGER PRIMARY KEY,
                username TEXT,
                first_name TEXT,
                created_at TEXT,
                last_active TEXT,
                current_era TEXT DEFAULT 'jurassic',
                quiz_score INTEGER DEFAULT 0,
                quiz_step INTEGER DEFAULT 0,
                quiz_total INTEGER DEFAULT 0
            )
            """
        )
        cur.execute(
            """
            CREATE TABLE IF NOT EXISTS file_cache (
                filename TEXT PRIMARY KEY,
                file_id TEXT
            )
            """
        )
        conn.commit()

        # Agar JSON kesh fayli bo'lsa, bazaga yuklaymiz
        if os.path.exists(CACHE_FILE):
            try:
                with open(CACHE_FILE, "r", encoding="utf-8") as f:
                    data = json.load(f)
                    for fn, fid in data.items():
                        cur.execute(
                            "INSERT OR REPLACE INTO file_cache (filename, file_id) VALUES (?, ?)",
                            (fn, fid),
                        )
                conn.commit()
            except Exception as e:
                logger.warning(f"Kesh faylini o'qishda ogohlantirish: {e}")
        conn.close()


def save_user(user_id: int, username: str = "", first_name: str = ""):
    now = datetime.utcnow().isoformat()
    with DB_LOCK:
        conn = get_db()
        cur = conn.cursor()
        cur.execute(
            """
            INSERT INTO users (user_id, username, first_name, created_at, last_active)
            VALUES (?, ?, ?, ?, ?)
            ON CONFLICT(user_id) DO UPDATE SET
                username = excluded.username,
                first_name = excluded.first_name,
                last_active = excluded.last_active
            """,
            (user_id, username or "", first_name or "", now, now),
        )
        conn.commit()
        conn.close()


def get_user_stats(user_id: int):
    with DB_LOCK:
        conn = get_db()
        cur = conn.cursor()
        cur.execute("SELECT * FROM users WHERE user_id = ?", (user_id,))
        row = cur.fetchone()
        conn.close()
        return dict(row) if row else None


def update_quiz_score(user_id: int, is_correct: bool):
    with DB_LOCK:
        conn = get_db()
        cur = conn.cursor()
        if is_correct:
            cur.execute(
                """
                UPDATE users
                SET quiz_score = quiz_score + 1,
                    quiz_step = quiz_step + 1,
                    quiz_total = quiz_total + 1
                WHERE user_id = ?
                """,
                (user_id,),
            )
        else:
            cur.execute(
                """
                UPDATE users
                SET quiz_step = quiz_step + 1,
                    quiz_total = quiz_total + 1
                WHERE user_id = ?
                """,
                (user_id,),
            )
        conn.commit()
        conn.close()


def reset_user_quiz(user_id: int):
    with DB_LOCK:
        conn = get_db()
        cur = conn.cursor()
        cur.execute(
            "UPDATE users SET quiz_step = 0, quiz_score = 0 WHERE user_id = ?",
            (user_id,),
        )
        conn.commit()
        conn.close()


def get_leaderboard(limit: int = 10):
    with DB_LOCK:
        conn = get_db()
        cur = conn.cursor()
        cur.execute(
            """
            SELECT first_name, username, quiz_score, quiz_total
            FROM users
            WHERE quiz_total > 0
            ORDER BY quiz_score DESC, quiz_total ASC
            LIMIT ?
            """,
            (limit,),
        )
        rows = cur.fetchall()
        conn.close()
        return [dict(r) for r in rows]


def get_cached_file_id(filename: str) -> str:
    with DB_LOCK:
        conn = get_db()
        cur = conn.cursor()
        cur.execute("SELECT file_id FROM file_cache WHERE filename = ?", (filename,))
        row = cur.fetchone()
        conn.close()
        return row["file_id"] if row else None


def set_cached_file_id(filename: str, file_id: str):
    with DB_LOCK:
        conn = get_db()
        cur = conn.cursor()
        cur.execute(
            "INSERT OR REPLACE INTO file_cache (filename, file_id) VALUES (?, ?)",
            (filename, file_id),
        )
        conn.commit()
        conn.close()
    try:
        data = {}
        if os.path.exists(CACHE_FILE):
            with open(CACHE_FILE, "r", encoding="utf-8") as f:
                data = json.load(f)
        data[filename] = file_id
        with open(CACHE_FILE, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
    except Exception as e:
        logger.warning(f"Kesh faylini saqlashda xato: {e}")


# ---------------------------------------------------------------------------
# MATNLARNI NORMALIZATSIYA QILISH (KIRILL -> LOTIN)
# ---------------------------------------------------------------------------
CYR_TO_LAT = {
    "а": "a", "б": "b", "в": "v", "г": "g", "д": "d", "е": "e", "ё": "yo",
    "ж": "j", "з": "z", "и": "i", "й": "y", "к": "k", "л": "l", "м": "m",
    "н": "n", "о": "o", "п": "p", "р": "r", "с": "s", "т": "t", "у": "u",
    "ф": "f", "х": "x", "ц": "ts", "ч": "ch", "ш": "sh", "щ": "sh", "ъ": "'",
    "ы": "i", "ь": "", "э": "e", "ю": "yu", "я": "ya", "ў": "o'", "қ": "q",
    "ғ": "g'", "ҳ": "h",
}


def normalize_text(text: str) -> str:
    if not text:
        return ""
    text = text.lower()
    res = []
    for ch in text:
        res.append(CYR_TO_LAT.get(ch, ch))
    return "".join(res).strip()


# ---------------------------------------------------------------------------
# KLAVIATURALAR VA TUGMALAR
# ---------------------------------------------------------------------------
def get_main_reply_keyboard():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    markup.add(
        types.KeyboardButton("⏳ Vaqt mashinasi (Davrlar)"),
        types.KeyboardButton("💡 Buyuk kashfiyotlar"),
    )
    markup.add(
        types.KeyboardButton("👤 Tarixiy shaxslar & Olimlar"),
        types.KeyboardButton("🧩 Viktorina (Test)"),
    )
    markup.add(
        types.KeyboardButton("🔍 Qidiruv"),
        types.KeyboardButton("🔗 Ulashish va Linklar"),
    )
    return markup


def get_eras_list_inline_markup():
    markup = types.InlineKeyboardMarkup(row_width=1)
    for era_id in ERA_ORDER:
        era = ERAS[era_id]
        markup.add(
            types.InlineKeyboardButton(
                text=era["short_title"],
                callback_data=f"era_view:{era_id}",
            )
        )
    markup.add(
        types.InlineKeyboardButton("🏠 Bosh sahifa", callback_data="nav_home")
    )
    return markup


def get_era_detail_inline_markup(era_id: str):
    era = ERAS[era_id]
    markup = types.InlineKeyboardMarkup(row_width=2)

    # Oldingi va keyingi davr tugmalari
    nav_row = []
    if era.get("prev_era"):
        nav_row.append(
            types.InlineKeyboardButton("⏪ Oldingi davr", callback_data=f"era_view:{era['prev_era']}")
        )
    if era.get("next_era"):
        nav_row.append(
            types.InlineKeyboardButton("Keyingi davr ⏩", callback_data=f"era_view:{era['next_era']}")
        )
    if nav_row:
        markup.row(*nav_row)

    markup.add(
        types.InlineKeyboardButton("💡 Ushbu davr kashfiyotlari", callback_data=f"era_invs:{era_id}"),
        types.InlineKeyboardButton("👤 Ushbu davr allomalari", callback_data=f"era_figures:{era_id}"),
    )
    markup.add(
        types.InlineKeyboardButton("📜 Barcha davrlar ro'yxati", callback_data="eras_list"),
        types.InlineKeyboardButton("🔗 Davr havolasi (Share)", callback_data=f"era_share:{era_id}"),
    )
    return markup


def get_figures_list_inline_markup(page: int = 0, era_filter: str = None):
    markup = types.InlineKeyboardMarkup(row_width=2)
    items = list(HISTORICAL_FIGURES.values())
    if era_filter:
        items = [f for f in items if f.get("era_id") == era_filter]

    per_page = 8
    start = page * per_page
    end = start + per_page
    current_items = items[start:end]

    for fig in current_items:
        markup.add(
            types.InlineKeyboardButton(
                text=f"👤 {fig['name'].split('(')[0].strip()}",
                callback_data=f"fig_view:{fig['slug']}",
            )
        )

    # Sahifalash tugmalari
    p_row = []
    if page > 0:
        p_row.append(types.InlineKeyboardButton("⬅️ Orqaga", callback_data=f"figs_page:{page-1}:{era_filter or 'all'}"))
    if end < len(items):
        p_row.append(types.InlineKeyboardButton("Oldinga ➡️", callback_data=f"figs_page:{page+1}:{era_filter or 'all'}"))
    if p_row:
        markup.row(*p_row)

    markup.add(types.InlineKeyboardButton("🏠 Bosh sahifa", callback_data="nav_home"))
    return markup


def get_figure_detail_inline_markup(slug: str):
    fig = HISTORICAL_FIGURES.get(slug)
    markup = types.InlineKeyboardMarkup(row_width=2)
    era_id = fig.get("era_id")
    markup.add(
        types.InlineKeyboardButton("⏳ Ushbu davrga o'tish", callback_data=f"era_view:{era_id}"),
        types.InlineKeyboardButton("💬 Hikmati", callback_data=f"fig_quote:{slug}"),
    )
    markup.add(
        types.InlineKeyboardButton("🔙 Allomalar ro'yxati", callback_data="figs_list"),
        types.InlineKeyboardButton("🔗 Ulashish", url=f"https://t.me/share/url?url={BOT_LINK}?start=fig_{slug}&text={urllib.parse.quote(fig['name'])}"),
    )
    return markup


def get_inventions_list_inline_markup():
    markup = types.InlineKeyboardMarkup(row_width=2)
    for slug, inv in INVENTIONS.items():
        markup.add(
            types.InlineKeyboardButton(
                text=inv["name"],
                callback_data=f"inv_view:{slug}",
            )
        )
    markup.add(types.InlineKeyboardButton("🏠 Bosh sahifa", callback_data="nav_home"))
    return markup


def get_invention_detail_inline_markup(slug: str):
    inv = INVENTIONS.get(slug)
    markup = types.InlineKeyboardMarkup(row_width=2)
    era_id = inv.get("era_id")
    markup.add(
        types.InlineKeyboardButton("⏳ Ushbu davrga o'tish", callback_data=f"era_view:{era_id}"),
        types.InlineKeyboardButton("💡 Barcha kashfiyotlar", callback_data="invs_list"),
    )
    return markup


def get_quiz_question_markup(q_index: int):
    q = QUIZ_QUESTIONS[q_index]
    markup = types.InlineKeyboardMarkup(row_width=1)
    letters = ["A", "B", "C", "D"]
    for i, opt in enumerate(q["options"]):
        prefix = f"{letters[i]}) "
        markup.add(
            types.InlineKeyboardButton(
                text=f"{prefix}{opt}",
                callback_data=f"quiz_ans:{q_index}:{i}",
            )
        )
    markup.add(
        types.InlineKeyboardButton("❌ Viktorinani to'xtatish", callback_data="nav_home")
    )
    return markup


# ---------------------------------------------------------------------------
# SURATLARNI YUBORISH (KESH VA TEZKOR YUKLASH)
# ---------------------------------------------------------------------------
def send_or_edit_photo(
    chat_id: int,
    filename: str,
    caption: str,
    reply_markup=None,
    message_id: int = None,
):
    """
    Suratni Telegram file_id keshidan bir soniyada yuboradi.
    Agar keshda bo'lmasa, diskdan yuklab, file_id ni kelgusi safarlar uchun saqlaydi.
    """
    photo_path = os.path.join(IMAGES_DIR, filename)
    cached_fid = get_cached_file_id(filename)

    # 1. Keshdagi file_id orqali yuborish
    if cached_fid:
        try:
            return bot.send_photo(
                chat_id=chat_id,
                photo=cached_fid,
                caption=caption,
                reply_markup=reply_markup,
            )
        except Exception as e:
            logger.warning(f"Keshdagi file_id bilan yuborishda xato ({filename}): {e}")

    # 2. Diskdagi fayldan yuborish va file_id ni saqlash
    if os.path.exists(photo_path):
        try:
            with open(photo_path, "rb") as f:
                msg = bot.send_photo(
                    chat_id=chat_id,
                    photo=f,
                    caption=caption,
                    reply_markup=reply_markup,
                )
                if msg and msg.photo:
                    new_fid = msg.photo[-1].file_id
                    set_cached_file_id(filename, new_fid)
                return msg
        except Exception as e:
            logger.error(f"Fayldan rasm yuborishda xato ({photo_path}): {e}")

    # 3. Zaxira: Rasm topilmasa matn sifatida yuborish
    return bot.send_message(
        chat_id=chat_id,
        text=caption,
        reply_markup=reply_markup,
    )


# ---------------------------------------------------------------------------
# BUYRUQLAR VA BOSH MENYU HANDLERLARI
# ---------------------------------------------------------------------------
@bot.message_handler(commands=["start"])
def handle_start(message: types.Message):
    user_id = message.from_user.id
    save_user(user_id, message.from_user.username, message.from_user.first_name)

    # Deep-link parametrlarini tekshirish (masalan: /start era_jurassic yoki /start fig_tesla)
    parts = message.text.split(maxsplit=1)
    if len(parts) > 1:
        param = parts[1].strip()
        if param.startswith("era_"):
            era_id = param.replace("era_", "")
            if era_id in ERAS:
                show_era(chat_id=message.chat.id, era_id=era_id)
                return
        elif param.startswith("fig_"):
            slug = param.replace("fig_", "")
            if slug in HISTORICAL_FIGURES:
                show_figure(chat_id=message.chat.id, slug=slug)
                return
        elif param.startswith("inv_"):
            slug = param.replace("inv_", "")
            if slug in INVENTIONS:
                show_invention(chat_id=message.chat.id, slug=slug)
                return
        elif param == "quiz":
            start_quiz_session(message.chat.id, user_id)
            return
        elif param == "share":
            show_share_screen(message.chat.id)
            return

    # Standart xush kelibsiz xabari
    first_name = message.from_user.first_name or "Do'stim"
    caption = (
        f"Assalomu alaykum, hurmatli <b>{first_name}</b>!\n\n"
        f"⏳ <b>«TARIXGA SAYOHAT BOTI»</b>ga xush kelibsiz!\n\n"
        f"Ushbu bot insoniyatning millionlab yillik buyuk tarixiy yo'lini o'zida jamlagan mukammal ensiklopediyadir:\n"
        f"🦖 <b>1-davr:</b> Yura va Mezozoy erasi (Dinozavrlar hukmronligi)\n"
        f"🪨 <b>2-davr:</b> Tosh davri va Olovning bo'ysundirilishi\n"
        f"🏺 <b>3-davr:</b> Qadimgi Sivilizatsiyalar (Piramidalar, G'ildirak, Qog'oz)\n"
        f"🌟 <b>4-davr:</b> Sharq Uyg'onishi (Al-Xorazmiy, Ibn Sino, Beruniy, Ulug'bek)\n"
        f"🎨 <b>5-davr:</b> Renessans va Bosmaxona (Leonardo da Vinchi, Gutenberg, Galiley)\n"
        f"⚙️ <b>6-davr:</b> Sanoat Inqilobi va Fan (Nyuton, Uatt, Tesla, Edison)\n"
        f"🚀 <b>7-davr:</b> XX asr: Kosmos, Aviatsiya va Atom (Eynshteyn, Gagarin, Tyuring)\n"
        f"🤖 <b>8-davr:</b> XXI asr: Sun'iy Intellekt va Koinot fath etilishi!\n\n"
        f"🔗 <b>Rasmiy bot havolasi:</b> {BOT_LINK}\n\n"
        f"<i>👇 Sayohatni boshlash uchun quyidagi tugmalardan birini tanlang:</i>"
    )

    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(
        types.InlineKeyboardButton("⏳ Vaqt mashinasini ishga tushirish", callback_data="era_view:jurassic"),
        types.InlineKeyboardButton("💡 Buyuk kashfiyotlar", callback_data="invs_list"),
    )
    markup.add(
        types.InlineKeyboardButton("👤 Tarixiy shaxslar & Olimlar", callback_data="figs_list"),
        types.InlineKeyboardButton("🧩 Viktorina (Test)", callback_data="quiz_start"),
    )
    markup.add(
        types.InlineKeyboardButton("🔗 Do'stlarga ulashish", callback_data="screen_share"),
    )

    # Avval Reply klaviaturani yangilaymiz
    bot.send_message(
        message.chat.id,
        "🏛️ Boshqaruv paneli yuklandi:",
        reply_markup=get_main_reply_keyboard(),
    )

    # So'ngra asosiy rasmli bannerni chiqaramiz
    send_or_edit_photo(
        chat_id=message.chat.id,
        filename="main_banner.jpg",
        caption=caption,
        reply_markup=markup,
    )


@bot.message_handler(commands=["help", "yordam"])
def handle_help(message: types.Message):
    text = (
        "<b>📖 BOTDAN FOYDALANISH BO'YICHA QO'LLANMA:</b>\n\n"
        "• <b>⏳ Vaqt mashinasi:</b> Yura davridan boshlab har bir bosqichni rasmlari, kashfiyotlari va qiziqarli faktlari bilan ko'rish.\n"
        "• <b>💡 Buyuk kashfiyotlar:</b> Olov, g'ildirak, yozuv, qog'oz, kompas, algebra, bosmaxona, bug' dvigateli, elektr, samolyot, kompyuter va AIni o'rganish.\n"
        "• <b>👤 Tarixiy shaxslar:</b> 20 dan ortiq buyuk olimlar, mutafakkirlar va ixtirochilarning biografiyasi va suratlari.\n"
        "• <b>🧩 Viktorina:</b> 15 ta qiziqarli test savoli orqali tarixdagi bilimlaringizni sinab ko'rish va ball to'plash.\n"
        "• <b>🔍 Qidiruv:</b> Botga xohlagan so'zingizni yozing (masalan: <i>nyuton, dinozavr, olov, tesla, beruniy, piramida</i>).\n\n"
        f"🔗 <b>Bot havolasi:</b> {BOT_LINK}"
    )
    bot.send_message(message.chat.id, text, reply_markup=get_main_reply_keyboard())


# ---------------------------------------------------------------------------
# SALOMLASHISH VA TEZKOR SO'ROV HANDLERLARI
# ---------------------------------------------------------------------------
GREETING_PATTERNS = [
    "salom", "assalom", "assalomu alaykum", "assalomu aleykum",
    "qalaysiz", "hello", "hi", "privet", "salam",
]


@bot.message_handler(func=lambda msg: any(g in normalize_text(msg.text) for g in GREETING_PATTERNS))
def handle_greetings(message: types.Message):
    user_id = message.from_user.id
    save_user(user_id, message.from_user.username, message.from_user.first_name)
    first_name = message.from_user.first_name or "Do'stim"

    reply_text = (
        f"Vaalaykum assalom, hurmatli <b>{first_name}</b>! 👋\n\n"
        f"<b>Tarixga Sayohat Boti</b>ga xush kelibsiz! "
        f"Insoniyatning eng qadimiy Yura davridan to zamonaviy kashfiyotlargacha bo'lgan "
        f"sayohatingizni boshlashga tayyormisiz?\n\n"
        f"<i>Quyidagi tugmalardan birini bosing va o'tmishga sayohat qiling:</i>"
    )
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(
        types.InlineKeyboardButton("🦖 Yura davridan boshlash", callback_data="era_view:jurassic"),
        types.InlineKeyboardButton("🧩 Bilimni sinash (Viktorina)", callback_data="quiz_start"),
    )
    bot.send_message(message.chat.id, reply_text, reply_markup=markup)


# ---------------------------------------------------------------------------
# ASOSIY REPLY TUGMALARNI QAYTA ISHLASH
# ---------------------------------------------------------------------------
@bot.message_handler(func=lambda msg: msg.text == "⏳ Vaqt mashinasi (Davrlar)")
def btn_eras(message: types.Message):
    show_era(chat_id=message.chat.id, era_id="jurassic")


@bot.message_handler(func=lambda msg: msg.text == "💡 Buyuk kashfiyotlar")
def btn_inventions(message: types.Message):
    show_inventions_menu(chat_id=message.chat.id)


@bot.message_handler(func=lambda msg: msg.text == "👤 Tarixiy shaxslar & Olimlar")
def btn_figures(message: types.Message):
    show_figures_menu(chat_id=message.chat.id)


@bot.message_handler(func=lambda msg: msg.text == "🧩 Viktorina (Test)")
def btn_quiz(message: types.Message):
    start_quiz_session(chat_id=message.chat.id, user_id=message.from_user.id)


@bot.message_handler(func=lambda msg: msg.text == "🔍 Qidiruv")
def btn_search(message: types.Message):
    text = (
        "🔍 <b>Tarixiy ma'lumotlar va shaxslarni qidirish</b>\n\n"
        "Qidirmoqchi bo'lgan alloma, davr yoki kashfiyot nomini yozing:\n"
        "<i>Masalan: «Nyuton», «Dinozavr», «Olov», «Tesla», «Xorazmiy», «Samolyot», «Piramida», «Internet»</i>"
    )
    bot.send_message(message.chat.id, text)


@bot.message_handler(func=lambda msg: msg.text == "🔗 Ulashish va Linklar")
def btn_share(message: types.Message):
    show_share_screen(chat_id=message.chat.id)


# ---------------------------------------------------------------------------
# TEKSTLI QIDIRUV HANDLERI (SEARCH ENGINE)
# ---------------------------------------------------------------------------
@bot.message_handler(content_types=["text"])
def handle_text_search(message: types.Message):
    query = normalize_text(message.text)
    user_id = message.from_user.id
    save_user(user_id, message.from_user.username, message.from_user.first_name)

    if len(query) < 2:
        bot.send_message(message.chat.id, "Iltimos, qidiruv uchun kamida 2 ta harf yozing.")
        return

    # 1. Shaxslar ichidan qidirish
    matched_figs = []
    for slug, fig in HISTORICAL_FIGURES.items():
        aliases = fig.get("aliases", []) + [fig["name"].lower()]
        for a in aliases:
            if query in normalize_text(a) or normalize_text(a) in query:
                matched_figs.append(fig)
                break

    # 2. Kashfiyotlar ichidan qidirish
    matched_invs = []
    for slug, inv in INVENTIONS.items():
        if query in normalize_text(inv["name"]) or query in normalize_text(inv["desc"]) or query in normalize_text(inv["inventor"]):
            matched_invs.append((slug, inv))

    # 3. Davrlar ichidan qidirish
    matched_eras = []
    for era_id, era in ERAS.items():
        if query in normalize_text(era["title"]) or query in normalize_text(era["details"]):
            matched_eras.append((era_id, era))

    # Natijalarni ko'rsatish
    if not (matched_figs or matched_invs or matched_eras):
        bot.send_message(
            message.chat.id,
            f"❌ «<b>{message.text}</b>» so'rovi bo'yicha hech narsa topilmadi.\n"
            f"Boshqa so'z bilan urinib ko'ring (masalan: <i>Arximed, Edison, Dinozavr, Gutenberg</i>).",
            reply_markup=get_main_reply_keyboard(),
        )
        return

    markup = types.InlineKeyboardMarkup(row_width=1)
    response_lines = [f"🔎 «<b>{message.text}</b>» bo'yicha topilgan natijalar:\n"]

    for fig in matched_figs[:5]:
        response_lines.append(f"• 👤 <b>{fig['name']}</b> ({fig['years']})")
        markup.add(
            types.InlineKeyboardButton(f"👤 {fig['name']} — To'liq ma'lumot", callback_data=f"fig_view:{fig['slug']}")
        )

    for slug, inv in matched_invs[:5]:
        response_lines.append(f"• {inv['name']} ({inv['year']})")
        markup.add(
            types.InlineKeyboardButton(f"💡 {inv['name']} — Ko'rish", callback_data=f"inv_view:{slug}")
        )

    for era_id, era in matched_eras[:3]:
        response_lines.append(f"• {era['title']}")
        markup.add(
            types.InlineKeyboardButton(f"⏳ {era['short_title']} — Davrga o'tish", callback_data=f"era_view:{era_id}")
        )

    bot.send_message(
        message.chat.id,
        "\n".join(response_lines),
        reply_markup=markup,
    )


# ---------------------------------------------------------------------------
# KO'RINISHLAR (VIEWS VA MODALLAR)
# ---------------------------------------------------------------------------
def show_era(chat_id: int, era_id: str):
    if era_id not in ERAS:
        era_id = "jurassic"
    era = ERAS[era_id]

    facts_text = "\n".join([f"  ⚡ {f}" for f in era.get("fun_facts", [])])
    caption = (
        f"{era['details']}\n\n"
        f"<b>🎯 Qiziqarli faktlar:</b>\n{facts_text}\n\n"
        f"<i>Keyingi yoki oldingi davrlarga o'tish uchun quyidagi tugmalardan foydalaning:</i>"
    )

    markup = get_era_detail_inline_markup(era_id)
    send_or_edit_photo(
        chat_id=chat_id,
        filename=era["image_file"],
        caption=caption,
        reply_markup=markup,
    )


def show_figure(chat_id: int, slug: str):
    fig = HISTORICAL_FIGURES.get(slug)
    if not fig:
        return
    caption = (
        f"{fig['bio']}\n\n"
        f"💬 <b>Hikmatli so'zi:</b>\n<i>{fig['quote']}</i>\n\n"
        f"🔗 Havola: {BOT_LINK}?start=fig_{slug}"
    )
    markup = get_figure_detail_inline_markup(slug)
    send_or_edit_photo(
        chat_id=chat_id,
        filename=fig["image_file"],
        caption=caption,
        reply_markup=markup,
    )


def show_invention(chat_id: int, slug: str):
    inv = INVENTIONS.get(slug)
    if not inv:
        return
    era = ERAS.get(inv.get("era_id"), {})
    text = (
        f"<b>{inv['name']}</b>\n"
        f"<i>⏳ Davr: {inv['year']}</i>\n"
        f"<i>👤 Kashfiyotchi: {inv['inventor']}</i>\n"
        f"<i>🏛️ Tegishli era: {era.get('short_title', 'Tarixiy davr')}</i>\n\n"
        f"<b>📖 Kashfiyot haqida:</b>\n{inv['desc']}\n\n"
        f"🔗 Havola: {BOT_LINK}?start=inv_{slug}"
    )
    markup = get_invention_detail_inline_markup(slug)
    # Ushbu davrning kartochkasi bilan birga yuboramiz
    image_file = era.get("image_file", "main_banner.jpg")
    send_or_edit_photo(
        chat_id=chat_id,
        filename=image_file,
        caption=text,
        reply_markup=markup,
    )


def show_inventions_menu(chat_id: int):
    text = (
        "<b>💡 BUYUK KASHFIYOTLAR VA IXTIROLAR ENSIKLOPEDIYASI</b>\n\n"
        "Olovning kashf qilinishidan to zamonaviy Sun'iy Intellektgacha bo'lgan "
        "dunyo tarixini tubdan o'zgartirgan buyuk ixtirolar ro'yxati.\n\n"
        "<i>Tafsilotlarini ko'rish uchun kashfiyot nomini tanlang:</i>"
    )
    markup = get_inventions_list_inline_markup()
    send_or_edit_photo(
        chat_id=chat_id,
        filename="ancient_world_card.jpg",
        caption=text,
        reply_markup=markup,
    )


def show_figures_menu(chat_id: int, page: int = 0, era_filter: str = None):
    text = (
        "<b>👤 TARIXIY SHAXSLAR VA BUYUK OLIMLAR RO'YXATI</b>\n\n"
        "Insoniyat ilm-fani, falsafasi va texnologiyasiga beqiyos hissa qo'shgan "
        "daholarning hayoti, asarlari va kashfiyotlari bilan tanishing.\n\n"
        "<i>Kerakli allomani tanlang:</i>"
    )
    markup = get_figures_list_inline_markup(page=page, era_filter=era_filter)
    send_or_edit_photo(
        chat_id=chat_id,
        filename="islamic_golden_age_card.jpg",
        caption=text,
        reply_markup=markup,
    )


def show_share_screen(chat_id: int):
    text = (
        "<b>🔗 TARIXGA SAYOHAT BOTI LINKLARI VA ULASHISH</b>\n\n"
        f"• <b>Botning asosiy havolasi:</b>\n{BOT_LINK}\n\n"
        f"• <b>Do'stlar va guruhlarga yuborish havolasi:</b>\n{SHARE_LINK}\n\n"
        "Botingizni do'stlaringiz bilan baham ko'ring va tarixdan birgalikda bahramand bo'ling!"
    )
    markup = types.InlineKeyboardMarkup(row_width=1)
    markup.add(
        types.InlineKeyboardButton("📤 Telegram orqali do'stlarga yuborish", url=SHARE_LINK),
        types.InlineKeyboardButton("🏠 Bosh sahifaga qaytish", callback_data="nav_home"),
    )
    send_or_edit_photo(
        chat_id=chat_id,
        filename="qr_share.jpg",
        caption=text,
        reply_markup=markup,
    )


# ---------------------------------------------------------------------------
# VIKTORINA (QUIZ) LOGIKASI
# ---------------------------------------------------------------------------
def start_quiz_session(chat_id: int, user_id: int):
    reset_user_quiz(user_id)
    send_quiz_step(chat_id, user_id, 0)


def send_quiz_step(chat_id: int, user_id: int, q_index: int):
    if q_index >= len(QUIZ_QUESTIONS):
        # Viktorina yakuni va natijalar
        stats = get_user_stats(user_id)
        score = stats.get("quiz_score", 0) if stats else 0
        total = len(QUIZ_QUESTIONS)
        percent = int((score / total) * 100)

        badge = "🥇 Oltin Daraja (Tarix dahosi)" if percent >= 80 else ("🥈 Kumush Daraja (Bilimdon)" if percent >= 50 else "🥉 Bronza Daraja (Sayohatchi)")

        text = (
            f"🎉 <b>VIKTORINA YAKUNLANDI!</b>\n\n"
            f"👤 Ishtirokchi: <b>{stats.get('first_name', 'Foydalanuvchi')}</b>\n"
            f"📊 Natija: <b>{score} / {total}</b> ta to'g'ri javob ({percent}%)\n"
            f"🏅 Sizning unvoningiz: <b>{badge}</b>\n\n"
            f"Bilimlaringizni do'stlaringizga ham ko'rsatmoqchimisiz? Havolani ulashing!"
        )
        markup = types.InlineKeyboardMarkup(row_width=1)
        markup.add(
            types.InlineKeyboardButton("🔄 Qaytadan topshirish", callback_data="quiz_start"),
            types.InlineKeyboardButton("🏆 Peshqadamlar reytingi", callback_data="quiz_lead"),
            types.InlineKeyboardButton("🏠 Bosh menyu", callback_data="nav_home"),
        )
        bot.send_message(chat_id, text, reply_markup=markup)
        return

    q = QUIZ_QUESTIONS[q_index]
    text = (
        f"<b>🧩 VIKTORINA: {q_index + 1}-SAVOL ({len(QUIZ_QUESTIONS)} tadan):</b>\n\n"
        f"<b>{q['question']}</b>"
    )
    markup = get_quiz_question_markup(q_index)
    bot.send_message(chat_id, text, reply_markup=markup)


# ---------------------------------------------------------------------------
# CALLBACK QUERY HANDLERLARI (INLINE TUGMALARNI BOSGANDA)
# ---------------------------------------------------------------------------
@bot.callback_query_handler(func=lambda call: True)
def handle_callback_query(call: types.CallbackQuery):
    data = call.data
    user_id = call.from_user.id
    chat_id = call.message.chat.id
    save_user(user_id, call.from_user.username, call.from_user.first_name)

    try:
        if data == "nav_home":
            bot.answer_callback_query(call.id)
            show_main_home(chat_id)

        elif data.startswith("era_view:"):
            bot.answer_callback_query(call.id)
            era_id = data.split(":", 1)[1]
            show_era(chat_id, era_id)

        elif data == "eras_list":
            bot.answer_callback_query(call.id)
            text = "⏳ <b>Barcha xronologik davrlar ro'yxati:</b>\nQaysi davrga sayohat qilmoqchisiz?"
            markup = get_eras_list_inline_markup()
            bot.send_message(chat_id, text, reply_markup=markup)

        elif data.startswith("era_invs:"):
            bot.answer_callback_query(call.id)
            era_id = data.split(":", 1)[1]
            show_era_inventions(chat_id, era_id)

        elif data.startswith("era_figures:"):
            bot.answer_callback_query(call.id)
            era_id = data.split(":", 1)[1]
            show_figures_menu(chat_id, page=0, era_filter=era_id)

        elif data.startswith("era_share:"):
            bot.answer_callback_query(call.id)
            era_id = data.split(":", 1)[1]
            era = ERAS.get(era_id, {})
            share_url = f"https://t.me/share/url?url={BOT_LINK}?start=era_{era_id}&text={urllib.parse.quote(era.get('short_title', 'Tarixiy davr'))}"
            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton("📤 Telegram orqali yuborish", url=share_url))
            bot.send_message(chat_id, f"🔗 <b>{era.get('title')}</b> havolasi:", reply_markup=markup)

        elif data.startswith("fig_view:"):
            bot.answer_callback_query(call.id)
            slug = data.split(":", 1)[1]
            show_figure(chat_id, slug)

        elif data.startswith("fig_quote:"):
            slug = data.split(":", 1)[1]
            fig = HISTORICAL_FIGURES.get(slug, {})
            bot.answer_callback_query(call.id, text=fig.get("quote", "Hikmat"), show_alert=True)

        elif data == "figs_list":
            bot.answer_callback_query(call.id)
            show_figures_menu(chat_id, page=0)

        elif data.startswith("figs_page:"):
            bot.answer_callback_query(call.id)
            parts = data.split(":")
            page = int(parts[1])
            f_era = None if parts[2] == "all" else parts[2]
            show_figures_menu(chat_id, page=page, era_filter=f_era)

        elif data == "invs_list":
            bot.answer_callback_query(call.id)
            show_inventions_menu(chat_id)

        elif data.startswith("inv_view:"):
            bot.answer_callback_query(call.id)
            slug = data.split(":", 1)[1]
            show_invention(chat_id, slug)

        elif data == "quiz_start":
            bot.answer_callback_query(call.id)
            start_quiz_session(chat_id, user_id)

        elif data.startswith("quiz_ans:"):
            parts = data.split(":")
            q_index = int(parts[1])
            chosen_opt = int(parts[2])
            q = QUIZ_QUESTIONS[q_index]

            is_correct = (chosen_opt == q["correct_index"])
            update_quiz_score(user_id, is_correct)

            result_icon = "✅ TO'G'RI!" if is_correct else "❌ NOTO'G'RI!"
            feedback_text = (
                f"{result_icon}\n\n"
                f"<b>Sharh:</b> {q['explanation']}"
            )
            bot.answer_callback_query(call.id, text=result_icon, show_alert=False)

            markup = types.InlineKeyboardMarkup(row_width=1)
            markup.add(
                types.InlineKeyboardButton("Keyingi savol ➡️", callback_data=f"quiz_next:{q_index + 1}")
            )
            bot.send_message(chat_id, feedback_text, reply_markup=markup)

        elif data.startswith("quiz_next:"):
            bot.answer_callback_query(call.id)
            next_q = int(data.split(":", 1)[1])
            send_quiz_step(chat_id, user_id, next_q)

        elif data == "quiz_lead":
            bot.answer_callback_query(call.id)
            show_leaderboard(chat_id)

        elif data == "screen_share":
            bot.answer_callback_query(call.id)
            show_share_screen(chat_id)

    except Exception as e:
        logger.error(f"Callback query xatosi ({data}): {e}")


def show_main_home(chat_id: int):
    caption = (
        f"🏛️ <b>«TARIXGA SAYOHAT BOTI» ASOSIY MENYUSI</b>\n\n"
        f"Qaysi bo'limga o'tishni xohlaysiz?\n"
        f"• ⏳ <b>Vaqt mashinasi:</b> Xronologik davrlar bo'ylab sayohat\n"
        f"• 💡 <b>Buyuk kashfiyotlar:</b> Olovdan to Sun'iy Intellektgacha\n"
        f"• 👤 <b>Tarixiy shaxslar:</b> Allomalar va ixtirochilar\n"
        f"• 🧩 <b>Viktorina:</b> Tarixiy bilimingizni sinash\n\n"
        f"🔗 Havola: {BOT_LINK}"
    )
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(
        types.InlineKeyboardButton("⏳ Vaqt mashinasi", callback_data="era_view:jurassic"),
        types.InlineKeyboardButton("💡 Buyuk kashfiyotlar", callback_data="invs_list"),
    )
    markup.add(
        types.InlineKeyboardButton("👤 Tarixiy shaxslar", callback_data="figs_list"),
        types.InlineKeyboardButton("🧩 Viktorina", callback_data="quiz_start"),
    )
    send_or_edit_photo(
        chat_id=chat_id,
        filename="main_banner.jpg",
        caption=caption,
        reply_markup=markup,
    )


def show_era_inventions(chat_id: int, era_id: str):
    era = ERAS.get(era_id, {})
    matched = [(s, inv) for s, inv in INVENTIONS.items() if inv.get("era_id") == era_id]
    if not matched:
        bot.send_message(chat_id, f"Bu davr bo'yicha kashfiyotlar ro'yxati yangilanmoqda.")
        return

    text = f"💡 <b>{era.get('short_title')}dagi buyuk kashfiyotlar:</b>\n\n"
    markup = types.InlineKeyboardMarkup(row_width=1)
    for s, inv in matched:
        text += f"• <b>{inv['name']}</b> ({inv['year']}) — {inv['inventor']}\n"
        markup.add(types.InlineKeyboardButton(inv["name"], callback_data=f"inv_view:{s}"))

    markup.add(types.InlineKeyboardButton("🔙 Davrga qaytish", callback_data=f"era_view:{era_id}"))
    bot.send_message(chat_id, text, reply_markup=markup)


def show_leaderboard(chat_id: int):
    leaders = get_leaderboard(limit=10)
    lines = ["🏆 <b>VIKTORINA PESHQADAMLAR JADVALI:</b>\n"]
    medals = ["🥇", "🥈", "🥉", "4.", "5.", "6.", "7.", "8.", "9.", "10."]
    for i, l in enumerate(leaders):
        name = l["first_name"] or l["username"] or "Sayohatchi"
        lines.append(f"{medals[i]} <b>{name}</b> — {l['quiz_score']} / {l['quiz_total']} ball")
    if not leaders:
        lines.append("Hozircha natijalar mavjud emas. Birinchi bo'lib testdan o'ting!")

    markup = types.InlineKeyboardMarkup(row_width=1)
    markup.add(
        types.InlineKeyboardButton("🧩 Testni boshlash", callback_data="quiz_start"),
        types.InlineKeyboardButton("🏠 Bosh sahifa", callback_data="nav_home"),
    )
    bot.send_message(chat_id, "\n".join(lines), reply_markup=markup)


# ---------------------------------------------------------------------------
# BOT METAMA'LUMOTLARINI SOZLASH (Telegram API)
# ---------------------------------------------------------------------------
def configure_bot_profile():
    try:
        commands = [
            types.BotCommand("start", "⏳ Botni ishga tushirish va Bosh menyu"),
            types.BotCommand("help", "📖 Bot haqida va foydalanish qo'llanmasi"),
        ]
        bot.set_my_commands(commands)
        bot.set_my_short_description(
            "⏳ Tarixga Sayohat Boti — Yura davridan to zamonaviy Sun'iy Intellektgacha bo'lgan tarixiy ensiklopediya!"
        )
        bot.set_my_description(
            "⏳ Tarixga Sayohat Botiga xush kelibsiz!\n\n"
            "Ushbu botda:\n"
            "🦖 Yura va Mezozoy davri (Dinozavrlar)\n"
            "🪨 Tosh davri va Olov kashfiyoti\n"
            "🏺 Qadimgi Sivilizatsiyalar (Piramidalar, G'ildirak, Qog'oz)\n"
            "🌟 Sharq Uyg'onishi (Al-Xorazmiy, Ibn Sino, Beruniy, Ulug'bek)\n"
            "🎨 Renessans va Bosmaxona (Leonardo da Vinchi, Gutenberg, Galiley)\n"
            "⚙️ Sanoat Inqilobi (Nyuton, Uatt, Tesla, Edison)\n"
            "🚀 XX asr: Aviatsiya, Kosmos va Axborot asri\n"
            "🤖 XXI asr: Sun'iy Intellekt va Kelajak!\n\n"
            "🔗 Link: https://t.me/Tarixga_sayoxatchibot\n"
            "👇 Boshlash uchun «START» tugmasini bosing!"
        )
        logger.info("Bot profili muvaffaqiyatli sozlandi.")
    except Exception as e:
        logger.warning(f"Bot profilini sozlashda ogohlantirish: {e}")


# ---------------------------------------------------------------------------
# SINGLE-INSTANCE TCP QULFI VA ISHGA TUSHIRISH
# ---------------------------------------------------------------------------
_INSTANCE_LOCK_SOCKET = None


def acquire_single_instance_lock(port: int = 47892) -> bool:
    """Bitta kompyuterda ikkita bot bir vaqtda ishlab 409 Conflict bermasligi uchun."""
    global _INSTANCE_LOCK_SOCKET
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.bind(("127.0.0.1", port))
        s.listen(1)
        _INSTANCE_LOCK_SOCKET = s
        return True
    except OSError:
        s.close()
        return False


def run_bot():
    if not acquire_single_instance_lock():
        logger.info("Tarixga Sayohat Boti allaqachon ishlab turibdi (Single-instance lock). Chiqilmoqda.")
        return

    init_db()

    try:
        from keep_alive import start_keep_alive_server
        start_keep_alive_server(8081)
        logger.info("🌐 Keep-Alive HTTP server ishga tushdi (port 8081)")
    except Exception as e:
        logger.warning(f"Keep-alive server ogohlantirish: {e}")

    while True:
        try:
            bot.remove_webhook()
            configure_bot_profile()
            me = bot.get_me()
            logger.info(f"🚀 {BOT_NAME} (@{me.username}, ID: {me.id}) 24/7 rejimida ishga tushdi! Havola: {BOT_LINK}")
            break
        except Exception as e:
            logger.warning(f"Internet yoki Telegram API kutilmoqda: {e}")
            time.sleep(5)

    while True:
        try:
            bot.infinity_polling(
                timeout=30,
                long_polling_timeout=25,
                skip_pending=False,
                allowed_updates=["message", "callback_query"],
            )
        except Exception as e:
            logger.error(f"24/7 Polling uzilishi, 4 soniyada qayta ulanmoqda: {e}")
            time.sleep(4)


if __name__ == "__main__":
    run_bot()
