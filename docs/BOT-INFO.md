# Telegram Bot (@print_id_bot) — Reference

This document describes the Telegram bot linked from this site. The bot source lives in a separate repository (`telegram_user_id_bot`).

## Description

The bot shows **User ID**, **Chat ID**, and Telegram update breakdown (for developers and debugging). It works in private chat and in groups/supergroups.

## Supported Languages (16)

| Code | Language |
|------|----------|
| `en` | English |
| `ru` | Russian |
| `fa` | Persian |
| `uz` | Uzbek |
| `hi` | Hindi |
| `zh` | Chinese |
| `tr` | Turkish |
| `pt` | Portuguese |
| `es` | Spanish |
| `ar` | Arabic |
| `id` | Indonesian |
| `de` | German |
| `ur` | Urdu |
| `fr` | French |
| `tl` | Tagalog (Filipino; `fil` maps to `tl`) |
| `am` | Amharic |

The bot chooses the response language from the user's `language_code`. Unsupported codes fall back to English.

## Commands

| Command | Description |
|---------|-------------|
| `/start` | Welcome message, User ID, Chat ID, and inline buttons (/id, /help) |
| `/id` | User ID and Chat ID (short reply) |
| `/help` | Help text and command list |
| `/json` | Current message as JSON |
| `/dump` | Full update breakdown and raw JSON (private chat only) |

## Functionality

### Private chat

- **/start** — Welcome, User ID, Chat ID, inline buttons (🆔 /id, ❓ /help)
- **/id** — User ID and Chat ID only
- **/help** — Full help with inline /id button
- **/json** — Message body as JSON
- **/dump** — Full update breakdown and raw JSON
- **Any other message** (text, media, photo, document, sticker, video, voice, location, contact) — Reply with User ID and Chat ID
- **Forwarded message** — Shows author name and ID (or "ID hidden" if sender privacy settings hide it); for channel/chat forwards — channel/chat name and ID
- **Edited message** — Reply with User ID and Chat ID
- **Callback (inline button)** — Same as /id or /help depending on button

### Group / supergroup

- **Bot added** — Welcome with group name and Chat ID
- **Reply to bot message** — Group name and Chat ID
- **/id** (with or without @bot) — Group name and Chat ID
- **/help** — Short help and link to open bot in private
- **/any@print_id_bot** — Group name and Chat ID
- **Message with @print_id_bot** — Group name and Chat ID
- **Other messages** — No reply (bot ignored)

### Group triggers

The bot responds in groups only when:

- User replies to the bot's message
- User sends `/id` or `/help` (with or without @bot)
- User sends any command with `@print_id_bot` (e.g. `/foo@print_id_bot`)
- User mentions `@print_id_bot` in the message

## Developer features

- **/dump** — Full update breakdown (structured) and raw JSON
- **/json** — Message body as JSON
- **Inline buttons** — /id and /help under welcome message
- **"Open in private"** button — URL to open bot in private chat (when added to group)

## Bot URL

- **Username:** @print_id_bot
- **Link:** https://t.me/print_id_bot
