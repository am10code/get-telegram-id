+++
title = "Руководства по Telegram Bot API chat_id"
description = "Руководства для разработчиков по Telegram Bot API chat_id: получение chat_id, исправление «chat not found», разбор updates и примеры для библиотек."
cta = { text = "Получите chat_id мгновенно с @print_id_bot.", label = "Open @print_id_bot", url = "https://t.me/print_id_bot" }
+++

**chat_id** нужен для большинства методов Telegram Bot API: sendMessage, sendPhoto, editMessageText и многих других. Он указывает получателя — личный чат (пользователь), группа, супергруппа или канал. В личном чате chat_id равен Telegram user ID пользователя (положительный). Для групп и супергрупп chat_id обычно отрицательный. Этот раздел собирает руководства для разработчиков по получению chat_id, исправлению типичных ошибок и использованию в популярных библиотеках.

Получить chat_id можно, когда пользователи взаимодействуют с вашим ботом (или вспомогательным ботом вроде @print_id_bot), и читать его из updates. Для webhooks — разбирать входящий JSON update и извлекать `chat.id`. Команда `/dump` в @print_id_bot выводит полную структуру update для отладки.

## Руководства

- **[Telegram Bot API: как получить chat_id]({{< relref "telegram-bot-api-chat-id.md" >}})** — Получение chat_id для личного чата, группы, супергруппы и канала. Использование @print_id_bot или собственного webhook.

- **[Telegram Bot API «chat not found»: частые причины]({{< relref "chat-not-found-telegram-bot.md" >}})** — Бот удалён из чата, неверный chat_id, миграция в супергруппу. Как исправить и получить правильный chat_id.

- **[Telegram update JSON: как разобрать вывод /dump]({{< relref "telegram-json-update.md" >}})** — Разбор сырой структуры update. Полезно для отладки webhooks и понимания полей message, chat и user.

- **[Aiogram: получение chat_id и user ID (примеры)]({{< relref "aiogram-get-chat-id.md" >}})** — Примеры на Python Aiogram: извлечение chat_id и user ID из updates.

- **[Telegraf (Node.js): получение chat_id и user ID]({{< relref "telegraf-get-chat-id.md" >}})** — Примеры на Node.js Telegraf: получение chat_id и user ID из context.

- **[python-telegram-bot: получение user ID и chat_id]({{< relref "python-telegram-bot-user-id.md" >}})** — Библиотека python-telegram-bot: извлечение user ID и chat_id из updates.

- **[Go Telegram Bot API: получение chat_id]({{< relref "go-telegram-bot-api-chat-id.md" >}})** — Go: получение chat_id из входящих updates для вашего бота.

## FAQ

### Почему возникает «chat not found»?

Частые причины: бот удалён из чата, используется неверный или устаревший chat_id, или группа перешла в супергруппу (chat_id мог измениться). Добавьте бота снова, получите актуальный chat_id через @print_id_bot и убедитесь, что используете правильное значение.

### Как отлаживать webhook updates?

Используйте команду `/dump` в @print_id_bot (в личном чате), чтобы увидеть полный update JSON. Она показывает структуру message, chat, user и других полей. Сравните с payload вашего webhook, чтобы найти, где находятся chat_id и user ID.

### Какой гайд по библиотеке выбрать?

Выберите гайд под ваш стек: Aiogram и python-telegram-bot для Python, Telegraf для Node.js, Go-гайд для Go. Общее руководство по Bot API подходит для любого языка.
