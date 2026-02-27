+++
title = "print_id_bot: Telegram ID va chat_id yordamchisi (buyruqlar, tillar, imkoniyatlar)"
description = "@print_id_bot to'liq ma'lumotnoma: buyruqlar, 16 til, guruh triggerlari va dasturchi imkoniyatlari (/json, /dump). Telegram user ID va chat_id ni soniyalar ichida oling."
cta = { text = "Botni oching — Telegram user ID va chat_id ni darhol ko'ring.", label = "Open @print_id_bot", url = "https://t.me/print_id_bot" }
+++

@print_id_bot — bu **Telegram user ID**, **chat_id** (guruhlar va superguruhlar uchun) va kanal ID sini ko'rsatadigan Telegram boti. Shaxsiy chatda va guruhlarda ishlaydi, Telegram til sozlamangizga qarab 16 tilda javob beradi.

## Buyruqlar

| Buyruq | Vazifasi |
|--------|----------|
| `/start` | Xush kelibsiz xabari, User ID va Chat ID, /id va /help uchun inline tugmalar |
| `/id` | User ID va Chat ID (qisqa javob) |
| `/help` | To'liq yordam matni va buyruqlar ro'yxati |
| `/json` | Joriy xabar JSON formatida (dasturchilar uchun) |
| `/dump` | To'liq yangilanish tahlili va xom JSON (faqat shaxsiy chatda) |

Shaxsiy chatda har qanday xabar (matn, foto, stiker va hokazo) yuborish ham User ID va Chat ID ni qaytaradi. Qayta yuborilgan xabarlar uchun bot muallif ID sini mavjud bo'lsa ko'rsatadi, yoki yuboruvchi maxfiylik sozlamalari bloklagan bo'lsa "ID hidden". Batafsil: [qayta yuborilgan xabarlar va yashirin ID lar]({{< relref "telegram-forwarded-message-id.md" "en" >}}).

## Qo'llab-quvvatlanadigan tillar (16)

Bot javob tilini Telegram `language_code` dan tanlaydi. Qo'llab-quvvatlanadi: ingliz, rus, fors, o'zbek, hind, xitoy, turk, portugal, ispan, arab, indonez, nemis, urdu, fransuz, tagalog, amxar. Qo'llab-quvvatlanmaydigan kodlar ingliz tiliga o'tadi. Bk. [til tanlash qanday ishlaydi]({{< relref "telegram-id-bot-languages.md" "en" >}}).

## Guruh va superguruhda xulq-atvor

Guruhlarda bot faqat quyidagilarda javob beradi:

- Bot xabariga javob berganingizda
- `/id` yoki `/help` yuborganingizda (@print_id_bot bilan yoki siz)
- @print_id_bot bilan har qanday buyruq yuborganingizda (masalan `/foo@print_id_bot`)
- Xabaringizda @print_id_bot dan gapirganingizda

Aks holda jim turadi. Guruhga qo'shilganda guruh nomi va chat_id bilan xush kelibsiz xabari yuboradi. Qisqa qo'llanma: [chat_id olish uchun guruhga bot qo'shish]({{< relref "add-bot-to-group-chat-id.md" "en" >}}).

## Dasturchi imkoniyatlari

- **/json** — Joriy xabarni JSON sifatida qaytaradi.
- **/dump** — To'liq yangilanish tahlili va xom JSON (faqat shaxsiy chatda). Bot API integratsiyalarini debug qilish uchun foydali. Bk. [Telegram yangilanish JSON ni tekshirish]({{< relref "telegram-json-update.md" "en" >}}).

## Bog'liq sahifalar

- [Telegram user ID olish (xavfsiz usullar)]({{< relref "get-telegram-user-id.md" "en" >}})
- [Telegram guruhining chat_id sini olish]({{< relref "get-telegram-chat-id.md" "en" >}})
- [Telegram ID ni topish]({{< relref "how-to-find-telegram-id.md" "en" >}})

## Tez-tez so'raladigan savollar

### Bot kanallarda ishlaydimi?
Bot shaxsiy chatda va guruhlar/superguruhlarda ishlaydi. Kanallar uchun kanal ID boshqa oqimdan kerak (masalan kanal sifatida post va yangilanishlar oladigan bot). Bk. [Bot API uchun Telegram kanal ID olish]({{< relref "how-to-get-channel-id-bot-api.md" "en" >}}).

### Boshqasining Telegram user ID sini olishim mumkinmi?
Bot o'z ID ingizni yoki a'zo bo'lgan chatlarning chat_id sini ko'rsatadi. Qayta yuborilgan xabarlar uchun yuboruvchi qayta yuborishga ruxsat bersa ID ko'rsatiladi; aks holda "ID hidden". Telefon raqami yoki username orqali ID qidirish mumkin emas. Bk. [Telegram ID va username]({{< relref "telegram-id-vs-username.md" "en" >}}).

### Nima uchun bot guruhimda javob bermayapti?
Bot faqat unga javob berganingizda, /id yoki /help yuborganingizda yoki @print_id_bot dan gapirganingizda javob beradi. To'liq ro'yxat: [guruhda javob bermaydigan bot]({{< relref "bot-not-responding-in-group.md" "en" >}}).

### Bot bepulmi?
Ha. Ro'yxatdan o'tish yoki to'lov kerak emas.

### user ID va chat_id o'rtasidagi farq nima?
**User ID** Telegram hisobini aniqlaydi. **chat_id** suhbatni (shaxsiy chat, guruh, superguruh, kanal). Bk. [Telegram ID va username]({{< relref "telegram-id-vs-username.md" "en" >}}).
