+++
title = "Guides Telegram Bot API chat_id"
description = "Guides développeur pour Telegram Bot API chat_id : obtenir chat_id, corriger 'chat not found', inspecter les updates et exemples par bibliothèque."
cta = { text = "Obtenez chat_id instantanément avec @print_id_bot.", label = "Open @print_id_bot", url = "https://t.me/print_id_bot" }
+++

Le **chat_id** est requis pour la plupart des méthodes de l'API Bot Telegram : sendMessage, sendPhoto, editMessageText et bien d'autres. Il identifie la destination — un chat privé (utilisateur), un groupe, un supergroupe ou un canal. Dans un chat privé, chat_id équivaut au Telegram user ID de l'utilisateur (positif). Pour les groupes et supergroupes, chat_id est typiquement négatif. Ce hub rassemble des guides développeur pour obtenir chat_id, corriger les erreurs courantes et l'utiliser dans des bibliothèques populaires.

Vous pouvez obtenir chat_id en faisant interagir les utilisateurs avec votre bot (ou un bot auxiliaire comme @print_id_bot) et en le lisant dans les updates. Pour les webhooks, inspectez le JSON de l'update entrant pour extraire `chat.id`. La commande `/dump` dans @print_id_bot affiche la structure complète de l'update pour le débogage.

## Guides

- **[Telegram Bot API : comment obtenir chat_id]({{< relref "telegram-bot-api-chat-id.md" >}})** — Obtenir chat_id pour chat privé, groupe, supergroupe et canal. Utilisez @print_id_bot ou votre propre webhook.

- **[Telegram Bot API 'chat not found' : causes courantes]({{< relref "chat-not-found-telegram-bot.md" >}})** — Bot supprimé du chat, chat_id incorrect, migration vers supergroupe. Comment corriger et obtenir le chat_id correct.

- **[Telegram update JSON : comment inspecter la sortie /dump]({{< relref "telegram-json-update.md" >}})** — Inspecter la structure brute de l'update. Utile pour déboguer les webhooks et comprendre les champs message, chat et user.

- **[Aiogram : obtenir chat_id et user ID (exemples)]({{< relref "aiogram-get-chat-id.md" >}})** — Exemples Python Aiogram : extraire chat_id et user ID des updates.

- **[Telegraf (Node.js) : obtenir chat_id et user ID]({{< relref "telegraf-get-chat-id.md" >}})** — Exemples Node.js Telegraf : obtenir chat_id et user ID du contexte.

- **[python-telegram-bot : obtenir user ID et chat_id]({{< relref "python-telegram-bot-user-id.md" >}})** — Bibliothèque python-telegram-bot : extraire user ID et chat_id des updates.

- **[Go Telegram Bot API : obtenir chat_id]({{< relref "go-telegram-bot-api-chat-id.md" >}})** — Go : obtenir chat_id des updates entrants pour votre bot.

## FAQ

### Pourquoi j'obtiens « chat not found » ?

Causes courantes : le bot a été supprimé du chat, vous utilisez un chat_id incorrect ou obsolète, ou le groupe a été mis à niveau en supergroupe (chat_id peut changer). Réajoutez le bot, obtenez le chat_id actuel avec @print_id_bot et assurez-vous d'utiliser la bonne valeur.

### Comment déboguer mes webhook updates ?

Utilisez la commande `/dump` dans @print_id_bot (en chat privé) pour voir le JSON complet de l'update. Elle affiche la structure de message, chat, user et autres champs. Comparez avec le payload de votre webhook pour trouver où se trouvent chat_id et user ID.

### Quel guide de bibliothèque utiliser ?

Choisissez le guide qui correspond à votre stack : Aiogram et python-telegram-bot pour Python, Telegraf pour Node.js, et le guide Go pour Go. Le guide général Bot API s'applique à tout langage.
