+++
title = "Comment obtenir le chat_id d'un groupe Telegram"
description = "Obtenez le chat_id d'un groupe ou supergroupe Telegram en quelques secondes. Ajoutez @print_id_bot, envoyez /id ou mentionnez-le et copiez le chat_id. Guide pas à pas."
cta = { text = "Ajoutez le bot à votre groupe et obtenez le chat_id en 10 secondes.", label = "Open @print_id_bot", url = "https://t.me/print_id_bot" }
+++

Le **chat_id** d'un groupe ou supergroupe Telegram est nécessaire pour les intégrations Bot API. Voici comment l'obtenir rapidement.

## Étape 1 : Ajoutez le bot à votre groupe

1. Ouvrez [@print_id_bot](https://t.me/print_id_bot) dans Telegram.
2. Appuyez sur **Démarrer**.
3. Ajoutez le bot au groupe : ouvrez le groupe → Ajouter des membres → recherchez `print_id_bot` → Ajouter.

Quand le bot est ajouté, il envoie un message de bienvenue avec le nom du groupe et le **chat_id**. Vous pouvez le copier depuis là.

## Étape 2 : Si vous devez le récupérer

Le bot répond dans les groupes uniquement quand :

- vous répondez au message du bot ;
- vous envoyez `/id` ou `/help` (avec ou sans @print_id_bot) ;
- vous envoyez une commande avec @print_id_bot (ex. `/foo@print_id_bot`) ;
- vous mentionnez @print_id_bot dans un message.

Envoyez `/id` ou mentionnez @print_id_bot, et le bot répondra avec le nom du groupe et le chat_id. Appuyez sur le nombre pour copier.

## Groupe vs supergroupe : chat_id

Les ID de groupes et supergroupes sont souvent **négatifs**. C'est normal. Quand un groupe devient supergroupe, le chat_id peut changer. Voir [chat_id groupe vs supergroupe]({{< relref "telegram-group-chat-id-vs-supergroup.md" "en" >}}) pour les détails.

## Dépannage

Si le bot ne répond pas, vérifiez :

- que le bot a la permission de lire les messages ;
- que vous l'avez bien déclenché (réponse, /id, /help ou @print_id_bot) ;
- que le bot n'est pas en mode confidentialité bloquant les messages de groupe (le cas échéant).

Liste complète : [le bot ne répond pas dans un groupe Telegram]({{< relref "bot-not-responding-in-group.md" "en" >}}).

## Pages connexes

- [Ajouter un bot à un groupe pour obtenir le chat_id (10 secondes)]({{< relref "add-bot-to-group-chat-id.md" "en" >}})
- [Telegram Bot API : comment obtenir le chat_id]({{< relref "telegram-bot-api-chat-id.md" "en" >}})
- [Pourquoi le chat_id Telegram peut être négatif]({{< relref "telegram-chat-id-negative.md" "en" >}})

## FAQ

### Pourquoi le chat_id de mon groupe est-il négatif ?
Les ID de groupes et supergroupes sont typiquement négatifs dans la Telegram Bot API. C'est voulu. Voir [format du chat_id Telegram]({{< relref "telegram-chat-id-format.md" "en" >}}).

### Puis-je obtenir le chat_id du groupe de quelqu'un d'autre ?
Seulement des groupes dont vous êtes membre. Ajoutez le bot au groupe et envoyez /id ou mentionnez-le.

### Le bot fonctionne-t-il dans les supergroupes ?
Oui. Groupes et supergroupes sont supportés. Le bot affiche le nom du groupe et le chat_id. Voir [chat_id groupe vs supergroupe]({{< relref "telegram-group-chat-id-vs-supergroup.md" "en" >}}).

### Et si le bot a été retiré du groupe ?
Ajoutez-le à nouveau. À l'ajout, il envoie un message de bienvenue avec le chat_id. Vous pouvez aussi l'obtenir en envoyant /id ou en mentionnant @print_id_bot.

### Le chat_id est-il le même pour groupe et supergroupe ?
Après migration en supergroupe, le chat_id peut changer. Utilisez toujours la valeur actuelle du bot ou de l'API.
