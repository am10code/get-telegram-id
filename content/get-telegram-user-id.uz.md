+++
title = "Telegram user ID olish (xavfsiz usullar)"
description = "Telegram user ID ni xavfsiz qanday olish mumkin. @print_id_bot bilan qadam-baqadam usullar. Dasturchi asboblari kerak emas. Mobil va kompyutda ishlaydi."
cta = { text = "Botni oching va Boshlash ni bosing — Telegram user ID darhol ko'rinadi.", label = "Open @print_id_bot", url = "https://t.me/print_id_bot" }
+++

**Telegram user ID** — bu hisobingiz uchun raqamli identifikator. Telegram ilovasida ko'rsatilmaydi, lekin botlar va integratsiyalar siz bilan o'zaro aloqada bo'lganda uni o'qiy oladi. Bu yerda uni xavfsiz olish usullari.

## Usul 1: @print_id_bot dan foydalaning (eng tez)

1. Telegramda [@print_id_bot](https://t.me/print_id_bot) ni oching.
2. **Boshlash** ni bosing.
3. Bot **User ID** va **Chat ID** bilan javob beradi (shaxsiy chatda ular bir xil).
4. Nusxalash uchun raqamni bosing.

Bot Telegram til sozlamangizga qarab 16 tilda javob beradi. Qo'llab-quvvatlanmaydigan tillar ingliz tiliga o'tadi.

## Usul 2: Botga har qanday xabar yuboring

@print_id_bot bilan shaxsiy chatda har qanday xabar, foto, stiker yoki hujjat yuboring. Bot User ID va Chat ID ni qaytaradi. Qisqa javob uchun `/id` dan ham foydalanishingiz mumkin.

## Usul 3: Xabarni qayta yuborish (va cheklovlar)

Agar boshqa foydalanuvchidan xabarni @print_id_bot ga qayta yuborsangiz, bot asl yuboruvchining User ID sini ko'rsatishi mumkin. Biroq yuboruvchida qayta yuborishda ID ni yashiruvchi maxfiylik sozlamalari bo'lsa, "ID hidden" ko'rasiz. Telefon raqami yoki username orqali boshqasining ID sini ishonchli olish mumkin emas. Batafsil: [qayta yuborilgan xabarlar va yashirin ID lar]({{< relref "telegram-forwarded-message-id.md" "en" >}}).

## Nima qilish mumkin emas

- **Telefon raqami bo'yicha qidirish**: Faqat telefon raqamidan Telegram user ID olish mumkin emas. Buni va'da qiladigan xizmatlar ko'pincha firibgarlik yoki maxfiylikni buzadi.
- **Username bo'yicha qidirish**: Username lar ID emas. ID olish uchun foydalanuvchi bot yoki ilova bilan o'zaro ta'sir qilishi kerak.
- **O'zaro ta'sirsiz boshqalarning ID larini ko'rish**: Faqat a'zo bo'lgan chatlarning yoki sizga qayta yuborilgan xabarlarni yuboruvchi (va qayta yuborishga ruxsat beruvchi) foydalanuvchilarning ID larini olishingiz mumkin.

## Bog'liq sahifalar

- [Telegram ID va username: farqi nima?]({{< relref "telegram-id-vs-username.md" "en" >}})
- [Nima uchun Telegram raqamli ID ni ko'rsatmaydi]({{< relref "telegram-id-not-in-ui.md" "en" >}})
- [print_id_bot: buyruqlar, tillar, imkoniyatlar]({{< relref "print-id-bot.md" "en" >}})

## Tez-tez so'raladigan savollar

### Telegram user ID im maxfiy?
Telegram interfeysida ko'rsatilmaydi, lekin botlar va ilovalar o'zaro ta'sir qilganda uni o'qiy oladi. Ishonchsiz xizmatlarga bermang.

### Telegram user ID ni o'zgartirish mumkinmi?
Yo'q. Bir marta tayinlanadi va o'zgarmaydi.

### Nima uchun bot qayta yuborilgan xabarlar uchun "ID hidden" ko'rsatadi?
Yuboruvchi qayta yuborishda ID ni yashiruvchi maxfiylik sozlamalarini yoqgan. Bk. [qayta yuborilgan yuboruvchi ID yashirin]({{< relref "telegram-privacy-forwarded-id-hidden.md" "en" >}}).

### @print_id_bot dan foydalanish xavfsizmi?
Ha. Bot faqat allaqachon kirish huquqingiz bor ID larni ko'rsatadi (o'zingizniki yoki a'zo bo'lgan chatlardan). Telegram taqdim etganidan tashqari ma'lumotlaringizni saqlamaydi yoki ulashmaydi.

### Telegram user ID qanday ko'rinadi?
Raqamli qiymat, odatda 9–10 raqam. Misol: `123456789`.
