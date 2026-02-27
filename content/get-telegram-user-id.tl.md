+++
title = "Kunin ang Telegram user ID (ligtas na paraan)"
description = "Paano ligtas na makuha ang iyong Telegram user ID. Mga paraan hakbang-hakbang gamit ang @print_id_bot. Walang kailangang developer tool. Gumagana sa mobile at desktop."
cta = { text = "Buksan ang bot at i-tap ang Simula para makita kaagad ang iyong Telegram user ID.", label = "Open @print_id_bot", url = "https://t.me/print_id_bot" }
+++

Ang **Telegram user ID** mo ay ang numerical identifier ng iyong account. Hindi ito ipinapakita sa Telegram app, pero mababasa ito ng mga bot at integration kapag nakikipag-ugnayan ka sa kanila. Narito ang mga ligtas na paraan para makuha ito.

## Paraan 1: Gumamit ng @print_id_bot (pinakamabilis)

1. Buksan ang [@print_id_bot](https://t.me/print_id_bot) sa Telegram.
2. I-tap ang **Simula**.
3. Ang bot ay sumasagot ng iyong **User ID** at **Chat ID** (pareho sa private chat).
4. I-tap ang numero para kopyahin.

Ang bot ay sumasagot sa 16 na wika batay sa iyong Telegram language setting. Ang unsupported na wika ay babalik sa Ingles.

## Paraan 2: Magpadala ng kahit anong mensahe sa bot

Sa private chat na may @print_id_bot, magpadala ng kahit anong mensahe, photo, sticker, o dokumento. Ang bot ay sumasagot ng iyong User ID at Chat ID. Maaari mo ring gamitin ang `/id` para sa maikling sagot.

## Paraan 3: I-forward ang mensahe (at limitasyon)

Kung magfo-forward ka ng mensahe mula sa ibang user papunta sa @print_id_bot, maaaring ipakita ng bot ang User ID ng original na nagpadala. Gayunpaman, kung ang nagpadala ay may privacy setting na nagtatago ng ID kapag nagfo-forward, makikita mo ang "ID hidden". Hindi mo maaaring mapagkakatiwalaang makuha ang ID ng iba sa pamamagitan ng phone number o username. Tingnan [forwarded na mensahe at nakatagong ID]({{< relref "telegram-forwarded-message-id.md" "en" >}}) para sa detalye.

## Hindi mo maaaring gawin

- **Maghanap sa phone number**: Hindi mo maaaring makuha ang Telegram user ID mula sa phone number lamang. Ang mga serbisyo na nagsasabing kaya nila ay madalas na scam o lumalabag sa privacy.
- **Maghanap sa username**: Ang username ay hindi ID. Kailangan ng user na makipag-ugnayan sa bot o app para makuha ang kanilang ID.
- **Tingnan ang ID ng iba nang walang interaksyon**: Maaari mo lamang makuha ang ID ng mga chat na kasama ka o ng mga user na nagfo-forward ng mensa na natatanggap mo (at nagpapahintulot ng forward).

## Kaugnay na pahina

- [Telegram ID vs username: ano ang pagkakaiba?]({{< relref "telegram-id-vs-username.md" "en" >}})
- [Bakit hindi ipinapakita ng Telegram ang iyong numerical ID]({{< relref "telegram-id-not-in-ui.md" "en" >}})
- [print_id_bot: mga command, wika, feature]({{< relref "print-id-bot.md" "en" >}})

## FAQ

### Pribado ba ang aking Telegram user ID?
Hindi ito ipinapakita sa Telegram UI, pero mababasa ito ng mga bot at app kapag nakikipag-ugnayan ka. Huwag ibahagi sa hindi mapagkakatiwalaang serbisyo.

### Maaari ko bang baguhin ang aking Telegram user ID?
Hindi. Ito ay itinatalaga sa isang beses at hindi nagbabago.

### Bakit ipinapakita ng bot ang "ID hidden" para sa forwarded na mensahe?
Ang nagpadala ay nag-enable ng privacy setting na nagtatago ng kanilang ID kapag nagfo-forward. Tingnan [nakatagong ID ng forwarded na nagpadala]({{< relref "telegram-privacy-forwarded-id-hidden.md" "en" >}}).

### Ligtas ba ang paggamit ng @print_id_bot?
Oo. Ang bot ay nagpapakita lamang ng mga ID na may access ka na (iyong sarili o mula sa mga chat na kasama ka). Hindi ito nag-i-store o nag-share ng iyong data lampas sa ibinibigay ng Telegram.

### Ano ang hitsura ng Telegram user ID?
Numerical value, madalas 9–10 digit. Halimbawa: `123456789`.
