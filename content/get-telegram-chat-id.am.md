+++
title = "የTelegram ቡድን chat_id እንዴት ማግኘት እንደሚችሉ"
description = "የTelegram ቡድን ወይም ሱፐርቡድን chat_id በሰከንዶች ያግኙ። @print_id_bot ይጨምሩ፣ /id ይላኩ ወይም ይጠቀሱት እና chat_id ይቅዱ። የደረጃ መመሪያ።"
cta = { text = "ቦቱን በቡድንዎ ውስጥ ይጨምሩ እና በ10 ሰከንዶች ውስጥ chat_id ያግኙ።", label = "Open @print_id_bot", url = "https://t.me/print_id_bot" }
+++

የTelegram ቡድን ወይም ሱፐርቡድን **chat_id** ለBot API ውህዶች ያስፈልጋል። በፍጥነት ለማግኘት ዘዴ እዚህ አለ።

## ደረጃ 1 ፡ ቦቱን በቡድንዎ ውስጥ ይጨምሩ

1. በቴሌግራም ውስጥ [@print_id_bot](https://t.me/print_id_bot) ይክፈቱ።
2. **ጀምር** ይጫኑ።
3. ቦቱን በቡድን ውስጥ ይጨምሩ፡ ቡድን ይክፈቱ → አባላት ይጨምሩ → `print_id_bot` ይፈልጉ → ይጨምሩ።

ቦቱ ሲጨመር የቡድን ስም እና **chat_id** ያለው የአማራጭ መልእክት ይላካል። ከዚያ ማግኘት ይችላሉ።

## ደረጃ 2 ፡ እንደገና ማግኘት ከፈለጉ

ቦቱ በቡድኖች ውስጥ በሚከተሉት ጊዜያት ብቻ ይመልሳል፡

- ለቦቱ መልእክት ሲመልሱ፤
- `/id` ወይም `/help` ሲላኩ (@print_id_bot ያለው ወይም ያለው)፤
- ከ@print_id_bot ጋር ማንኛውንም ትዕዛዝ ሲላኩ (ምሳሌ `/foo@print_id_bot`)፤
- በመልእክት ውስጥ @print_id_bot ሲጠቀሱ።

`/id` ይላኩ ወይም @print_id_bot ይጠቀሱ፤ ቦቱ የቡድን ስም እና chat_id ይመልሳል። ለመቅዳት በቁጥሩ ላይ ይጫኑ።

## ቡድን እና ሱፐርቡድን፡ chat_id

የቡድን እና ሱፐርቡድን መለያዎች ብዙውን ጊዜ **አሉታዊ ቁጥሮች** ናቸው። ይህ የተለመደ ነው። ቡድን ወደ ሱፐርቡድን ሲያድግ chat_id ሊቀየር ይችላል። ዝርዝር: [ቡድን እና ሱፐርቡድን chat_id]({{< relref "telegram-group-chat-id-vs-supergroup.md" "en" >}})።

## ችግር መፍታት

ቦቱ ካልመለሰ ያረጋግጡ፡

- ቦቱ መልእክቶችን የማንበብ ፍቃድ አለው፤
- በትክክል አስነስተዋል (መልስ፣ /id፣ /help ወይም @print_id_bot)፤
- ቦቱ የቡድን መልእክቶችን በሚያጋስስ የግል ሁነት ሁነት ውስጥ አይደለም (ከተፈቀደ)።

ሙሉ የቼክ ዝርዝር: [ቦት በTelegram ቡድን ውስጥ አይመልስም]({{< relref "bot-not-responding-in-group.md" "en" >}})።

## ተዛማጅ ገጾች

- [chat_id ለማግኘት ቡድን ውስጥ ቦት ማከል (10 ሰከንዶች)]({{< relref "add-bot-to-group-chat-id.md" "en" >}})
- [Telegram Bot API: chat_id እንዴት ማግኘት እንደሚችሉ]({{< relref "telegram-bot-api-chat-id.md" "en" >}})
- [ለምን Telegram chat_id አሉታዊ ሊሆን ይችላል]({{< relref "telegram-chat-id-negative.md" "en" >}})

## ተለጣጣ ጥያቄዎች

### የቡድኔ chat_id ለምን አሉታዊ ነው?
የቡድን እና ሱፐርቡድን መለያዎች በTelegram Bot API ውስጥ ብዙውን ጊዜ አሉታዊ ናቸው። ይህ በንድፍ ነው። ይመልከቱ [የTelegram chat_id ቅርጸት]({{< relref "telegram-chat-id-format.md" "en" >}})።

### የሌላ ሰው ቡድን chat_id ማግኘት እችላለሁ?
ያሉበትን ቡድኖች ብቻ። ቦቱን በቡድን ውስጥ ይጨምሩ እና /id ይላኩ ወይም ይጠቀሱት።

### ቦቱ በሱፐርቡድኖች ውስጥ ይሰራል?
አዎ። ቡድን እና ሱፐርቡድን ሁለቱም ይደገፋሉ። ቦቱ የቡድን ስም እና chat_id ያሳያል። ይመልከቱ [ቡድን እና ሱፐርቡድን chat_id]({{< relref "telegram-group-chat-id-vs-supergroup.md" "en" >}})።

### ቦቱ ከቡድን ቢወገድ ምን ማድረግ አለብኝ?
እንደገና ይጨምሩ። ሲጨመር chat_id ያለው የአማራጭ መልእክት ይላካል። /id በመላክ ወይም @print_id_bot በመጠቀም ማግኘት ይችላሉ።

### ቡድን እና ሱፐርቡድን ለchat_id ተመሳሳይ ነው?
ወደ ሱፐርቡድን ማስተላለፍ ካለቀ በኋላ chat_id ሊቀየር ይችላል። ሁልጊዜ ከቦት ወይም API የአሁኑን ዋጋ ይጠቀሙ።
