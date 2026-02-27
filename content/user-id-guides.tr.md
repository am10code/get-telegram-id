+++
title = "Telegram user ID rehberleri"
description = "Telegram user ID'nizi bulmak, kopyalamak ve anlamak için rehberler. Güvenli yöntemler, gizlilik ipuçları ve sık sorulan sorular."
cta = { text = "Telegram user ID'nizi anında alın.", label = "Open @print_id_bot", url = "https://t.me/print_id_bot" }
+++

**Telegram user ID** hesabınızın sayısal tanımlayıcısıdır. Sabittir, bir kez atanır ve Telegram uygulamasında hiçbir yerde gösterilmez. Botlar ve entegrasyonlar yalnızca onlarla etkileşime girdiğinizde okuyabilir — örneğin bir bot açıp Başlat'a tıkladığınızda veya mesaj gönderdiğinizde. Bu hub, user ID'nizi güvenli bir şekilde bulmanıza, kopyalamanıza ve anlamanıza yardımcı olacak rehberleri toplar.

Başka birinin ID'sini yalnızca telefon numarası veya kullanıcı adıyla alamazsınız. «Telefonla ID arama» vaat eden hizmetler genellikle dolandırıcılık veya gizlilik ihlalidir. ID'ler yalnızca etkileşim yoluyla elde edilir: kullanıcı bir bot açar, mesaj iletir (izin verirse) veya erişebildiğiniz bir sohbete katılır.

## Rehberler

- **[Telegram ID'nizi nasıl bulursunuz]({{< relref "how-to-find-telegram-id.md" >}})** — User ID'nizi almak için adım adım yöntemler. En hızlı yol bir bot kullanmak: açın, Başlat'a tıklayın ve numarayı kopyalayın.

- **[Telegram user ID alın (güvenli yöntemler)]({{< relref "get-telegram-user-id.md" >}})** — ID'nizi almanın güvenli yolları: bot üzerinden, mesaj göndererek veya iletimle (gizlilik sınırlarıyla). Ne yapamayacağınız ve neden.

- **[Telegram ID ve kullanıcı adı: fark nedir?]({{< relref "telegram-id-vs-username.md" >}})** — ID'ler sayısal ve sabittir; kullanıcı adları isteğe bağlı ve değiştirilebilir. Bot API veya entegrasyonlar için ID ne zaman gerekir.

- **[Telegram ID'nizi güvenle nasıl kopyalar ve paylaşırsınız]({{< relref "how-to-copy-telegram-id.md" >}})** — Bottan kopyalamak için tıklayın, güvenle paylaşın ve dolandırıcılıktan kaçının. ID paylaşırken gizlilik ipuçları.

- **[Telegram neden sayısal ID'nizi göstermiyor (ve ne yapmalı)]({{< relref "telegram-id-not-in-ui.md" >}})** — Telegram sayısal ID'nizi uygulamada gizler. Neden gizli ve ihtiyaç duyduğunuzda nasıl alınır.

- **[Telegram'da iletilen mesajlar: ID'ler neden gizlenebilir]({{< relref "telegram-forwarded-message-id.md" >}})** — Bir mesajı bota ilettiğinizde, gönderenin ID'si görünebilir veya iletimi engelleyen gizlilik ayarları varsa «ID hidden» olabilir.

## FAQ

### Telegram ID'm gizli mi?

Telegram ID'niz Telegram arayüzünde herkese açık gösterilmez, ancak botlar ve uygulamalar onlarla etkileşime girdiğinizde okuyabilir. Hangi bot ve uygulamaları kullandığınızı seçerek kimin alacağını kontrol edersiniz.

### Başka birinin ID'sini telefon numarası veya kullanıcı adıyla alabilir miyim?

Hayır. Yalnızca telefon numarası veya kullanıcı adıyla güvenilir şekilde Telegram user ID alamazsınız. ID'ler yalnızca kullanıcı bir bot veya uygulamayla etkileşime girdiğinde veya mesaj ilettiğinde (ve iletimine izin verdiğinde) elde edilir. Aksi iddia eden hizmetlerden kaçının.

### user ID ile chat_id arasındaki fark nedir?

**User ID** bir Telegram hesabını tanımlar. **chat_id** bir sohbeti tanımlar (özel sohbet, grup, süpergrup, kanal). Özel sohbette user ID ve chat_id aynı sayıdır.
