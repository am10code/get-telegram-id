+++
title = "أدلة Telegram Bot API chat_id"
description = "أدلة المطورين لـ Telegram Bot API chat_id: الحصول على chat_id، إصلاح 'chat not found'، فحص التحديثات، وأمثلة حسب المكتبة."
cta = { text = "احصل على chat_id فورًا مع @print_id_bot.", label = "Open @print_id_bot", url = "https://t.me/print_id_bot" }
+++

**chat_id** مطلوب لمعظم طرق Telegram Bot API: sendMessage، sendPhoto، editMessageText، وعدة أخرى. يحدد الوجهة — محادثة خاصة (مستخدم)، مجموعة، سوبرغروب، أو قناة. في المحادثة الخاصة، chat_id يساوي معرف مستخدم Telegram للمستخدم (موجب). للمجموعات والسوبرغروبات، chat_id عادة سالب. يجمع هذا المحور أدلة المطورين للحصول على chat_id، إصلاح الأخطاء الشائعة، واستخدامه في المكتبات الشائعة.

يمكنك الحصول على chat_id بجعل المستخدمين يتفاعلون مع بوتك (أو بوت مساعد مثل @print_id_bot) وقراءته من التحديثات. للويب هوكس، افحص JSON التحديث الوارد لاستخراج `chat.id`. الأمر `/dump` في @print_id_bot يخرج بنية التحديث الكاملة للتشخيص.

## أدلة

- **[Telegram Bot API: كيفية الحصول على chat_id]({{< relref "telegram-bot-api-chat-id.md" >}})** — احصل على chat_id للمحادثة الخاصة، المجموعة، السوبرغروب، والقناة. استخدم @print_id_bot أو ويب هوك الخاص بك.

- **[Telegram Bot API 'chat not found': الأسباب الشائعة]({{< relref "chat-not-found-telegram-bot.md" >}})** — البوت أُزيل من المحادثة، chat_id خاطئ، الترحيل إلى سوبرغروب. كيفية الإصلاح والحصول على chat_id الصحيح.

- **[Telegram update JSON: كيفية فحص مخرجات /dump]({{< relref "telegram-json-update.md" >}})** — فحص بنية التحديث الخام. مفيد لتصحيح ويب هوكس وفهم حقول message وchat وuser.

- **[Aiogram: الحصول على chat_id ومعرف المستخدم (أمثلة)]({{< relref "aiogram-get-chat-id.md" >}})** — أمثلة Python Aiogram: استخراج chat_id ومعرف المستخدم من التحديثات.

- **[Telegraf (Node.js): الحصول على chat_id ومعرف المستخدم]({{< relref "telegraf-get-chat-id.md" >}})** — أمثلة Node.js Telegraf: الحصول على chat_id ومعرف المستخدم من السياق.

- **[python-telegram-bot: الحصول على معرف المستخدم وchat_id]({{< relref "python-telegram-bot-user-id.md" >}})** — مكتبة python-telegram-bot: استخراج معرف المستخدم وchat_id من التحديثات.

- **[Go Telegram Bot API: الحصول على chat_id]({{< relref "go-telegram-bot-api-chat-id.md" >}})** — Go: الحصول على chat_id من التحديثات الواردة لبوتك.

## FAQ

### لماذا أحصل على "chat not found"؟

الأسباب الشائعة: تم إزالة البوت من المحادثة، تستخدم chat_id خاطئ أو قديم، أو تم ترقية المجموعة إلى سوبرغروب (chat_id قد يتغير). أضف البوت مرة أخرى، احصل على chat_id الحالي مع @print_id_bot، وتأكد من استخدام القيمة الصحيحة.

### كيف أصحح تحديثات ويب هوك؟

استخدم الأمر `/dump` في @print_id_bot (في المحادثة الخاصة) لرؤية JSON التحديث الكامل. يعرض بنية message وchat وuser والحقول الأخرى. قارن مع payload ويب هوك الخاص بك للعثور على مكان chat_id ومعرف المستخدم.

### أي دليل مكتبة يجب أن أستخدم؟

اختر الدليل الذي يطابق stack الخاص بك: Aiogram وpython-telegram-bot لـ Python، Telegraf لـ Node.js، ودليل Go لـ Go. دليل Bot API العام ينطبق على أي لغة.
