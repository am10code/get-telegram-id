+++
title = "Why Telegram doesn't show your numeric ID (and what to do)"
description = "Telegram hides your numeric user ID in the app. Why it's hidden, how to get it with @print_id_bot, and when you need it for integrations."
cta = { text = "Get your Telegram user ID with @print_id_bot in one tap.", label = "Open @print_id_bot", url = "https://t.me/print_id_bot" }
+++

Telegram does not show your **numeric user ID** anywhere in the app. You see your name, username, and phone number, but not the ID. Here is why and how to get it.

## Why Telegram hides it

The user ID is an internal identifier. Most users do not need it. Showing it could confuse people or encourage misuse (e.g. fake "ID lookup" services). Bots and integrations get it when you interact with them, but the app itself does not display it.

## How to get your user ID

1. Open [@print_id_bot](https://t.me/print_id_bot) in Telegram.
2. Tap **Start**.
3. The bot replies with your **User ID** and **Chat ID** (they match in private chat).
4. Tap the number to copy.

You can also send any message, photo, or sticker — the bot replies with your IDs. The response language follows your Telegram `language_code`; 16 languages are supported, with fallback to English.

## When you need your user ID

- **Bot integrations** — Some bots or services ask for your ID to link your account.
- **Developer testing** — When building a bot, you need your ID to test private messages.
- **Support** — Some services use it for account verification.

## What you cannot do

- **Look up others by phone** — You cannot get someone's Telegram user ID from their phone number. Avoid services that claim this.
- **Look up by username** — Usernames are not IDs. You need the user to interact with a bot. See [Telegram ID vs username](/telegram-id-vs-username/).

## Related pages

- [Get Telegram user ID (safe methods)](/get-telegram-user-id/)
- [Telegram ID vs username](/telegram-id-vs-username/)
- [How to copy and share your Telegram ID safely](/how-to-copy-telegram-id/)

## FAQ

### Is my user ID secret?
It is not shown in the app, but bots and apps can read it when you interact with them. Do not share it with untrusted services.

### Can I change my user ID?
No. It is assigned once and does not change.

### Why do some services ask for my ID?
They need it to send you messages or link your account. Use only trusted services.

### Is it safe to give my ID to @print_id_bot?
The bot only displays IDs you already have access to. It does not store or share your data beyond what Telegram provides.

### What if I have two accounts?
Each account has its own user ID. Open @print_id_bot in each account to get the respective ID.
