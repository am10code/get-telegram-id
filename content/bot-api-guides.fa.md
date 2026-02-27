+++
title = "راهنماهای Telegram Bot API chat_id"
description = "راهنماهای توسعه‌دهنده برای Telegram Bot API chat_id: گرفتن chat_id، رفع 'chat not found'، بررسی آپدیت‌ها و مثال‌های هر کتابخانه."
cta = { text = "با @print_id_bot فوراً chat_id بگیرید.", label = "Open @print_id_bot", url = "https://t.me/print_id_bot" }
+++

**chat_id** برای اکثر متدهای Telegram Bot API لازم است: sendMessage، sendPhoto، editMessageText و بسیاری دیگر. مقصد را مشخص می‌کند — چت خصوصی (کاربر)، گروه، سوپرگروه، یا کانال. در چت خصوصی، chat_id برابر با شناسه کاربر Telegram کاربر است (مثبت). برای گروه‌ها و سوپرگروه‌ها، chat_id معمولاً منفی است. این هاب راهنماهای توسعه‌دهنده برای گرفتن chat_id، رفع خطاهای رایج و استفاده در کتابخانه‌های محبوب را گردآوری می‌کند.

می‌توانید chat_id را با تعامل کاربران با ربات یا ربات کمکی مثل @print_id_bot و خواندن آن از آپدیت‌ها بگیرید. برای وب‌هوک‌ها، JSON آپدیت ورودی را بررسی کنید تا `chat.id` را استخراج کنید. دستور `/dump` در @print_id_bot ساختار کامل آپدیت را برای دیباگ خروجی می‌دهد.

## راهنماها

- **[Telegram Bot API: چگونه chat_id بگیرید]({{< relref "telegram-bot-api-chat-id.md" >}})** — chat_id برای چت خصوصی، گروه، سوپرگروه و کانال بگیرید. از @print_id_bot یا وب‌هوک خود استفاده کنید.

- **[Telegram Bot API 'chat not found': علل رایج]({{< relref "chat-not-found-telegram-bot.md" >}})** — ربات از چت حذف شد، chat_id اشتباه، مهاجرت به سوپرگروه. چگونه رفع و chat_id صحیح بگیرید.

- **[Telegram update JSON: چگونه خروجی /dump را بررسی کنید]({{< relref "telegram-json-update.md" >}})** — ساختار خام آپدیت را بررسی کنید. برای دیباگ وب‌هوک‌ها و درک فیلدهای message، chat و user مفید.

- **[Aiogram: گرفتن chat_id و شناسه کاربر (مثال‌ها)]({{< relref "aiogram-get-chat-id.md" >}})** — مثال‌های Python Aiogram: استخراج chat_id و شناسه کاربر از آپدیت‌ها.

- **[Telegraf (Node.js): گرفتن chat_id و شناسه کاربر]({{< relref "telegraf-get-chat-id.md" >}})** — مثال‌های Node.js Telegraf: گرفتن chat_id و شناسه کاربر از context.

- **[python-telegram-bot: گرفتن شناسه کاربر و chat_id]({{< relref "python-telegram-bot-user-id.md" >}})** — کتابخانه python-telegram-bot: استخراج شناسه کاربر و chat_id از آپدیت‌ها.

- **[Go Telegram Bot API: گرفتن chat_id]({{< relref "go-telegram-bot-api-chat-id.md" >}})** — Go: گرفتن chat_id از آپدیت‌های ورودی برای ربات شما.

## FAQ

### چرا "chat not found" می‌گیرم؟

علل رایج: ربات از چت حذف شد، chat_id اشتباه یا منسوخ استفاده می‌کنید، یا گروه به سوپرگروه ارتقا یافت (chat_id می‌تواند تغییر کند). ربات را دوباره اضافه کنید، chat_id فعلی را با @print_id_bot بگیرید و مطمئن شوید مقدار صحیح استفاده می‌کنید.

### چگونه آپدیت‌های وب‌هوک را دیباگ کنم؟

از دستور `/dump` در @print_id_bot (در چت خصوصی) برای دیدن JSON کامل آپدیت استفاده کنید. ساختار message، chat، user و فیلدهای دیگر را نشان می‌دهد. با payload وب‌هوک خود مقایسه کنید تا ببینید chat_id و شناسه کاربر کجا هستند.

### کدام راهنمای کتابخانه را استفاده کنم؟

راهنمایی را انتخاب کنید که با stack شما مطابقت دارد: Aiogram و python-telegram-bot برای Python، Telegraf برای Node.js، و راهنمای Go برای Go. راهنمای عمومی Bot API برای هر زبان اعمال می‌شود.
