+++
title = "Why Telegram chat_id can be negative"
description = "Telegram group and channel chat_ids are often negative numbers. Why this happens, what it means for the Bot API, and when to expect positive vs negative IDs."
cta = { text = "Get your group chat_id with @print_id_bot — negative IDs are normal.", label = "Open @print_id_bot", url = "https://t.me/print_id_bot" }
+++

In the Telegram Bot API, **chat_id** values for groups, supergroups, and channels are often **negative**. This is expected and correct.

## When chat_id is negative

- **Groups** — typically negative (e.g. `-1001234567890`)
- **Supergroups** — typically negative
- **Channels** — typically negative

## When chat_id is positive

- **Private chats** — your chat_id with a user equals their user ID (positive)
- **Your own user ID** — positive

## Why negative?

Telegram uses the sign to distinguish chat types. Positive IDs are for users (private chats); negative IDs are for groups, supergroups, and channels. This lets the API and your code handle different chat types correctly.

## Practical impact

When you get a group or channel chat_id from [@print_id_bot](https://t.me/print_id_bot), a negative number is normal. Use it as-is in API calls. Do not try to "fix" it by removing the minus sign.

## Migration: group to supergroup

When a group is upgraded to a supergroup, the chat_id can change. Always use the current value from the bot or API. See [group vs supergroup chat_id](/telegram-group-chat-id-vs-supergroup/).

## Related pages

- [Telegram chat_id format explained](/telegram-chat-id-format/)
- [How to get Telegram chat_id for a group](/get-telegram-chat-id/)
- [Telegram Bot API: how to get chat_id](/telegram-bot-api-chat-id/)

## FAQ

### Is a negative chat_id an error?
No. Negative chat_ids for groups and channels are correct and expected.

### Can I convert a negative ID to positive?
No. Use the value as returned by the API. Converting it would break your requests.

### Why does my private chat have a positive ID?
In a private chat, the chat_id equals the other user's user ID, which is positive.

### Do all supergroups have negative IDs?
Yes. Supergroup and channel IDs are negative in the Bot API.

### Where can I see examples?
Add @print_id_bot to a group and send /id. The bot shows the chat_id. See [Telegram chat_id format](/telegram-chat-id-format/) for more examples.
