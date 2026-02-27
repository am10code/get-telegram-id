+++
title = "Get Telegram user ID (safe methods)"
description = "How to get your Telegram user ID safely. Step-by-step methods using @print_id_bot. No developer tools required. Works on mobile and desktop."
cta = { text = "Open the bot and tap Start to see your Telegram user ID instantly.", label = "Open @print_id_bot", url = "https://t.me/print_id_bot" }
+++

Your **Telegram user ID** is a numeric identifier for your account. It is not shown in the Telegram app, but bots and integrations can read it when you interact with them. Here are safe ways to get it.

## Method 1: Use @print_id_bot (fastest)

1. Open [@print_id_bot](https://t.me/print_id_bot) in Telegram.
2. Tap **Start**.
3. The bot replies with your **User ID** and **Chat ID** (they match in private chat).
4. Tap the number to copy it.

The bot responds in 16 languages based on your Telegram language setting. Unsupported languages fall back to English.

## Method 2: Send any message to the bot

In private chat with @print_id_bot, send any message, photo, sticker, or document. The bot replies with your User ID and Chat ID. You can also use `/id` for a short reply.

## Method 3: Forward a message (and limitations)

If you forward a message from another user to @print_id_bot, the bot may show the original sender's User ID. However, if the sender has privacy settings that hide their ID when forwarding, you will see "ID hidden". You cannot reliably get someone else's ID by phone number or username. See [forwarded messages and hidden IDs]({{< relref "telegram-forwarded-message-id.md" >}}) for details.

## What you cannot do

- **Look up by phone number**: You cannot get a Telegram user ID from a phone number alone. Services that claim to do this are often scams or privacy-violating.
- **Look up by username**: Usernames are not IDs. You need the user to interact with a bot or app to obtain their ID.
- **See others' IDs without interaction**: You can only get IDs of chats you are in or of users who forward messages you receive (and who allow forwarding).

## Related pages

- [Telegram ID vs username: what's the difference?]({{< relref "telegram-id-vs-username.md" >}})
- [Why Telegram doesn't show your numeric ID]({{< relref "telegram-id-not-in-ui.md" >}})
- [print_id_bot: commands, languages, features]({{< relref "print-id-bot.md" >}})

## FAQ

### Is my Telegram user ID private?
It is not shown in the Telegram UI, but bots and apps can read it when you interact with them. Do not share it with untrusted services.

### Can I change my Telegram user ID?
No. It is assigned once and does not change.

### Why does the bot show "ID hidden" for forwarded messages?
The sender has enabled privacy settings that hide their ID when messages are forwarded. See [forwarded sender ID hidden]({{< relref "telegram-privacy-forwarded-id-hidden.md" >}}).

### Is it safe to use @print_id_bot?
Yes. The bot only displays IDs you already have access to (your own or from chats you're in). It does not store or share your data beyond what Telegram provides.

### What does the Telegram user ID look like?
It is a numeric value, often 9–10 digits. Example: `123456789`.
