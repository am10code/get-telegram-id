+++
title = "Cara mendapatkan chat_id grup Telegram"
description = "Dapatkan chat_id grup atau supergrup Telegram dalam hitungan detik. Tambahkan @print_id_bot, kirim /id atau sebutkan, dan salin chat_id. Panduan langkah demi langkah."
cta = { text = "Tambahkan bot ke grup Anda dan dapatkan chat_id dalam 10 detik.", label = "Open @print_id_bot", url = "https://t.me/print_id_bot" }
+++

**chat_id** grup atau supergrup Telegram diperlukan untuk integrasi Bot API. Berikut cara mendapatkannya dengan cepat.

## Langkah 1: Tambahkan bot ke grup Anda

1. Buka [@print_id_bot](https://t.me/print_id_bot) di Telegram.
2. Ketuk **Mulai**.
3. Tambahkan bot ke grup: Buka grup → Tambah anggota → cari `print_id_bot` → Tambah.

Saat bot ditambahkan, ia mengirim pesan selamat datang dengan nama grup dan **chat_id**. Anda bisa menyalinnya dari sana.

## Langkah 2: Jika perlu mendapatkannya lagi

Bot merespons di grup hanya ketika:

- Anda membalas pesan bot;
- Anda mengirim `/id` atau `/help` (dengan atau tanpa @print_id_bot);
- Anda mengirim perintah apa pun dengan @print_id_bot (mis. `/foo@print_id_bot`);
- Anda menyebut @print_id_bot dalam pesan.

Kirim `/id` atau sebutkan @print_id_bot, dan bot akan membalas dengan nama grup dan chat_id. Ketuk angka untuk menyalin.

## Grup vs supergrup: chat_id

ID grup dan supergrup sering berupa **angka negatif**. Itu normal. Saat grup ditingkatkan ke supergrup, chat_id bisa berubah. Lihat [chat_id grup vs supergrup]({{< relref "telegram-group-chat-id-vs-supergroup.md" "en" >}}) untuk detail.

## Pemecahan masalah

Jika bot tidak merespons, periksa:

- bot punya izin membaca pesan;
- Anda memicunya dengan benar (balas, /id, /help, atau @print_id_bot);
- bot tidak dalam mode privasi yang memblokir pesan grup (jika berlaku).

Daftar lengkap: [bot tidak merespons di grup Telegram]({{< relref "bot-not-responding-in-group.md" "en" >}}).

## Halaman terkait

- [Tambahkan bot ke grup untuk mendapatkan chat_id (10 detik)]({{< relref "add-bot-to-group-chat-id.md" "en" >}})
- [Telegram Bot API: cara mendapatkan chat_id]({{< relref "telegram-bot-api-chat-id.md" "en" >}})
- [Mengapa chat_id Telegram bisa negatif]({{< relref "telegram-chat-id-negative.md" "en" >}})

## FAQ

### Mengapa chat_id grup saya negatif?
ID grup dan supergrup biasanya negatif di Telegram Bot API. Itu by design. Lihat [format chat_id Telegram]({{< relref "telegram-chat-id-format.md" "en" >}}).

### Bisakah saya mendapatkan chat_id grup orang lain?
Hanya grup yang Anda ikuti. Tambahkan bot ke grup dan kirim /id atau sebutkan.

### Apakah bot berfungsi di supergrup?
Ya. Grup dan supergrup didukung. Bot menampilkan nama grup dan chat_id. Lihat [chat_id grup vs supergrup]({{< relref "telegram-group-chat-id-vs-supergroup.md" "en" >}}).

### Bagaimana jika bot dihapus dari grup?
Tambahkan lagi. Saat ditambahkan, ia mengirim pesan selamat datang dengan chat_id. Anda juga bisa mendapatkannya dengan mengirim /id atau menyebut @print_id_bot.

### Apakah chat_id sama untuk grup dan supergrup?
Setelah migrasi ke supergrup, chat_id bisa berubah. Selalu gunakan nilai terbaru dari bot atau API.
