+++
title = "How to get Telegram chat_id for a group"
description = "Get the chat_id of a Telegram group or supergroup in seconds. Add @print_id_bot, send /id or mention it, and copy the chat_id. Step-by-step guide."
cta = { text = "Add the bot to your group and get the chat_id in 10 seconds.", label = "Open @print_id_bot", url = "https://t.me/print_id_bot" }
+++

The **chat_id** of a Telegram group or supergroup is required for Bot API integrations. Here is how to get it quickly.

## Step 1: Add the bot to your group

1. Open [@print_id_bot](https://t.me/print_id_bot) in Telegram.
2. Tap **Start**.
3. Add the bot to your group: Open the group → Add members → search for `print_id_bot` → Add.

When the bot is added, it sends a welcome message with the group name and **chat_id**. You can copy it from there.

## Step 2: If you need to get it again

The bot responds in groups only when:

- You reply to the bot's message
- You send `/id` or `/help` (with or without @print_id_bot)
- You send any command with @print_id_bot (e.g. `/foo@print_id_bot`)
- You mention @print_id_bot in a message

Send `/id` or mention @print_id_bot, and the bot replies with the group name and chat_id. Tap the number to copy.

## Group vs supergroup chat_id

Group and supergroup IDs are often **negative numbers**. That is normal. When a group is upgraded to a supergroup, the chat_id can change. See [group vs supergroup chat_id]({{< relref "telegram-group-chat-id-vs-supergroup.md" >}}) for details.

## Troubleshooting

If the bot does not reply, check:

- The bot has permission to read messages
- You triggered it correctly (reply, /id, /help, or @print_id_bot)
- The bot is not in privacy mode blocking group messages (if applicable)

See [bot not responding in a Telegram group]({{< relref "bot-not-responding-in-group.md" >}}) for a full checklist.

## Related pages

- [Add a bot to a group to get chat_id (10 seconds)]({{< relref "add-bot-to-group-chat-id.md" >}})
- [Telegram Bot API: how to get chat_id]({{< relref "telegram-bot-api-chat-id.md" >}})
- [Why Telegram chat_id can be negative]({{< relref "telegram-chat-id-negative.md" >}})

## FAQ

### Why is my group chat_id negative?
Group and supergroup IDs are typically negative in the Telegram Bot API. This is by design. See [Telegram chat_id format]({{< relref "telegram-chat-id-format.md" >}}).

### Can I get someone else's group chat_id?
You can only get the chat_id of groups you are a member of. Add the bot to the group and send /id or mention it.

### Does the bot work in supergroups?
Yes. Both groups and supergroups are supported. The bot shows the group name and chat_id. See [group vs supergroup chat_id]({{< relref "telegram-group-chat-id-vs-supergroup.md" >}}).

### What if the bot was removed from the group?
Add it again. When you add, it sends a welcome message with the chat_id. You can also get it by sending /id or mentioning @print_id_bot.

### Is the chat_id the same for group and supergroup?
After migration to supergroup, the chat_id can change. Always use the current value from the bot or API.
