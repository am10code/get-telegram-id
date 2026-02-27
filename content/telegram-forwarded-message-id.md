+++
title = "Forwarded messages in Telegram: why IDs can be hidden"
description = "When you forward a message to @print_id_bot, the sender's ID may show as 'ID hidden'. Privacy settings, forwarded origin types, and what you can and cannot get."
cta = { text = "Forward a message to @print_id_bot to see the sender's ID (when allowed).", label = "Open @print_id_bot", url = "https://t.me/print_id_bot" }
+++

When you forward a message to [@print_id_bot](https://t.me/print_id_bot), the bot tries to show the original sender's **Telegram user ID** or the source **channel ID** / **chat_id**. Sometimes you see **"ID hidden"** instead. Here is why.

## What the bot shows

- **Forwarded from user** — Sender name and User ID (if allowed)
- **Forwarded from channel** — Channel name and channel ID
- **Forwarded from chat** — Chat name and chat_id
- **ID hidden** — Sender has privacy settings that hide their ID when forwarding

## Why "ID hidden" appears

Telegram lets users control who can see their identity when messages are forwarded. If the sender:

- Has "Forwarded from" privacy set to "Nobody" or "My contacts"
- Or uses a forwarded-origin type that hides the sender

then the bot cannot show their numeric ID. You see "ID hidden. The sender can enable forwarding in Telegram privacy settings."

## What you cannot do

- **Get ID by phone number** — You cannot look up someone's Telegram user ID from their phone number. Services that claim this are often scams.
- **Get ID by username** — Usernames are not IDs. You need the user to interact with a bot or app.
- **Bypass privacy settings** — If the sender hides their ID, you cannot obtain it.

## Developer note: forward_origin

In Telegram updates, `forward_origin` describes the source. Types include `user`, `hidden_user`, `chat`, `channel`. For `hidden_user`, the ID is not available. Use @print_id_bot's `/dump` in private chat to inspect the structure; for groups, `/json` shows the message body.

## Related pages

- [Forwarded sender ID hidden: reasons and limits](/telegram-privacy-forwarded-id-hidden/)
- [Get Telegram user ID (safe methods)](/get-telegram-user-id/)
- [Telegram ID vs username](/telegram-id-vs-username/)

## FAQ

### Can I get the ID if the sender allows forwarding?
Yes. Forward the message to @print_id_bot. If the sender's privacy allows it, the bot shows their User ID.

### What about forwarded messages from channels?
The bot shows the channel name and channel ID. Channel IDs are typically available when the message is forwarded.

### Why does the bot show a name but not an ID?
For `hidden_user` origin, Telegram provides a display name but not the numeric ID. The sender's privacy settings block it.

### Is "ID hidden" a bug?
No. It is Telegram enforcing the sender's privacy choices.

### Can I ask the sender to change settings?
They can enable "Forwarded from" in Telegram privacy settings if they want their ID to be visible when messages are forwarded. That is their choice.
