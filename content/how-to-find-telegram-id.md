+++
title = "How to find your Telegram ID"
description = "Step-by-step ways to get your Telegram user ID and chat_id (groups) safely. The fastest method is using a Telegram bot."
cta = { text = "Fastest way: open the bot and it will show your Telegram ID instantly.", label = "Open the Telegram ID bot", url = "https://t.me/print_id_bot" }
+++

## The quickest way (1 second)

Open the bot and press **Start**. It will return:

- Your **Telegram user ID**
- Your **username** (if you have one)
- (In groups) the **chat_id** of the group/supergroup

## Method 1 — Use a Telegram bot (recommended)

1. Open the bot: https://t.me/print_id_bot
2. Tap **Start**
3. Copy your Telegram ID from the message

**Why this method is best:** it's simple, works on mobile/desktop, and doesn't require developer tools.

## Method 2 — Get a group chat_id (for Bot API)

If you need a group **chat_id** for integrations:

1. Add the bot to your group
2. Send any message in the group (or use the bot's command like `/id`)
3. The bot will reply with the group **chat_id**

> Note: group/supergroup IDs are often negative numbers. That's normal.

## Common issues

- **The bot doesn't reply in my group**: make sure the bot has permission to read messages, and check privacy mode settings (depending on how the bot is built).
- **I only see a username, not an ID**: usernames are not IDs. IDs are numeric.
- **I want someone else's ID**: this tool is for getting your own ID or the chat_id of chats where you are present.

## FAQ

### Is my Telegram ID private?
Your Telegram ID is not publicly shown in the Telegram UI, but bots and apps can read it when you interact with them.

### Can I get an ID by phone number or username?
Officially, you generally can't reliably get someone's numeric ID just from a phone number/username without interaction. Avoid services that promise "ID lookup by phone" — they're often scams or privacy-violating.

### What is the difference between user ID and chat_id?
- **User ID** identifies a Telegram account.
- **chat_id** identifies a conversation (private chat, group, supergroup, channel).
