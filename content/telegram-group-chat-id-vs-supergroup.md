+++
title = "Group vs supergroup chat_id: key differences"
description = "Telegram group vs supergroup chat_id. When chat_id changes, migration, and how to get the current ID with @print_id_bot."
cta = { text = "Get your group or supergroup chat_id with @print_id_bot.", label = "Open @print_id_bot", url = "https://t.me/print_id_bot" }
+++

Telegram has **groups** and **supergroups**. Both have a **chat_id**, but they behave differently.

## Group

- Up to 200 members (legacy) or 200,000 (newer)
- chat_id is typically negative
- When upgraded to supergroup, the chat_id can change

## Supergroup

- Up to 200,000 members
- Has a username (optional)
- chat_id is typically negative
- Created when a group is upgraded or when you create a "supergroup" directly

## Migration: group → supergroup

When a group becomes a supergroup (e.g. when adding a username or exceeding a limit), Telegram may assign a **new chat_id**. Your old chat_id can stop working. The API may include `migrate_to_chat_id` in the update to indicate the new ID.

## How to get the current chat_id

1. Add [@print_id_bot](https://t.me/print_id_bot) to the group or supergroup.
2. When added, it sends a welcome message with the group name and chat_id.
3. Or send `/id` or mention @print_id_bot — it replies with the current chat_id.

Always use the latest value. If your integration breaks after a migration, get the new chat_id from the bot.

## Both use negative IDs

Group and supergroup chat_ids are typically negative. See [why chat_id can be negative](/telegram-chat-id-negative/) and [chat_id format](/telegram-chat-id-format/).

## Related pages

- [How to get Telegram chat_id for a group](/get-telegram-chat-id/)
- [Add a bot to a group to get chat_id](/add-bot-to-group-chat-id/)
- [Telegram chat_id format](/telegram-chat-id-format/)

## FAQ

### How do I know if my chat is a group or supergroup?
Check `chat.type` in the update: `"group"` or `"supergroup"`. @print_id_bot shows the chat_id; the type is in the raw JSON if you use /dump.

### Will my chat_id change when we add a username?
Adding a username can trigger migration to supergroup. The chat_id may change. Get the new one from @print_id_bot.

### Can I use the old chat_id after migration?
No. Use the new chat_id. The old one may return "chat not found". See [chat not found: common causes](/chat-not-found-telegram-bot/).

### Are group and supergroup IDs formatted the same?
Yes. Both are negative numbers. The format is the same; only the value can change on migration.

### Does @print_id_bot work in both?
Yes. Add it to the group or supergroup and send /id or mention it to get the chat_id.
