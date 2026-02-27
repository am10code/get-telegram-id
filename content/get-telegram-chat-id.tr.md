+++
title = "Telegram grubu için chat_id nasıl alınır"
description = "Telegram grubu veya süpergrubun chat_id'sini saniyeler içinde alın. @print_id_bot ekleyin, /id gönderin veya etiketleyin ve chat_id'yi kopyalayın. Adım adım rehber."
cta = { text = "Botu grubunuza ekleyin ve 10 saniyede chat_id alın.", label = "Open @print_id_bot", url = "https://t.me/print_id_bot" }
+++

Telegram grubu veya süpergrubun **chat_id**'si Bot API entegrasyonları için gereklidir. Hızlıca nasıl alınacağı aşağıda.

## Adım 1: Botu grubunuza ekleyin

1. Telegram'da [@print_id_bot](https://t.me/print_id_bot) açın.
2. **Başlat**'a dokunun.
3. Botu gruba ekleyin: Grubu açın → Üye ekle → `print_id_bot` arayın → Ekle.

Bot eklendiğinde grup adı ve **chat_id** ile hoş geldin mesajı gönderir. Oradan kopyalayabilirsiniz.

## Adım 2: Tekrar almanız gerekiyorsa

Bot grupta yalnızca şu durumlarda yanıt verir:

- Botun mesajına yanıt verdiğinizde;
- `/id` veya `/help` gönderdiğinizde (@print_id_bot ile veya olmadan);
- @print_id_bot ile herhangi bir komut gönderdiğinizde (örn. `/foo@print_id_bot`);
- Mesajda @print_id_bot etiketlediğinizde.

`/id` gönderin veya @print_id_bot etiketleyin; bot grup adı ve chat_id ile yanıt verir. Kopyalamak için numaraya dokunun.

## Grup vs süpergrup: chat_id

Grup ve süpergrup ID'leri genellikle **negatif sayılardır**. Bu normaldir. Grup süpergruba yükseltildiğinde chat_id değişebilir. Ayrıntılar için bkz. [grup vs süpergrup chat_id]({{< relref "telegram-group-chat-id-vs-supergroup.md" "en" >}}).

## Sorun giderme

Bot yanıt vermiyorsa kontrol edin:

- Botun mesajları okuma izni var mı;
- Doğru tetiklediniz mi (yanıt, /id, /help veya @print_id_bot);
- Bot gizlilik modunda grup mesajlarını engellemiyor mu (varsa).

Tam liste için bkz. [Telegram grubunda bot yanıt vermiyor]({{< relref "bot-not-responding-in-group.md" "en" >}}).

## İlgili sayfalar

- [chat_id almak için gruba bot ekleme (10 saniye)]({{< relref "add-bot-to-group-chat-id.md" "en" >}})
- [Telegram Bot API: chat_id nasıl alınır]({{< relref "telegram-bot-api-chat-id.md" "en" >}})
- [Telegram chat_id neden negatif olabilir]({{< relref "telegram-chat-id-negative.md" "en" >}})

## FAQ

### Grubumun chat_id'si neden negatif?
Grup ve süpergrup ID'leri Telegram Bot API'de genellikle negatiftir. Tasarım gereği. Bkz. [Telegram chat_id formatı]({{< relref "telegram-chat-id-format.md" "en" >}}).

### Başkasının grubunun chat_id'sini alabilir miyim?
Yalnızca üye olduğunuz grupların. Botu gruba ekleyin ve /id gönderin veya etiketleyin.

### Bot süpergruplarda çalışıyor mu?
Evet. Hem gruplar hem süpergruplar desteklenir. Bot grup adını ve chat_id'yi gösterir. Bkz. [grup vs süpergrup chat_id]({{< relref "telegram-group-chat-id-vs-supergroup.md" "en" >}}).

### Bot gruptan kaldırıldıysa ne olur?
Tekrar ekleyin. Eklediğinizde chat_id ile hoş geldin mesajı gönderir. /id göndererek veya @print_id_bot etiketleyerek de alabilirsiniz.

### Grup ve süpergrup için chat_id aynı mı?
Süpergruba geçişten sonra chat_id değişebilir. Her zaman bot veya API'den güncel değeri kullanın.
