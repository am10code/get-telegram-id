+++
title = "Telegram Bot API 'chat not found': common causes"
description = "Telegram Bot API 'chat not found' error: bot removed from chat, wrong chat_id, migration to supergroup. How to fix and get the correct chat_id."
cta = { text = "Get the correct chat_id with @print_id_bot.", label = "Open @print_id_bot", url = "https://t.me/print_id_bot" }
+++

The Telegram Bot API can return **"chat not found"** when you send a message. Common causes and fixes:

## 1. Bot was removed from the chat

If the bot was removed from the group, supergroup, or channel, the API returns "chat not found" for that chat_id.

**Fix:** Add the bot back to the chat. For groups, add [@print_id_bot](https://t.me/print_id_bot) and send /id to get the current chat_id. For channels, add your bot as admin again.

## 2. Wrong chat_id

Using an old, mistyped, or incorrect chat_id causes the error.

**Fix:** Get the correct chat_id. In a group: add @print_id_bot, send /id or mention it, and copy the chat_id. In private chat: open @print_id_bot and tap Start to get your User ID (which equals chat_id for private chats).

## 3. Group migrated to supergroup

When a group becomes a supergroup, the chat_id can change. The old ID may no longer work.

**Fix:** Get the new chat_id. Add @print_id_bot to the (super)group and send /id. Use the new value. See [group vs supergroup chat_id](/telegram-group-chat-id-vs-supergroup/).

## 4. User blocked the bot or deleted account

For private chats, if the user blocked the bot or deleted their account, "chat not found" can occur.

**Fix:** The user must unblock the bot or use an active account. You cannot fix this from the bot side.

## 5. Channel: bot not admin

To post in a channel, the bot must be an administrator. Otherwise you may get permission errors or "chat not found."

**Fix:** Add the bot to the channel as admin with the right permissions (e.g. post messages).

## Verify your chat_id

Use @print_id_bot to confirm:

- **Private:** Open the bot, tap Start — User ID = chat_id
- **Group/supergroup:** Add the bot, send /id — copy the chat_id from the reply
- **Channel:** Forward a channel post to the bot — it shows the channel ID

## Related pages

- [How to get Telegram chat_id for a group](/get-telegram-chat-id/)
- [Group vs supergroup chat_id](/telegram-group-chat-id-vs-supergroup/)
- [Telegram Bot API: how to get chat_id](/telegram-bot-api-chat-id/)

## FAQ

### Can I recover an old chat_id after migration?
No. Use the new chat_id. Get it from @print_id_bot by adding it to the group and sending /id.

### Does "chat not found" mean the chat was deleted?
Not always. It often means the bot was removed or the chat_id is wrong. For private chats, the user may have blocked the bot.

### How do I get the chat_id for a channel I own?
Add your bot as admin, post a message, and read `channel_post.chat.id` from the update. Or forward a post to @print_id_bot to see the channel ID.

### Why does it work in one group but not another?
Each chat has its own chat_id. If one works and another does not, the bot may have been removed from the second chat, or you are using the wrong chat_id.

### Should I cache chat_ids?
You can cache them, but re-fetch after migrations or if you get "chat not found." Add @print_id_bot and send /id to verify.
