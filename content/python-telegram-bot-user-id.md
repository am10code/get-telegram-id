+++
title = "python-telegram-bot: get user ID and chat_id"
description = "Get user ID and chat_id in python-telegram-bot. From Message, CallbackQuery, and channel_post. Use @print_id_bot /json and /dump for debugging."
cta = { text = "Use @print_id_bot /dump to inspect update JSON for python-telegram-bot.", label = "Open @print_id_bot", url = "https://t.me/print_id_bot" }
+++

In **python-telegram-bot**, you get `user_id` and `chat_id` from the update. Here are examples.

## From a message (PTB v20+)

```python
async def message_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message = update.effective_message
    chat_id = update.effective_chat.id
    user_id = update.effective_user.id
    await message.reply_text(f"Chat ID: {chat_id}, User ID: {user_id}")
```

- `update.effective_chat.id` — chat_id
- `update.effective_user.id` — sender's Telegram user ID

## From a callback query

```python
async def callback_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    chat_id = query.message.chat.id
    user_id = query.from_user.id
    await query.answer()
    await query.message.reply_text(f"Chat ID: {chat_id}, User ID: {user_id}")
```

## From channel_post

```python
async def channel_post_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message = update.channel_post
    chat_id = message.chat.id  # channel ID
    await message.reply_text(f"Channel ID: {chat_id}")
```

## Debugging with @print_id_bot

Use [@print_id_bot](https://t.me/print_id_bot) to inspect the raw update:

- **/json** — Message as JSON. Compare with `update.to_dict()` or similar.
- **/dump** — Full update and raw JSON (private chat only). Shows `message.chat.id`, `message.from.id`, and the full structure.

Forward a message to the bot and send /dump to verify the format.

## Related pages

- [Aiogram: get chat_id](/aiogram-get-chat-id/)
- [Telegram Bot API: how to get chat_id](/telegram-bot-api-chat-id/)
- [Telegram update JSON: /dump output](/telegram-json-update/)

## FAQ

### What is effective_chat vs chat?
`effective_chat` is the chat where the update originated (e.g. for replies, the chat of the replied-to message). For most handlers, `update.effective_chat` is what you need.

### How do I get chat_id for a new group?
Add your bot to the group. When someone sends a message, your handler receives it with `update.effective_chat.id`. Or add @print_id_bot and send /id to get it manually.

### Can I use update.message.chat.id?
Yes. For message updates, `update.message.chat.id` equals `update.effective_chat.id`. Use whichever fits your code style.

### Where is the update structure documented?
The [Telegram Bot API](https://core.telegram.org/bots/api) documents the Update object. Use /dump in @print_id_bot to see real examples.

### Does chat_id differ for groups and supergroups?
Both use negative chat_ids. After migration, the value can change. See [group vs supergroup chat_id](/telegram-group-chat-id-vs-supergroup/).
