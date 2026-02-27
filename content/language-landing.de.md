+++
title = "Telegram-ID erhalten"
description = "Holen Sie sich Ihre Telegram user ID und Gruppen-chat_id in Sekunden. Der Bot @print_id_bot funktioniert im Privatchat und in Gruppen. Sicher und kostenlos."
cta = { url = "https://t.me/print_id_bot", label = "Open @print_id_bot" }
+++

Die **Telegram user ID** ist der numerische Identifikator Ihres Kontos. Sie wird für Integrationen, Bots und Entwicklung benötigt. In der Telegram-Oberfläche ist sie nicht sichtbar, aber Sie können sie in Sekunden mit dem Bot @print_id_bot erhalten. Mehr zu sicheren Methoden in den [user-ID-Anleitungen]({{< relref "user-id-guides.md" >}}).

## So erhalten Sie Ihre Telegram user ID im Privatchat

Öffnen Sie den Bot @print_id_bot im Privatchat und tippen Sie auf **Start**. Der Bot liefert sofort Ihre **Telegram user ID**, Ihren Benutzernamen (falls vorhanden) und die chat_id. Mehr ist nicht nötig: Kopieren Sie einfach die Zahl aus der Nachricht.

Im Privatchat antwortet der Bot auf jede Nachricht: Text, Foto, Sticker oder den Befehl `/id`. Senden Sie, was Sie möchten — Sie erhalten Ihre ID. Es ist privat: Nur Sie sehen die Antwort.

## So erhalten Sie die chat_id einer Gruppe

Um die **chat_id** einer Gruppe oder Supergruppe zu erhalten, fügen Sie @print_id_bot zur Gruppe hinzu. Nach dem Hinzufügen sendet der Bot eine Willkommensnachricht mit dem Gruppennamen und der chat_id.

In Gruppen antwortet der Bot **nur bei bestimmten Aktionen**. Um die chat_id zu erhalten, tun Sie eines der folgenden:

- Senden Sie den Befehl **/id** oder **/help** (mit oder ohne @print_id_bot)
- Antworten Sie auf eine Nachricht des Bots
- Erwähnen Sie **@print_id_bot** in Ihrer Nachricht
- Senden Sie einen beliebigen Befehl mit @print_id_bot (z. B. `/foo@print_id_bot`)

Normale Nachrichten ohne Erwähnung des Bots lösen keine Antwort aus: So vermeidet der Bot Spam. Die ID von Gruppen und Supergruppen ist oft negativ; das ist normal.

## Wo Sie anfangen

- [Telegram user-ID-Anleitungen]({{< relref "user-id-guides.md" >}}) — wie Sie Ihre user ID finden, kopieren und verstehen
- [chat_id-Anleitungen]({{< relref "chat-id-guides.md" >}}) — chat_id von Gruppen und Supergruppen erhalten
- [Bot-API-Anleitungen]({{< relref "bot-api-guides.md" >}}) — Integration mit der Telegram Bot API

## FAQ

### Ist meine Telegram-ID privat?

Ihre Telegram-ID wird in der App nicht öffentlich angezeigt. Bots und Apps erhalten sie nur, wenn Sie mit ihnen interagieren — z. B. wenn Sie einen Bot öffnen und auf Start tippen. Sie entscheiden, welchen Bots Sie vertrauen.

### Warum antwortet der Bot in der Gruppe nicht?

Der Bot antwortet nur, wenn Sie auf seine Nachricht antworten, /id oder /help senden oder @print_id_bot erwähnen. Normale Nachrichten ohne diese Auslöser ignoriert er. Stellen Sie sicher, dass der Bot in der Gruppe ist und Nachrichten lesen kann.

### Was ist der Unterschied zwischen user ID und chat_id?

Die **user ID** identifiziert Ihr Telegram-Konto. Die **chat_id** identifiziert den Chat: privat, Gruppe, Supergruppe oder Kanal. Im Privatchat sind user ID und chat_id dieselbe Zahl. Bei Gruppen ist die chat_id meist negativ.
