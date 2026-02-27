+++
title = "Telethon: get Telegram user ID (quick guide)"
description = "Get user ID and chat_id in Telethon (Python). From Message, events. Use @print_id_bot /json and /dump for Bot API structure comparison."
cta = { text = "Use @print_id_bot /dump to verify ID structure.", label = "Open @print_id_bot", url = "https://t.me/print_id_bot" }
+++

**Telethon** uses the Telegram MTProto API. Here is how to get `user_id` and `chat_id`.

## From a message event

```python
from telethon import events

@client.on(events.NewMessage)
async def handler(event):
    chat_id = event.chat_id
    user_id = event.sender_id
    await event.respond(f"Chat ID: {chat_id}, User ID: {user_id}")
```

- `event.chat_id` — chat_id (private, group, supergroup, or channel)
- `event.sender_id` — sender's Telegram user ID

## From event.chat and event.sender

```python
@client.on(events.NewMessage)
async def handler(event):
    chat = await event.get_chat()
    sender = await event.get_sender()
    chat_id = event.chat_id  # or chat.id if you have the entity
    user_id = sender.id if sender else None
    await event.respond(f"Chat ID: {chat_id}, User ID: {user_id}")
```

## Get your own user ID

```python
me = await client.get_me()
my_user_id = me.id
```

## Debugging with @print_id_bot

Telethon uses MTProto; [@print_id_bot](https://t.me/print_id_bot) uses the Bot API. ID formats match. Use the bot to verify:

- **/json** — Message as JSON. Compare IDs with your Telethon event.
- **/dump** — Full update (private chat only). Use to confirm structure.

Forward a message to @print_id_bot and send /dump to see the equivalent Bot API update.

## Related pages

- [Pyrogram: get chat_id](/pyrogram-get-chat-id/)
- [Telegram chat_id format](/telegram-chat-id-format/)
- [Get Telegram user ID (safe methods)](/get-telegram-user-id/)

## FAQ

### Is Telethon ID format same as Bot API?
Yes. User IDs and chat_ids use the same numeric format across MTProto and Bot API.

### How do I get chat_id for a channel I joined?
Use `event.chat_id` when you receive a message from the channel. Or use `client.get_dialogs()` and read `dialog.entity.id` for channels you have access to.

### What if event.sender_id is None?
For channel posts, the sender may be the channel. Use `event.chat_id` for the channel ID. For anonymous group admins, sender might be None.

### Can I use Telethon with a bot account?
Telethon is for user accounts (MTProto). For bots, use python-telegram-bot or Aiogram. ID formats are the same.

### Where is the update structure?
Telethon wraps MTProto types. For Bot API structure, use /dump in @print_id_bot to see the JSON format.
