+++
title = "Telegram user ID alma (güvenli yöntemler)"
description = "Telegram user ID'nizi güvenle nasıl alırsınız. @print_id_bot ile adım adım yöntemler. Geliştirici araçları gerekmez. Mobil ve masaüstünde çalışır."
cta = { text = "Botu açın ve Başlat'a dokunun — Telegram user ID'niz anında görünecektir.", label = "Open @print_id_bot", url = "https://t.me/print_id_bot" }
+++

**Telegram user ID** hesabınızın sayısal tanımlayıcısıdır. Telegram uygulamasında gösterilmez, ancak etkileşime girdiğinizde botlar ve entegrasyonlar okuyabilir. İşte güvenle almanın yolları.

## Yöntem 1: @print_id_bot kullanın (en hızlı)

1. Telegram'da [@print_id_bot](https://t.me/print_id_bot) açın.
2. **Başlat**'a dokunun.
3. Bot **User ID** ve **Chat ID** ile yanıt verir (özel sohbette aynıdır).
4. Kopyalamak için numaraya dokunun.

Bot Telegram dil ayarınıza göre 16 dilde yanıt verir. Desteklenmeyen diller İngilizce'ye döner.

## Yöntem 2: Bota herhangi bir mesaj gönderin

@print_id_bot ile özel sohbette herhangi bir mesaj, fotoğraf, sticker veya belge gönderin. Bot User ID ve Chat ID'nizi döndürür. Kısa yanıt için `/id` de kullanabilirsiniz.

## Yöntem 3: Mesaj iletin (ve sınırlamalar)

Başka bir kullanıcıdan gelen mesajı @print_id_bot'a iletirseniz, bot orijinal gönderenin User ID'sini gösterebilir. Ancak gönderenin iletme sırasında ID'sini gizleyen gizlilik ayarları varsa "ID hidden" görürsünüz. Telefon numarası veya username ile başkasının ID'sini güvenilir şekilde alamazsınız. Ayrıntılar için [iletilen mesajlar ve gizli ID'ler]({{< relref "telegram-forwarded-message-id.md" "en" >}}) sayfasına bakın.

## Yapamayacaklarınız

- **Telefon numarasıyla arama**: Yalnızca telefon numarası ile Telegram user ID alamazsınız. Bunu vaat eden hizmetler genelde dolandırıcılık veya gizlilik ihlalidir.
- **Username ile arama**: Username'ler ID değildir. ID almak için kullanıcının bot veya uygulama ile etkileşime girmesi gerekir.
- **Etkileşim olmadan başkalarının ID'lerini görme**: Yalnızca bulunduğunuz sohbetlerin veya size mesaj ileten (ve iletmeye izin veren) kullanıcıların ID'lerini alabilirsiniz.

## İlgili sayfalar

- [Telegram ID vs username: fark nedir?]({{< relref "telegram-id-vs-username.md" "en" >}})
- [Telegram neden sayısal ID'nizi göstermiyor]({{< relref "telegram-id-not-in-ui.md" "en" >}})
- [print_id_bot: komutlar, diller, özellikler]({{< relref "print-id-bot.md" "en" >}})

## SSS

### Telegram user ID'm gizli mi?
Telegram arayüzünde gösterilmez, ancak etkileşime girdiğinizde botlar ve uygulamalar okuyabilir. Güvenilir olmayan hizmetlerle paylaşmayın.

### Telegram user ID'mi değiştirebilir miyim?
Hayır. Bir kez atanır ve değişmez.

### İletilen mesajlarda bot neden "ID hidden" gösteriyor?
Gönderen, mesajlar iletildiğinde ID'sini gizleyen gizlilik ayarlarını etkinleştirmiştir. Bkz. [iletilen gönderen ID'si gizli]({{< relref "telegram-privacy-forwarded-id-hidden.md" "en" >}}).

### @print_id_bot kullanmak güvenli mi?
Evet. Bot yalnızca zaten erişiminiz olan ID'leri gösterir (kendi ID'niz veya bulunduğunuz sohbetlerden). Telegram'ın sağladığından öte verilerinizi saklamaz veya paylaşmaz.

### Telegram user ID nasıl görünür?
Genelde 9–10 haneli sayısal bir değerdir. Örnek: `123456789`.
