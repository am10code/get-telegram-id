+++
title = "Telegram ID 机器人支持 16 种语言：语言选择如何工作"
description = "@print_id_bot 如何根据你的 Telegram language_code 选择回复语言。16 种支持的语言，回退到英语。俄语、波斯语、阿拉伯语等。"
cta = { text = "打开 @print_id_bot — 它以你的 Telegram 语言回复。", label = "Open @print_id_bot", url = "https://t.me/print_id_bot" }
+++

@print_id_bot 根据你的 Telegram 语言设置以 **16 种语言** 回复。无需手动选择语言。

## 工作原理

机器人从更新中读取你的 **language_code**。使用代码的第一部分（例如 pt-BR 转为 pt）并映射到支持的语言环境。不支持的语言代码回退到 **英语**。

## 支持的语言（16）

| 代码 | 语言 |
|------|------|
| en | 英语 |
| ru | 俄语 |
| fa | 波斯语 |
| uz | 乌兹别克语 |
| hi | 印地语 |
| zh | 中文 |
| tr | 土耳其语 |
| pt | 葡萄牙语 |
| es | 西班牙语 |
| ar | 阿拉伯语 |
| id | 印尼语 |
| de | 德语 |
| ur | 乌尔都语 |
| fr | 法语 |
| tl | 他加禄语（菲律宾语；fil 映射到 tl）|
| am | 阿姆哈拉语 |

## 特殊情况

- **菲律宾语** — Telegram 发送 fil；机器人映射到 tl（他加禄语）。
- **葡萄牙语（巴西）** — pt-BR 使用 pt（葡萄牙语）。
- **中文** — zh-CN、zh-TW 使用 zh（中文）。

## 已本地化的内容

所有机器人回复：欢迎文本、标签（User ID、Chat ID、群组名称）、帮助文本、按钮以及「ID hidden」或「点击数字以复制」等消息。 /json 和 /dump 中的原始 JSON 不变；只有可读标签使用你的语言。

## 相关页面

- [如果你不说英语，使用 @print_id_bot]({{< relref "telegram-id-bot-for-non-english.md" "en" >}})
- [print_id_bot：命令、语言、功能]({{< relref "print-id-bot.md" "en" >}})
- [获取 Telegram user ID（安全方法）]({{< relref "get-telegram-user-id.md" "en" >}})

## 常见问题

### 如何更改机器人的语言？
在设置 → 语言中更改 Telegram 应用语言。机器人会使用它。机器人内没有语言开关。

### 如果我的语言不受支持怎么办？
机器人会回退到英语。所有功能同样可用。

### 机器人是否支持从右到左 (RTL) 的语言？
是的。阿拉伯语、波斯语和乌尔都语均支持。Telegram 处理 RTL 渲染。

### 我可以请求新语言吗？
机器人支持 16 种语言。添加更多取决于维护者。英语回退确保每个人都能使用。

### 语言会被存储或发送到其他地方吗？
不会。机器人从每次更新中读取 language_code，仅用于选择回复字符串。不会被存储或共享。
