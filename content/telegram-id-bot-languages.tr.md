+++
title = "Telegram ID botu 16 dilde: dil seçimi nasıl çalışır"
description = "@print_id_bot yanıt dilini Telegram language_code'unuzdan nasıl seçiyor. 16 desteklenen dil, İngilizce'ye fallback. Rusça, Farsça, Arapça ve daha fazlası."
cta = { text = "@print_id_bot'u açın — Telegram dilinizde yanıt verir.", label = "Open @print_id_bot", url = "https://t.me/print_id_bot" }
+++

@print_id_bot Telegram dil ayarınıza göre **16 dilde** yanıt verir. Manuel dil seçimi gerekmez.

## Nasıl çalışır

Bot **language_code**'unuzu update'ten okur (`message.from.language_code`, `edited_message.from.language_code` veya `callback_query.from.language_code`). Kodun ilk kısmını kullanır (örn. `pt-BR` → `pt`) ve desteklenen locale'e eşler. Desteklenmeyen kodlar **İngilizce**'ye döner.

## Desteklenen diller (16)

| Kod | Dil |
|-----|-----|
| `en` | İngilizce |
| `ru` | Rusça |
| `fa` | Farsça |
| `uz` | Özbekçe |
| `hi` | Hintçe |
| `zh` | Çince |
| `tr` | Türkçe |
| `pt` | Portekizce |
| `es` | İspanyolca |
| `ar` | Arapça |
| `id` | Endonezce |
| `de` | Almanca |
| `ur` | Urduca |
| `fr` | Fransızca |
| `tl` | Tagalog (Filipince; `fil` → `tl`) |
| `am` | Amharca |

## Özel durumlar

- **Filipince** — Telegram `fil` gönderir; bot `tl` (Tagalog) ile eşler.
- **Portekizce (Brezilya)** — `pt-BR` `pt` (Portekizce) kullanır.
- **Çince** — `zh-CN`, `zh-TW` `zh` (Çince) kullanır.

## Neler yerelleştirildi

Tüm bot yanıtları: hoş geldin metni, etiketler (User ID, Chat ID, grup adı), yardım metni, düğmeler ve "ID hidden" veya "Kopyalamak için numaraya dokunun" gibi mesajlar. /json ve /dump'taki ham JSON değişmez; sadece okunabilir etiketler dilinizi kullanır.

## İlgili sayfalar

- [İngilizce bilmiyorsanız @print_id_bot kullanımı]({{< relref "telegram-id-bot-for-non-english.md" "en" >}})
- [print_id_bot: komutlar, diller, özellikler]({{< relref "print-id-bot.md" "en" >}})
- [Telegram user ID al (güvenli yöntemler)]({{< relref "get-telegram-user-id.md" "en" >}})

## FAQ

### Botun dilini nasıl değiştiririm?
Telegram uygulama dilini Ayarlar → Dil'den değiştirin. Bot bunu kullanır. Bottaki dil anahtarı yoktur.

### Dilim desteklenmiyorsa?
Bot İngilizce'ye döner. Tüm işlevler aynı çalışır.

### Bot sağdan sola (RTL) dilleri destekliyor mu?
Evet. Arapça, Farsça ve Urduca desteklenir. Telegram RTL render'ı yönetir.

### Yeni dil talep edebilir miyim?
Bot 16 dil destekler. Daha fazlası bakıcılara bağlıdır. İngilizce fallback herkesin kullanmasını sağlar.

### Dil saklanıyor veya başka yere gönderiliyor mu?
Hayır. Bot her update'ten `language_code` okur ve sadece yanıt dizelerini seçmek için kullanır. Saklanmaz veya paylaşılmaz.
