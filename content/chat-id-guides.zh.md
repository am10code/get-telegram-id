+++
title = "Telegram chat_id 指南（群组与超级群组）"
description = "获取和理解 Telegram 群组与超级群组 chat_id 的指南。添加机器人、复制 chat_id、解决常见问题。"
cta = { text = "将 @print_id_bot 添加到群组，几秒内获得 chat_id。", label = "Open @print_id_bot", url = "https://t.me/print_id_bot" }
+++

Telegram 群组或超级群组的 **chat_id** 是 Bot API 集成所需的：发送消息、管理成员或构建自动化。与你的用户 ID 不同，群组和超级群组的 chat_id 通常是**负数** — 这是正常且设计如此。本中心收集了帮助你获取和理解群组与超级群组 chat_id 的指南。

获取群组 chat_id 最快的方式是将 @print_id_bot 等机器人添加到群组。添加后，它会发送包含群组名称和 chat_id 的欢迎消息。你也可以发送 `/id` 或提及机器人来再次获取。机器人只在你回复它、发送命令或提及时响应 — 不会响应每条消息。

## 指南

- **[如何获取群组的 Telegram chat_id]({{< relref "get-telegram-chat-id.md" >}})** — 逐步：添加机器人、获取欢迎消息或使用 `/id`。机器人在群组中的行为。

- **[添加机器人到群组获取 chat_id（10 秒）]({{< relref "add-bot-to-group-chat-id.md" >}})** — 快速指南：打开机器人、添加到群组，从欢迎消息复制 chat_id。

- **[Telegram chat_id 格式说明（含示例）]({{< relref "telegram-chat-id-format.md" >}})** — 私聊、群组、超级群组和频道的 chat_id 形式。示例与结构。

- **[为什么 Telegram chat_id 可能是负数]({{< relref "telegram-chat-id-negative.md" >}})** — 群组和超级群组 ID 通常为负数。原因及对你的集成何时重要。

- **[群组与超级群组 chat_id：主要区别]({{< relref "telegram-group-chat-id-vs-supergroup.md" >}})** — 群组升级为超级群组时，chat_id 可能变化。预期情况与处理方式。

- **[Telegram 群组中机器人不响应：检查清单]({{< relref "bot-not-responding-in-group.md" >}})** — 机器人无响应？检查清单：回复机器人、使用 `/id`、提及它并检查权限。

## FAQ

### 为什么我的群组 chat_id 是负数？

群组和超级群组的 chat_id 在 Telegram Bot API 中通常为负数。这是为了与用户 ID（私聊中为正数）区分的设计。正常且符合预期。

### 如果机器人在群组中不回复怎么办？

群组中的机器人通常只在你回复它们、发送 `/id` 或 `/help`，或提及它们（如 @print_id_bot）时响应。若仍无响应，请确认机器人有读取消息的权限，且隐私模式（如适用）允许其查看群组消息。

### 升级为超级群组时 chat_id 会变吗？

会。群组升级为超级群组时，chat_id 可能变化。若你保存了旧的群组 chat_id，可能不再有效。请重新添加机器人，从欢迎消息或 `/id` 获取新的 chat_id。
