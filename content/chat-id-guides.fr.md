+++
title = "Guides Telegram chat_id (groupes et supergroupes)"
description = "Guides pour obtenir et comprendre le chat_id Telegram des groupes et supergroupes. Ajoutez un bot, copiez chat_id, résolvez les problèmes courants."
cta = { text = "Ajoutez @print_id_bot à votre groupe et obtenez chat_id en quelques secondes.", label = "Open @print_id_bot", url = "https://t.me/print_id_bot" }
+++

Le **chat_id** d'un groupe ou supergroupe Telegram est requis pour les intégrations Bot API : envoyer des messages, gérer les membres ou créer des automatisations. Contrairement à votre user ID, les chat_ids des groupes et supergroupes sont souvent des **nombres négatifs** — c'est normal et voulu. Ce hub rassemble des guides pour vous aider à obtenir et comprendre le chat_id des groupes et supergroupes.

La façon la plus rapide d'obtenir le chat_id d'un groupe est d'ajouter un bot comme @print_id_bot. Une fois ajouté, il envoie un message de bienvenue avec le nom du groupe et le chat_id. Vous pouvez aussi envoyer `/id` ou mentionner le bot pour l'obtenir à nouveau. Le bot répond uniquement quand vous lui répondez, envoyez une commande ou le mentionnez — pas à chaque message.

## Guides

- **[Comment obtenir le chat_id Telegram pour un groupe]({{< relref "get-telegram-chat-id.md" >}})** — Étape par étape : ajoutez le bot, obtenez le message de bienvenue ou utilisez `/id`. Comportement du bot dans les groupes.

- **[Ajouter un bot à un groupe pour obtenir chat_id (10 secondes)]({{< relref "add-bot-to-group-chat-id.md" >}})** — Guide rapide : ouvrez le bot, ajoutez-le à votre groupe et copiez le chat_id du message de bienvenue.

- **[Format du chat_id Telegram expliqué (avec exemples)]({{< relref "telegram-chat-id-format.md" >}})** — À quoi ressemble le chat_id pour chat privé, groupe, supergroupe et canal. Exemples et structure.

- **[Pourquoi le chat_id Telegram peut être négatif]({{< relref "telegram-chat-id-negative.md" >}})** — Les ID des groupes et supergroupes sont typiquement négatifs. Pourquoi et quand c'est important pour votre intégration.

- **[chat_id groupe vs supergroupe : différences clés]({{< relref "telegram-group-chat-id-vs-supergroup.md" >}})** — Quand un groupe est mis à niveau en supergroupe, le chat_id peut changer. À quoi s'attendre et comment gérer.

- **[Le bot ne répond pas dans un groupe Telegram : checklist]({{< relref "bot-not-responding-in-group.md" >}})** — Le bot reste silencieux ? Checklist : répondez au bot, utilisez `/id`, mentionnez-le et vérifiez les permissions.

## FAQ

### Pourquoi le chat_id de mon groupe est-il négatif ?

Les chat_ids des groupes et supergroupes sont typiquement négatifs dans l'API Bot Telegram. C'est voulu pour les distinguer des user IDs (positifs en chat privé). C'est normal et attendu.

### Que faire si le bot ne répond pas dans mon groupe ?

Les bots dans les groupes répondent souvent uniquement quand vous leur répondez, envoyez `/id` ou `/help`, ou les mentionnez (ex. @print_id_bot). S'il reste silencieux, vérifiez que le bot a la permission de lire les messages et que le mode confidentialité (le cas échéant) lui permet de voir les messages du groupe.

### Le chat_id change-t-il lors du passage en supergroupe ?

Oui. Quand un groupe est mis à niveau en supergroupe, le chat_id peut changer. Si vous avez enregistré l'ancien chat_id du groupe, il peut ne plus fonctionner. Ajoutez le bot à nouveau et obtenez le nouveau chat_id du message de bienvenue ou `/id`.
