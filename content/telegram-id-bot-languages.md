+++
title = "Telegram ID bot in 16 languages: how language selection works"
description = "How @print_id_bot picks response language from your Telegram language_code. 16 supported languages, fallback to English. Russian, Persian, Arabic, and more."
cta = { text = "Open @print_id_bot — it responds in your Telegram language.", label = "Open @print_id_bot", url = "https://t.me/print_id_bot" }
+++

@print_id_bot responds in **16 languages** based on your Telegram language setting. No manual language selection is needed.

## How it works

The bot reads your **language_code** from the update (from `message.from.language_code`, `edited_message.from.language_code`, or `callback_query.from.language_code`). It uses the first part of the code (e.g. `pt-BR` → `pt`) and maps it to a supported locale. Unsupported codes fall back to **English**.

## Supported languages (16)

| Code | Language |
|------|----------|
| `en` | English |
| `ru` | Russian |
| `fa` | Persian |
| `uz` | Uzbek |
| `hi` | Hindi |
| `zh` | Chinese |
| `tr` | Turkish |
| `pt` | Portuguese |
| `es` | Spanish |
| `ar` | Arabic |
| `id` | Indonesian |
| `de` | German |
| `ur` | Urdu |
| `fr` | French |
| `tl` | Tagalog (Filipino; `fil` maps to `tl`) |
| `am` | Amharic |

## Special cases

- **Filipino** — Telegram sends `fil`; the bot maps it to `tl` (Tagalog).
- **Portuguese (Brazil)** — `pt-BR` uses `pt` (Portuguese).
- **Chinese** — `zh-CN`, `zh-TW` use `zh` (Chinese).

## What is localized

All bot responses: welcome text, labels (User ID, Chat ID, Group name), help text, buttons, and messages like "ID hidden" or "Tap the number to copy." The raw JSON in /json and /dump is unchanged; only the human-readable labels use your language.

## Related pages

- [Using @print_id_bot if you don't speak English]({{< relref "telegram-id-bot-for-non-english.md" >}})
- [print_id_bot: commands, languages, features]({{< relref "print-id-bot.md" >}})
- [Get Telegram user ID (safe methods)]({{< relref "get-telegram-user-id.md" >}})

## FAQ

### How do I change the bot's language?
Change your Telegram app language in Settings → Language. The bot uses that. There is no in-bot language switch.

### What if my language is not supported?
The bot falls back to English. All functionality works the same.

### Does the bot support right-to-left (RTL) languages?
Yes. Arabic, Persian, and Urdu are supported. Telegram handles RTL rendering.

### Can I request a new language?
The bot supports 16 languages. Adding more depends on the bot maintainers. English fallback ensures everyone can use it.

### Is the language stored or sent elsewhere?
No. The bot reads `language_code` from each update and uses it only to pick the response strings. It is not stored or shared.
