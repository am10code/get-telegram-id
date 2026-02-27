+++
title = "Telegram-ID-Bot in 16 Sprachen: wie die Sprachauswahl funktioniert"
description = "Wie @print_id_bot die Antwortsprache aus deinem Telegram language_code wählt. 16 unterstützte Sprachen, Fallback auf Englisch. Russisch, Persisch, Arabisch und mehr."
cta = { text = "Öffne @print_id_bot — er antwortet in deiner Telegram-Sprache.", label = "Open @print_id_bot", url = "https://t.me/print_id_bot" }
+++

@print_id_bot antwortet in **16 Sprachen** basierend auf deiner Telegram-Spracheinstellung. Keine manuelle Sprachauswahl nötig.

## Wie es funktioniert

Der Bot liest deinen **language_code** aus dem Update (`message.from.language_code`, `edited_message.from.language_code` oder `callback_query.from.language_code`). Er nutzt den ersten Teil des Codes (z. B. `pt-BR` → `pt`) und mappt ihn auf eine unterstützte Locale. Nicht unterstützte Codes fallen auf **Englisch** zurück.

## Unterstützte Sprachen (16)

| Code | Sprache |
|------|---------|
| `en` | Englisch |
| `ru` | Russisch |
| `fa` | Persisch |
| `uz` | Usbekisch |
| `hi` | Hindi |
| `zh` | Chinesisch |
| `tr` | Türkisch |
| `pt` | Portugiesisch |
| `es` | Spanisch |
| `ar` | Arabisch |
| `id` | Indonesisch |
| `de` | Deutsch |
| `ur` | Urdu |
| `fr` | Französisch |
| `tl` | Tagalog (Filipino; `fil` → `tl`) |
| `am` | Amharisch |

## Sonderfälle

- **Filipino** — Telegram sendet `fil`; der Bot mappt auf `tl` (Tagalog).
- **Portugiesisch (Brasilien)** — `pt-BR` nutzt `pt` (Portugiesisch).
- **Chinesisch** — `zh-CN`, `zh-TW` nutzen `zh` (Chinesisch).

## Was lokalisiert ist

Alle Bot-Antworten: Willkommenstext, Labels (User ID, Chat ID, Gruppenname), Hilfetext, Buttons und Nachrichten wie "ID hidden" oder "Auf die Zahl tippen zum Kopieren". Das rohe JSON in /json und /dump bleibt unverändert; nur die lesbaren Labels nutzen deine Sprache.

## Verwandte Seiten

- [@print_id_bot nutzen wenn du kein Englisch sprichst]({{< relref "telegram-id-bot-for-non-english.md" "en" >}})
- [print_id_bot: Befehle, Sprachen, Funktionen]({{< relref "print-id-bot.md" "en" >}})
- [Telegram User ID erhalten (sichere Methoden)]({{< relref "get-telegram-user-id.md" "en" >}})

## FAQ

### Wie ändere ich die Bot-Sprache?
Ändere die Telegram-App-Sprache unter Einstellungen → Sprache. Der Bot nutzt das. Es gibt keinen Sprachschalter im Bot.

### Was wenn meine Sprache nicht unterstützt wird?
Der Bot fällt auf Englisch zurück. Alle Funktionen arbeiten gleich.

### Unterstützt der Bot Rechts-nach-Links (RTL) Sprachen?
Ja. Arabisch, Persisch und Urdu werden unterstützt. Telegram übernimmt das RTL-Rendering.

### Kann ich eine neue Sprache anfragen?
Der Bot unterstützt 16 Sprachen. Weitere hängen von den Maintainern ab. Der Englisch-Fallback stellt sicher, dass alle ihn nutzen können.

### Wird die Sprache gespeichert oder woanders gesendet?
Nein. Der Bot liest `language_code` aus jedem Update und nutzt ihn nur zur Auswahl der Antwortstrings. Er wird nicht gespeichert oder geteilt.
