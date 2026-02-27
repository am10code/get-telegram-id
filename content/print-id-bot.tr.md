+++
title = "print_id_bot: Telegram ID ve chat_id yardımcısı (komutlar, diller, özellikler)"
description = "@print_id_bot için tam referans: komutlar, 16 desteklenen dil, grup tetikleyicileri ve geliştirici özellikleri (/json, /dump). Telegram user ID ve chat_id'nizi saniyeler içinde alın."
cta = { text = "Botu açın — Telegram user ID ve chat_id'nizi anında göreceksiniz.", label = "Open @print_id_bot", url = "https://t.me/print_id_bot" }
+++

@print_id_bot, **Telegram user ID**'nizi, **chat_id**'nizi (gruplar ve süpergruplar için) ve kanal ID'sini gösteren bir Telegram botudur. Özel sohbette ve gruplarda çalışır; Telegram dil ayarınıza göre 16 dilde yanıt verir.

## Komutlar

| Komut | İşlevi |
|-------|--------|
| `/start` | Hoş geldin mesajı, User ID ve Chat ID, /id ve /help için inline düğmeler |
| `/id` | User ID ve Chat ID (kısa yanıt) |
| `/help` | Tam yardım metni ve komut listesi |
| `/json` | Mevcut mesaj JSON formatında (geliştiriciler için) |
| `/dump` | Tam update ayrıntısı ve ham JSON (yalnızca özel sohbette) |

Özel sohbette herhangi bir mesaj (metin, fotoğraf, sticker vb.) göndermek de User ID ve Chat ID'nizi döndürür. İletilen mesajlarda bot, yazarın ID'sini mümkünse gösterir; gönderenin gizlilik ayarları engelliyorsa "ID hidden" gösterir. Ayrıntılar için [iletilen mesajlar ve gizli ID'ler]({{< relref "telegram-forwarded-message-id.md" "en" >}}) sayfasına bakın.

## Desteklenen diller (16)

Bot yanıt dilini Telegram `language_code` ayarınızdan seçer. Desteklenenler: İngilizce, Rusça, Farsça, Özbekçe, Hintçe, Çince, Türkçe, Portekizce, İspanyolca, Arapça, Endonezce, Almanca, Urduca, Fransızca, Tagalogca, Amharca. Desteklenmeyen kodlar İngilizce'ye döner. Bkz. [dil seçiminin nasıl çalıştığı]({{< relref "telegram-id-bot-languages.md" "en" >}}).

## Grup ve süpergrup davranışı

Gruplarda bot yalnızca şu durumlarda yanıt verir:

- Botun mesajına yanıt verdiğinizde
- `/id` veya `/help` gönderdiğinizde (@print_id_bot ile veya olmadan)
- @print_id_bot ile herhangi bir komut gönderdiğinizde (örn. `/foo@print_id_bot`)
- Mesajınızda @print_id_bot'dan bahsettiğinizde

Aksi halde sessiz kalır. Gruba eklendiğinde grup adı ve chat_id ile hoş geldin mesajı gönderir. Kısa rehber: [chat_id almak için gruba bot ekleme]({{< relref "add-bot-to-group-chat-id.md" "en" >}}).

## Geliştirici özellikleri

- **/json** — Mevcut mesajı JSON olarak döndürür.
- **/dump** — Tam update ayrıntısı ve ham JSON (yalnızca özel sohbette). Bot API entegrasonlarını hata ayıklamak için kullanışlıdır. Bkz. [Telegram update JSON'unu inceleme]({{< relref "telegram-json-update.md" "en" >}}).

## İlgili sayfalar

- [Telegram user ID alma (güvenli yöntemler)]({{< relref "get-telegram-user-id.md" "en" >}})
- [Telegram'da grup chat_id alma]({{< relref "get-telegram-chat-id.md" "en" >}})
- [Telegram ID'nizi bulma]({{< relref "how-to-find-telegram-id.md" "en" >}})

## SSS

### Bot kanallarda çalışır mı?
Bot özel sohbette ve gruplarda/süpergruplarda çalışır. Kanallar için kanal ID'si farklı bir akıştan alınmalıdır (örn. kanal olarak yayınlamak ve update alan bir bot kullanmak). Bkz. [Bot API için Telegram kanal ID'si alma]({{< relref "how-to-get-channel-id-bot-api.md" "en" >}}).

### Başkasının Telegram user ID'sini alabilir miyim?
Bot kendi ID'nizi veya bulunduğunuz sohbetlerin chat_id'sini gösterir. İletilen mesajlarda yalnızca gönderen iletmeye izin verdiyse ID gösterilir; aksi halde "ID hidden". Telefon numarası veya username ile ID arayamazsınız. Bkz. [Telegram ID ve username]({{< relref "telegram-id-vs-username.md" "en" >}}).

### Bot neden grubumda yanıt vermiyor?
Bot yalnızca ona yanıt verdiğinizde, /id veya /help gönderdiğinizde veya @print_id_bot'dan bahsettiğinizde yanıt verir. Tam liste için bkz. [grupta yanıt vermeyen bot]({{< relref "bot-not-responding-in-group.md" "en" >}}).

### Bot ücretsiz mi?
Evet. Kayıt veya ödeme gerekmez.

### user ID ile chat_id arasındaki fark nedir?
**User ID** bir Telegram hesabını tanımlar. **chat_id** bir sohbeti tanımlar (özel sohbet, grup, süpergrup, kanal). Bkz. [Telegram ID ve username]({{< relref "telegram-id-vs-username.md" "en" >}}).
