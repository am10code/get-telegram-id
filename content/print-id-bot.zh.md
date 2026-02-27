+++
title = "print_id_bot：Telegram ID 与 chat_id 助手（命令、语言、功能）"
description = "@print_id_bot 完整参考：命令、16 种语言、群组触发条件和开发者功能（/json、/dump）。几秒内获取你的 Telegram user ID 和 chat_id。"
cta = { text = "打开机器人，即刻获取你的 Telegram user ID 和 chat_id。", label = "Open @print_id_bot", url = "https://t.me/print_id_bot" }
+++

@print_id_bot 是一个 Telegram 机器人，可显示你的 **Telegram user ID**、**chat_id**（适用于群组和超级群组）以及频道 ID。在私聊和群组中均可使用，并根据你的 Telegram 语言设置以 16 种语言回复。

## 命令

| 命令 | 功能 |
|------|------|
| `/start` | 欢迎消息、你的 User ID 和 Chat ID、/id 和 /help 的内联按钮 |
| `/id` | 你的 User ID 和 Chat ID（简短回复） |
| `/help` | 完整帮助文本和命令列表 |
| `/json` | 当前消息的 JSON 格式（供开发者使用） |
| `/dump` | 完整 update 解析和原始 JSON（仅私聊） |

在私聊中，发送任何消息（文本、照片、贴纸等）也会返回你的 User ID 和 Chat ID。对于转发的消息，机器人会在可用时显示作者 ID，或在发送者隐私设置阻止时显示「ID hidden」。详情见 [转发的消息与隐藏的 ID]({{< relref "telegram-forwarded-message-id.md" "en" >}})。

## 支持的语言（16 种）

机器人根据你的 Telegram `language_code` 选择回复语言。支持：英语、俄语、波斯语、乌兹别克语、印地语、中文、土耳其语、葡萄牙语、西班牙语、阿拉伯语、印尼语、德语、乌尔都语、法语、他加禄语、阿姆哈拉语。不支持的代码会回退到英语。见 [语言选择如何工作]({{< relref "telegram-id-bot-languages.md" "en" >}})。

## 群组与超级群组行为

在群组中，机器人仅在以下情况下回复：

- 你回复机器人的消息时
- 你发送 `/id` 或 `/help` 时（带或不带 @print_id_bot）
- 你发送带 @print_id_bot 的任何命令时（例如 `/foo@print_id_bot`）
- 你在消息中提到 @print_id_bot 时

否则保持静默。被添加到群组时，会发送包含群组名称和 chat_id 的欢迎消息。快速指南见 [添加机器人到群组以获取 chat_id]({{< relref "add-bot-to-group-chat-id.md" "en" >}})。

## 开发者功能

- **/json** — 以 JSON 格式返回当前消息。
- **/dump** — 完整 update 解析和原始 JSON（仅私聊）。用于调试 Bot API 集成。见 [检查 Telegram update JSON]({{< relref "telegram-json-update.md" "en" >}})。

## 相关页面

- [获取 Telegram user ID（安全方法）]({{< relref "get-telegram-user-id.md" "en" >}})
- [如何获取 Telegram 群组 chat_id]({{< relref "get-telegram-chat-id.md" "en" >}})
- [如何查找你的 Telegram ID]({{< relref "how-to-find-telegram-id.md" "en" >}})

## 常见问题

### 机器人在频道中可用吗？
机器人可在私聊和群组/超级群组中使用。频道需要从其他流程获取频道 ID（例如以频道身份发布并使用接收 update 的机器人）。见 [获取 Bot API 的 Telegram 频道 ID]({{< relref "how-to-get-channel-id-bot-api.md" "en" >}})。

### 我能获取他人的 Telegram user ID 吗？
机器人只显示你自己的 ID 或你所在聊天的 chat_id。对于转发的消息，仅在发送者允许转发时显示其 ID；否则显示「ID hidden」。无法通过电话号码或用户名查找 ID。见 [Telegram ID 与用户名]({{< relref "telegram-id-vs-username.md" "en" >}})。

### 为什么机器人在我的群组中不回复？
机器人仅在你回复它、发送 /id 或 /help 或提到 @print_id_bot 时回复。完整检查清单见 [群组中不回复的机器人]({{< relref "bot-not-responding-in-group.md" "en" >}})。

### 机器人免费吗？
是的。无需注册或付费。

### user ID 与 chat_id 有何区别？
**User ID** 标识 Telegram 账户。**chat_id** 标识对话（私聊、群组、超级群组、频道）。见 [Telegram ID 与用户名]({{< relref "telegram-id-vs-username.md" "en" >}})。
