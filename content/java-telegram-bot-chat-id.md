+++
title = "Java Telegram bot: get chat_id"
description = "Get chat_id and user ID in Java Telegram bots. From telegram-bot-api or Rubenlagus/TelegramBots. Use @print_id_bot /json and /dump for debugging."
cta = { text = "Use @print_id_bot /dump to inspect update structure for Java bots.", label = "Open @print_id_bot", url = "https://t.me/print_id_bot" }
+++

In **Java** Telegram bots, you get `chat_id` and `user_id` from the update. Here are examples.

## Using telegram-bot-api (Java)

```java
@Override
public void onUpdateReceived(Update update) {
    if (update.hasMessage()) {
        Message message = update.getMessage();
        Long chatId = message.getChatId();
        Long userId = message.getFrom().getId();
        sendMessage(chatId, "Chat ID: " + chatId + ", User ID: " + userId);
    }
}
```

- `message.getChatId()` — chat_id
- `message.getFrom().getId()` — sender's Telegram user ID

## From callback query

```java
if (update.hasCallbackQuery()) {
    CallbackQuery callback = update.getCallbackQuery();
    Long chatId = callback.getMessage().getChatId();
    Long userId = callback.getFrom().getId();
    // ...
}
```

## From channel post

```java
if (update.hasChannelPost()) {
    Message post = update.getChannelPost();
    Long chatId = post.getChatId();  // channel ID
    // ...
}
```

## Debugging with @print_id_bot

Use [@print_id_bot](https://t.me/print_id_bot) to inspect the raw update:

- **/json** — Message as JSON. Compare with your Update object.
- **/dump** — Full update and raw JSON (private chat only). Use to verify structure.

Forward a message to the bot and send /dump to see the exact format.

## Related pages

- [Telegram Bot API: how to get chat_id](/telegram-bot-api-chat-id/)
- [Telegram update JSON: /dump output](/telegram-json-update/)
- [C# Telegram bot: get chat_id](/csharp-telegram-bot-chat-id/)

## FAQ

### How do I get chat_id when the bot is added to a group?
When a user sends a message, your handler receives it with `getMessage().getChatId()`. Or add @print_id_bot and send /id to get it manually.

### Should I use Long or long for chat_id?
Use `Long` to handle null. For message updates, `getChatId()` returns a non-null Long.

### Where is the update structure?
The [Telegram Bot API](https://core.telegram.org/bots/api) documents it. Use /dump in @print_id_bot for real examples.

### What if getFrom() is null?
For channel_post, there is no from. Check for null before calling `getId()`.

### Can I log the raw update?
Yes. Log `update` or serialize it to JSON. Compare with /dump output from @print_id_bot.
