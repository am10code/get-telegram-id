+++
title = "Telegraf (Node.js): get chat_id and user ID"
description = "Get chat_id and user ID in Telegraf (Node.js). From ctx.message, ctx.callbackQuery. Use @print_id_bot /json and /dump for debugging."
cta = { text = "Use @print_id_bot /dump to inspect update structure for Telegraf.", label = "Open @print_id_bot", url = "https://t.me/print_id_bot" }
+++

In **Telegraf** (Node.js Telegram Bot framework), you get `chat_id` and `user_id` from the context. Here are examples.

## From a message

```javascript
bot.on('message', (ctx) => {
  const chatId = ctx.chat.id;
  const userId = ctx.from.id;
  return ctx.reply(`Chat ID: ${chatId}, User ID: ${userId}`);
});
```

- `ctx.chat.id` — chat_id
- `ctx.from.id` — sender's Telegram user ID

## From a callback query

```javascript
bot.on('callback_query', (ctx) => {
  const chatId = ctx.chat.id;
  const userId = ctx.from.id;
  return ctx.answerCbQuery().then(() =>
    ctx.reply(`Chat ID: ${chatId}, User ID: ${userId}`)
  );
});
```

## From channel_post

```javascript
bot.on('channel_post', (ctx) => {
  const chatId = ctx.chat.id;  // channel ID
  return ctx.reply(`Channel ID: ${chatId}`);
});
```

## Debugging with @print_id_bot

Use [@print_id_bot](https://t.me/print_id_bot) to inspect the raw update:

- **/json** — Message as JSON. Compare with `ctx.update`.
- **/dump** — Full update and raw JSON (private chat only). Use to verify `message.chat.id`, `message.from.id`, and nested fields.

Forward a message to the bot and send /dump to see the exact structure Telegraf receives.

## Related pages

- [grammY: get chat_id](/grammy-get-chat-id/)
- [Telegram Bot API: how to get chat_id](/telegram-bot-api-chat-id/)
- [Telegram update JSON: /dump output](/telegram-json-update/)

## FAQ

### Where is chat_id in ctx?
`ctx.chat.id`. For most updates, `ctx.chat` is the chat where the update originated.

### How do I get chat_id when the bot is added to a group?
When a user sends a message after the bot is added, `ctx.chat.id` in that message handler is the group chat_id. Or add @print_id_bot and send /id to get it manually.

### Does Telegraf pass the raw update?
Yes. `ctx.update` contains the full Telegram update. Use /dump in @print_id_bot to compare.

### What about ctx.message.chat.id?
Same as `ctx.chat.id` for message updates. Telegraf normalizes `ctx.chat` for convenience.

### Can I use this for channels?
Yes. For `channel_post`, `ctx.chat.id` is the channel ID. Your bot must be an admin to receive those updates.
