+++
title = "print_id_bot: Bantuan Telegram ID & chat_id (perintah, bahasa, fitur)"
description = "Referensi lengkap @print_id_bot: perintah, 16 bahasa, pemicu grup, dan fitur pengembang (/json, /dump). Dapatkan Telegram user ID dan chat_id Anda dalam hitungan detik."
cta = { text = "Buka bot untuk mendapatkan Telegram user ID dan chat_id Anda secara instan.", label = "Open @print_id_bot", url = "https://t.me/print_id_bot" }
+++

@print_id_bot adalah bot Telegram yang menampilkan **Telegram user ID**, **chat_id** (untuk grup dan supergrup), dan ID kanal Anda. Berfungsi di chat pribadi dan grup, dengan respons dalam 16 bahasa berdasarkan pengaturan bahasa Telegram Anda.

## Perintah

| Perintah | Fungsi |
|----------|--------|
| `/start` | Pesan selamat datang, User ID dan Chat ID Anda, tombol inline untuk /id dan /help |
| `/id` | User ID dan Chat ID Anda (balasan singkat) |
| `/help` | Teks bantuan lengkap dan daftar perintah |
| `/json` | Pesan saat ini dalam JSON (untuk pengembang) |
| `/dump` | Rincian update lengkap dan JSON mentah (hanya di chat pribadi) |

Di chat pribadi, mengirim pesan apa pun (teks, foto, stiker, dll.) juga mengembalikan User ID dan Chat ID Anda. Untuk pesan yang diteruskan, bot menampilkan ID penulis jika tersedia, atau "ID hidden" jika pengaturan privasi pengirim memblokirnya. Lihat [pesan diteruskan dan ID tersembunyi]({{< relref "telegram-forwarded-message-id.md" "en" >}}) untuk detail.

## Bahasa yang didukung (16)

Bot memilih bahasa respons dari `language_code` Telegram Anda. Didukung: Inggris, Rusia, Persia, Uzbek, Hindi, Cina, Turki, Portugis, Spanyol, Arab, Indonesia, Jerman, Urdu, Prancis, Tagalog, Amhar. Kode yang tidak didukung kembali ke Inggris. Lihat [cara kerja pemilihan bahasa]({{< relref "telegram-id-bot-languages.md" "en" >}}).

## Perilaku di grup dan supergrup

Di grup, bot hanya merespons ketika Anda:

- Membalas pesan bot
- Mengirim `/id` atau `/help` (dengan atau tanpa @print_id_bot)
- Mengirim perintah apa pun dengan @print_id_bot (mis. `/foo@print_id_bot`)
- Menyebut @print_id_bot dalam pesan Anda

Jika tidak, bot diam. Saat ditambahkan ke grup, bot mengirim pesan selamat datang dengan nama grup dan chat_id. Lihat [menambahkan bot ke grup untuk mendapatkan chat_id]({{< relref "add-bot-to-group-chat-id.md" "en" >}}) untuk panduan singkat.

## Fitur pengembang

- **/json** — Mengembalikan pesan saat ini sebagai JSON.
- **/dump** — Rincian update lengkap dan JSON mentah (hanya di chat pribadi). Berguna untuk debugging integrasi Bot API. Lihat [memeriksa JSON update Telegram]({{< relref "telegram-json-update.md" "en" >}}).

## Halaman terkait

- [Dapatkan Telegram user ID (metode aman)]({{< relref "get-telegram-user-id.md" "en" >}})
- [Cara mendapatkan chat_id grup Telegram]({{< relref "get-telegram-chat-id.md" "en" >}})
- [Cara menemukan Telegram ID Anda]({{< relref "how-to-find-telegram-id.md" "en" >}})

## FAQ

### Apakah bot berfungsi di kanal?
Bot berfungsi di chat pribadi dan grup/supergrup. Untuk kanal, Anda memerlukan ID kanal dari alur lain (mis. memposting sebagai kanal dan menggunakan bot yang menerima update). Lihat [dapatkan ID kanal Telegram untuk Bot API]({{< relref "how-to-get-channel-id-bot-api.md" "en" >}}).

### Bisakah saya mendapatkan Telegram user ID orang lain?
Bot menampilkan ID Anda sendiri atau chat_id dari chat tempat Anda berada. Untuk pesan diteruskan, bot menampilkan ID pengirim hanya jika mereka mengizinkan penerusan; jika tidak, "ID hidden". Anda tidak dapat mencari ID berdasarkan nomor telepon atau username. Lihat [Telegram ID vs username]({{< relref "telegram-id-vs-username.md" "en" >}}).

### Mengapa bot tidak merespons di grup saya?
Bot hanya merespons ketika Anda membalasnya, mengirim /id atau /help, atau menyebut @print_id_bot. Lihat [bot tidak merespons di grup]({{< relref "bot-not-responding-in-group.md" "en" >}}) untuk daftar lengkap.

### Apakah bot gratis?
Ya. Tidak perlu pendaftaran atau pembayaran.

### Apa perbedaan antara user ID dan chat_id?
**User ID** mengidentifikasi akun Telegram. **chat_id** mengidentifikasi percakapan (chat pribadi, grup, supergrup, kanal). Lihat [Telegram ID vs username]({{< relref "telegram-id-vs-username.md" "en" >}}).
