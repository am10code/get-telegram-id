+++
title = "获取 Telegram user ID（安全方法）"
description = "如何安全地获取你的 Telegram user ID。使用 @print_id_bot 的逐步方法。无需开发者工具。适用于手机和桌面。"
cta = { text = "打开机器人并点击开始，即刻显示你的 Telegram user ID。", label = "Open @print_id_bot", url = "https://t.me/print_id_bot" }
+++

你的 **Telegram user ID** 是账户的数字标识符。它不会在 Telegram 应用中显示，但当你与机器人或集成交互时，它们可以读取。以下是安全获取的方式。

## 方法 1：使用 @print_id_bot（最快）

1. 在 Telegram 中打开 [@print_id_bot](https://t.me/print_id_bot)。
2. 点击 **开始**。
3. 机器人回复你的 **User ID** 和 **Chat ID**（在私聊中两者相同）。
4. 点击数字即可复制。

机器人根据你的 Telegram 语言设置以 16 种语言回复。不支持的语言会回退到英语。

## 方法 2：向机器人发送任意消息

在与 @print_id_bot 的私聊中，发送任意消息、照片、贴纸或文档。机器人会回复你的 User ID 和 Chat ID。你也可以使用 `/id` 获取简短回复。

## 方法 3：转发消息（及限制）

如果你将另一个用户的消息转发给 @print_id_bot，机器人可能会显示原始发送者的 User ID。但若发送者设置了在转发时隐藏其 ID 的隐私选项，你会看到「ID hidden」。无法通过电话号码或用户名可靠地获取他人的 ID。详情见 [转发的消息与隐藏的 ID]({{< relref "telegram-forwarded-message-id.md" "en" >}})。

## 你不能做的事

- **按电话号码查找**：无法仅凭电话号码获取 Telegram user ID。声称可以的服务往往属于诈骗或侵犯隐私。
- **按用户名查找**：用户名不是 ID。需要用户与机器人或应用交互才能获取其 ID。
- **在无交互的情况下查看他人 ID**：只能获取你所在聊天的 ID，或转发你收到的消息（且允许转发）的用户的 ID。

## 相关页面

- [Telegram ID 与用户名：有何区别？]({{< relref "telegram-id-vs-username.md" "en" >}})
- [为什么 Telegram 不显示你的数字 ID]({{< relref "telegram-id-not-in-ui.md" "en" >}})
- [print_id_bot：命令、语言、功能]({{< relref "print-id-bot.md" "en" >}})

## 常见问题

### 我的 Telegram user ID 是私密的吗？
它不会在 Telegram 界面中显示，但当你与机器人或应用交互时，它们可以读取。不要与不可信的服务分享。

### 可以更改我的 Telegram user ID 吗？
不可以。它一经分配就不会改变。

### 为什么转发消息时机器人显示「ID hidden」？
发送者启用了在转发时隐藏其 ID 的隐私设置。见 [转发的发送者 ID 隐藏]({{< relref "telegram-privacy-forwarded-id-hidden.md" "en" >}})。

### 使用 @print_id_bot 安全吗？
是的。机器人只显示你已有访问权限的 ID（你自己的或你所在聊天的）。它不会在 Telegram 提供之外存储或分享你的数据。

### Telegram user ID 是什么样子？
它是一个数值，通常为 9–10 位数字。例如：`123456789`。
