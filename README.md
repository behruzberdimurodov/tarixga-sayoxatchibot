# ⏳ Tarixga Sayohat Boti (@Tarixga_sayoxatchibot)

Mukammal, 24/7 uzluksiz ishlovchi, ko'p foydalanuvchili (multi-user), Yura davridan to zamonaviy Sun'iy Intellektgacha bo'lgan insoniyat tarixini, buyuk kashfiyotlarni va allomalarni o'zida jamlagan Telegram ensiklopediyasi.

---

## 🌟 Asosiy Xususiyatlar va Imkoniyatlar

1. **🦖 Yura Davridan Boshlab O'sib Boruvchi Xronologiya:**
   - **1-davr:** 🦖 Yura va Mezozoy davri (Dinozavrlar erasi, T-Rex, Richard Ouen)
   - **2-davr:** 🪨 Tosh davri va Ibtidoiy jamoa (Olov kashfiyoti, Neolit inqilobi)
   - **3-davr:** 🏺 Qadimgi Sivilizatsiyalar (Piramidalar, G'ildirak, Qog'oz, Arximed, Tsay Lun)
   - **4-davr:** 🌟 Sharq Uyg'onishi (Al-Xorazmiy, Ibn Sino, Beruniy, Mirzo Ulug'bek)
   - **5-davr:** 🎨 Renessans va Dengiz sayohatlari (Gutenberg bosmaxonasi, Leonardo da Vinchi, Galiley)
   - **6-davr:** ⚙️ Sanoat Inqilobi va Fan (Nyuton, Uatt, Tesla, Edison, Mendeleyev)
   - **7-davr:** 🚀 XX asr: Kosmos, Aviatsiya va Atom (Samolyot, Penitsillin, Eynshteyn, Gagarin, Tyuring)
   - **8-davr:** 🤖 XXI asr: Raqamli Dunyo va Sun'iy Intellekt (AI, Internet, Kvant kompyuterlari)

2. **💡 Buyuk Kashfiyotlar Ensiklopediyasi:**
   - Olov, G'ildirak, Yozuv, Qog'oz, Algebra, Bosmaxona, Teleskop, Bug' mashinasi, Elektr, Telefon, Samolyot, Penitsillin, Kompyuter, Kosmik parvoz, Internet va Sun'iy Intellekt.

3. **👤 Allomalar va Kashfiyotchilar Galereyasi:**
   - 20 dan ortiq buyuk olimlarning tarjimai holi, kashfiyotlari, hikmatlari va nufuzli arxiv fotosuratlari.

4. **🖼️ Muzey Darajasidagi Kartochkalar (Internetdan suratlar):**
   - Har bir davr va kashfiyotchi uchun yuqori sifatli vizual kartochkalar.
   - Telegram Cloud `file_id` kesh tizimi orqali har bir foydalanuvchiga 0.1 soniyada yuboriladi.

5. **🧩 Interaktiv Viktorina (15 ta test savoli):**
   - Ballar hisobi, darajalar (Oltin, Kumush, Bronza) va Peshqadamlar reytingi.

6. **🔍 Aqlli Qidiruv Tizimi:**
   - Foydalanuvchi xohlagan so'zini (masalan: `nyuton`, `dinozavr`, `olov`, `tesla`, `beruniy`, `samolyot`) yozganda darhol topib beradi. Kirill va lotin yozuvlarini avtomatik tushunadi.

7. **🔗 Havolalar va Deep-Linking:**
   - Asosiy bot linki: `https://t.me/Tarixga_sayoxatchibot`
   - Telegram orqali do'stlarga bir bosishda ulashish (Share link).
   - Har bir davr va alloma uchun shaxsiy chuqur havolalar (`/start era_jurassic`, `/start fig_tesla` va hk.).

8. **⚡ Hammada Birdek Ishlash (Ko'p oqimli & 24/7):**
   - 16 oqimli multi-thread rejim (`telebot.TeleBot(..., threaded=True, num_threads=16)`).
   - SQLite DB (`tarix_storage.db`) orqali xavfsiz multi-user boshqaruvi.
   - GitHub Actions bulutli serveri (`.github/workflows/bot_24_7.yml`) orqali 24/7 uzluksiz ishlash.

---

## 🚀 Ishga Tushirish

### 1. Mahalliy kompyuterda:
```bash
pip install -r requirements.txt
python download_images.py
python bot.py
```

### 2. Oynasiz (Fon rejimida) ishga tushirish:
`start_24_7_background.vbs` faylini ishga tushiring.

### 3. GitHub Cloud orqali 24/7 ishlatish:
Kodni GitHub repozitoriyasiga yuklaganingizda, `.github/workflows/bot_24_7.yml` avtomatik ishga tushadi va kompyuteringiz o'chiq bo'lsa ham bot 24/7 ishlayveradi.
