+++
title = "Telegram ID'nizi nasıl bulursunuz"
description = "Telegram kullanıcı ID'nizi ve chat_id'nizi (gruplar) güvenli bir şekilde almanın adım adım yolları. En hızlı yöntem bir Telegram botu kullanmaktır."
cta = { text = "En hızlı yol: botu açın, Telegram ID'nizi anında gösterecektir.", label = "Open @print_id_bot", url = "https://t.me/print_id_bot" }
+++

## En hızlı yol (1 saniye)

Botu açın ve **Başlat**'a basın. Şunları döndürecektir:

- **Telegram kullanıcı ID'niz**
- **Kullanıcı adınız** (varsa)
- (Gruplarda) grubun veya süpergrubun **chat_id**'si

## Yöntem 1 — Telegram botu kullanın (önerilen)

1. Botu açın: https://t.me/print_id_bot
2. **Başlat**'a dokunun
3. Telegram ID'nizi mesajdan kopyalayın

**Bu yöntem neden en iyi:** basit, mobil ve masaüstünde çalışır, geliştirici araçları gerektirmez.

## Yöntem 2 — Grup chat_id alın (Bot API için)

Entegrasyonlar için grup **chat_id**'sine ihtiyacınız varsa:

1. Botu grubunuza ekleyin
2. Grupta herhangi bir mesaj gönderin (veya botun `/id` gibi komutunu kullanın)
3. Bot grubun **chat_id**'siyle yanıt verecektir

> Not: Grup ve süpergrup ID'leri genellikle negatif sayılardır. Bu normaldir.

## Yaygın sorunlar

- **Bot grubumda yanıt vermiyor:** botun mesajları okuma iznine sahip olduğundan emin olun ve gizlilik modu ayarlarını kontrol edin (botun nasıl yapılandırıldığına bağlı).
- **Sadece kullanıcı adı görüyorum, ID değil:** kullanıcı adları ID değildir. ID'ler sayısal.
- **Başka birinin ID'sini istiyorum:** bu araç kendi ID'nizi veya bulunduğunuz sohbetlerin chat_id'sini almak içindir.

## SSS

### Telegram ID'm gizli mi?
Telegram ID'niz Telegram arayüzünde herkese açık gösterilmez, ancak botlar ve uygulamalar bunu etkileşime girdiğinizde okuyabilir.

### Telefon numarası veya kullanıcı adıyla ID alabilir miyim?
Resmi olarak, etkileşim olmadan genellikle telefon numarası veya kullanıcı adından birinin sayısal ID'sini güvenilir şekilde alamazsınız. «Telefonla ID arama» vaat eden hizmetlerden kaçının — bunlar genellikle dolandırıcılık veya gizlilik ihlalidir.

### User ID ile chat_id arasındaki fark nedir?
- **User ID** bir Telegram hesabını tanımlar.
- **chat_id** bir sohbeti tanımlar (özel sohbet, grup, süpergrup, kanal).
