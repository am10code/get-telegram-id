+++
title = "print_id_bot: Telegram ID & chat_id helper (commands, languages, features)"
description = "Complete reference for @print_id_bot: commands, 16 supported languages, group triggers, and developer features (/json, /dump). Get your Telegram user ID and chat_id in seconds."
cta = { text = "Open the bot to get your Telegram user ID and chat_id instantly.", label = "Open @print_id_bot", url = "https://t.me/print_id_bot" }
+++

@print_id_bot is a Telegram bot that shows your **Telegram user ID**, **chat_id** (for groups and supergroups), and channel ID. It works in private chat and in groups, with responses in 16 languages based on your Telegram language setting.

## Commands

| Command | What it does |
|---------|--------------|
| `/start` | Welcome message, your User ID and Chat ID, inline buttons for /id and /help |
| `/id` | Your User ID and Chat ID (short reply) |
| `/help` | Full help text and command list |
| `/json` | Current message as JSON (for developers) |
| `/dump` | Full update breakdown and raw JSON (private chat only) |

In private chat, sending any message (text, photo, sticker, etc.) also returns your User ID and Chat ID. For forwarded messages, the bot shows the author's ID when available, or "ID hidden" when the sender's privacy settings block it. See [forwarded messages and hidden IDs](/telegram-forwarded-message-id/) for details.

## Supported languages (16)

The bot picks the response language from your Telegram `language_code`. Supported: English, Russian, Persian, Uzbek, Hindi, Chinese, Turkish, Portuguese, Spanish, Arabic, Indonesian, German, Urdu, French, Tagalog, Amharic. Unsupported codes fall back to English. See [how language selection works](/telegram-id-bot-languages/).

## Group and supergroup behavior

In groups, the bot responds only when you:

- Reply to the bot's message
- Send `/id` or `/help` (with or without @print_id_bot)
- Send any command with @print_id_bot (e.g. `/foo@print_id_bot`)
- Mention @print_id_bot in your message

Otherwise it stays silent. When added to a group, it sends a welcome message with the group name and chat_id. See [add a bot to a group to get chat_id](/add-bot-to-group-chat-id/) for a quick guide.

## Developer features

- **/json** — Returns the current message as JSON.
- **/dump** — Full update breakdown and raw JSON (private chat only). Useful for debugging Bot API integrations. See [inspecting Telegram update JSON](/telegram-json-update/).

## Related pages

- [Get Telegram user ID (safe methods)](/get-telegram-user-id/)
- [How to get Telegram chat_id for a group](/get-telegram-chat-id/)
- [How to find your Telegram ID](/how-to-find-telegram-id/)

## FAQ

### Does the bot work in channels?
The bot works in private chat and in groups/supergroups. For channels, you need the channel ID from a different flow (e.g. posting as the channel and using a bot that receives updates). See [get Telegram channel ID for Bot API](/how-to-get-channel-id-bot-api/).

### Can I get someone else's Telegram user ID?
The bot shows your own ID or the chat_id of chats you're in. For forwarded messages, it shows the sender's ID only if they allow forwarding; otherwise you see "ID hidden". You cannot look up someone's ID by phone number or username. See [Telegram ID vs username](/telegram-id-vs-username/).

### Why doesn't the bot reply in my group?
The bot only responds when you reply to it, send /id or /help, or mention @print_id_bot. See [bot not responding in a Telegram group](/bot-not-responding-in-group/) for a full checklist.

### Is the bot free?
Yes. No signup or payment required.

### What is the difference between user ID and chat_id?
**User ID** identifies a Telegram account. **chat_id** identifies a conversation (private chat, group, supergroup, or channel). See [Telegram ID vs username](/telegram-id-vs-username/).
