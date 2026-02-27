+++
title = "Pyrogram: get user ID and chat_id"
description = "Get user ID and chat_id in Pyrogram (Python MTProto). From Message, CallbackQuery. Use @print_id_bot /json and /dump for Bot API structure."
cta = { text = "Use @print_id_bot /dump to compare Bot API update structure.", label = "Open @print_id_bot", url = "https://t.me/print_id_bot" }
+++

**Pyrogram** uses the Telegram MTProto API (userbot/client), not the Bot API. Chat and user IDs work similarly. Here is how to get them.

## From a message

```python
@app.on_message(filters.private)
async def handle_private(client, message):
    chat_id = message.chat.id
    user_id = message.from_user.id
    await message.reply(f"Chat ID: {chat_id}, User ID: {user_id}")
```

- `message.chat.id` — chat_id (same format as Bot API)
- `message.from_user.id` — sender's Telegram user ID

## From a callback query

```python
@app.on_callback_query()
async def handle_callback(client, callback_query):
    chat_id = callback_query.message.chat.id
    user_id = callback_query.from_user.id
    await callback_query.answer()
    await callback_query.message.reply(f"Chat ID: {chat_id}, User ID: {user_id}")
```

## Group and channel

```python
@app.on_message(filters.group)
async def handle_group(client, message):
    chat_id = message.chat.id  # negative for groups/supergroups
    user_id = message.from_user.id
    await message.reply(f"Group chat_id: {chat_id}, Your user_id: {user_id}")
```

## Debugging with @print_id_bot (Bot API reference)

Pyrogram uses MTProto; [@print_id_bot](https://t.me/print_id_bot) uses the Bot API. The ID formats are the same. Use the bot to verify:

- **/json** — Message as JSON (Bot API format). IDs match Pyrogram.
- **/dump** — Full update (private chat only). Use to confirm chat_id and user_id structure.

Forward a message to @print_id_bot and send /dump to see the Bot API equivalent.

## Related pages

- [Telethon: get Telegram user ID](/telethon-get-user-id/)
- [Telegram chat_id format](/telegram-chat-id-format/)
- [Telegram Bot API: how to get chat_id](/telegram-bot-api-chat-id/)

## FAQ

### Is Pyrogram ID format the same as Bot API?
Yes. Chat IDs and user IDs use the same numeric format. Negative for groups/channels, positive for users.

### How do I get my own user ID in Pyrogram?
Use `(await client.get_me()).id` or handle any message and read `message.from_user.id` when you send it.

### Can I get chat_id without a message?
You can use `client.get_chat(chat_id)` if you already have it, or iterate dialogs. To discover a new group's ID, have someone send a message or add @print_id_bot (Bot API) and send /id.

### Does Pyrogram support Bot API?
Pyrogram is for userbots (MTProto). For bots, use python-telegram-bot or Aiogram. ID formats are compatible.

### Where is channel ID in Pyrogram?
For channel posts, `message.chat.id` is the channel ID. Same as Bot API's `channel_post.chat.id`.
