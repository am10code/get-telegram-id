+++
title = "Go Telegram Bot API: get chat_id"
description = "Get chat_id and user ID in Go Telegram bot. From telegram-bot-api or tucnak/telebot. Use @print_id_bot /json and /dump for debugging."
cta = { text = "Use @print_id_bot /dump to inspect update structure for Go bots.", label = "Open @print_id_bot", url = "https://t.me/print_id_bot" }
+++

In **Go** Telegram bots, you get `chat_id` and `user_id` from the update. Here are examples for common libraries.

## Using go-telegram-bot-api/telegram-bot-api

```go
func handleUpdate(bot *tgbotapi.BotAPI, update tgbotapi.Update) {
    if update.Message != nil {
        chatID := update.Message.Chat.ID
        userID := update.Message.From.ID
        msg := tgbotapi.NewMessage(chatID, fmt.Sprintf("Chat ID: %d, User ID: %d", chatID, userID))
        bot.Send(msg)
    }
}
```

- `update.Message.Chat.ID` — chat_id
- `update.Message.From.ID` — sender's Telegram user ID

## Using tucnak/telebot

```go
bot.Handle("/hello", func(c tele.Context) error {
    chatID := c.Chat().ID
    userID := c.Sender().ID
    return c.Send(fmt.Sprintf("Chat ID: %d, User ID: %d", chatID, userID))
})
```

## From callback query

```go
// telegram-bot-api
if update.CallbackQuery != nil {
    chatID := update.CallbackQuery.Message.Chat.ID
    userID := update.CallbackQuery.From.ID
    // ...
}

// telebot
bot.Handle(tele.OnCallback, func(c tele.Context) error {
    chatID := c.Chat().ID
    userID := c.Sender().ID
    return c.Respond()
})
```

## Debugging with @print_id_bot

Use [@print_id_bot](https://t.me/print_id_bot) to inspect the raw update:

- **/json** — Message as JSON. Compare with your handler's input.
- **/dump** — Full update and raw JSON (private chat only). Use to verify `message.chat.id`, `message.from.id`, and structure.

Forward a message to the bot and send /dump to see the exact format.

## Related pages

- [Telegram Bot API: how to get chat_id](/telegram-bot-api-chat-id/)
- [Telegram update JSON: /dump output](/telegram-json-update/)
- [Telegram chat_id format](/telegram-chat-id-format/)

## FAQ

### How do I get chat_id when the bot is added to a group?
When a user sends a message, your handler receives the update with `Message.Chat.ID`. Or add @print_id_bot and send /id to get it manually.

### Can I use int64 for chat_id?
Yes. In Go, Telegram IDs are typically `int64`. Use the type your library provides.

### Where is channel_post?
Check `update.ChannelPost`. For channel posts, `ChannelPost.Chat.ID` is the channel ID.

### Does the update structure match the Telegram API?
Yes. Libraries parse the JSON from the API. Use /dump in @print_id_bot to see the raw structure.

### What if From is nil?
For channel_post, there is no From. Check for nil before accessing.
