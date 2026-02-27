+++
title = "Obtenir le Telegram user ID (méthodes sûres)"
description = "Comment obtenir votre Telegram user ID en toute sécurité. Méthodes pas à pas avec @print_id_bot. Aucun outil développeur requis. Fonctionne sur mobile et desktop."
cta = { text = "Ouvrez le bot et appuyez sur Démarrer pour voir votre Telegram user ID instantanément.", label = "Open @print_id_bot", url = "https://t.me/print_id_bot" }
+++

Votre **Telegram user ID** est un identifiant numérique de votre compte. Il n'est pas affiché dans l'app Telegram, mais les bots et intégrations peuvent le lire lorsque vous interagissez avec eux. Voici des moyens sûrs de l'obtenir.

## Méthode 1 : Utiliser @print_id_bot (le plus rapide)

1. Ouvrez [@print_id_bot](https://t.me/print_id_bot) dans Telegram.
2. Appuyez sur **Démarrer**.
3. Le bot répond avec votre **User ID** et **Chat ID** (ils sont identiques en chat privé).
4. Appuyez sur le nombre pour le copier.

Le bot répond en 16 langues selon le paramètre de langue Telegram. Les langues non supportées basculent sur l'anglais.

## Méthode 2 : Envoyer n'importe quel message au bot

En chat privé avec @print_id_bot, envoyez un message, une photo, un sticker ou un document. Le bot répond avec votre User ID et Chat ID. Vous pouvez aussi utiliser `/id` pour une réponse courte.

## Méthode 3 : Transférer un message (et limites)

Si vous transférez un message d'un autre utilisateur à @print_id_bot, le bot peut afficher le User ID de l'expéditeur d'origine. Cependant, si l'expéditeur a des paramètres de confidentialité qui masquent son ID lors du transfert, vous verrez « ID hidden ». Vous ne pouvez pas obtenir de manière fiable l'ID de quelqu'un d'autre par numéro de téléphone ou username. Voir [messages transférés et IDs cachés]({{< relref "telegram-forwarded-message-id.md" "en" >}}) pour les détails.

## Ce que vous ne pouvez pas faire

- **Rechercher par numéro de téléphone** : Vous ne pouvez pas obtenir un Telegram user ID à partir d'un numéro de téléphone seul. Les services qui le prétendent sont souvent des arnaques ou violent la confidentialité.
- **Rechercher par username** : Les usernames ne sont pas des IDs. L'utilisateur doit interagir avec un bot ou une app pour obtenir son ID.
- **Voir les IDs d'autres sans interaction** : Vous ne pouvez obtenir que les IDs de chats où vous êtes ou d'utilisateurs qui transfèrent des messages que vous recevez (et qui autorisent le transfert).

## Pages connexes

- [Telegram ID vs username : quelle est la différence ?]({{< relref "telegram-id-vs-username.md" "en" >}})
- [Pourquoi Telegram n'affiche pas votre ID numérique]({{< relref "telegram-id-not-in-ui.md" "en" >}})
- [print_id_bot : commandes, langues, fonctionnalités]({{< relref "print-id-bot.md" "en" >}})

## FAQ

### Mon Telegram user ID est-il privé ?
Il n'est pas affiché dans l'interface Telegram, mais les bots et apps peuvent le lire lorsque vous interagissez avec eux. Ne le partagez pas avec des services non fiables.

### Puis-je modifier mon Telegram user ID ?
Non. Il est attribué une fois et ne change pas.

### Pourquoi le bot affiche-t-il « ID hidden » pour les messages transférés ?
L'expéditeur a activé des paramètres de confidentialité qui masquent son ID lors du transfert. Voir [ID de l'expéditeur transféré caché]({{< relref "telegram-privacy-forwarded-id-hidden.md" "en" >}}).

### Est-il sûr d'utiliser @print_id_bot ?
Oui. Le bot n'affiche que les IDs auxquels vous avez déjà accès (le vôtre ou ceux des chats où vous êtes). Il ne stocke ni ne partage vos données au-delà de ce que Telegram fournit.

### À quoi ressemble un Telegram user ID ?
C'est une valeur numérique, souvent de 9 à 10 chiffres. Exemple : `123456789`.
