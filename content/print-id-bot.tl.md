+++
title = "print_id_bot: Telegram ID at chat_id helper (mga command, wika, feature)"
description = "Kumpletong reference para sa @print_id_bot: mga command, 16 na wika, group trigger, at developer feature (/json, /dump). Kunin ang iyong Telegram user ID at chat_id sa loob ng ilang segundo."
cta = { text = "Buksan ang bot para makuha kaagad ang iyong Telegram user ID at chat_id.", label = "Open @print_id_bot", url = "https://t.me/print_id_bot" }
+++

Ang @print_id_bot ay isang Telegram bot na nagpapakita ng iyong **Telegram user ID**, **chat_id** (para sa mga grupo at supergroup), at channel ID. Gumagana sa private chat at sa mga grupo, may respons sa 16 na wika batay sa iyong Telegram language setting.

## Mga command

| Command | Ginagawa |
|---------|----------|
| `/start` | Mensahe ng welcome, iyong User ID at Chat ID, inline button para sa /id at /help |
| `/id` | Iyong User ID at Chat ID (maikling sagot) |
| `/help` | Buong help text at listahan ng command |
| `/json` | Kasalukuyang mensahe sa JSON (para sa mga developer) |
| `/dump` | Buong update breakdown at raw JSON (private chat lang) |

Sa private chat, ang pagpapadala ng kahit anong mensahe (text, photo, sticker, atbp.) ay nagbabalik din ng iyong User ID at Chat ID. Para sa forwarded na mensahe, ipinapakita ng bot ang ID ng may-akda kapag available, o "ID hidden" kapag ang privacy setting ng nagpadala ay nag-block. Tingnan [forwarded na mensahe at nakatagong ID]({{< relref "telegram-forwarded-message-id.md" "en" >}}) para sa detalye.

## Suportadong wika (16)

Pinipili ng bot ang wika ng respons mula sa iyong Telegram `language_code`. Suportado: Ingles, Ruso, Persian, Uzbek, Hindi, Chinese, Turkish, Portuguese, Spanish, Arabic, Indonesian, German, Urdu, French, Tagalog, Amharic. Ang unsupported na code ay babalik sa Ingles. Tingnan [paano gumagana ang language selection]({{< relref "telegram-id-bot-languages.md" "en" >}}).

## Pag-uugali sa grupo at supergroup

Sa grupo, ang bot ay sumasagot lang kapag:

- Sumasagot ka sa mensahe ng bot
- Nagpapadala ka ng `/id` o `/help` (may o walang @print_id_bot)
- Nagpapadala ka ng kahit anong command na may @print_id_bot (hal. `/foo@print_id_bot`)
- Binabanggit mo ang @print_id_bot sa iyong mensahe

Kung hindi, nananatiling tahimik. Kapag idinagdag sa grupo, nagpapadala ng welcome message na may grupo name at chat_id. Tingnan [magdagdag ng bot sa grupo para makuha ang chat_id]({{< relref "add-bot-to-group-chat-id.md" "en" >}}) para sa mabilis na gabay.

## Developer feature

- **/json** — Nagbabalik ng kasalukuyang mensahe sa JSON.
- **/dump** — Buong update breakdown at raw JSON (private chat lang). Kapaki-pakinabang para sa pag-debug ng Bot API integration. Tingnan [suriin ang Telegram update JSON]({{< relref "telegram-json-update.md" "en" >}}).

## Kaugnay na pahina

- [Kunin ang Telegram user ID (ligtas na paraan)]({{< relref "get-telegram-user-id.md" "en" >}})
- [Paano makuha ang chat_id ng Telegram grupo]({{< relref "get-telegram-chat-id.md" "en" >}})
- [Paano hanapin ang iyong Telegram ID]({{< relref "how-to-find-telegram-id.md" "en" >}})

## FAQ

### Gumagana ba ang bot sa mga channel?
Ang bot ay gumagana sa private chat at sa mga grupo/supergroup. Para sa channel, kailangan ang channel ID mula sa ibang flow (hal. mag-post bilang channel at gumamit ng bot na tumatanggap ng update). Tingnan [kumuha ng Telegram channel ID para sa Bot API]({{< relref "how-to-get-channel-id-bot-api.md" "en" >}}).

### Maaari ko bang makuha ang Telegram user ID ng iba?
Ang bot ay nagpapakita ng iyong sariling ID o chat_id ng mga chat na kasama ka. Para sa forwarded na mensahe, ipinapakita ang ID ng nagpadala lang kung pinapayagan nila ang forward; kung hindi, "ID hidden". Hindi mo maaaring hanapin ang ID sa pamamagitan ng phone number o username. Tingnan [Telegram ID vs username]({{< relref "telegram-id-vs-username.md" "en" >}}).

### Bakit hindi sumasagot ang bot sa aking grupo?
Ang bot ay sumasagot lang kapag sumasagot ka rito, nagpapadala ng /id o /help, o binabanggit ang @print_id_bot. Tingnan [bot na hindi sumasagot sa grupo]({{< relref "bot-not-responding-in-group.md" "en" >}}) para sa buong checklist.

### Libre ba ang bot?
Oo. Walang kailangang signup o bayad.

### Ano ang pagkakaiba ng user ID at chat_id?
Ang **User ID** ay nag-iidentify ng Telegram account. Ang **chat_id** ay nag-iidentify ng conversation (private chat, grupo, supergroup, channel). Tingnan [Telegram ID vs username]({{< relref "telegram-id-vs-username.md" "en" >}}).
