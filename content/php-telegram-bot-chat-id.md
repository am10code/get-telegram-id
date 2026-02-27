+++
title = "PHP Telegram bot: get chat_id"
description = "Get chat_id and user ID in PHP Telegram bots. From telegram-bot/api or longman/telegram-bot. Use @print_id_bot /json and /dump for debugging."
cta = { text = "Use @print_id_bot /dump to inspect update structure for PHP bots.", label = "Open @print_id_bot", url = "https://t.me/print_id_bot" }
+++

In **PHP** Telegram bots, you get `chat_id` and `user_id` from the update. Here are examples.

## Using telegram-bot/api (raw)

```php
$update = json_decode(file_get_contents('php://input'), true);

if (isset($update['message'])) {
    $chatId = $update['message']['chat']['id'];
    $userId = $update['message']['from']['id'];
    // Send response...
}
```

## Using longman/telegram-bot

```php
$telegram->on('message', function ($message) {
    $chatId = $message->getChat()->getId();
    $userId = $message->getFrom()->getId();
    $telegram->sendMessage([
        'chat_id' => $chatId,
        'text' => "Chat ID: $chatId, User ID: $userId",
    ]);
});
```

## From callback query

```php
if (isset($update['callback_query'])) {
    $chatId = $update['callback_query']['message']['chat']['id'];
    $userId = $update['callback_query']['from']['id'];
    // ...
}
```

## From channel_post

```php
if (isset($update['channel_post'])) {
    $chatId = $update['channel_post']['chat']['id'];  // channel ID
    // ...
}
```

## Debugging with @print_id_bot

Use [@print_id_bot](https://t.me/print_id_bot) to inspect the raw update:

- **/json** — Message as JSON. Compare with `$update['message']`.
- **/dump** — Full update and raw JSON (private chat only). Use to verify structure.

Forward a message to the bot and send /dump to see the exact format your webhook receives.

## Related pages

- [Telegram Bot API: how to get chat_id](/telegram-bot-api-chat-id/)
- [Telegram update JSON: /dump output](/telegram-json-update/)
- [Telegram chat_id format](/telegram-chat-id-format/)

## FAQ

### How do I get chat_id when the bot is added to a group?
When a user sends a message, the webhook receives `message.chat.id`. Or add @print_id_bot and send /id to get it manually.

### Can I use $_POST for update?
Telegram sends updates as JSON in the request body. Use `file_get_contents('php://input')` or your framework's input handler.

### Where is the update structure documented?
The [Telegram Bot API](https://core.telegram.org/bots/api) documents the Update object. Use /dump in @print_id_bot for real examples.

### What if from is missing?
For channel_post, there is no from. Check `isset($update['message']['from'])` before accessing.

### Is chat_id always an integer?
Yes. In Telegram's JSON it is a number. PHP may decode it as int or float; ensure you use it correctly in API calls.
