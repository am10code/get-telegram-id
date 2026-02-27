+++
title = "C# Telegram bot: get chat_id"
description = "Get chat_id and user ID in C# Telegram bots. From Telegram.Bot. Use @print_id_bot /json and /dump for debugging."
cta = { text = "Use @print_id_bot /dump to inspect update structure for C# bots.", label = "Open @print_id_bot", url = "https://t.me/print_id_bot" }
+++

In **C#** Telegram bots (Telegram.Bot library), you get `chat_id` and `user_id` from the update. Here are examples.

## From a message

```csharp
botClient.OnMessage(async (client, update, cancellationToken) =>
{
    var message = update.Message;
    if (message == null) return;

    var chatId = message.Chat.Id;
    var userId = message.From?.Id;

    await client.SendTextMessageAsync(
        chatId,
        $"Chat ID: {chatId}, User ID: {userId}",
        cancellationToken: cancellationToken);
});
```

- `message.Chat.Id` — chat_id
- `message.From?.Id` — sender's Telegram user ID

## From a callback query

```csharp
botClient.OnCallbackQuery(async (client, update, cancellationToken) =>
{
    var query = update.CallbackQuery;
    var chatId = query.Message.Chat.Id;
    var userId = query.From.Id;

    await client.AnswerCallbackQueryAsync(query.Id, cancellationToken: cancellationToken);
    await client.SendTextMessageAsync(
        chatId,
        $"Chat ID: {chatId}, User ID: {userId}",
        cancellationToken: cancellationToken);
});
```

## From channel post

```csharp
botClient.OnChannelPost(async (client, update, cancellationToken) =>
{
    var post = update.ChannelPost;
    var chatId = post.Chat.Id;  // channel ID

    await client.SendTextMessageAsync(
        chatId,
        $"Channel ID: {chatId}",
        cancellationToken: cancellationToken);
});
```

## Debugging with @print_id_bot

Use [@print_id_bot](https://t.me/print_id_bot) to inspect the raw update:

- **/json** — Message as JSON. Compare with your Update object.
- **/dump** — Full update and raw JSON (private chat only). Use to verify structure.

Forward a message to the bot and send /dump to see the exact format.

## Related pages

- [Telegram Bot API: how to get chat_id](/telegram-bot-api-chat-id/)
- [Telegram update JSON: /dump output](/telegram-json-update/)
- [Java Telegram bot: get chat_id](/java-telegram-bot-chat-id/)

## FAQ

### How do I get chat_id when the bot is added to a group?
When a user sends a message, your handler receives it with `Message.Chat.Id`. Or add @print_id_bot and send /id to get it manually.

### What type is Chat.Id?
`long` (Int64). Telegram IDs can be large; use the correct type.

### Where is the update structure?
The [Telegram Bot API](https://core.telegram.org/bots/api) documents it. Use /dump in @print_id_bot for real examples.

### What if Message.From is null?
For channel_post, there is no From. Use null-conditional: `message.From?.Id`.

### Can I serialize the update to JSON?
Yes. Serialize the Update object and compare with /dump output from @print_id_bot.
