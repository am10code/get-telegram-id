+++
title = "Bot Telegram ID dalam 16 bahasa: cara kerja pemilihan bahasa"
description = "Bagaimana @print_id_bot memilih bahasa respons dari language_code Telegram Anda. 16 bahasa didukung, fallback ke Inggris. Rusia, Persia, Arab, dan lainnya."
cta = { text = "Buka @print_id_bot — ia merespons dalam bahasa Telegram Anda.", label = "Open @print_id_bot", url = "https://t.me/print_id_bot" }
+++

@print_id_bot merespons dalam **16 bahasa** berdasarkan pengaturan bahasa Telegram. Tidak perlu pemilihan manual.

## Cara kerjanya

Bot membaca **language_code** Anda dari update (`message.from.language_code`, `edited_message.from.language_code` atau `callback_query.from.language_code`). Menggunakan bagian pertama kode (mis. `pt-BR` → `pt`) dan memetakan ke locale yang didukung. Kode tidak didukung fallback ke **Inggris**.

## Bahasa yang didukung (16)

| Kode | Bahasa |
|------|--------|
| `en` | Inggris |
| `ru` | Rusia |
| `fa` | Persia |
| `uz` | Uzbek |
| `hi` | Hindi |
| `zh` | Tionghoa |
| `tr` | Turki |
| `pt` | Portugis |
| `es` | Spanyol |
| `ar` | Arab |
| `id` | Indonesia |
| `de` | Jerman |
| `ur` | Urdu |
| `fr` | Prancis |
| `tl` | Tagalog (Filipino; `fil` memetakan ke `tl`) |
| `am` | Amhar |

## Kasus khusus

- **Filipino** — Telegram mengirim `fil`; bot memetakan ke `tl` (Tagalog).
- **Portugis (Brasil)** — `pt-BR` menggunakan `pt` (Portugis).
- **Tionghoa** — `zh-CN`, `zh-TW` menggunakan `zh` (Tionghoa).

## Apa yang dilokalkan

Semua respons bot: teks selamat datang, label (User ID, Chat ID, nama grup), teks bantuan, tombol, dan pesan seperti "ID hidden" atau "Ketuk angka untuk menyalin". JSON mentah di /json dan /dump tidak berubah; hanya label yang terbaca menggunakan bahasa Anda.

## Halaman terkait

- [Menggunakan @print_id_bot jika Anda tidak berbahasa Inggris]({{< relref "telegram-id-bot-for-non-english.md" "en" >}})
- [print_id_bot: perintah, bahasa, fitur]({{< relref "print-id-bot.md" "en" >}})
- [Dapatkan Telegram user ID (metode aman)]({{< relref "get-telegram-user-id.md" "en" >}})

## FAQ

### Bagaimana cara mengubah bahasa bot?
Ubah bahasa app Telegram di Pengaturan → Bahasa. Bot menggunakannya. Tidak ada pengalih bahasa di bot.

### Bagaimana jika bahasa saya tidak didukung?
Bot fallback ke Inggris. Semua fungsi bekerja sama.

### Apakah bot mendukung bahasa kanan-ke-kiri (RTL)?
Ya. Arab, Persia, dan Urdu didukung. Telegram menangani rendering RTL.

### Bisakah saya meminta bahasa baru?
Bot mendukung 16 bahasa. Menambah lebih tergantung maintainer. Fallback Inggris memastikan semua bisa menggunakannya.

### Apakah bahasa disimpan atau dikirim ke tempat lain?
Tidak. Bot membaca `language_code` dari setiap update dan menggunakannya hanya untuk memilih string respons. Tidak disimpan atau dibagikan.
