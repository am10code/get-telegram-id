+++
title = "print_id_bot: Telegram ID & chat_id Helfer (Befehle, Sprachen, Funktionen)"
description = "Vollständige Referenz für @print_id_bot: Befehle, 16 Sprachen, Gruppentrigger und Entwicklerfunktionen (/json, /dump). Telegram User ID und chat_id in Sekunden."
cta = { text = "Bot öffnen — Telegram User ID und chat_id sofort anzeigen.", label = "Open @print_id_bot", url = "https://t.me/print_id_bot" }
+++

@print_id_bot ist ein Telegram-Bot, der deine **Telegram User ID**, **chat_id** (für Gruppen und Supergruppen) und Kanal-ID anzeigt. Er funktioniert im Privatchat und in Gruppen, mit Antworten in 16 Sprachen basierend auf deiner Telegram-Spracheinstellung.

## Befehle

| Befehl | Funktion |
|--------|----------|
| `/start` | Willkommensnachricht, User ID und Chat ID, Inline-Buttons für /id und /help |
| `/id` | User ID und Chat ID (kurze Antwort) |
| `/help` | Vollständiger Hilfetext und Befehlsliste |
| `/json` | Aktuelle Nachricht als JSON (für Entwickler) |
| `/dump` | Vollständige Update-Aufschlüsselung und Roh-JSON (nur im Privatchat) |

Im Privatchat liefert das Senden jeder Nachricht (Text, Foto, Sticker usw.) ebenfalls deine User ID und Chat ID. Bei weitergeleiteten Nachrichten zeigt der Bot die ID des Autors, wenn verfügbar, oder "ID hidden", wenn die Privatsphäre-Einstellungen des Absenders dies blockieren. Details: [weitergeleitete Nachrichten und versteckte IDs]({{< relref "telegram-forwarded-message-id.md" "en" >}}).

## Unterstützte Sprachen (16)

Der Bot wählt die Antwortsprache anhand deines Telegram-`language_code`. Unterstützt: Englisch, Russisch, Persisch, Usbekisch, Hindi, Chinesisch, Türkisch, Portugiesisch, Spanisch, Arabisch, Indonesisch, Deutsch, Urdu, Französisch, Tagalog, Amharisch. Nicht unterstützte Codes fallen auf Englisch zurück. Siehe [wie die Sprachauswahl funktioniert]({{< relref "telegram-id-bot-languages.md" "en" >}}).

## Verhalten in Gruppen und Supergruppen

In Gruppen antwortet der Bot nur, wenn du:

- Auf die Nachricht des Bots antwortest
- `/id` oder `/help` sendest (mit oder ohne @print_id_bot)
- Einen beliebigen Befehl mit @print_id_bot sendest (z.B. `/foo@print_id_bot`)
- @print_id_bot in deiner Nachricht erwähnst

Sonst bleibt er stumm. Beim Hinzufügen zu einer Gruppe sendet er eine Willkommensnachricht mit Gruppennamen und chat_id. Kurzanleitung: [Bot zu Gruppe hinzufügen für chat_id]({{< relref "add-bot-to-group-chat-id.md" "en" >}}).

## Entwicklerfunktionen

- **/json** — Gibt die aktuelle Nachricht als JSON zurück.
- **/dump** — Vollständige Update-Aufschlüsselung und Roh-JSON (nur im Privatchat). Nützlich zum Debuggen von Bot-API-Integrationen. Siehe [Telegram-Update-JSON untersuchen]({{< relref "telegram-json-update.md" "en" >}}).

## Verwandte Seiten

- [Telegram User ID erhalten (sichere Methoden)]({{< relref "get-telegram-user-id.md" "en" >}})
- [Telegram chat_id für eine Gruppe erhalten]({{< relref "get-telegram-chat-id.md" "en" >}})
- [Deine Telegram ID finden]({{< relref "how-to-find-telegram-id.md" "en" >}})

## FAQ

### Funktioniert der Bot in Kanälen?
Der Bot funktioniert im Privatchat und in Gruppen/Supergruppen. Für Kanäle benötigst du die Kanal-ID aus einem anderen Ablauf (z.B. als Kanal posten und einen Bot nutzen, der Updates erhält). Siehe [Telegram-Kanal-ID für Bot API erhalten]({{< relref "how-to-get-channel-id-bot-api.md" "en" >}}).

### Kann ich die Telegram User ID einer anderen Person erhalten?
Der Bot zeigt deine eigene ID oder die chat_id von Chats, in denen du bist. Bei weitergeleiteten Nachrichten zeigt er die ID des Absenders nur, wenn Weiterleitung erlaubt ist; sonst "ID hidden". Du kannst keine ID per Telefonnummer oder Username nachschlagen. Siehe [Telegram ID vs Username]({{< relref "telegram-id-vs-username.md" "en" >}}).

### Warum antwortet der Bot nicht in meiner Gruppe?
Der Bot antwortet nur, wenn du ihm antwortest, /id oder /help sendest oder @print_id_bot erwähnst. Siehe [Bot antwortet nicht in Gruppe]({{< relref "bot-not-responding-in-group.md" "en" >}}) für eine vollständige Checkliste.

### Ist der Bot kostenlos?
Ja. Keine Anmeldung oder Zahlung erforderlich.

### Was ist der Unterschied zwischen User ID und chat_id?
**User ID** identifiziert ein Telegram-Konto. **chat_id** identifiziert eine Unterhaltung (Privatchat, Gruppe, Supergruppe, Kanal). Siehe [Telegram ID vs Username]({{< relref "telegram-id-vs-username.md" "en" >}}).
