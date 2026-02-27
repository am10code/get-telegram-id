+++
title = "Forwarded sender ID hidden in Telegram: reasons and limits"
description = "Why you see 'ID hidden' when forwarding to @print_id_bot. Telegram privacy settings, forward_origin types, and what you can and cannot get."
cta = { text = "Forward a message to @print_id_bot to see when ID is available or hidden.", label = "Open @print_id_bot", url = "https://t.me/print_id_bot" }
+++

When you forward a message to [@print_id_bot](https://t.me/print_id_bot), you may see **"ID hidden"** instead of the sender's Telegram user ID. Here is why and what you can do.

## Why "ID hidden" appears

Telegram lets users control who can see their identity when messages are forwarded. In **Settings → Privacy and Security → Forwarded Messages**, users can set:

- **Everyone** — Forwarded messages show their name and ID (when the bot has access).
- **Contacts** — Only contacts see it.
- **Nobody** — No one sees the sender's identity; you get "ID hidden."

When the sender chooses "Nobody" or restricts it to contacts, the bot cannot show their numeric ID. You see: "ID hidden. The sender can enable forwarding in Telegram privacy settings."

## What the bot shows

| Forward source | What you see |
|----------------|--------------|
| User (forwarding allowed) | Sender name and User ID |
| User (forwarding restricted) | "ID hidden" |
| Channel | Channel name and channel ID |
| Chat (group) | Chat name and chat_id |

Channel and chat IDs are usually available. User IDs depend on the sender's privacy settings.

## What you cannot do

- **Bypass privacy** — You cannot get the ID if the sender has restricted forwarding.
- **Look up by phone** — You cannot get a user ID from a phone number. Avoid services that claim this.
- **Look up by username** — Usernames are not IDs. The user must interact with a bot. See [Telegram ID vs username](/telegram-id-vs-username/).

## Developer note

In the update, `forward_origin.type` can be `user`, `hidden_user`, `chat`, or `channel`. For `hidden_user`, only a display name may be present; the numeric ID is not available. Use /dump in @print_id_bot to inspect the structure.

## Related pages

- [Forwarded messages: why IDs can be hidden](/telegram-forwarded-message-id/)
- [Get Telegram user ID (safe methods)](/get-telegram-user-id/)
- [Telegram ID vs username](/telegram-id-vs-username/)

## FAQ

### Can the sender change settings so I can see their ID?
Yes. If they set "Forwarded Messages" to "Everyone," the bot can show their ID when you forward. That is their choice.

### Does "ID hidden" apply to channels?
No. Channel IDs are typically available when you forward a channel post. Only user identity can be hidden.

### Why does the bot show a name but not an ID?
For `hidden_user`, Telegram may provide a display name (e.g. "John") but not the numeric ID. Privacy settings block the ID.

### Is this a bug in the bot?
No. The bot shows what Telegram provides. Privacy settings limit the data.

### Can I use a different bot to get the ID?
No. All bots receive the same update structure. If Telegram hides the ID, no bot can show it.
