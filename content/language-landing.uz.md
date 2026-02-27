+++
title = "Telegram ID olish"
description = "Telegram user ID va guruh chat_id ni soniyalar ichida oling. @print_id_bot shaxsiy chat va guruhlarda ishlaydi. Xavfsiz va bepul."
cta = { url = "https://t.me/print_id_bot", label = "Open @print_id_bot" }
+++

**Telegram user ID** — bu hisobingizning raqamli identifikatori. Integratsiyalar, botlar va dasturlash uchun kerak. Telegram interfeysida koʻrinmaydi, lekin @print_id_bot orqali soniyalar ichida olish mumkin. Xavfsiz usullar haqida koʻproq — [user ID boʻyicha qoʻllanmalarda]({{< relref "user-id-guides.md" >}}).

## Shaxsiy chatda Telegram user ID qanday olish

@print_id_bot ni shaxsiy chatda oching va **Boshlash** ni bosing. Bot darhol **Telegram user ID** ingizni, foydalanuvchi nomingizni (agar bor boʻlsa) va chat_id ni qaytaradi. Boshqa hech narsa kerak emas: xabardagi raqamni nusxalang.

Shaxsiy chatda bot har qanday xabarga javob beradi: matn, foto, stiker yoki `/id` buyrugʻi. Nima yuborsangiz, ID ingizni olasiz. Maxfiy: javobni faqat siz koʻrasiz.

## Guruh chat_id qanday olish

Guruh yoki superguruh **chat_id** sini olish uchun @print_id_bot ni guruhga qoʻshing. Qoʻshilgandan soʻng bot guruh nomi va chat_id bilan salomlashuv xabarini yuboradi.

Guruhlarda bot **faqat maʼlum harakatlarda** javob beradi. chat_id olish uchun quyidagilardan birini qiling:

- **/id** yoki **/help** buyrugʻini yuboring (@print_id_bot bilan yoki sizsiz)
- Bot xabariga javob bering
- Xabaringizda **@print_id_bot** ni eslatib oʻting
- @print_id_bot bilan har qanday buyruqni yuboring (masalan, `/foo@print_id_bot`)

Botni eslatmasdan oddiy xabarlar javob bermaydi: shu orqali bot spamlardan qochadi. Guruh va superguruh ID lari odatda manfiy; bu odatiy hol.

## Qayerdan boshlash

- [Telegram user ID qoʻllanmalari]({{< relref "user-id-guides.md" >}}) — user ID ni qanday topish, nusxalash va tushunish
- [chat_id qoʻllanmalari]({{< relref "chat-id-guides.md" >}}) — guruhlar va superguruhlar uchun chat_id olish
- [Bot API qoʻllanmalari]({{< relref "bot-api-guides.md" >}}) — Telegram Bot API bilan integratsiya

## FAQ

### Mening Telegram ID im maxfiymi?

Telegram ID ingiz ilovada ochiq koʻrsatilmaydi. Botlar va ilovalar uni faqat ular bilan aloqa qilganingizda oladi — masalan, bot ochib Boshlash ni bosganingizda. Qaysi botlarga ishonishni siz hal qilasiz.

### Nima uchun bot guruhda javob bermayapti?

Bot faqat uning xabariga javob berganda, /id yoki /help yuborganingizda yoki @print_id_bot ni eslatganingizda javob beradi. Ushbu triggerlarsiz oddiy xabarlarni eʼtiborsiz qoldiradi. Bot guruhda ekanligi va xabarlarni oʻqiy olishini tekshiring.

### user ID va chat_id orasidagi farq nima?

**user ID** Telegram hisobingizni aniqlaydi. **chat_id** suhbatni aniqlaydi: shaxsiy, guruh, superguruh yoki kanal. Shaxsiy chatda user ID va chat_id bir xil raqam. Guruhlar uchun chat_id odatda manfiy.
