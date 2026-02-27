+++
title = "Using @print_id_bot if you don't speak English (supported languages)"
description = "@print_id_bot works in 16 languages: Russian, Persian, Arabic, Hindi, Chinese, and more. Set your Telegram language and the bot responds in your language."
cta = { text = "Open @print_id_bot — it responds in your language.", label = "Open @print_id_bot", url = "https://t.me/print_id_bot" }
+++

You do not need to speak English to use [@print_id_bot](https://t.me/print_id_bot). The bot responds in **16 languages** based on your Telegram app language.

## Supported languages

- **English** (en)
- **Russian** (ru)
- **Persian** (fa)
- **Uzbek** (uz)
- **Hindi** (hi)
- **Chinese** (zh)
- **Turkish** (tr)
- **Portuguese** (pt)
- **Spanish** (es)
- **Arabic** (ar)
- **Indonesian** (id)
- **German** (de)
- **Urdu** (ur)
- **French** (fr)
- **Tagalog / Filipino** (tl; Telegram sends `fil`)
- **Amharic** (am)

## How to use it in your language

1. Set your Telegram app language: **Settings → Language** (or equivalent).
2. Open @print_id_bot and tap **Start**.
3. The bot replies in your language. Labels like "User ID," "Chat ID," and "Tap the number to copy" appear in your locale.

No extra setup. The bot reads your `language_code` from Telegram and picks the right strings.

## If your language is not listed

The bot falls back to **English**. All commands and features work the same; only the text is in English. You can still get your Telegram user ID, chat_id, and use /help, /json, and /dump.

## Commands in any language

Commands are the same in all languages:

- `/start` — Welcome and your IDs
- `/id` — User ID and Chat ID
- `/help` — Help text
- `/json` — Message as JSON
- `/dump` — Full update (private chat only)

The command names are in English, but the bot's replies use your language.

## Related pages

- [Telegram ID bot in 16 languages: how selection works](/telegram-id-bot-languages/)
- [print_id_bot: commands, languages, features](/print-id-bot/)
- [How to find your Telegram ID](/how-to-find-telegram-id/)

## FAQ

### Do I need to type commands in my language?
No. Use `/start`, `/id`, `/help`, etc. The bot's responses are in your language.

### Can I switch language mid-chat?
The bot uses the `language_code` from each update. If you change your Telegram app language and send a new message, the next response will use the new language.

### Is the bot menu in my language?
The bot registers commands with Telegram for all 16 languages. Your Telegram client may show the command descriptions in your language in the menu.

### What about RTL languages?
Arabic, Persian, and Urdu are supported. Telegram handles right-to-left layout.

### Does /dump output change with language?
The human-readable labels (User ID, Chat ID, etc.) use your language. The raw JSON at the end is unchanged.
