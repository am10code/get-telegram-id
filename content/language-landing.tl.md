+++
title = "Kunin ang Telegram ID"
description = "Kunin ang iyong Telegram user ID at chat_id ng grupo sa loob ng ilang segundo. Ang bot @print_id_bot ay gumagana sa private chat at mga grupo. Ligtas at libre."
cta = { url = "https://t.me/print_id_bot", label = "Open @print_id_bot" }
+++

Ang **Telegram user ID** ay ang numerical identifier ng iyong account. Kailangan ito para sa mga integrasyon, bot, at development. Hindi ito makikita sa Telegram interface, ngunit makukuha mo ito sa loob ng ilang segundo gamit ang bot @print_id_bot. Higit pang impormasyon tungkol sa mga ligtas na paraan sa [mga gabay sa user ID]({{< relref "user-id-guides.md" >}}).

## Paano makuha ang iyong Telegram user ID sa private chat

Buksan ang bot @print_id_bot sa private chat at pindutin ang **Simula**. Ibabalik kaagad ng bot ang iyong **Telegram user ID**, username (kung mayroon), at chat_id. Walang ibang kailangan: kopyahin lang ang numero mula sa mensahe.

Sa private chat, sumasagot ang bot sa anumang mensahe: text, photo, sticker, o ang command na `/id`. Magpadala ng kahit ano at makukuha mo ang iyong ID. Pribado: ikaw lang ang makakakita ng sagot.

## Paano makuha ang chat_id ng grupo

Para makuha ang **chat_id** ng grupo o supergroup, idagdag ang @print_id_bot sa grupo. Pagkatapos idagdag, magpapadala ang bot ng welcome message na may pangalan ng grupo at chat_id.

Sa mga grupo, sumasagot ang bot **lamang sa ilang partikular na aksyon**. Para makuha ang chat_id, gawin ang isa sa mga sumusunod:

- Magpadala ng command na **/id** o **/help** (may o walang @print_id_bot)
- Tumugon sa mensahe ng bot
- Banggitin ang **@print_id_bot** sa iyong mensahe
- Magpadala ng kahit anong command na may @print_id_bot (hal. `/foo@print_id_bot`)

Ang mga ordinaryong mensahe na walang pagbanggit sa bot ay hindi nagti-trigger ng sagot: para maiwasan ng bot ang spam. Ang mga ID ng grupo at supergroup ay madalas na negatibo; normal iyon.

## Magsimula rito

- [Mga gabay sa Telegram user ID]({{< relref "user-id-guides.md" >}}) — paano hanapin, kopyahin, at maintindihan ang iyong user ID
- [Mga gabay sa chat_id]({{< relref "chat-id-guides.md" >}}) — pagkuha ng chat_id ng mga grupo at supergroup
- [Mga gabay sa Bot API]({{< relref "bot-api-guides.md" >}}) — integrasyon sa Telegram Bot API

## FAQ

### Pribado ba ang aking Telegram ID?

Ang iyong Telegram ID ay hindi ipinapakita nang publiko sa app. Ang mga bot at app ay nakukuha ito lamang kapag nakikipag-ugnayan ka sa kanila — halimbawa kapag nagbukas ng bot at pinindot ang Simula. Ikaw ang nagdedesisyon kung aling mga bot ang pagkakatiwalaan.

### Bakit hindi sumasagot ang bot sa grupo?

Sumasagot ang bot lamang kapag tumutugon ka sa mensahe nito, nagpapadala ng /id o /help, o binabanggit ang @print_id_bot. Ang mga ordinaryong mensahe na walang mga trigger na ito ay binabalewala. Siguruhing nasa grupo ang bot at makakabasa ng mga mensahe.

### Ano ang pagkakaiba ng user ID at chat_id?

Ang **user ID** ay tumutukoy sa iyong Telegram account. Ang **chat_id** ay tumutukoy sa usapan: private chat, grupo, supergroup, o channel. Sa private chat, ang user ID at chat_id ay parehong numero. Para sa mga grupo, ang chat_id ay madalas na negatibo.
