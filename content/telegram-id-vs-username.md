+++
title = "Telegram ID vs username: what's the difference?"
description = "Telegram user ID vs username: key differences. IDs are numeric and stable; usernames are optional and changeable. Why you need IDs for Bot API and integrations."
cta = { text = "Get your Telegram user ID instantly with @print_id_bot.", label = "Open @print_id_bot", url = "https://t.me/print_id_bot" }
+++

**Telegram user ID** and **username** are different. Understanding both helps when building bots or integrations.

## Telegram user ID

- **Numeric** (e.g. `123456789`)
- **Assigned once** and does not change
- **Not shown** in the Telegram app
- **Required** for many Bot API operations (sending messages, etc.)
- Bots and apps can read it when you interact with them

To get yours: open [@print_id_bot](https://t.me/print_id_bot), tap Start, and copy the User ID from the reply.

## Username

- **Text** (e.g. `@johndoe`)
- **Optional** — not all users have one
- **Changeable** in Telegram settings
- **Public** if set — anyone can find you by username
- Used for sharing profiles and deep links

## Why IDs matter for developers

The Bot API uses **user ID** and **chat_id**, not usernames. You cannot send a message to a user by username alone; you need their numeric ID. Usernames are useful for display and links, but the API works with IDs.

## Can you get an ID from a username?

**No.** You cannot reliably get someone's numeric ID from their username or phone number without them interacting with your bot or app. Services that claim "ID lookup by phone" or "ID by username" are often scams or violate privacy. See [why Telegram doesn't show your numeric ID](/telegram-id-not-in-ui/).

## Related pages

- [Get Telegram user ID (safe methods)](/get-telegram-user-id/)
- [Telegram ID not in UI](/telegram-id-not-in-ui/)
- [How to find your Telegram ID](/how-to-find-telegram-id/)

## FAQ

### Can I use a username instead of ID in the Bot API?
No. The Bot API requires numeric user IDs and chat_ids for sending messages and most operations.

### Why does @print_id_bot show both username and ID?
The bot shows your User ID (always) and username (if you have one). The ID is what integrations need; the username is for reference.

### Is my username the same as my ID?
No. Username is optional text; ID is a numeric identifier. They are different fields.

### Can someone find my ID from my username?
Not directly. They would need you to interact with a bot or app. Your ID is not publicly listed.

### What if I change my username?
Your user ID stays the same. Only the username changes. Integrations using your ID continue to work.
