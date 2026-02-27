+++
title = "Telegram Bot API chat_id 指南"
description = "Telegram Bot API chat_id 开发者指南：获取 chat_id、修复「chat not found」、检查 updates 及按库示例。"
cta = { text = "使用 @print_id_bot 立即获取 chat_id。", label = "Open @print_id_bot", url = "https://t.me/print_id_bot" }
+++

**chat_id** 是大多数 Telegram Bot API 方法所必需的：sendMessage、sendPhoto、editMessageText 等。它标识目标 — 私聊（用户）、群组、超级群组或频道。在私聊中，chat_id 等于用户的 Telegram 用户 ID（正数）。在群组和超级群组中，chat_id 通常为负数。本中心收集了用于获取 chat_id、修复常见错误并在流行库中使用的开发者指南。

可通过让用户与你的机器人（或 @print_id_bot 等辅助机器人）交互，并从 updates 中读取来获取 chat_id。对于 webhook，检查传入的 update JSON 并提取 `chat.id`。@print_id_bot 中的 `/dump` 命令会输出完整的 update 结构供调试。

## 指南

- **[Telegram Bot API：如何获取 chat_id]({{< relref "telegram-bot-api-chat-id.md" >}})** — 获取私聊、群组、超级群组和频道的 chat_id。使用 @print_id_bot 或你自己的 webhook。

- **[Telegram Bot API「chat not found」：常见原因]({{< relref "chat-not-found-telegram-bot.md" >}})** — 机器人被移出聊天、chat_id 错误、迁移到超级群组。如何修复并获取正确的 chat_id。

- **[Telegram update JSON：如何检查 /dump 输出]({{< relref "telegram-json-update.md" >}})** — 检查原始 update 结构。有助于调试 webhook 并理解 message、chat 和 user 字段。

- **[Aiogram：获取 chat_id 和用户 ID（示例）]({{< relref "aiogram-get-chat-id.md" >}})** — Python Aiogram 示例：从 updates 中提取 chat_id 和用户 ID。

- **[Telegraf (Node.js)：获取 chat_id 和用户 ID]({{< relref "telegraf-get-chat-id.md" >}})** — Node.js Telegraf 示例：从 context 获取 chat_id 和用户 ID。

- **[python-telegram-bot：获取用户 ID 和 chat_id]({{< relref "python-telegram-bot-user-id.md" >}})** — python-telegram-bot 库：从 updates 中提取用户 ID 和 chat_id。

- **[Go Telegram Bot API：获取 chat_id]({{< relref "go-telegram-bot-api-chat-id.md" >}})** — Go：从传入的 updates 中为你的机器人获取 chat_id。

## FAQ

### 为什么会出现「chat not found」？

常见原因：机器人被移出聊天、使用了错误或过期的 chat_id，或群组已升级为超级群组（chat_id 可能变化）。请重新添加机器人，使用 @print_id_bot 获取当前 chat_id，并确保使用正确的值。

### 如何调试 webhook updates？

在 @print_id_bot 中（私聊）使用 `/dump` 命令查看完整 update JSON。它会显示 message、chat、user 及其他字段的结构。与你的 webhook payload 对比，找出 chat_id 和用户 ID 的位置。

### 应该使用哪个库指南？

选择与你技术栈匹配的指南：Python 用 Aiogram 和 python-telegram-bot，Node.js 用 Telegraf，Go 用 Go 指南。通用 Bot API 指南适用于任何语言。
