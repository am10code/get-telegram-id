+++
title = "Telegram chat_id für eine Gruppe erhalten"
description = "Hole die chat_id einer Telegram-Gruppe oder -Supergruppe in Sekunden. @print_id_bot hinzufügen, /id senden oder erwähnen und chat_id kopieren. Schritt-für-Schritt-Anleitung."
cta = { text = "Bot zur Gruppe hinzufügen und chat_id in 10 Sekunden erhalten.", label = "Open @print_id_bot", url = "https://t.me/print_id_bot" }
+++

Die **chat_id** einer Telegram-Gruppe oder -Supergruppe wird für Bot-API-Integrationen benötigt. So erhältst du sie schnell.

## Schritt 1: Bot zur Gruppe hinzufügen

1. Öffne [@print_id_bot](https://t.me/print_id_bot) in Telegram.
2. Tippe auf **Start**.
3. Füge den Bot zur Gruppe hinzu: Gruppe öffnen → Mitglieder hinzufügen → `print_id_bot` suchen → Hinzufügen.

Wenn der Bot hinzugefügt ist, sendet er eine Willkommensnachricht mit Gruppennamen und **chat_id**. Von dort kannst du kopieren.

## Schritt 2: Falls du sie erneut brauchst

Der Bot antwortet in Gruppen nur, wenn:

- du auf die Nachricht des Bots antwortest;
- du `/id` oder `/help` sendest (mit oder ohne @print_id_bot);
- du einen beliebigen Befehl mit @print_id_bot sendest (z. B. `/foo@print_id_bot`);
- du @print_id_bot in einer Nachricht erwähnst.

Sende `/id` oder erwähne @print_id_bot, und der Bot antwortet mit Gruppennamen und chat_id. Tippe auf die Zahl zum Kopieren.

## Gruppe vs. Supergruppe: chat_id

Gruppen- und Supergruppen-IDs sind oft **negative Zahlen**. Das ist normal. Wenn eine Gruppe zur Supergruppe wird, kann sich die chat_id ändern. Details: [Gruppen- vs. Supergruppen-chat_id]({{< relref "telegram-group-chat-id-vs-supergroup.md" "en" >}}).

## Fehlerbehebung

Wenn der Bot nicht antwortet, prüfe:

- ob der Bot Berechtigung hat, Nachrichten zu lesen;
- ob du ihn richtig ausgelöst hast (Antwort, /id, /help oder @print_id_bot);
- ob der Bot nicht im Privatsphäre-Modus ist, der Gruppennachrichten blockiert (falls zutreffend).

Vollständige Checkliste: [Bot antwortet nicht in Telegram-Gruppe]({{< relref "bot-not-responding-in-group.md" "en" >}}).

## Verwandte Seiten

- [Bot zu Gruppe hinzufügen für chat_id (10 Sekunden)]({{< relref "add-bot-to-group-chat-id.md" "en" >}})
- [Telegram Bot API: chat_id erhalten]({{< relref "telegram-bot-api-chat-id.md" "en" >}})
- [Warum Telegram chat_id negativ sein kann]({{< relref "telegram-chat-id-negative.md" "en" >}})

## FAQ

### Warum ist die chat_id meiner Gruppe negativ?
Gruppen- und Supergruppen-IDs sind in der Telegram Bot API typischerweise negativ. Das ist so vorgesehen. Siehe [Telegram chat_id-Format]({{< relref "telegram-chat-id-format.md" "en" >}}).

### Kann ich die chat_id der Gruppe eines anderen bekommen?
Nur von Gruppen, in denen du Mitglied bist. Füge den Bot zur Gruppe hinzu und sende /id oder erwähne ihn.

### Funktioniert der Bot in Supergruppen?
Ja. Gruppen und Supergruppen werden unterstützt. Der Bot zeigt Gruppennamen und chat_id. Siehe [Gruppen- vs. Supergruppen-chat_id]({{< relref "telegram-group-chat-id-vs-supergroup.md" "en" >}}).

### Was, wenn der Bot aus der Gruppe entfernt wurde?
Füge ihn erneut hinzu. Beim Hinzufügen sendet er eine Willkommensnachricht mit chat_id. Du kannst sie auch per /id oder @print_id_bot erhalten.

### Ist die chat_id für Gruppe und Supergruppe gleich?
Nach der Migration zur Supergruppe kann sich die chat_id ändern. Verwende immer den aktuellen Wert vom Bot oder der API.
