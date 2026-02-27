+++
title = "Telegram chat_id format explained (with examples)"
description = "Telegram chat_id format: positive for private chats, negative for groups and channels. Examples, structure, and how to get each type with @print_id_bot."
cta = { text = "Get chat_id examples with @print_id_bot.", label = "Open @print_id_bot", url = "https://t.me/print_id_bot" }
+++

The **chat_id** in the Telegram Bot API has a consistent format. Understanding it helps when building integrations.

## Private chat

- **Format:** Positive integer
- **Value:** Equals the user's Telegram user ID
- **Example:** `123456789`

In a private chat, `chat_id` is the same as the user's ID. Get yours: open [@print_id_bot](https://t.me/print_id_bot), tap Start, and copy the User ID.

## Group and supergroup

- **Format:** Negative integer
- **Example:** `-1001234567890`

Group and supergroup IDs are typically negative. Add @print_id_bot to the group and send /id to get the chat_id. See [why chat_id can be negative](/telegram-chat-id-negative/).

## Channel

- **Format:** Negative integer
- **Example:** `-1009876543210`

Channel IDs are also negative. Forward a channel post to @print_id_bot to get the channel ID. See [get Telegram channel ID](/how-to-get-channel-id-bot-api/).

## Summary table

| Chat type | Sign | Example |
|-----------|------|---------|
| Private | Positive | `123456789` |
| Group | Negative | `-1001234567890` |
| Supergroup | Negative | `-1001234567890` |
| Channel | Negative | `-1009876543210` |

## Use in API calls

Pass the chat_id as-is. Do not modify the sign. For example:

```
sendMessage?chat_id=-1001234567890&text=Hello
```

## Migration note

When a group becomes a supergroup, the chat_id can change. Always use the current value from @print_id_bot or your updates. See [group vs supergroup chat_id](/telegram-group-chat-id-vs-supergroup/).

## Related pages

- [Why Telegram chat_id can be negative](/telegram-chat-id-negative/)
- [Telegram Bot API: how to get chat_id](/telegram-bot-api-chat-id/)
- [How to get Telegram chat_id for a group](/get-telegram-chat-id/)

## FAQ

### Can chat_id be zero?
No. Valid chat_ids are non-zero integers. Private chats are positive; groups and channels are negative.

### Why is my group ID so long?
Supergroup and channel IDs often have many digits. This is normal. Use the full value.

### Is the format same for all Bot API methods?
Yes. sendMessage, sendPhoto, and other methods use the same chat_id format.

### Can I have the same chat_id for different chats?
No. Each chat has a unique chat_id.

### Where do I see the format in an update?
Use @print_id_bot's /dump in private chat. The output shows `message.chat.id` or `channel_post.chat.id`. The raw JSON has the exact value.
