+++
title = "Add a bot to a group to get chat_id (10 seconds)"
description = "Get your Telegram group chat_id in 10 seconds. Add @print_id_bot, get the welcome message with chat_id, or send /id. No coding required."
cta = { text = "Add @print_id_bot to your group and get chat_id instantly.", label = "Open @print_id_bot", url = "https://t.me/print_id_bot" }
+++

Getting the **chat_id** of a Telegram group takes about 10 seconds with @print_id_bot.

## Step 1: Open the bot

1. Open [@print_id_bot](https://t.me/print_id_bot) in Telegram.
2. Tap **Start** (if prompted).

## Step 2: Add the bot to your group

1. Open the group where you need the chat_id.
2. Tap the group name → **Add members** (or equivalent).
3. Search for `print_id_bot`.
4. Add the bot.

## Step 3: Get the chat_id

As soon as the bot is added, it sends a welcome message with:

- Group name
- **chat_id** (the number you need)
- A tip to tap the number to copy

Copy the chat_id from that message. Group and supergroup IDs are often negative — that is normal. See [why chat_id can be negative](/telegram-chat-id-negative/).

## Getting the chat_id again later

The bot responds in groups only when you:

- Reply to the bot's message
- Send `/id` or `/help`
- Send any command with @print_id_bot (e.g. `/foo@print_id_bot`)
- Mention @print_id_bot in a message

Send `/id` or mention @print_id_bot, and it replies with the group name and chat_id.

## Troubleshooting

If the bot does not reply, see [bot not responding in a Telegram group](/bot-not-responding-in-group/). Common causes: the bot needs to be triggered correctly, or it may not have permission to read messages.

## Related pages

- [How to get Telegram chat_id for a group](/get-telegram-chat-id/)
- [Telegram Bot API: how to get chat_id](/telegram-bot-api-chat-id/)
- [print_id_bot: commands and features](/print-id-bot/)

## FAQ

### Do I need to keep the bot in the group?
You can remove it after copying the chat_id. Add it again when you need to verify or get the ID again (e.g. after supergroup migration).

### Can I add the bot to multiple groups?
Yes. Each group has its own chat_id. Add the bot to each group and copy the respective chat_id.

### Why is the chat_id negative?
Group and supergroup IDs are typically negative in the Telegram Bot API. See [Telegram chat_id format](/telegram-chat-id-format/).

### Does this work for supergroups?
Yes. The bot works in both groups and supergroups. See [group vs supergroup chat_id](/telegram-group-chat-id-vs-supergroup/).

### What if the bot was already in the group?
Send `/id` or mention @print_id_bot to get the chat_id again.
