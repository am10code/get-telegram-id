+++
title = "获取 Telegram ID"
description = "几秒钟内获取您的 Telegram 用户 ID 和群组 chat_id。机器人 @print_id_bot 在私聊和群组中均可使用。安全且免费。"
cta = { url = "https://t.me/print_id_bot", label = "Open @print_id_bot" }
+++

**Telegram 用户 ID** 是您账户的数字标识符。用于集成、机器人和开发。在 Telegram 界面中不可见，但可通过 @print_id_bot 在几秒钟内获取。更多安全方法请参阅 [用户 ID 指南]({{< relref "user-id-guides.md" >}})。

## 如何在私聊中获取 Telegram 用户 ID

在私聊中打开 @print_id_bot 并点击**开始**。机器人会立即返回您的 **Telegram 用户 ID**、用户名（如有）和 chat_id。无需其他操作：只需从消息中复制数字即可。

在私聊中，机器人会回复任何消息：文字、图片、贴纸或 `/id` 命令。发送任意内容即可获得您的 ID。私密：只有您能看到回复。

## 如何获取群组 chat_id

要获取群组或超级群组的 **chat_id**，请将 @print_id_bot 添加到群组。添加后，机器人会发送包含群组名称和 chat_id 的欢迎消息。

在群组中，机器人**仅在特定操作时**回复。要获取 chat_id，请执行以下任一操作：

- 发送 **/id** 或 **/help** 命令（可带或不带 @print_id_bot）
- 回复机器人的消息
- 在消息中提及 **@print_id_bot**
- 发送带 @print_id_bot 的任何命令（例如 `/foo@print_id_bot`）

未提及机器人的普通消息不会触发回复：这样可避免垃圾信息。群组和超级群组的 ID 通常为负数；这是正常的。

## 从这里开始

- [Telegram 用户 ID 指南]({{< relref "user-id-guides.md" >}}) — 如何查找、复制和理解您的用户 ID
- [chat_id 指南]({{< relref "chat-id-guides.md" >}}) — 获取群组和超级群组的 chat_id
- [Bot API 指南]({{< relref "bot-api-guides.md" >}}) — 与 Telegram Bot API 集成

## 常见问题

### 我的 Telegram ID 是私密的吗？

您的 Telegram ID 不会在应用中公开显示。机器人和应用只有在您与其交互时才能获取 — 例如打开机器人并点击开始。您可以选择信任哪些机器人。

### 为什么机器人在群组中不回复？

机器人仅在您回复其消息、发送 /id 或 /help、或提及 @print_id_bot 时回复。没有这些触发条件的普通消息会被忽略。请确保机器人已加入群组且可以读取消息。

### 用户 ID 和 chat_id 有什么区别？

**用户 ID** 标识您的 Telegram 账户。**chat_id** 标识对话：私聊、群组、超级群组或频道。在私聊中，用户 ID 和 chat_id 是同一数字。群组的 chat_id 通常为负数。
