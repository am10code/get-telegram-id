+++
title = "Telegram ID bot sa 16 na wika: paano gumagana ang pagpili ng wika"
description = "Paano pinipili ng @print_id_bot ang wika ng sagot mula sa iyong Telegram language_code. 16 na sinusuportahang wika, fallback sa Ingles. Ruso, Persyano, Arabo at iba pa."
cta = { text = "Buksan ang @print_id_bot — sumasagot ito sa wika ng iyong Telegram.", label = "Open @print_id_bot", url = "https://t.me/print_id_bot" }
+++

Ang @print_id_bot ay sumasagot sa **16 na wika** batay sa iyong Telegram language setting. Walang kailangang manual na pagpili ng wika.

## Paano ito gumagana

Binabasa ng bot ang iyong **language_code** mula sa update. Ginagamit ang unang bahagi ng code (hal. pt-BR to pt) at ima-map sa sinusuportahang locale. Ang unsupported na code ay babalik sa **Ingles**.

## Sinusuportahang wika (16)

| Code | Wika |
|------|------|
| en | Ingles |
| ru | Ruso |
| fa | Persyano |
| uz | Uzbek |
| hi | Hindi |
| zh | Tsino |
| tr | Turko |
| pt | Portuges |
| es | Espanyol |
| ar | Arabo |
| id | Indones |
| de | Aleman |
| ur | Urdu |
| fr | Pranses |
| tl | Tagalog (Filipino; fil to tl) |
| am | Amharic |

## Espesyal na kaso

- **Filipino** — Nagpapadala ang Telegram ng fil; ima-map ng bot sa tl (Tagalog).
- **Portuges (Brazil)** — Gumagamit ang pt-BR ng pt (Portuges).
- **Tsino** — Ang zh-CN, zh-TW ay gumagamit ng zh (Tsino).

## Ano ang naka-localize

Lahat ng sagot ng bot: welcome text, labels (User ID, Chat ID, pangalan ng grupo), help text, mga button at mensahe tulad ng "ID hidden" o "I-tap ang numero para kopyahin." Ang raw JSON sa /json at /dump ay hindi nagbabago; tanging ang mababasa na labels ang gumagamit ng iyong wika.

## Kaugnay na pahina

- [Gumamit ng @print_id_bot kung hindi ka nagsasalita ng Ingles]({{< relref "telegram-id-bot-for-non-english.md" "en" >}})
- [print_id_bot: mga command, wika, feature]({{< relref "print-id-bot.md" "en" >}})
- [Kunin ang Telegram user ID (ligtas na paraan)]({{< relref "get-telegram-user-id.md" "en" >}})

## FAQ

### Paano ko babaguhin ang wika ng bot?
Baguhin ang wika ng Telegram app sa Settings, Language. Ginagamit ito ng bot. Walang language switch sa bot.

### Paano kung ang aking wika ay hindi sinusuportahan?
Babalik ang bot sa Ingles. Lahat ng functionality ay gumagana pa rin.

### Sinusuportahan ba ng bot ang right-to-left (RTL) na wika?
Oo. Ang Arabo, Persyano at Urdu ay sinusuportahan. Hinahandle ng Telegram ang RTL rendering.

### Maaari ko bang humiling ng bagong wika?
Ang bot ay sumusuporta ng 16 na wika. Ang pagdagdag ng higit pa ay depende sa mga maintainer. Tinitiyak ng Ingles fallback na lahat ay makakagamit.

### Naka-store ba o ipinapadala ang wika sa ibang lugar?
Hindi. Binabasa ng bot ang language_code mula sa bawat update at ginagamit lamang para pumili ng response strings. Hindi naka-store o na-share.
