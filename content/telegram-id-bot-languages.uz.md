+++
title = "Telegram ID boti 16 tilda: til tanlash qanday ishlaydi"
description = "@print_id_bot javob tilini Telegram language_code dan qanday tanlaydi. 16 ta qo'llab-quvvatlanadigan til, ingliz tiliga o'tish. Rus, fors, arab va boshqalar."
cta = { text = "@print_id_bot ni oching — u Telegram tilingizda javob beradi.", label = "Open @print_id_bot", url = "https://t.me/print_id_bot" }
+++

@print_id_bot Telegram til sozlamangizga qarab **16 tilda** javob beradi. Qo'lda til tanlash kerak emas.

## Qanday ishlaydi

Bot **language_code** ni yangilanishdan o'qiydi. Kodning birinchi qismidan foydalanadi (masalan pt-BR dan pt) va qo'llab-quvvatlanadigan locale ga xaritaga tushiradi. Qo'llab-quvvatlanmaydigan kodlar **ingliz** tiliga o'tadi.

## Qo'llab-quvvatlanadigan tillar (16)

| Kod | Til |
|-----|-----|
| en | Ingliz |
| ru | Rus |
| fa | Fors |
| uz | O'zbek |
| hi | Hind |
| zh | Xitoy |
| tr | Turk |
| pt | Portugal |
| es | Ispan |
| ar | Arab |
| id | Indonez |
| de | Nemis |
| ur | Urdu |
| fr | Fransuz |
| tl | Tagalog (Filipin; fil -> tl) |
| am | Amxar |

## Maxsus holatlar

- **Filipin** — Telegram fil yuboradi; bot tl (Tagalog) ga xaritaga tushiradi.
- **Portugal (Braziliya)** — pt-BR pt (Portugal) dan foydalanadi.
- **Xitoy** — zh-CN, zh-TW zh (Xitoy) dan foydalanadi.

## Nima lokalizatsiya qilingan

Barcha bot javoblari: xush kelibsiz matni, yorliqlar (User ID, Chat ID, guruh nomi), yordam matni, tugmalar va "ID hidden" yoki "Nusxalash uchun raqamni bosing" kabi xabarlar. /json va /dump dagi xom JSON o'zgarmaydi; faqat o'qiladigan yorliqlar tilingizdan foydalanadi.

## Bog'liq sahifalar

- [Ingliz tilini bilmasangiz @print_id_bot dan foydalanish]({{< relref "telegram-id-bot-for-non-english.md" "en" >}})
- [print_id_bot: buyruqlar, tillar, imkoniyatlar]({{< relref "print-id-bot.md" "en" >}})
- [Telegram user ID olish (xavfsiz usullar)]({{< relref "get-telegram-user-id.md" "en" >}})

## Tez-tez so'raladigan savollar

### Bot tilini qanday o'zgartirish mumkin?
Telegram ilova tilini Sozlamalar, Til dan o'zgartiring. Bot undan foydalanadi. Bottda til kaliti yo'q.

### Tilim qo'llab-quvvatlanmasa?
Bot ingliz tiliga o'tadi. Barcha funksiyalar bir xil ishlaydi.

### Bot o'ngdan chapga (RTL) tillarni qo'llab-quvvatlaydimi?
Ha. Arab, fors va urdu qo'llab-quvvatlanadi. Telegram RTL render qilishni boshqaradi.

### Yangi til so'rashim mumkinmi?
Bot 16 tilni qo'llab-quvvatlaydi. Qo'shimcha qo'shish bakuvchilarga bog'liq. Ingliz fallback hammaga foydalanish imkonini beradi.

### Til saqlanadimi yoki boshqa joyga yuboriladimi?
Yo'q. Bot har yangilanishdan language_code ni o'qiydi va faqat javob satrlarini tanlash uchun ishlatadi. Saqlanmaydi yoki ulashilmaydi.
