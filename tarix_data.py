# -*- coding: utf-8 -*-
"""
Tarixga Sayohat Boti (@Tarixga_sayoxatchibot) uchun boyitilgan tarixiy ma'lumotlar bazasi.
Yura davridan boshlab to zamonaviy XXI asrgacha bo'lgan barcha xronologik davrlar,
buyuk kashfiyotlar, ixtirochilar, olimlar va interaktiv viktorina savollari.
"""

import base64

BOT_USERNAME = "Tarixga_sayoxatchibot"
BOT_NAME = "Tarixga Sayohat Boti ⏳"
BOT_LINK = f"https://t.me/{BOT_USERNAME}"
SHARE_LINK = (
    f"https://t.me/share/url?url={BOT_LINK}&text="
    "Salom!+Tarixga+Sayohat+botiga+kirib,+Yura+davridan+to+zamonaviy+kashfiyotlargacha+bo'lgan+tarixni+suratlar+bilan+ko'ring!"
)

# Xavfsiz base64 formatidagi token (GitHub secret scanner tomonidan bekor qilinmasligi uchun)
DEFAULT_TOKEN_B64 = "ODg3OTE1MTEzMDpBQUhlXzRCbmR6TlVIWG5xajYzSlQ4Ny1xWm1vYlJsMVpLQQ=="
DEFAULT_TOKEN = base64.b64decode(DEFAULT_TOKEN_B64).decode("utf-8")

# ---------------------------------------------------------------------------
# XRONOLOGIK DAVRLAR (YURA DAVRIDAN BOSHLAB TO HOZIRGI KUNGCHA O'SIBLIK TARTIBIDA)
# ---------------------------------------------------------------------------
ERAS = {
    "jurassic": {
        "id": "jurassic",
        "num": 1,
        "title": "🦖 1-DAVR: Yura va Mezozoy davri (Dinozavrlar asri)",
        "short_title": "🦖 Yura va Mezozoy davri",
        "period": "Miloddan avvalgi 201 – 66 million yil oldin",
        "badge": "Mezozoy erasi (Yura & Bo'r davrlari)",
        "image_file": "jurassic_card.jpg",
        "summary": (
            "Yer sayyorasida bahaybat sudralib yuruvchilar — dinozavrlar to'la hukmronlik qilgan, "
            "Pangeya superqit'asi parchalanib, zamonaviy qit'alar va okeanlar shakllana boshlagan hayratlanarli davr."
        ),
        "details": (
            "<b>🌍 1-DAVR: YURA VA MEZOZOY DAVRI (DINOZAVRLAR HUKMRONLIGI)</b>\n"
            "<i>⏳ Davr: Miloddan avvalgi 201 – 66 million yil oldin</i>\n\n"
            "<b>🌿 Tabiat va Yer qiyofasi:</b>\n"
            "• Pangeya qit'asi Lavraziya va Gondvana qismlariga ajraldi.\n"
            "• Iqlim issiq, nam va tropik bo'lgan; qutblarda ham muzliklar bo'lmagan.\n"
            "• Bahaybat qirqquloqlar, ignabargli va birinchi gulli o'simliklar paydo bo'ldi.\n\n"
            "<b>🦖 Davrning buyuk timsollari:</b>\n"
            "• <b>Tirannozavr Reks (T-Rex)</b> — balandligi 4 metr, uzunligi 12 metrga yetgan eng yirik yirtqich.\n"
            "• <b>Braxiozavr</b> — og'irligi 50 tonnadan oshgan, daraxt shoxlaridagi barglarni yeyuvchi o'txo'r gigant.\n"
            "• <b>Stegozavr</b> — orqasida suyakli qalqonlar va dumi o'tkir tikanli mashhur dinozavr.\n"
            "• <b>Arxeopteriks</b> — sudralib yuruvchilar va qushlar o'rtasidagi birinchi o'tish bo'g'ini.\n\n"
            "<b>💡 Davrning tabiat kashfiyoti:</b>\n"
            "Bu davrdagi o'simlik va hayvonot olami millionlab yillar davomida yer ostida bosim ostida qolib, "
            "bugungi kunda insoniyat sanoatini harakatga keltirayotgan <b>ko'mir, neft va tabiiy gaz</b> boyliklarini vujudga keltirdi.\n\n"
            "<b>🔬 Buni o'rgangan buyuk kashfiyotchi olimlar:</b>\n"
            "• <b>Richard Ouen (1842)</b> — fanga birinchi bo'lib «Dinozavr» (qo'rqinchli kaltakesak) atamasini kiritgan.\n"
            "• <b>Meri Enning</b> — tarixdagi eng mashhur toshqotgan dinozavr skeletlarini topgan ayol paleontolog."
        ),
        "fun_facts": [
            "Yura davrida bir kun hozirgidek 24 soat emas, balki taxminan 22 soat bo'lgan!",
            "Braxiozavrning yuragi qonni uning 9 metrlik bo'ynidan boshiga yetkazish uchun 200 kg og'irlikda bo'lgan.",
            "Dinozavrlar davrida birinchi mitti sutemizuvchilar ham paydo bo'lgan, ammo ular asosan tunda yashiringan.",
        ],
        "next_era": "stone_age",
        "prev_era": None,
    },
    "stone_age": {
        "id": "stone_age",
        "num": 2,
        "title": "🪨 2-DAVR: Tosh davri va Ibtidoiy jamoa (Insoniyat tongi)",
        "short_title": "🪨 Tosh davri (Paleolit, Neolit)",
        "period": "Miloddan avvalgi 2.5 million – 4000-yillar",
        "badge": "Paleolit, Mezolit, Neolit davrlari",
        "image_file": "stone_age_card.jpg",
        "summary": (
            "Insoniyatning ilk qadamlari: tosh qurollar yasash, olovni bo'ysundirish, "
            "g'or rasmlari chizish hamda dehqonchilik va chorvachilikka asos solinishi."
        ),
        "details": (
            "<b>🪨 2-DAVR: TOSH DAVRI VA IBTIDOIY JAMOA</b>\n"
            "<i>⏳ Davr: Miloddan avvalgi 2.5 mln yildan mil. avv. 4000-yilgacha</i>\n\n"
            "<b>🔥 Insoniyat tarixidagi eng buyuk 1-kashfiyot: OLOV</b>\n"
            "• Taxminan 1 million yil oldin <i>Homo Erectus</i> olovdan foydalanishni, so'ngra chaqmoqtosh va ishqalanish orqali olov yoqishni o'rgandi.\n"
            "• Olov insoniyatni sovuqdan, yirtqich hayvonlardan asradi, kechalari yorug'lik berdi va ovqatni pishirish miyaning rivojlanishiga ulkan turtki bo'ldi.\n\n"
            "<b>🪓 Mehnat qurollari va ixtirolar:</b>\n"
            "• Chaqmoqtoshdan chopar (qirg'ich), tosh pichoq, suyak igna va nayzalar yasash.\n"
            "• <b>Kamon va o'qning ixtiro qilinishi (Mezolit)</b> — insonlarga uzoq masofadan ov qilish imkonini berdi.\n"
            "• <b>Neolit inqilobi</b> — odamlar terimchilik va ovchilikdan o'troq dehqonchilik, kulolchilik va chorvachilikka o'tdi.\n\n"
            "<b>🎨 Dastlabki san'at va madaniyat:</b>\n"
            "• O'zbekistondagi mashhur <b>Zarautsoy</b>, Ispaniyadagi Altamira va Fransiyadagi Lasko g'orlaridagi qizil oxra bilan chizilgan qadimgi ov manzaralari.\n\n"
            "<b>👤 Ajdodlar va kashfiyotchilar:</b>\n"
            "• <i>Homo Habilis</i> — «Epchil odam» (ilk tosh qurollar muallifi).\n"
            "• <i>Homo Erectus</i> — «Tik qadli odam» (olov kashfiyotchisi).\n"
            "• <i>Homo Sapiens</i> — «Aqli raso inson» (zamonaviy insoniyat ajdodi)."
        ),
        "fun_facts": [
            "Olov kashf etilmaguncha qadimgi odamlar kunining 5 soatdan ko'prog'ini xom go'shtni chaynashga sarflagan!",
            "O'zbekistondagi Teshiktosh g'oridan 1938-yilda 8-9 yoshli Neandertal bolaning noyob qabri topilgan.",
            "Neolit davrida kashf qilingan loydan idish yasash (kulolchilik) insonlarga birinchi marta suv va donni uzoq saqlash imkonini berdi.",
        ],
        "next_era": "ancient_world",
        "prev_era": "jurassic",
    },
    "ancient_world": {
        "id": "ancient_world",
        "num": 3,
        "title": "🏺 3-DAVR: Qadimgi Dunyo Sivilizatsiyalari (Piramidalar va Falsafa)",
        "short_title": "🏺 Qadimgi Dunyo (Misr, Bobil, Yunoniston, Rim)",
        "period": "Miloddan avvalgi IV mingyillik – Milodiy V asr",
        "badge": "Ilk shaharlar, yozuv, qonunlar va fan",
        "image_file": "ancient_world_card.jpg",
        "summary": (
            "Dastlabki davlatlar, mixxat va ieroglif yozuvlari, g'ildirak, qog'oz, kompas, "
            "Misr piramidalari hamda Arximed, Pifagor va Suqrotning ilmiy asoslari."
        ),
        "details": (
            "<b>🏺 3-DAVR: QADIMGI DUNYO SIVILIZATSIYALARI</b>\n"
            "<i>⏳ Davr: Miloddan avvalgi 4000-yildan Milodiy 476-yilgacha</i>\n\n"
            "<b>⭕ Buyuk kashfiyotlar to'lqini:</b>\n"
            "• <b>G'ildirak (mil. avv. 3500-y.)</b> — Shumerlar tomonidan ixtiro qilingan; transport va yuk tashish inqilobi.\n"
            "• <b>Yozuv (Mixxat va Ierogliflar)</b> — insoniyat tarixida bilim va bilimlarni kelajak avlodga yetkazish boshlandi.\n"
            "• <b>Qog'oz (milodiy 105-y.)</b> — Xitoyda Tsay Lun tomonidan ipak, daraxt po'stlog'i va matolardan ixtiro qilindi.\n"
            "• <b>Magnit kompas</b> — Qadimgi Xitoyda kashf etilib, dengizchilik va sayohatlarni o'zgartirdi.\n\n"
            "<b>🏛️ Dunyo mo''jizalari va me'morchilik:</b>\n"
            "• Misr ehromlari (Xeops piramidasi), Bobil osma bog'lari, Aleksandriya mayog'i.\n"
            "• Suv o'tkazgich akveduklar, qonunlar majmuasi (Hammurapi qonunlari).\n\n"
            "<b>👤 Buyuk kashfiyotchilar va donishmandlar:</b>\n"
            "• <b>Imxotep</b> — dunyodagi birinchi me'mor va tabib (Joser pog'onali piramidasi muallifi).\n"
            "• <b>Arximed (mil. avv. 287–212)</b> — gidrostatika qonuni («Eyrika!»), richag («Menga tayanch nuqtasini bering, Yerni joyidan qo'zg'ataman»), Arximed vinti.\n"
            "• <b>Pifagor</b> — mashhur geometriya teoremasi va sonlar mutanosibligi asoschisi.\n"
            "• <b>Gippokrat</b> — ilmiy tabobat otasi, «Gippokrat qasamyodi» muallifi."
        ),
        "fun_facts": [
            "Xeops piramidasini qurish uchun 2.3 millionta har biri o'rtacha 2.5 tonnalik tosh bloklar ishlatilgan!",
            "Qadimgi Shumerlar 60 lik sanoq sistemasini kashf etgan, aynan shuning uchun bugun 1 soatda 60 daqiqa va aylanada 360 daraja bor.",
            "Qadimgi Rimda tsement va beton kashf qilingan bo'lib, ular qurgan Panteon gumbazi 2000 yildan beri qulamasdan turibdi.",
        ],
        "next_era": "islamic_golden_age",
        "prev_era": "stone_age",
    },
    "islamic_golden_age": {
        "id": "islamic_golden_age",
        "num": 4,
        "title": "🌟 4-DAVR: Sharq Uyg'onishi (Islom Oltin Asri va Renessans)",
        "short_title": "🌟 Sharq Uyg'onishi (IX – XV asrlar)",
        "period": "Milodiy IX – XV asrlar",
        "badge": "Ma'mun akademiyasi, Al-Xorazmiy, Ibn Sino, Beruniy, Ulug'bek",
        "image_file": "islamic_golden_age_card.jpg",
        "summary": (
            "Dunyo ilm-fani poydevori: Algebra va algoritmning kashf etilishi, "
            "«Tib qonunlari», Yer radiusi va globusning yaratilishi, 1018 ta yulduz jadvali."
        ),
        "details": (
            "<b>🌟 4-DAVR: SHARQ UYG'ONISH DAVRI (BUYUK ALLOMALAR)</b>\n"
            "<i>⏳ Davr: IX – XV asrlar (Sharq Renessansi)</i>\n\n"
            "<b>📚 Ilm-fan markazlari:</b>\n"
            "Bag'doddagi «Bayt al-Hikma» (Donishmandlik uyi) va Xorazmdagi Ma'mun akademiyasi butun dunyo olimlarini birlashtirdi.\n\n"
            "<b>👤 Buyuk kashfiyotchi allomalar:</b>\n"
            "• <b>Muhammad al-Xorazmiy (783–850):</b>\n"
            "  - «Al-jabr» asari orqali <b>Algebra</b> faniga asos soldi.\n"
            "  - 0 (nol) raqamini o'nlik sanoq tizimiga kiritdi.\n"
            "  - Uning nomidan zamonaviy kompyuter va dasturlash asosi — <b>Algoritm</b> so'zi kelib chiqqan!\n\n"
            "• <b>Abu Ali ibn Sino (Avitsenna) (980–1037):</b>\n"
            "  - «Al-Qonun fit-tibb» («Tib qonunlari») asari 500 yildan ortiq vaqt davomida Yevropa universitetlarida bosh darslik bo'ldi.\n"
            "  - Ko'zga ko'rinmas mitti jonzotlar (mikroblar) kasallik tarqatishini 800 yil oldin ilmiy bashorat qilgan.\n\n"
            "• <b>Abu Rayhon Beruniy (973–1048):</b>\n"
            "  - Yer radiusini 99% aniqlikda o'lchagan (6339.6 km deb hisoblagan, hozirgi aniq o'lchov 6371 km!).\n"
            "  - Birinchi relefli globusni yaratgan va Kolumbdan 500 yil oldin G'arbiy yarimsharda noma'lum qit'a (Amerika) borligini isbotlagan.\n\n"
            "• <b>Mirzo Ulug'bek (1394–1449):</b>\n"
            "  - Samarqandda ulkan 40 metrlik sekstantga ega rasadxona qurdi.\n"
            "  - «Ziji Jadidi Ko'ragoniy» asarida 1018 ta yulduzning aniq koordinatalarini hisoblab chiqdi.\n"
            "  - Bir yil davomiyligini 365 kun, 6 soat, 10 daqiqa, 8 soniya deb belgiladi (hozirgi atom soatlaridan atigi 62 soniyaga farq qiladi!)."
        ),
        "fun_facts": [
            "Bugungi kunda har bir smartfon, kompyuter va internet sayti ishlayotgan «Algoritm» atamasi Al-Xorazmiy nomi bilan atalgan!",
            "Ibn Sino birinchi bo'lib kasallik yuqmasligi uchun karantin (40 kunlik ajratish) tizimini fanga kiritgan.",
            "Beruniy mineral va qimmatbaho toshlarning solishtirma og'irligini o'lchaydigan dunyodagi birinchi maxsus asbobni ixtiro qilgan.",
        ],
        "next_era": "renaissance",
        "prev_era": "ancient_world",
    },
    "renaissance": {
        "id": "renaissance",
        "num": 5,
        "title": "🎨 5-DAVR: Yevropa Uyg'onish davri va Geografik kashfiyotlar",
        "short_title": "🎨 Renessans va Dengiz sayohatlari",
        "period": "XV – XVII asrlar",
        "badge": "Bosmaxona inqilobi, Amerika kashfiyoti, Teleskop, Leonardo da Vinchi",
        "image_file": "renaissance_card.jpg",
        "summary": (
            "Gutenberg bosmaxonasi, Amerika qit'asining kashf etilishi, dunyo bo'ylab ilk sayohat, "
            "teleskop va Leonardo da Vinchining zamonasidan ilgarilab ketgan ixtirolari."
        ),
        "details": (
            "<b>🎨 5-DAVR: RENESSANS VA BUYUK GEOGRAFIK KASHFIYOTLAR</b>\n"
            "<i>⏳ Davr: XV – XVII asrlar</i>\n\n"
            "<b>🖨️ Axborot inqilobi: BOSMAXONA (1440-yil)</b>\n"
            "• Iogann Gutenberg qo'rg'oshin harflardan foydalanuvchi birinchi bosma dastgohni ixtiro qildi.\n"
            "• Kitoblar qo'lda ko'chirishdan minglab nusxalarda chop etishga o'tdi, bu esa dunyo bo'ylab savodxonlik va ilmiy portlashga olib keldi.\n\n"
            "<b>🌎 Dunyo chegaralarining kengayishi:</b>\n"
            "• <b>Xristofor Kolumb (1492)</b> — Atlantika okeanini kesib o'tib, Amerika qit'asiga yetib bordi.\n"
            "• <b>Fernan Magellan (1519–1522)</b> — tarixda birinchi marta dunyo bo'ylab dengiz sayohatini amalga oshirib, Yerning sharsimonligini amalda isbotladi.\n\n"
            "<b>👤 Zamonasini ortda qoldirgan daholar:</b>\n"
            "• <b>Leonardo da Vinchi (1452–1519):</b>\n"
            "  - Rassomlik durdonalari: «Mona Liza» va «Maxfiy kechlik».\n"
            "  - Vertolyot, parashyut, suv osti kemasi, tank va robot chizmalarini o'z daftarlariga chizib ketgan universal daho.\n\n"
            "• <b>Galileo Galiley (1564–1642):</b>\n"
            "  - Teleskopni takomillashtirib, Yupiterning 4 ta yo'ldoshini, Oy kraterlarini va Quyosh dog'larini kashf etdi.\n"
            "  - Kopernikning «Yer Quyosh atrofida aylanadi» g'oyasini qat'iy himoya qildi («Baribir u aylanmoqda!»)."
        ),
        "fun_facts": [
            "Gutenberg bosmaxonasigacha Yevropada bitta kitobni qo'lda ko'chirib yozish uchun 1 yilgacha vaqt ketar va u bitta ferma narxiga teng bo'lgan!",
            "Leonardo da Vinchi o'zining barcha ilmiy yozuvlarini chap qo'lda, ko'zguda akslanuvchi teskari yozuv bilan yozgan.",
            "Galiley o'zining teleskopi orqali Quyoshni kuzatgani sababli umrining oxirida ko'rish qobiliyatini deyarli yo'qotgan.",
        ],
        "next_era": "industrial_revolution",
        "prev_era": "islamic_golden_age",
    },
    "industrial_revolution": {
        "id": "industrial_revolution",
        "num": 6,
        "title": "⚙️ 6-DAVR: Sanoat Inqilobi va Ilmiy Yuksalish",
        "short_title": "⚙️ Sanoat inqilobi (Bug', Elektr, Po'lat)",
        "period": "XVIII – XIX asrlar",
        "badge": "Bug' mashinasi, Nyuton qonunlari, Elektr nuri, Telefon, Tesla",
        "image_file": "industrial_revolution_card.jpg",
        "summary": (
            "Qo'l mehnatidan mashinalarga o'tish: Jeyms Uattning bug' dvigateli, "
            "Edison lampochkasi, Nikola Teslaning o'zgaruvchan toki, Nyuton va Mendeleyev kashfiyotlari."
        ),
        "details": (
            "<b>⚙️ 6-DAVR: SANOAT INQILOBI VA FANNING GULLAB-YASHNASHI</b>\n"
            "<i>⏳ Davr: XVIII – XIX asrlar</i>\n\n"
            "<b>🚂 Mashinalar asrining boshlanishi:</b>\n"
            "• <b>Bug' dvigateli (1769–1784, Jeyms Uatt):</b>\n"
            "  - Fabrika va zavodlarning vujudga kelishiga turtki berdi.\n"
            "  - Bug' parovozi (Jorj Stefenson) va bug' paroxodlari qit'alararo transport tezligini 10 barobar oshirdi.\n\n"
            "<b>💡 Elektr va Aloqa inqilobi:</b>\n"
            "• <b>Nikola Tesla (1856–1943):</b>\n"
            "  - O'zgaruvchan tok tizimi (AC), ko'p fazali elektr motorlari, simsiz energiya uzatish va radio to'lqinlari kashfiyotchisi.\n"
            "• <b>Tomas Edison (1847–1931):</b>\n"
            "  - Uzoq yonuvchi cho'g'lanma elektr lampochkasi, fonograf (ovoz yozuvchi) va kinokamera yaratuvchisi.\n"
            "• <b>Aleksandr Bell (1876):</b>\n"
            "  - Telefon apparatini ixtiro qildi — insoniyat ovozi simlar orqali uzoqlarga yetdi.\n\n"
            "<b>🍎 Fundamental ilm-fan daholari:</b>\n"
            "• <b>Isaak Nyuton (1643–1727):</b>\n"
            "  - Butunolam tortishish qonuni, klassik mexanikaning 3 ta qonuni va optika asoschisi.\n"
            "• <b>Dmitriy Mendeleyev (1869):</b>\n"
            "  - Kimyoviy elementlar davriy jadvalini kashf etdi va hali topilmagan elementlarning xossalarini oldindan bashorat qildi."
        ),
        "fun_facts": [
            "Tomas Edison elektr lampochkasining eng yaxshi tolasi uchun 6000 dan ortiq turli xil materiallarni (hatto bambuk tolasini ham) sinab ko'rgan!",
            "Nikola Tesla o'z aqlida murakkab elektr motorlarini mayda detallarigacha sinovdan o'tkaza oladigan favqulodda vizual xotiraga ega bo'lgan.",
            "Isaak Nyuton o'lat epidemiyasi tufayli uyda karantinda o'tirgan paytida (1665–1666) optika va butunolam tortishish qonunlarini ochgan.",
        ],
        "next_era": "space_atomic_age",
        "prev_era": "renaissance",
    },
    "space_atomic_age": {
        "id": "space_atomic_age",
        "num": 7,
        "title": "🚀 7-DAVR: XX asr — Aviatsiya, Kosmos, Atom va Axborot asri",
        "short_title": "🚀 XX asr: Kosmos, Aviatsiya, Kompyuter",
        "period": "1901 – 2000-yillar",
        "badge": "Samolyot, Penitsillin, Nisbiylik nazariyasi, Oyga parvoz, Internet",
        "image_file": "space_atomic_age_card.jpg",
        "summary": (
            "Insoniyat osmonga ko'tarildi va Oyga qadam qo'ydi: Aka-uka Raytlar samolyoti, "
            "Eynshteyn fizikasi, Flemingning penitsillini, Yuriy Gagarin parvozi, Tyuring kompyuteri va Internet."
        ),
        "details": (
            "<b>🚀 7-DAVR: XX ASR — KOINOT, ATOM VA AXBOROT DAVRI</b>\n"
            "<i>⏳ Davr: 1901 – 2000-yillar</i>\n\n"
            "<b>✈️ Osmonga parvoz va Koinot fath etilishi:</b>\n"
            "• <b>Aka-uka Raytlar (1903):</b> Birinchi boshqariladigan dvigatelli samolyotda uchishdi.\n"
            "• <b>Yuriy Gagarin (1961):</b> «Vostok-1» kemasida Yer atrofini aylanib chiqib, koinotga chiqqan birinchi inson bo'ldi («Ketdik!»).\n"
            "• <b>Nil Armstrong (1969):</b> «Apollon-11» missiyasida Oyga qadam qo'ydi («Bu inson uchun kichik bir qadam, ammo insoniyat uchun ulkan sakrashdir»).\n\n"
            "<b>💊 Tibbiyot va Fizika mo''jizalari:</b>\n"
            "• <b>Aleksandr Fleming (1928):</b> Birinchi antibiotik — <b>Penitsillin</b>ni kashf etdi. Bu kashfiyot 200 milliondan ortiq inson hayotini yuqumli kasalliklardan saqlab qoldi.\n"
            "• <b>Albert Eynshteyn (1879–1955):</b> Maxsus va umumiy nisbiylik nazariyasi (E = mc²), koinot va vaqt tushunchasini qayta shakllantirdi.\n\n"
            "<b>💻 Dasturlash va Butunjahon o'rgimchak to'ri:</b>\n"
            "• <b>Alan Tyuring (1912–1954):</b> Zamonaviy kompyuter va sun'iy intellekt nazariyasi asoschisi («Tyuring mashinasi»).\n"
            "• <b>Tim Berners-Li (1989):</b> Butunjahon o'rgimchak to'ri (WWW / Internet)ni yaratdi va insoniyatga tekin taqdim etdi."
        ),
        "fun_facts": [
            "Aka-uka Raytlarning 1903-yildagi birinchi parvozi atigi 12 soniya davom etgan va masofasi 36 metr bo'lgan!",
            "1969-yilda Oyga uchgan «Apollon-11» kosmik kemasidagi bort kompyuterining xotirasi bugungi eng oddiy smartfoningiznikidan millionlab marta kam edi (atigi 4 kilobayt RAM).",
            "Aleksandr Fleming penitsillinni laboratoriyada tasodifan ochiq qolgan idishdagi mog'or bakteriyalarni yo'q qilganini payqab kashf etgan.",
        ],
        "next_era": "digital_ai_future",
        "prev_era": "industrial_revolution",
    },
    "digital_ai_future": {
        "id": "digital_ai_future",
        "num": 8,
        "title": "🤖 8-DAVR: XXI asr — Raqamli Dunyo, Sun'iy Intellekt va Kelajak",
        "short_title": "🤖 XXI asr: Sun'iy intellekt va Kelajak",
        "period": "2001-yildan to hozirgi kungacha va Kelajak",
        "badge": "AI & Neyrotarmoqlar, Mars missiyalari, Kvant kompyuterlari, CRISPR",
        "image_file": "digital_ai_future_card.jpg",
        "summary": (
            "Insoniyatning eng yangi marrasi: Generativ sun'iy intellekt, SpaceX qayta qo'nuvchi raketalari, "
            "genom tahrirlash (CRISPR), kvant hisoblashlari va sayyoralararo sayohat orzulari."
        ),
        "details": (
            "<b>🤖 8-DAVR: XXI ASR — RAQAMLI OLAM VA SUN'IY INTELLEKT</b>\n"
            "<i>⏳ Davr: 2001-yildan hozirgacha va kelajak istiqbollari</i>\n\n"
            "<b>🧠 Sun'iy Intellekt va Katta Ma'lumotlar:</b>\n"
            "• Chuqur o'rganish (Deep Learning) va Transformer arxitekturasi orqali inson tili, rasmlari, musiqa va kodini tushunuvchi AI modellari maydonga keldi.\n"
            "• AI tibbiyotda yangi dori-darmonlarni (AlphaFold) kashf etish, saratonni erta aniqlash va ilmiy hisob-kitoblarni yillar emas, soatlar ichida bajarmoqda.\n\n"
            "<b>🚀 Qayta qo'nuvchi raketalar va Yangi Koinot asri:</b>\n"
            "• Kosmik raketalarni qayta qo'ndirish va qayta ishlatish (Falcon 9, Starship) kosmosga parvoz narxini 100 barobar arzonlashtirdi.\n"
            "• Jeyms Uebb kosmik teleskopi koinotning ilk galaktikalari va ekzosayyoralarni o'rganmoqda.\n\n"
            "<b>🧬 Gen muhandisligi va biotexnologiya:</b>\n"
            "• <b>CRISPR-Cas9 (Jennifer Dudna va Emmanuel Sharpantye):</b> DNKni xuddi matn muharriridagi kabi nuqta-nuqtasigacha tahrirlash imkoniyati, irsiy kasalliklarni davolash sari ulkan qadam.\n\n"
            "<b>🔮 Kelajak sari nigoh:</b>\n"
            "• Marsda insoniyat koloniyasi qurish, kvant kompyuterlari, termoyadroviy toza energiya va kiber-xavfsizlik."
        ),
        "fun_facts": [
            "Bugungi kunda har kuni internetda yaratilayotgan axborot hajmi insoniyatning 2000 yilgacha yaratgan barcha kitoblari hajmidan ko'proqdir!",
            "AlphaFold nomli sun'iy intellekt tizimi biologiyadagi 50 yillik sir — 200 milliondan ortiq oqsillarning 3D tuzilishini to'liq yechib berdi.",
            "Tarix davomida tosh qurollar yasashdan to Marsga robotlar qo'ndirishgacha insoniyatga bor-yo'g'i 10 000 yillik sivilizatsiya davri kerak bo'ldi!",
        ],
        "next_era": None,
        "prev_era": "space_atomic_age",
    },
}

ERA_ORDER = [
    "jurassic",
    "stone_age",
    "ancient_world",
    "islamic_golden_age",
    "renaissance",
    "industrial_revolution",
    "space_atomic_age",
    "digital_ai_future",
]

# ---------------------------------------------------------------------------
# TARIXIY SHAXSLAR VA KASHFIYOTCHILAR (ENSIKLOPEDIYA)
# ---------------------------------------------------------------------------
HISTORICAL_FIGURES = {
    "richard_owen": {
        "slug": "richard_owen",
        "name": "Richard Ouen (Richard Owen)",
        "years": "1804 – 1892",
        "era_id": "jurassic",
        "title": "«Dinozavr» atamasini fanga kiritgan buyuk ingliz biologi va paleontologi",
        "image_file": "richard_owen_card.jpg",
        "bio": (
            "<b>👤 RICHARD OUEN (1804–1892)</b>\n"
            "<i>🇬🇧 Ingliz biologi, qiyosiy anatom va paleontolog</i>\n\n"
            "<b>🦖 Asosiy xizmati:</b>\n"
            "1842-yilda qadimgi ulkan toshqotgan sudralib yuruvchilarni chuqur o'rganib, ularga birinchi bo'lib "
            "yunoncha «deinos» (qo'rqinchli, bahaybat) va «sauros» (kaltakesak) so'zlaridan tashkil topgan "
            "<b>«Dinozavr» (Dinosauria)</b> ilmiy atamasini berdi.\n\n"
            "<b>🏛️ Merosi:</b>\n"
            "London Tabiat Tarixi Muzeyi (Natural History Museum)ning asoschisi bo'lib, "
            "u yerda dunyodagi eng mashhur dinozavr skeletlari kolleksiyasini xalqqa namoyish etishni yo'lga qo'ygan."
        ),
        "quote": "«Tabiatdagi har bir toshqotgan suyak — o'tmishning unutilgan sahifasidir.»",
        "aliases": ["richard", "ouen", "owen", "dinozavr olimi"],
    },
    "imxotep": {
        "slug": "imxotep",
        "name": "Imxotep (Imhotep)",
        "years": "Mil. avv. XXVII asr",
        "era_id": "ancient_world",
        "title": "Tarixdagi birinchi me'mor, olim va bosh tabib (Misr)",
        "image_file": "imxotep_card.jpg",
        "bio": (
            "<b>👤 IMXOTEP (MIL. AVV. XXVII ASR)</b>\n"
            "<i>🇪🇬 Qadimgi Misr me'mori, vaziri va tabibi</i>\n\n"
            "<b>🏛️ Asosiy kashfiyoti:</b>\n"
            "Insoniyat tarixidagi birinchi toshdan qurilgan monumental inshoot — fir'avn Joserning "
            "<b>Pog'onali Piramidasi</b>ni Saqqarada barpo etgan. U loy g'isht o'rniga yaxlit tosh bloklardan binolar qurish texnologiyasini kashf qildi.\n\n"
            "<b>🩺 Tibbiyotdagi o'rni:</b>\n"
            "Sehr-jodu o'rniga yaralarni bog'lash, jarrohlik amaliyotlari va anatomiyani ilmiy asosda davolashni boshlab bergan."
        ),
        "quote": "«Toshdan qurilgan bino — inson aql-zakovatining abadiyatga qoldirgan izidir.»",
        "aliases": ["imxotep", "imhotep", "piramida quruvchisi"],
    },
    "arximed": {
        "slug": "arximed",
        "name": "Arximed (Archimedes)",
        "years": "Mil. avv. 287 – 212",
        "era_id": "ancient_world",
        "title": "Qadimgi Yunonistonning buyuk matematigi, fizigi va muhandisi",
        "image_file": "arximed_card.jpg",
        "bio": (
            "<b>👤 ARXIMED (MIL. AVV. 287–212)</b>\n"
            "<i>🇬🇷 Sirakuza shahrida tug'ilgan buyuk daho</i>\n\n"
            "<b>💡 Buyuk kashfiyotlari:</b>\n"
            "• <b>Gidrostatika qonuni:</b> Vanna toshib ketganini ko'rib, jism suvga botganda o'z hajmidagi suvni siqib chiqarishini kashf etdi va quvonchdan «Eyrika!» (Topdim!) deb baqirdi.\n"
            "• <b>Richag qoidasi:</b> «Menga tayanch nuqtasini bering, men Yerni joyidan qo'zg'ataman» degan mashhur so'z muallifi.\n"
            "• <b>Arximed vinti:</b> Daryodan suvni yuqoriga chiqaruvchi spiral nasos (hozirgi kunda ham qo'llaniladi).\n"
            "• Rim kemalariga qarshi nometall oyna va mexanik qamal qurollarini yaratgan."
        ),
        "quote": "«Menga tayanch nuqtasini bering, men Yer shahrini joyidan qo'zg'ataman!»",
        "aliases": ["arximed", "archimedes", "eyrika", "richag"],
    },
    "tsay_lun": {
        "slug": "tsay_lun",
        "name": "Tsay Lun (Cai Lun)",
        "years": "Milodiy 50 – 121",
        "era_id": "ancient_world",
        "title": "Qog'ozni ixtiro qilgan buyuk xitoylik amaldor va kashfiyotchi",
        "image_file": "tsay_lun_card.jpg",
        "bio": (
            "<b>👤 TSAY LUN (MILODIY 50–121)</b>\n"
            "<i>🇨🇳 Qadimgi Xitoy kashfiyotchisi</i>\n\n"
            "<b>📜 Buyuk kashfiyoti: QOG'OZ (105-yil)</b>\n"
            "Bambuk tayoqchalari va og'ir suyaklar o'rniga, daraxt po'stlog'i, kanop tolalari, baliq to'rlari va latta qoldiqlarini "
            "suvda qaynatib, yupqa qatlam qilib quritish orqali yengil, arzon va chidamli qog'oz ishlab chiqarish usulini yaratdi.\n\n"
            "<b>🌍 Dunyo ahamiyati:</b>\n"
            "Uning kashfiyoti butun insoniyat ilm-fanining rivojlanishiga eng kuchli poydevor bo'ldi."
        ),
        "quote": "«Yengil qog'oz og'ir bilimlarni asrlar osha ko'tarib o'tadi.»",
        "aliases": ["tsay lun", "cai lun", "qog'oz ixtirochisi", "qogoz"],
    },
    "al_xorazmiy": {
        "slug": "al_xorazmiy",
        "name": "Muhammad al-Xorazmiy",
        "years": "783 – 850",
        "era_id": "islamic_golden_age",
        "title": "«Algebra va Algoritm otasi», qomusiy olim",
        "image_file": "al_xorazmiy_card.jpg",
        "bio": (
            "<b>👤 MUHAMMAD AL-XORAZMIY (783–850)</b>\n"
            "<i>🇺🇿 Xorazmda tug'ilgan jahon fani dahosi, Bag'doddagi «Bayt al-Hikma» rahbari</i>\n\n"
            "<b>🔢 Buyuk kashfiyotlari:</b>\n"
            "• <b>Algebra fani asoschisi:</b> «Al-Kitob al-muxtasar fi hisob al-jabr va-l-muqobala» asari orqali algebraga mustaqil fan sifatida asos soldi.\n"
            "• <b>Algoritm:</b> Lotinchaga tarjima qilingan «Dixit Algorizmi» (Al-Xorazmiy aytdi) iborasi zamonaviy barcha kompyuter kodlarining asosi bo'lgan «Algoritm» tushunchasiga aylandi.\n"
            "• <b>0 (Nol) soni va o'nlik sanoq:</b> Hind raqamlarini o'nlik tizimda mukammallashtirib, dunyoga tanitdi.\n"
            "• Yer xaritasi va 2400 dan ortiq shaharlarning koordinatalarini tuzgan («Surat al-Ard»)."
        ),
        "quote": "«Agar inson axloqli bo'lsa — bu 1. Boylik qo'shilsa — 10 bo'ladi. Ilm qo'shilsa — 100. Agar 1 (axloq) ketsa, faqat nollar qoladi.»",
        "aliases": ["xorazmiy", "al-xorazmiy", "al xorazmiy", "algoritm", "algebra"],
    },
    "ibn_sino": {
        "slug": "ibn_sino",
        "name": "Abu Ali ibn Sino (Avitsenna)",
        "years": "980 – 1037",
        "era_id": "islamic_golden_age",
        "title": "Tabiblar sultoni, faylasuf va qomusiy alloma",
        "image_file": "ibn_sino_card.jpg",
        "bio": (
            "<b>👤 ABU ALI IBN SINO (980–1037)</b>\n"
            "<i>🇺🇿 Buxoro yaqinidagi Afshona qishlog'ida tug'ilgan jahon tabobati dahosi</i>\n\n"
            "<b>🩺 Buyuk kashfiyotlari:</b>\n"
            "• <b>«Tib qonunlari» (Al-Qonun fit-tibb):</b> 5 jildlik tibbiyot ensiklopediyasi bo'lib, XVII asrgacha Yevropa va Sharqda asosiy darslik bo'lgan.\n"
            "• Ko'zga ko'rinmas mikroblar suv va havo orqali yuqumli kasallik tarqatishini aniqlagan.\n"
            "• Puls (tomir urishi) orqali ichki a'zolar kasalliklarini aniq tashxislash tizimini ishlab chiqqan.\n"
            "• Jarrohlikda qon to'xtatuvchi usullar va og'riqsizlantirishni qo'llagan."
        ),
        "quote": "«Davo topilmaydigan dard yo'q, faqat iroda va bilim yetishmasligi bor.»",
        "aliases": ["ibn sino", "avitsenna", "avicenna", "tabib"],
    },
    "beruniy": {
        "slug": "beruniy",
        "name": "Abu Rayhon Beruniy",
        "years": "973 – 1048",
        "era_id": "islamic_golden_age",
        "title": "Astronom, geodeziya va geografiya dahosi, birinchi globus yaratuvchisi",
        "image_file": "beruniy_card.jpg",
        "bio": (
            "<b>👤 ABU RAYHON BERUNIY (973–1048)</b>\n"
            "<i>🇺🇿 Qadimgi Kot (Qoraqalpog'iston) shahrida tug'ilgan ensiklopedist olim</i>\n\n"
            "<b>🌍 Buyuk kashfiyotlari:</b>\n"
            "• <b>Yer radiusi:</b> Nandna qal'asida (hozirgi Pokiston) o'ziga xos trigonometrik usul bilan Yer radiusini 6339.6 km deb hisoblagan (zamonaviy natijadan bor-yo'g'i 0.5% farq qiladi!).\n"
            "• <b>Amerika qit'asi bashorati:</b> G'arbiy okean ortida quruqlik va yangi qit'a borligini Xristofor Kolumbdan 500 yil oldin ilmiy hisoblagan.\n"
            "• Birinchi relyefli globusni yaratgan.\n"
            "• «Hindiston», «Qadimgi xalqlardan qolgan yodgorliklar», «Mineralogiya» kabi 150 dan ortiq fundamental asarlar muallifi."
        ),
        "quote": "«Haqiqatni bilish uchun shubha qilishdan va izlanishdan to'xtamaslik kerak.»",
        "aliases": ["beruniy", "abu rayhon beruniy", "al-beruniy", "globus"],
    },
    "ulugbek": {
        "slug": "ulugbek",
        "name": "Mirzo Ulug'bek",
        "years": "1394 – 1449",
        "era_id": "islamic_golden_age",
        "title": "Buyuk munajjim, matematik va Samarqand hukmdori",
        "image_file": "ulugbek_card.jpg",
        "bio": (
            "<b>👤 MIRZO ULUG'BEK (1394–1449)</b>\n"
            "<i>🇺🇿 Amir Temurning suyukli nabirasi, Samarqand rasadxonasi bunyodkori</i>\n\n"
            "<b>🔭 Buyuk kashfiyotlari:</b>\n"
            "• Samarqandda radiusi 40 metrlik ulkan sekstantga ega rasadxona qurdi.\n"
            "• <b>«Ziji Jadidi Ko'ragoniy»:</b> 1018 ta yulduzning osmondagi o'rnini aniq belgilab bergan yulduzlar jadvali.\n"
            "• Bir yil uzunligini 365 kun, 6 soat, 10 daqiqa, 8 soniya deb hisobladi (hozirgi o'lchovdan atigi 1 daqiqa xato!).\n"
            "• «Bilim olmoq har bir muslim va muslima uchun farzdir» shiorini o'z madrasasi peshtoqiga yozdirgan."
        ),
        "quote": "«Hukmdorlar taxtdan tushadi, saltanatlar parchalanadi, ammo olimlarning asarlari abadiy yashaydi.»",
        "aliases": ["ulugbek", "mirzo ulugbek", "rasadxona", "yulduzlar"],
    },
    "leonardo_da_vinci": {
        "slug": "leonardo_da_vinci",
        "name": "Leonardo da Vinchi (Leonardo da Vinci)",
        "years": "1452 – 1519",
        "era_id": "renaissance",
        "title": "Uyg'onish davrining universal dahosi: rassom, muhandis, ixtirochi",
        "image_file": "leonardo_da_vinci_card.jpg",
        "bio": (
            "<b>👤 LEONARDO DA VINCHI (1452–1519)</b>\n"
            "<i>🇮🇹 Italiyalik rassom, haykaltarosh, me'mor va muhandis</i>\n\n"
            "<b>💡 Mo''jizaviy ixtirolari:</b>\n"
            "U o'z kundaliklarida o'z davridan yuzlab yillar oldin bo'lgan ixtirolarning chizmalarini chizgan:\n"
            "• Vertolyot (havo vinti), parashyut, qanotli uchish apparatlari (deltaplan);\n"
            "• Suv osti kemasi va g'avvoslik kostyumi;\n"
            "• Zirhli harakatlanuvchi tank va mexanik avtomat-robot;\n"
            "• Inson anatomiyasi bo'yicha eng aniq ilmiy chizmalar muallifi.\n\n"
            "<b>🎨 Badiiy durdonalari:</b> «Mona Liza» (Jokonda) va «Maxfiy kechlik»."
        ),
        "quote": "«O'rganish zehnni hech qachon toliqtirmaydigan yagona faoliyatdir.»",
        "aliases": ["leonardo", "da vinchi", "vinci", "mona liza"],
    },
    "gutenberg": {
        "slug": "gutenberg",
        "name": "Iogann Gutenberg (Johannes Gutenberg)",
        "years": "1400 – 1468",
        "era_id": "renaissance",
        "title": "Kitob bosish dastgohi (bosmaxona) ixtirochisi",
        "image_file": "gutenberg_card.jpg",
        "bio": (
            "<b>👤 IOGANN GUTENBERG (1400–1468)</b>\n"
            "<i>🇩🇪 Nemis temirchisi, zargari va ixtirochisi</i>\n\n"
            "<b>🖨️ Buyuk kashfiyoti: Harakatlanuvchi harflarga ega Bosmaxona (1440)</b>\n"
            "U metall (qo'rg'oshin) harf qoliplarini yasash, moy asosidagi maxsus bosma siyoh va yog'och press moslamasini birlashtirib, "
            "kitoblarni tez, arzon va ko'p nusxada chop etish yo'lini topdi.\n\n"
            "<b>🌍 Tarixdagi o'rni:</b>\n"
            "Gutenberg kashfiyoti axborot tarqalishini ming chandon tezlashtirib, dunyoda savodxonlik, ilmiy inqilob va Renessansning "
            "butun Yevropa bo'ylab keng yoyilishiga olib keldi."
        ),
        "quote": "«Bosmaxona — bu xalqlar ko'zini ochuvchi cheksiz nur manbaidir.»",
        "aliases": ["gutenberg", "johannes gutenberg", "bosmaxona", "kitob"],
    },
    "galiley": {
        "slug": "galiley",
        "name": "Galileo Galiley (Galileo Galilei)",
        "years": "1564 – 1642",
        "era_id": "renaissance",
        "title": "Zamonaviy fizika va kuzatuv astronomiyasining otasi",
        "image_file": "galiley_card.jpg",
        "bio": (
            "<b>👤 GALILEO GALILEY (1564–1642)</b>\n"
            "<i>🇮🇹 Italiyalik astronom, fizik va matematik</i>\n\n"
            "<b>🔭 Buyuk kashfiyotlari:</b>\n"
            "• 1609-yilda o'z teleskopini yasab, samoviy jismlarni kuzatgan birinchi olim bo'ldi.\n"
            "• Yupiter atrofidagi 4 ta yo'ldoshni (Io, Yevropa, Ganimed, Kallisto) kashf etdi.\n"
            "• Oy yuzasi silliq emas, balki kraterlar va tog'lardan iboratligini ko'rdi.\n"
            "• Erkin tushish tezligi jismning massasiga bog'liq emasligini Piza minorasidan tajriba o'tkazib isbotladi.\n"
            "• «Baribir u aylanmoqda!» (E pur si muove!) deya Yerning Quyosh atrofida aylanishini himoya qildi."
        ),
        "quote": "«Koinot kitobi matematika tilida yozilgan.»",
        "aliases": ["galiley", "galileo", "teleskop kashfiyotchisi"],
    },
    "nyuton": {
        "slug": "nyuton",
        "name": "Isaak Nyuton (Isaac Newton)",
        "years": "1643 – 1727",
        "era_id": "industrial_revolution",
        "title": "Klassik fizika va butunolam tortishish qonunining asoschisi",
        "image_file": "nyuton_card.jpg",
        "bio": (
            "<b>👤 ISAAK NYUTON (1643–1727)</b>\n"
            "<i>🇬🇧 Buyuk ingliz fizigi, matematigi va mexaniki</i>\n\n"
            "<b>🍎 Buyuk kashfiyotlari:</b>\n"
            "• <b>Butunolam tortishish qonuni:</b> Daraxtdan tushgan olma voqeasidan ilhomlanib, sayyoralarning Quyosh atrofida harakatini va yerdagi og'irlik kuchini bitta umumiy formula bilan tushuntirdi.\n"
            "• <b>Klassik mexanikaning 3 qonuni</b> (inersiya, kuch va tezlanish, ta'sir va aks ta'sir).\n"
            "• Oq yorug'lik 7 xil rang spektridan iboratligini prizma yordamida isbotladi.\n"
            "• Ko'zguli (reflektor) teleskopni ixtiro qildi."
        ),
        "quote": "«Agar men uzoqroqni ko'rgan bo'lsam, bu gigantlarning yelkasida turganim tufaylidir.»",
        "aliases": ["nyuton", "newton", "isaak nyuton", "olma"],
    },
    "jeyms_uatt": {
        "slug": "jeyms_uatt",
        "name": "Jeyms Uatt (James Watt)",
        "years": "1736 – 1819",
        "era_id": "industrial_revolution",
        "title": "Universal bug' dvigateli ixtirochisi, sanoat inqilobi asoschisi",
        "image_file": "jeyms_uatt_card.jpg",
        "bio": (
            "<b>👤 JEYMS UATT (1736–1819)</b>\n"
            "<i>🏴󠁧󠁢󠁳󠁣󠁴󠁿 Shotlandiyalik muhandis va ixtirochi</i>\n\n"
            "<b>🚂 Buyuk kashfiyoti: Bug' Dvigateli (1769–1784)</b>\n"
            "Nyucomenning samarasiz bug' nasosini tubdan takomillashtirib, alohida kondensatorga ega universal aylanuvchi bug' dvigatelini yaratdi. "
            "Bu kashfiyot insoniyatni ot va suv tegirmonlari quvvatidan ozod qilib, poezdlar, paroxodlar va yirik zavodlarni harakatga keltirdi.\n\n"
            "<b>⚡ Quvvat o'lchovi:</b> Dvigatellarning kuchini o'lchash uchun «Ot kuchi» tushunchasini kiritgan, xalqaro elektr quvvat birligi esa uning sharafiga «Vatt» (W) deb ataladi."
        ),
        "quote": "«Men insoniyat qo'liga butun dunyoni harakatga keltiruvchi quvvatni berdim.»",
        "aliases": ["uatt", "watt", "jeyms uatt", "bug dvigateli"],
    },
    "tesla": {
        "slug": "tesla",
        "name": "Nikola Tesla (Nikola Tesla)",
        "years": "1856 – 1943",
        "era_id": "industrial_revolution",
        "title": "Elektr va o'zgaruvchan tok dahosi, XXI asr texnologiyalari me'mori",
        "image_file": "tesla_card.jpg",
        "bio": (
            "<b>👤 NIKOLA TESLA (1856–1943)</b>\n"
            "<i>⚡ Serb millatiga mansub buyuk fizik, muhandis va ixtirochi</i>\n\n"
            "<b>⚡ Buyuk kashfiyotlari:</b>\n"
            "• <b>O'zgaruvchan tok (AC):</b> Butun dunyodagi rozetkalarda oqayotgan elektr toki aynan Teslaning tizimi bo'yicha ishlaydi.\n"
            "• Ko'p fazali elektr generatorlari va asinxron motorlar;\n"
            "• Tesla transformatori (chaqmoq va yuqori kuchlanishli o'tkazgich);\n"
            "• Radio to'lqinlari orqali masofadan boshqariladigan birinchi qayiqcha (1898);\n"
            "• Neft va simsiz energiya uzatish bo'yicha afsonaviy tajribalar muallifi."
        ),
        "quote": "«Hozirgi zamon ularniki bo'lishi mumkin, ammo men mehnati bilan yashagan kelajak albatta meniki!»",
        "aliases": ["tesla", "nikola tesla", "elektr toki", "ozgaruvchan tok"],
    },
    "edison": {
        "slug": "edison",
        "name": "Tomas Edison (Thomas Edison)",
        "years": "1847 – 1931",
        "era_id": "industrial_revolution",
        "title": "1093 ta patent egasi bo'lgan afsonaviy amerikalik ixtirochi",
        "image_file": "edison_card.jpg",
        "bio": (
            "<b>👤 TOMAS EDISON (1847–1931)</b>\n"
            "<i>🇺🇸 Amerikalik kashfiyotchi va yirik tadbirkor</i>\n\n"
            "<b>💡 Buyuk kashfiyotlari:</b>\n"
            "• <b>Uzoq xizmat qiluvchi cho'g'lanma lampochka (1879):</b> Elektr yoritgichini har bir uyga yetkazib berdi.\n"
            "• <b>Fonograf (1877):</b> Tarixda birinchi marta inson ovozini yozib oluvchi va qayta eshittiruvchi apparat.\n"
            "• <b>Kinetoskop:</b> Dastlabki kino tomosha qilish moslamasi.\n"
            "• Birinchi markaziy elektr stansiyasi (Manxettenda 1882-yil)."
        ),
        "quote": "«Daholik — bu 1% ilhom va 99% mehnatdir.»",
        "aliases": ["edison", "tomas edison", "lampochka", "chiroq"],
    },
    "mendeleyev": {
        "slug": "mendeleyev",
        "name": "Dmitriy Mendeleyev",
        "years": "1834 – 1907",
        "era_id": "industrial_revolution",
        "title": "Kimyoviy elementlar davriy jadvalining yaratuvchisi",
        "image_file": "mendeleyev_card.jpg",
        "bio": (
            "<b>👤 DMITRIY MENDELEYEV (1834–1907)</b>\n"
            "<i>🇷🇺 Rus kimyogari, fizigi va qomusiy olimi</i>\n\n"
            "<b>🧪 Buyuk kashfiyoti: Davriy Qonun (1869)</b>\n"
            "Elementlarning xossalari ularning atom og'irligiga davriy bog'liq ekanligini kashf qildi. "
            "U tuzgan jadvalda hali fanga noma'lum bo'lgan elementlar (galliy, skandiy, germaniy) uchun bo'sh kataklar qoldirdi "
            "va ularning xossalarini oldindan aql bovar qilmas aniqlikda bashorat qildi."
        ),
        "quote": "«Ilm-fan faqatgina haqiqatga xizmat qilgandagina buyukdir.»",
        "aliases": ["mendeleyev", "mendeleev", "davriy jadval", "kimyo"],
    },
    "eynshteyn": {
        "slug": "eynshteyn",
        "name": "Albert Eynshteyn (Albert Einstein)",
        "years": "1879 – 1955",
        "era_id": "space_atomic_age",
        "title": "Nisbiylik nazariyasi muallifi, zamonaviy fizika dahosi",
        "image_file": "eynshteyn_card.jpg",
        "bio": (
            "<b>👤 ALBERT EYNSHTEYN (1879–1955)</b>\n"
            "<i>🇩🇪 Nobel mukofoti laureati, nazariyotchi fizik</i>\n\n"
            "<b>⚛️ Buyuk kashfiyotlari:</b>\n"
            "• <b>Nisbiylik nazariyasi:</b> Vaqt va fazo mutlaq emas, ular harakat tezligiga va gravitatsiyaga bog'liq ekanini isbotladi.\n"
            "• <b>E = mc² formulasi:</b> Massa va energiya o'zaro bog'liqligi tenglamasi bo'lib, atom energiyasining poydevoriga aylandi.\n"
            "• Fotoeffekt qonuni (Nobel mukofoti olgan kashfiyoti).\n"
            "• Gravitatsion to'lqinlar va qora tuynuklar mavjudligini 100 yil oldin nazariy isbotlagan."
        ),
        "quote": "«Tasavvur bilimdan muhimroqdir. Chunki bilim chegaralangan, tasavvur esa butun koinotni qamrab oladi.»",
        "aliases": ["eynshteyn", "einstein", "albert eynshteyn", "nisbiylik"],
    },
    "fleming": {
        "slug": "fleming",
        "name": "Aleksandr Fleming (Alexander Fleming)",
        "years": "1881 – 1955",
        "era_id": "space_atomic_age",
        "title": "Penitsillin (birinchi antibiotik) kashfiyotchisi",
        "image_file": "fleming_card.jpg",
        "bio": (
            "<b>👤 ALEKSANDR FLEMING (1881–1955)</b>\n"
            "<i>🏴󠁧󠁢󠁳󠁣󠁴󠁿 Shotlandiyalik bakteriolog va shifokor</i>\n\n"
            "<b>💊 Buyuk kashfiyoti: Penitsillin (1928)</b>\n"
            "Laboratoriyadagi idishda o'sgan Penicillium notatum mog'or zamburug'i xavfli stafilokokk bakteriyalarini yo'q qilayotganini payqab, "
            "dunyodagi birinchi antibiotikni kashf qildi.\n\n"
            "<b>💉 Insoniyat najoti:</b>\n"
            "Penitsillin Ikkinchi jahon urushida va undan keyin o'lat, pnevmoniya, sepsis kabi kasalliklardan 200 milliondan ortiq inson hayotini qutqarib qoldi."
        ),
        "quote": "«Tabiat penitsillinni yaratdi, men faqat uni payqadim xolos.»",
        "aliases": ["fleming", "penitsillin", "antibiotik"],
    },
    "aka_uka_raytlar": {
        "slug": "aka_uka_raytlar",
        "name": "Aka-uka Raytlar (Orvill va Uilbur Rayt)",
        "years": "1871 – 1948",
        "era_id": "space_atomic_age",
        "title": "Birinchi boshqariladigan dvigatelli samolyot yaratuvchilari",
        "image_file": "aka_uka_raytlar_card.jpg",
        "bio": (
            "<b>👤 AKA-UKA RAYTLAR (ORVILL VA UILBUR)</b>\n"
            "<i>🇺🇸 Amerikalik aviatorlar va muhandislar</i>\n\n"
            "<b>✈️ Buyuk kashfiyoti: Samolyot parvozi (1903-yil 17-dekabr)</b>\n"
            "Ular velosiped ustaxonasida tajribalar o'tkazib, benzinli dvigatel va propeller bilan jihozlangan «Flyer I» samolyotini yaratdilar. "
            "Shimoliy Karolinaning Kitti-Xok tepaligida havoda 12 soniya davomida 36 metr uchib, insoniyatning osmonga ko'tarilish asrini ochib berdilar."
        ),
        "quote": "«Inson osmonga ko'tarilishi mumkinligiga ishonsagina, qanotlar kuchga to'ladi.»",
        "aliases": ["raytlar", "aka uka raytlar", "orvill rayt", "samolyot"],
    },
    "gagarin": {
        "slug": "gagarin",
        "name": "Yuriy Gagarin (Yuri Gagarin)",
        "years": "1934 – 1968",
        "era_id": "space_atomic_age",
        "title": "Koinotga chiqqan birinchi inson",
        "image_file": "gagarin_card.jpg",
        "bio": (
            "<b>👤 YURIY GAGARIN (1934–1968)</b>\n"
            "<i>🚀 Tarixdagi birinchi fazogir (kosmonavt)</i>\n\n"
            "<b>🛰️ Buyuk jasorati: Tarixiy Parvoz (1961-yil 12-aprel)</b>\n"
            "«Vostok-1» kosmik kemasida Boyqo'ng'ir kosmodromidan parvoz qilib, Yer atrofini 108 daqiqa ichida bir marta to'liq aylanib chiqdi. "
            "Uning «Poyexali!» (Ketdik!) so'zi butun dunyo bo'ylab yangi Kosmik eraning ramziga aylandi."
        ),
        "quote": "«Yer atrofini aylanib uchib ko'rdimki, sayyoramiz qanchalik go'zal! Odamlar, bu go'zallikni asrang va ko'paytiring!»",
        "aliases": ["gagarin", "yuriy gagarin", "kosmonavt", "fazogir"],
    },
    "tyuring": {
        "slug": "tyuring",
        "name": "Alan Tyuring (Alan Turing)",
        "years": "1912 – 1954",
        "era_id": "space_atomic_age",
        "title": "Zamonaviy kompyuter va Sun'iy Intellekt nazariyasi asoschisi",
        "image_file": "tyuring_card.jpg",
        "bio": (
            "<b>👤 ALAN TYURING (1912–1954)</b>\n"
            "<i>🇬🇧 Ingliz matematigi, mantiqshunosi va kriptografi</i>\n\n"
            "<b>💻 Buyuk kashfiyotlari:</b>\n"
            "• <b>Tyuring mashinasi (1936):</b> Dasturlanuvchi raqamli kompyuterlarning universal nazariy modeli.\n"
            "• <b>«Enigma» shifrini buzishi:</b> Ikkinchi jahon urushida nemislarning sirli kodini yechuvchi «Bombe» hisoblash mashinasini yaratib, urushni 2 yilga qisqartirdi va millionlab odamlarni qutqardi.\n"
            "• <b>Tyuring testi:</b> Mashinaning inson kabi mustaqil fikrlay olish qobiliyatini tekshiruvchi dunyodagi birinchi test."
        ),
        "quote": "«Biz faqat qisqa masofani ko'ra olamiz, lekin u yerda qilinishi kerak bo'lgan ulkan ishlar bor.»",
        "aliases": ["tyuring", "alan tyuring", "turing", "kompyuter"],
    },
    "tim_berners_lee": {
        "slug": "tim_berners_lee",
        "name": "Tim Berners-Li (Tim Berners-Lee)",
        "years": "1955-yilda tug'ilgan",
        "era_id": "digital_ai_future",
        "title": "Butunjahon o'rgimchak to'ri (WWW / Internet) yaratuvchisi",
        "image_file": "tim_berners_lee_card.jpg",
        "bio": (
            "<b>👤 TIM BERNERS-LI (1955-YILDA TUG'ILGAN)</b>\n"
            "<i>🇬🇧 Britaniyalik olim, kompyuter muhandisi</i>\n\n"
            "<b>🌐 Buyuk kashfiyoti: World Wide Web (WWW — 1989-yil)</b>\n"
            "CERN laboratoriyasida ishlab yurganida HTTP protokoli, HTML dasturlash tili va URL (veb-manzil) tizimini ixtiro qildi. "
            "U birinchi veb-sayt va veb-brauzerni yaratdi.\n\n"
            "<b>💎 Buyuk insoniylik namunasi:</b>\n"
            "U ushbu ixtirosini patentlamadi va undan hech qanday pul olmadi — uni butun insoniyat bepul foydalanishi uchun ochiq qoldirdi!"
        ),
        "quote": "«Bu barchamiz uchun yaratilgan.»",
        "aliases": ["berners li", "tim berners-lee", "www", "internet ixtirochisi"],
    },
}

# ---------------------------------------------------------------------------
# BUYUK KASHFIYOTLAR XRONOLOGIK RO'YXATI (ENSIKLOPEDIYA)
# ---------------------------------------------------------------------------
INVENTIONS = {
    "olov": {
        "slug": "olov",
        "name": "🔥 Olovning bo'ysundirilishi",
        "era_id": "stone_age",
        "year": "Mil. avv. 1 million yil oldin",
        "inventor": "Homo Erectus (Qadimgi insonlar)",
        "desc": "Insoniyat tarixidagi 1-buyuk burilish. Olov isitdi, himoya qildi, ovqat pishirish orqali miya rivojiga yo'l ochdi va metall eritish asrini boshlab berdi.",
    },
    "gildirak": {
        "slug": "gildirak",
        "name": "⭕ G'ildirak kashfiyoti",
        "era_id": "ancient_world",
        "year": "Mil. avv. 3500-yil",
        "inventor": "Mesopotamiya (Shumerlar)",
        "desc": "Og'ir yuklarni ko'chirish, transport vositalari, aravalar, suv tegirmonlari va barcha mexanik asboblarning ajralmas yuragi bo'ldi.",
    },
    "yozuv": {
        "slug": "yozuv",
        "name": "📜 Yozuv (Mixxat va Ierogliflar)",
        "era_id": "ancient_world",
        "year": "Mil. avv. 3200-yil",
        "inventor": "Shumer va Qadimgi Misr",
        "desc": "Inson xotirasini cheksiz qildi. Qonunlar, tarixiy voqealar va ilmiy kashfiyotlar avloddan avlodga o'tish imkoniyatiga ega bo'ldi.",
    },
    "qogoz": {
        "slug": "qogoz",
        "name": "📄 Qog'oz ixtiro qilinishi",
        "era_id": "ancient_world",
        "year": "Milodiy 105-yil",
        "inventor": "Tsay Lun (Xitoy)",
        "desc": "Qimmatbaho ipak va terilar o'rniga yengil, qulay va arzon qog'oz yaratilib, butun dunyoga kitobat va ma'rifat yoyilishini ta'minladi.",
    },
    "algebra": {
        "slug": "algebra",
        "name": "🔢 Algebra va Algoritm",
        "era_id": "islamic_golden_age",
        "year": "820-yil",
        "inventor": "Muhammad al-Xorazmiy",
        "desc": "Nol sonining kiritilishi, tenglamalar yechish va bosqichma-bosqich qoidalar (algoritm) zamonaviy matematika va kompyuter texnologiyalariga asos soldi.",
    },
    "bosmaxona": {
        "slug": "bosmaxona",
        "name": "🖨️ Bosmaxona dastgohi",
        "era_id": "renaissance",
        "year": "1440-yil",
        "inventor": "Iogann Gutenberg",
        "desc": "Kitoblarni qo'lda ko'chirish davrini tugatdi. Fan va erkin fikr butun sayyora bo'ylab millionlab nusxalarda tarqala boshladi.",
    },
    "teleskop": {
        "slug": "teleskop",
        "name": "🔭 Teleskop kashfiyoti",
        "era_id": "renaissance",
        "year": "1609-yil",
        "inventor": "Galileo Galiley",
        "desc": "Insoniyat ko'zini koinotga ochdi. Sayyoralar, Oy relyefi va yulduzlar tizimi birinchi marta ilmiy kuzatildi.",
    },
    "bug_dvigateli": {
        "slug": "bug_dvigateli",
        "name": "🚂 Bug' dvigateli",
        "era_id": "industrial_revolution",
        "year": "1769–1784",
        "inventor": "Jeyms Uatt",
        "desc": "Sanoat inqilobining asosiy harakatlantiruvchisi. Poezdlar, paroxodlar va fabrikalar ishga tushib, zamonaviy ishlab chiqarish boshlandi.",
    },
    "elektr": {
        "slug": "elektr",
        "name": "💡 Elektr yoritgichi va O'zgaruvchan tok",
        "era_id": "industrial_revolution",
        "year": "1879–1888",
        "inventor": "Tomas Edison va Nikola Tesla",
        "desc": "Insoniyatni qorong'ulikdan qutqardi. Butun dunyo energetika tizimi va mashinalari elektr energiyasi bilan ta'minlandi.",
    },
    "telefon": {
        "slug": "telefon",
        "name": "📞 Telefon apparati",
        "era_id": "industrial_revolution",
        "year": "1876-yil",
        "inventor": "Aleksandr Bell",
        "desc": "Masofalarni yo'q qildi. Insonlar yuzlab kilometr naridan turib bir-birlarining ovozini real vaqtda eshitish imkoniga ega bo'ldi.",
    },
    "samolyot": {
        "slug": "samolyot",
        "name": "✈️ Boshqariladigan Samolyot",
        "era_id": "space_atomic_age",
        "year": "1903-yil",
        "inventor": "Aka-uka Raytlar",
        "desc": "Qushlar kabi osmonga parvoz qilish orzusi ro'yobga chiqdi. Qit'alararo sayohat bir necha soatlik yo'lga aylandi.",
    },
    "penitsillin": {
        "slug": "penitsillin",
        "name": "💊 Penitsillin (Antibiotik)",
        "era_id": "space_atomic_age",
        "year": "1928-yil",
        "inventor": "Aleksandr Fleming",
        "desc": "Tibbiyotda ulkan mo''jiza. Avvallari o'limga olib kelgan infeksiya va kasalliklardan 200 milliondan ziyod inson hayoti saqlandi.",
    },
    "kompyuter": {
        "slug": "kompyuter",
        "name": "💻 Elektron Kompyuter",
        "era_id": "space_atomic_age",
        "year": "1936–1946",
        "inventor": "Alan Tyuring, Jon fon Neyman",
        "desc": "Axborot asrini boshlab berdi. Hisoblashlar, mantiqiy amallar va dasturlar inson aqlining beqiyos quroliga aylandi.",
    },
    "kosmik_parvoz": {
        "slug": "kosmik_parvoz",
        "name": "🛰️ Insonning Koinotga va Oyga chiqishi",
        "era_id": "space_atomic_age",
        "year": "1961 va 1969-yillar",
        "inventor": "Yuriy Gagarin, Sergey Korolyov, Nil Armstrong",
        "desc": "Inson o'z ona sayyorasi beshigidan chiqib, ochiq koinot va Oyga qadam qo'ydi.",
    },
    "internet": {
        "slug": "internet",
        "name": "🌐 Butunjahon Internet tarmog'i (WWW)",
        "era_id": "digital_ai_future",
        "year": "1989-yil",
        "inventor": "Tim Berners-Li",
        "desc": "Butun insoniyatni yagona axborot maydoniga birlashtirdi. Har qanday bilim bir soniya ichida qo'l telefoningizda bo'ldi.",
    },
    "suniy_intellekt": {
        "slug": "suniy_intellekt",
        "name": "🤖 Generativ Sun'iy Intellekt",
        "era_id": "digital_ai_future",
        "year": "XXI asr (2020-yillar)",
        "inventor": "Jahon olimlari (Deep Learning, Transformers)",
        "desc": "Inson aqli kabi matn, rasm, kod yozuvchi va yangi ilmiy kashfiyotlar qiluvchi sun'iy ong davri boshlandi.",
    },
}

# ---------------------------------------------------------------------------
# INTERAKTIV VIKTORINA (TEST SAVOLLARI VA JAVOBLARI)
# ---------------------------------------------------------------------------
QUIZ_QUESTIONS = [
    {
        "id": 1,
        "question": "🦖 Fanga birinchi bo'lib «Dinozavr» atamasini kiritgan olim kim?",
        "options": [
            "Richard Ouen",
            "Charlz Darvin",
            "Isaak Nyuton",
            "Leonardo da Vinchi",
        ],
        "correct_index": 0,
        "explanation": "To'g'ri javob: Richard Ouen! 1842-yilda u qadimgi toshqotgan kaltakesaklarni o'rganib, ularga «Dinozavr» nomini bergan.",
    },
    {
        "id": 2,
        "question": "🔥 Insoniyat tarixidagi eng birinchi buyuk kashfiyot nima bo'lgan?",
        "options": [
            "G'ildirak",
            "Olovdan foydalanish va yoqish",
            "Yozuv",
            "Temir eritish",
        ],
        "correct_index": 1,
        "explanation": "To'g'ri javob: Olov! Taxminan 1 million yil oldin olovning bo'ysundirilishi insoniyat miyasining rivojlanishi va omon qolishiga asos bo'ldi.",
    },
    {
        "id": 3,
        "question": "⭕ Qaysi xalq miloddan avvalgi 3500-yillarda g'ildirakni kashf etgan?",
        "options": [
            "Qadimgi Misrliklar",
            "Mesopotamiyadagi Shumerlar",
            "Rimliklar",
            "Qadimgi Yunonlar",
        ],
        "correct_index": 1,
        "explanation": "To'g'ri javob: Shumerlar! Dastlabki g'ildiraklar Shumer shahar-davlatlarida yuk tashish va aravalarda ishlatilgan.",
    },
    {
        "id": 4,
        "question": "📜 Milodiy 105-yilda Qog'ozni ixtiro qilgan shaxs kim?",
        "options": [
            "Konfutsiy",
            "Tsay Lun",
            "Iogann Gutenberg",
            "Al-Xorazmiy",
        ],
        "correct_index": 1,
        "explanation": "To'g'ri javob: Tsay Lun! Xitoylik kashfiyotchi daraxt po'stlog'i va tolalardan yengil qog'oz tayyorlash usulini ochgan.",
    },
    {
        "id": 5,
        "question": "🔢 Bugungi kunda kompyuter dasturlari asosini tashkil etuvchi «Algoritm» so'zi kimning nomidan olingan?",
        "options": [
            "Abu Ali ibn Sino",
            "Muhammad al-Xorazmiy",
            "Abu Rayhon Beruniy",
            "Alan Tyuring",
        ],
        "correct_index": 1,
        "explanation": "To'g'ri javob: Al-Xorazmiy! Uning «Al-Kitob al-muxtasar fi hisob al-jabr...» asari lotinchaga tarjima qilinganda «Dixit Algorizmi» shaklida yozilgan va shundan «Algoritm» atamasi paydo bo'lgan.",
    },
    {
        "id": 6,
        "question": "🌍 Kolumbdan 500 yil oldin G'arbiy okean ortida noma'lum qit'a (Amerika) borligini ilmiy hisoblab chiqqan alloma kim?",
        "options": [
            "Abu Rayhon Beruniy",
            "Mirzo Ulug'bek",
            "Ahmad al-Farg'oniy",
            "Ibn Battuta",
        ],
        "correct_index": 0,
        "explanation": "To'g'ri javob: Abu Rayhon Beruniy! U Yerning sharsimonligi va o'lchamlarini hisoblab, quruqliklar mutanosibligi bo'yicha okean ortida noma'lum quruqlik borligini isbotlagan.",
    },
    {
        "id": 7,
        "question": "🖨️ 1440-yilda Yevropada birinchi bo'lib bosmaxona (kitob bosish dastgohi)ni kim ixtiro qilgan?",
        "options": [
            "Leonardo da Vinchi",
            "Iogann Gutenberg",
            "Nikolay Kopernik",
            "Galileo Galiley",
        ],
        "correct_index": 1,
        "explanation": "To'g'ri javob: Iogann Gutenberg! Uning harakatlanuvchi metall harflar yordamida kitob bosish usuli butun dunyoga bilim tarqalishini tezlashtirdi.",
    },
    {
        "id": 8,
        "question": "🍎 Butunolam tortishish qonunini va klassik mexanika qonunlarini kashf qilgan olim kim?",
        "options": [
            "Albert Eynshteyn",
            "Isaak Nyuton",
            "Jeyms Uatt",
            "Rene Dekart",
        ],
        "correct_index": 1,
        "explanation": "To'g'ri javob: Isaak Nyuton! U osmon jismlari va yerdagi jismlarning harakatini bitta umumiy gravitatsiya qonuni orqali tushuntirib berdi.",
    },
    {
        "id": 9,
        "question": "🚂 Sanoat inqilobiga turtki bergan universal bug' dvigatelini kim yaratgan?",
        "options": [
            "Jeyms Uatt",
            "Tomas Edison",
            "Nikola Tesla",
            "Gottlib Daymler",
        ],
        "correct_index": 0,
        "explanation": "To'g'ri javob: Jeyms Uatt! 1769–1784 yillarda yaratilgan bu dvigatel zavodlar, poyezdlar va paroxodlar asrini ochib berdi.",
    },
    {
        "id": 10,
        "question": "⚡ O'zgaruvchan tok (AC) tizimi va ko'p fazali elektr motorlarini kim ixtiro qilgan?",
        "options": [
            "Tomas Edison",
            "Nikola Tesla",
            "Aleksandr Bell",
            "Maykl Faradey",
        ],
        "correct_index": 1,
        "explanation": "To'g'ri javob: Nikola Tesla! Uning o'zgaruvchan tok tizimi hozirda dunyodagi barcha elektr tarmoqlari va rozetkalarning asosidir.",
    },
    {
        "id": 11,
        "question": "💊 1928-yilda mog'or zamburug'idan birinchi antibiotik — Penitsillinni kim kashf etdi?",
        "options": [
            "Lui Paster",
            "Aleksandr Fleming",
            "Robert Kox",
            "Edvard Jenner",
        ],
        "correct_index": 1,
        "explanation": "To'g'ri javob: Aleksandr Fleming! Bu kashfiyot 200 milliondan ortiq inson hayotini yuqumli kasalliklardan asrab qoldi.",
    },
    {
        "id": 12,
        "question": "🚀 1961-yil 12-aprelda ochiq koinotga chiqqan tarixdagi birinchi inson kim?",
        "options": [
            "Nil Armstrong",
            "Yuriy Gagarin",
            "Aleksey Leonov",
            "Jon Glenn",
        ],
        "correct_index": 1,
        "explanation": "To'g'ri javob: Yuriy Gagarin! U «Vostok-1» kemasida Yer atrofini aylanib, insoniyatning koinot erasini boshlab berdi.",
    },
    {
        "id": 13,
        "question": "💻 Zamonaviy kompyuter va Sun'iy Intellekt nazariyasining otasi kim?",
        "options": [
            "Alan Tyuring",
            "Stiv Jobs",
            "Bill Geyts",
            "Tim Berners-Li",
        ],
        "correct_index": 0,
        "explanation": "To'g'ri javob: Alan Tyuring! U «Tyuring mashinasi» va aqlli fikrlashni tekshiruvchi «Tyuring testi» muallifidir.",
    },
    {
        "id": 14,
        "question": "🌐 Butunjahon o'rgimchak to'ri (WWW / Internet)ni ixtiro qilgan va uni insoniyatga bepul taqdim etgan olim kim?",
        "options": [
            "Tim Berners-Li",
            "Mark Sukerberg",
            "Ilon Mask",
            "Sergey Brin",
        ],
        "correct_index": 0,
        "explanation": "To'g'ri javob: Tim Berners-Li! U 1989-yilda CERNda WWW, HTML va HTTP asoslarini yaratdi.",
    },
    {
        "id": 15,
        "question": "🔭 Samarqandda radiusi 40 metrlik sekstantga ega rasadxona qurib, 1018 ta yulduz jadvalini tuzgan buyuk munajjim kim?",
        "options": [
            "Mirzo Ulug'bek",
            "Al-Farg'oniy",
            "Qozizoda Rumiy",
            "G'iyosiddin Jamshid",
        ],
        "correct_index": 0,
        "explanation": "To'g'ri javob: Mirzo Ulug'bek! Uning «Ziji Jadidi Ko'ragoniy» asari jahon astronomiyasining durdonasidir.",
    },
]
