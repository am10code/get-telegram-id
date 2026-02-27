+++
title = "print_id_bot: የTelegram ID እና chat_id ረዳት (ትዕዛዞች፣ ቋንቋዎች፣ ባህሪያት)"
description = "ለሙሉ ማጣቀሻ @print_id_bot: ትዕዛዞች፣ 16 ቋንቋዎች፣ የቡድን ቀስቶች እና የገንቢ ባህሪያት (/json፣ /dump)። የTelegram user ID እና chat_id ዎን በሰከንዶች ያግኙ።"
cta = { text = "ቦቱን ይክፈቱ — የTelegram user ID እና chat_id ዎን በፍጥነት ያግኙ።", label = "Open @print_id_bot", url = "https://t.me/print_id_bot" }
+++

@print_id_bot የTelegram ቦት ነው የዎን **Telegram user ID**፣ **chat_id** (ለቡድኖች እና ለሱፐርቡድኖች) እና የሰርግ ID ያሳያል። በግል ቻት እና በቡድኖች ውስጥ ይሰራል፣ በቴሌግራም የቋንቋ ቅንብርዎ መሰረት በ16 ቋንቋዎች መልስ ይሰጣል።

## ትዕዛዞች

| ትዕዛዝ | ስራ |
|---------|-----|
| `/start` | የሰላምታ መልእክት፣ User ID እና Chat ID ዎ፣ ለ/id እናና /help የሚያገለግሉ በመስመር ላይ ቁልፎች |
| `/id` | User ID እና Chat ID ዎ (አጭር መልስ) |
| `/help` | ሙሉ የእርዳታ ጽሑፍ እና የትዕዛዝ ዝርዝር |
| `/json` | የአሁኑ መልእክት በJSON (ለገንቢዎች) |
| `/dump` | ሙሉ የእድሳት ስርጭት እና በቀጥታ JSON (በግል ቻት ብቻ) |

በግል ቻት ውስጥ ማንኛውንም መልእክት (ጽሑፍ፣ ፎቶ፣ ስቲከር ወዘተ) መላክ ደግሞ User ID እና Chat ID ዎን ይመልሳል። ለተላለፉ መልእክቶች ቦቱ የደራሲውን ID በሚገኝ ጊዜ ያሳያል፣ ወይም "ID hidden" የመላኪያ ግል ቅንብሮች ሲበሉጉ። ዝርዝር: [ተላልፈው የቀረቡ መልእክቶች እና የተሰወሩ IDዎች]({{< relref "telegram-forwarded-message-id.md" "en" >}})።

## የተደገፉ ቋንቋዎች (16)

ቦቱ የመልስ ቋንቋዎን ከቴሌግራም `language_code` ዎ ይመርጣል። የተደገፉ: እንግሊዝኛ፣ ሩስኛ፣ ፐርሺያኛ፣ ኡዝበክኛ፣ ሂንዲኛ፣ ቻይንኛ፣ ቱርክኛ፣ ፖርቱጋልኛ፣ ስፓንሽ፣ ዓረብኛ፣ ኢንዶኔዥያኛ፣ ጀርመንኛ፣ ኡርዱኛ፣ ፈረንሳይኛ፣ ታጋሎግኛ፣ አማርኛ። ያልተደገፉ ኮዶች ወደ እንግሊዝኛ ይመለሳሉ። ይመልከቱ [የቋንቋ ምርጫ እንዴት ይሰራል]({{< relref "telegram-id-bot-languages.md" "en" >}})።

## በቡድን እና በሱፐርቡድን ውስጥ ባህሪ

በቡድን ውስጥ ቦቱ የሚመልስ የሚሆነው ስለሚከተለው ብቻ ነው ።

- ለቦቱ መልእክት ስትመልስ
- `/id` ወይም `/help` ስትላክ (@print_id_bot ወይም ያለ)
- ማንኛውንም ትዕዛዝ ከ@print_id_bot ጋር ስትላክ (ለምሳሌ `/foo@print_id_bot`)
- በመልእክትዎ ውስጥ @print_id_bot ስትጠቅስ

- አለበለዚያ ዝም ይላል። ወደ ቡድን ሲጨመር የቡድን ስም እና chat_id ያለው የሰላምታ መልእክት ይላካል። በፍጥነት መመሪያ: [chat_id ለማግኘት ቦት ወደ ቡድን ማከል]({{< relref "add-bot-to-group-chat-id.md" "en" >}})።

## የገንቢ ባህሪያት

- **/json** — የአሁኑ መልእክት በJSON ይመልሳል።
- **/dump** — ሙሉ የእድሳት ስርጭት እና በቀጥታ JSON (በግል ቻት ብቻ)። የBot API ማዋሃዶችን ለማስተካከል ጠቃሚ። ይመልከቱ [የቴሌግራም እድሳት JSON መመርመር]({{< relref "telegram-json-update.md" "en" >}})።

## ተዛማጅ ገጾች

- [Telegram user ID ያግኙ (ደህን ዘዴዎች)]({{< relref "get-telegram-user-id.md" "en" >}})
- [የTelegram ቡድን chat_id እንዴት ያግኙ]({{< relref "get-telegram-chat-id.md" "en" >}})
- [የTelegram ID ዎን እንዴት ያግኙ]({{< relref "how-to-find-telegram-id.md" "en" >}})

## ተለጣጣ ጥያቄዎች

### ቦቱ በሰርጎች ውስጥ ይሰራል?
ቦቱ በግል ቻት እና በቡድኖች/ሱፐርቡድኖች ውስጥ ይሰራል። ለሰርጎች የሰርግ ID ከሌላ ፍሰት ያስፈልጋል (ለምሳሌ እንደ ሰርግ መለጠፍ እና እድሳት የሚቀበል ቦት መጠቀም)። ይመልከቱ [የBot API ለTelegram ሰርግ ID ያግኙ]({{< relref "how-to-get-channel-id-bot-api.md" "en" >}})።

### የሌላ ሰው Telegram user ID ማግኘት እችላለሁ?
ቦቱ የራስዎን ID ወይም ያሉበትን ቻቶች chat_id ያሳያል። ለተላለፉ መልእክቶች የመላኪያ ግል ቅንብር ለማስተላለፍ ቢፈቅድ ብቻ የመላኪያ ID ያሳያል፤ አለበለዚያ "ID hidden"። በስልክ ቁጥር ወይም username በዲ ID መፈለግ አይችሉም። ይመልከቱ [Telegram ID እና username]({{< relref "telegram-id-vs-username.md" "en" >}})።

### ቦቱ በቡድኔ ውስጥ ለምን አይመልስም?
ቦቱ በግል ቻት እና በቡድኖች/ሱፐርቡድኖች ውስጥ ይሰራል። ለሰርጎች የሰርግ ID ከሌላ ፍሰት ያስፈልጋል (ለምሳሌ እንደ ሰርግ መለጠፍ እና እድሳት የሚቀበል ቦት መጠቀም)። ይመልከቱ [ቦት በቡድን ውስጥ የማይመልስ]({{< relref "bot-not-responding-in-group.md" "en" >}}) ለሙሉ የእርስዎ ዝርዝር።

### ቦቱ ነፃ ነው?
አዎ። ምዝገባ ወይም ክፍያ አያስፈልግም።

### በuser ID እና chat_id መካከል ምን ልዩነት አለ?
**User ID** የTelegram መለያ ያሳያል። **chat_id** ውይይትን ያሳያል (ግል ቻት፣ ቡድን፣ ሱፐርቡድን፣ ሰርግ)። ይመልከቱ [Telegram ID እና username]({{< relref "telegram-id-vs-username.md" "en" >}})።
