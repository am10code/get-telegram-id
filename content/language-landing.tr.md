+++
title = "Telegram ID Al"
description = "Telegram user ID ve grup chat_id'nizi saniyeler içinde alın. @print_id_bot özel sohbette ve gruplarda çalışır. Güvenli ve ücretsiz."
cta = { url = "https://t.me/print_id_bot", label = "Open @print_id_bot" }
+++

**Telegram user ID**, hesabınızın sayısal tanımlayıcısıdır. Entegrasyonlar, botlar ve geliştirme için gereklidir. Telegram arayüzünde görünmez, ancak @print_id_bot ile saniyeler içinde alabilirsiniz. Güvenli yöntemler hakkında daha fazla bilgi [user ID rehberlerinde]({{< relref "user-id-guides.md" >}}).

## Özel sohbette Telegram user ID nasıl alınır

@print_id_bot'u özel sohbette açın ve **Başlat**'a dokunun. Bot anında **Telegram user ID**'nizi, kullanıcı adınızı (varsa) ve chat_id'yi döndürür. Başka bir şey gerekmez: sadece mesajdaki sayıyı kopyalayın.

Özel sohbette bot her mesaja yanıt verir: metin, fotoğraf, çıkartma veya `/id` komutu. Ne gönderirseniz gönderin, ID'nizi alırsınız. Gizlidir: yanıtı sadece siz görürsünüz.

## Grubun chat_id'si nasıl alınır

Bir grubun veya süpergrubun **chat_id**'sini almak için @print_id_bot'u gruba ekleyin. Eklendikten sonra bot, grubun adı ve chat_id ile bir karşılama mesajı gönderir.

Gruplarda bot **yalnızca belirli eylemlerde** yanıt verir. chat_id almak için şunlardan birini yapın:

- **/id** veya **/help** komutunu gönderin (@print_id_bot ile veya olmadan)
- Botun mesajına yanıt verin
- Mesajınızda **@print_id_bot**'u etiketleyin
- @print_id_bot ile herhangi bir komut gönderin (örneğin `/foo@print_id_bot`)

Botu etiketlemeyen normal mesajlar yanıt tetiklemez: böylece spam önlenir. Grup ve süpergrup ID'leri genellikle negatiftir; bu normaldir.

## Nereden başlamalı

- [Telegram user ID rehberleri]({{< relref "user-id-guides.md" >}}) — user ID'nizi nasıl bulacağınız, kopyalayacağınız ve anlayacağınız
- [chat_id rehberleri]({{< relref "chat-id-guides.md" >}}) — gruplar ve süpergruplar için chat_id alma
- [Bot API rehberleri]({{< relref "bot-api-guides.md" >}}) — Telegram Bot API entegrasyonu

## FAQ

### Telegram ID'm gizli mi?

Telegram ID'niz uygulamada herkese açık gösterilmez. Botlar ve uygulamalar yalnızca onlarla etkileşime girdiğinizde alır — örneğin bir bot açıp Başlat'a dokunduğunuzda. Hangi botlara güveneceğinize siz karar verirsiniz.

### Bot neden grupta yanıt vermiyor?

Bot yalnızca mesajına yanıt verdiğinizde, /id veya /help gönderdiğinizde veya @print_id_bot'u etiketlediğinizde yanıt verir. Bu tetikleyiciler olmadan normal mesajları yok sayar. Botun grupta olduğundan ve mesajları okuyabildiğinden emin olun.

### user ID ile chat_id arasındaki fark nedir?

**user ID** Telegram hesabınızı tanımlar. **chat_id** sohbeti tanımlar: özel, grup, süpergrup veya kanal. Özel sohbette user ID ve chat_id aynı sayıdır. Gruplarda chat_id genellikle negatiftir.
