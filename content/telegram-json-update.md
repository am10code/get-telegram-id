+++
title = "Telegram update JSON: how to inspect /dump output"
description = "Use @print_id_bot /dump to inspect Telegram update JSON. Structure of message, chat, from, forward_origin. Debugging Bot API integrations."
cta = { text = "Use /dump in @print_id_bot to inspect update structure.", label = "Open @print_id_bot", url = "https://t.me/print_id_bot" }
+++

@print_id_bot's **/dump** command shows a full breakdown of the Telegram update plus the raw JSON. Use it to debug Bot API integrations and understand the update structure.

## How to use /dump

1. Open [@print_id_bot](https://t.me/print_id_bot) in **private chat**.
2. Send `/dump` (with or without a message).
3. The bot replies with:
   - A structured breakdown (Update ID, message, sender, chat, etc.)
   - The raw JSON of the update

/dump works only in private chat. In groups, use /id or /help; /dump in a group returns the group chat_id, not the full update.

## What you see in the output

- **update_id** — Unique update identifier
- **message** — The message object (if present)
- **message.from** — Sender: user ID, username, first_name, last_name, language_code
- **message.chat** — Chat: chat_id, type (private, group, supergroup, channel), title
- **message.text** — Message text
- **message.forward_origin** — Forward source (user, hidden_user, chat, channel)
- **message.entities** — Formatting (commands, mentions, etc.)
- **Raw JSON** — Full update as returned by the Telegram API

## /json vs /dump

- **/json** — Returns only the current message as JSON. Works in private chat and when the bot replies in a group.
- **/dump** — Full update breakdown + raw JSON. Private chat only.

Use /json for quick message inspection; use /dump for full update debugging.

## Language and formatting

The bot uses your Telegram `language_code` for labels (User ID, Chat ID, etc.). Unsupported codes fall back to English. The raw JSON is unchanged.

## Related pages

- [Telegram Bot API: how to get chat_id](/telegram-bot-api-chat-id/)
- [Forwarded messages: why IDs can be hidden](/telegram-forwarded-message-id/)
- [Aiogram: get chat_id](/aiogram-get-chat-id/)

## FAQ

### Why doesn't /dump work in a group?
/dump is available only in private chat to avoid long replies in groups. In groups, use /id for chat_id or /json if the bot replies.

### Is the raw JSON exactly what the API sends?
Yes. It is the same structure your webhook or polling handler receives.

### Can I use /dump for channel_post?
/dump shows the update you send. For channel_post, your bot must be added to the channel and receive those updates. @print_id_bot focuses on message updates; for channel structure, forward a channel post and use /dump on the forwarded message.

### What if the output is truncated?
Telegram limits message length. Very long updates may be cut with "(truncated)". The important fields (chat.id, from.id) are usually at the start.

### How do I find chat_id in the dump?
Look at `message.chat.id` or `channel_post.chat.id`. The bot's structured output also labels it as "ChatID" or "ChannelID".
