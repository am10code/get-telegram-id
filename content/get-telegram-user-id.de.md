+++
title = "Telegram User ID erhalten (sichere Methoden)"
description = "So erhältst du deine Telegram User ID sicher. Schritt-für-Schritt-Methoden mit @print_id_bot. Keine Entwicklertools nötig. Funktioniert auf Mobil und Desktop."
cta = { text = "Bot öffnen und Start antippen — deine Telegram User ID wird sofort angezeigt.", label = "Open @print_id_bot", url = "https://t.me/print_id_bot" }
+++

Deine **Telegram User ID** ist ein numerischer Identifier für dein Konto. Sie wird in der Telegram-App nicht angezeigt, aber Bots und Integrationen können sie lesen, wenn du mit ihnen interagierst. Hier sind sichere Wege, sie zu erhalten.

## Methode 1: @print_id_bot verwenden (am schnellsten)

1. Öffne [@print_id_bot](https://t.me/print_id_bot) in Telegram.
2. Tippe auf **Start**.
3. Der Bot antwortet mit deiner **User ID** und **Chat ID** (im Privatchat sind sie gleich).
4. Tippe auf die Zahl, um sie zu kopieren.

Der Bot antwortet in 16 Sprachen basierend auf deiner Telegram-Spracheinstellung. Nicht unterstützte Sprachen fallen auf Englisch zurück.

## Methode 2: Beliebige Nachricht an den Bot senden

Im Privatchat mit @print_id_bot sende eine beliebige Nachricht, ein Foto, einen Sticker oder ein Dokument. Der Bot antwortet mit deiner User ID und Chat ID. Du kannst auch `/id` für eine kurze Antwort verwenden.

## Methode 3: Nachricht weiterleiten (und Einschränkungen)

Wenn du eine Nachricht von einem anderen Nutzer an @print_id_bot weiterleitest, kann der Bot die User ID des ursprünglichen Absenders anzeigen. Hat der Absender jedoch Privatsphäre-Einstellungen, die die ID beim Weiterleiten verbergen, siehst du "ID hidden". Du kannst die ID einer anderen Person nicht zuverlässig per Telefonnummer oder Username ermitteln. Details: [weitergeleitete Nachrichten und versteckte IDs]({{< relref "telegram-forwarded-message-id.md" "en" >}}).

## Was du nicht tun kannst

- **Per Telefonnummer suchen**: Du kannst eine Telegram User ID nicht allein aus einer Telefonnummer ermitteln. Dienste, die das behaupten, sind oft Betrug oder verletzen die Privatsphäre.
- **Per Username suchen**: Usernames sind keine IDs. Der Nutzer muss mit einem Bot oder einer App interagieren, um die ID zu erhalten.
- **IDs anderer ohne Interaktion sehen**: Du kannst nur IDs von Chats erhalten, in denen du bist, oder von Nutzern, die dir weitergeleitete Nachrichten schicken (und die Weiterleitung erlauben).

## Verwandte Seiten

- [Telegram ID vs Username: Was ist der Unterschied?]({{< relref "telegram-id-vs-username.md" "en" >}})
- [Warum Telegram deine numerische ID nicht anzeigt]({{< relref "telegram-id-not-in-ui.md" "en" >}})
- [print_id_bot: Befehle, Sprachen, Funktionen]({{< relref "print-id-bot.md" "en" >}})

## FAQ

### Ist meine Telegram User ID privat?
Sie wird in der Telegram-Oberfläche nicht angezeigt, aber Bots und Apps können sie lesen, wenn du mit ihnen interagierst. Teile sie nicht mit nicht vertrauenswürdigen Diensten.

### Kann ich meine Telegram User ID ändern?
Nein. Sie wird einmal zugewiesen und ändert sich nicht.

### Warum zeigt der Bot bei weitergeleiteten Nachrichten "ID hidden"?
Der Absender hat Privatsphäre-Einstellungen aktiviert, die die ID beim Weiterleiten verbergen. Siehe [weitergeleiteter Absender-ID versteckt]({{< relref "telegram-privacy-forwarded-id-hidden.md" "en" >}}).

### Ist die Nutzung von @print_id_bot sicher?
Ja. Der Bot zeigt nur IDs an, zu denen du bereits Zugang hast (deine eigene oder aus Chats, in denen du bist). Er speichert oder teilt deine Daten nicht über das hinaus, was Telegram bereitstellt.

### Wie sieht eine Telegram User ID aus?
Es ist ein numerischer Wert, oft 9–10 Ziffern. Beispiel: `123456789`.
