+++
title = "如何获取 Telegram 群组的 chat_id"
description = "几秒钟内获取 Telegram 群组或超级群组的 chat_id。添加 @print_id_bot，发送 /id 或提及它，然后复制 chat_id。分步指南。"
cta = { text = "将机器人添加到群组，10 秒内获取 chat_id。", label = "Open @print_id_bot", url = "https://t.me/print_id_bot" }
+++

Telegram 群组或超级群组的 **chat_id** 是 Bot API 集成所需的。以下是快速获取方法。

## 步骤 1：将机器人添加到群组

1. 在 Telegram 中打开 [@print_id_bot](https://t.me/print_id_bot)。
2. 点击 **开始**。
3. 将机器人添加到群组：打开群组，添加成员，搜索 print_id_bot，添加。

机器人添加后，会发送包含群组名称和 **chat_id** 的欢迎消息。可从该处复制。

## 步骤 2：如需再次获取

机器人仅在以下情况下在群组中回复：你回复了机器人的消息；你发送了 /id 或 /help；你发送了带 @print_id_bot 的任何命令；你在消息中提及了 @print_id_bot。

发送 /id 或提及 @print_id_bot，机器人会回复群组名称和 chat_id。点击数字即可复制。

## 群组与超级群组：chat_id

群组和超级群组的 ID 通常为负数。这是正常的。群组升级为超级群组时，chat_id 可能会变化。详情见 [群组与超级群组 chat_id]({{< relref "telegram-group-chat-id-vs-supergroup.md" "en" >}})。

## 故障排除

若机器人不回复，请检查：机器人是否有读取消息的权限；你是否正确触发了它；机器人是否处于会屏蔽群组消息的隐私模式。

完整清单见 [Telegram 群组中机器人不回复]({{< relref "bot-not-responding-in-group.md" "en" >}})。

## 相关页面

- [添加机器人到群组以获取 chat_id（10 秒）]({{< relref "add-bot-to-group-chat-id.md" "en" >}})
- [Telegram Bot API：如何获取 chat_id]({{< relref "telegram-bot-api-chat-id.md" "en" >}})
- [为什么 Telegram chat_id 可能为负数]({{< relref "telegram-chat-id-negative.md" "en" >}})

## 常见问题

### 为什么我的群组 chat_id 是负数？
在 Telegram Bot API 中，群组和超级群组 ID 通常为负数。这是设计如此。见 [Telegram chat_id 格式]({{< relref "telegram-chat-id-format.md" "en" >}})。

### 能否获取他人群组的 chat_id？
只能获取你所在群组的。将机器人添加到群组并发送 /id 或提及它。

### 机器人在超级群组中可用吗？
是的。群组和超级群组均支持。机器人会显示群组名称和 chat_id。见 [群组与超级群组 chat_id]({{< relref "telegram-group-chat-id-vs-supergroup.md" "en" >}})。

### 若机器人被移出群组怎么办？
重新添加。添加时会发送包含 chat_id 的欢迎消息。也可通过发送 /id 或提及 @print_id_bot 获取。

### 群组和超级群组的 chat_id 相同吗？
迁移到超级群组后，chat_id 可能变化。请始终使用机器人或 API 返回的当前值。
