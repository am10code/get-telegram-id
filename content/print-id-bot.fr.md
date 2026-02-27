+++
title = "print_id_bot : Telegram ID et chat_id (commandes, langues, fonctionnalités)"
description = "Référence complète pour @print_id_bot : commandes, 16 langues, déclencheurs en groupe et fonctionnalités développeur (/json, /dump). Obtenez votre Telegram user ID et chat_id en secondes."
cta = { text = "Ouvrez le bot pour obtenir votre Telegram user ID et chat_id instantanément.", label = "Open @print_id_bot", url = "https://t.me/print_id_bot" }
+++

@print_id_bot est un bot Telegram qui affiche votre **Telegram user ID**, **chat_id** (pour les groupes et supergroupes) et l'ID de canal. Il fonctionne en chat privé et en groupes, avec des réponses en 16 langues selon le paramètre de langue Telegram.

## Commandes

| Commande | Fonction |
|----------|----------|
| `/start` | Message de bienvenue, votre User ID et Chat ID, boutons inline pour /id et /help |
| `/id` | Votre User ID et Chat ID (réponse courte) |
| `/help` | Texte d'aide complet et liste des commandes |
| `/json` | Message actuel en JSON (pour les développeurs) |
| `/dump` | Détail complet de l'update et JSON brut (chat privé uniquement) |

En chat privé, l'envoi de tout message (texte, photo, sticker, etc.) renvoie également votre User ID et Chat ID. Pour les messages transférés, le bot affiche l'ID de l'auteur quand disponible, ou « ID hidden » si les paramètres de confidentialité de l'expéditeur le bloquent. Voir [messages transférés et IDs cachés]({{< relref "telegram-forwarded-message-id.md" "en" >}}) pour les détails.

## Langues supportées (16)

Le bot choisit la langue de réponse selon votre `language_code` Telegram. Supportées : anglais, russe, persan, ouzbek, hindi, chinois, turc, portugais, espagnol, arabe, indonésien, allemand, ourdou, français, tagalog, amharique. Les codes non supportés basculent sur l'anglais. Voir [comment fonctionne la sélection de langue]({{< relref "telegram-id-bot-languages.md" "en" >}}).

## Comportement en groupe et supergroupe

En groupe, le bot ne répond que lorsque vous :

- Répondez au message du bot
- Envoyez `/id` ou `/help` (avec ou sans @print_id_bot)
- Envoyez une commande avec @print_id_bot (ex. `/foo@print_id_bot`)
- Mentionnez @print_id_bot dans votre message

Sinon il reste silencieux. Lors de l'ajout à un groupe, il envoie un message de bienvenue avec le nom du groupe et le chat_id. Voir [ajouter un bot au groupe pour obtenir le chat_id]({{< relref "add-bot-to-group-chat-id.md" "en" >}}) pour un guide rapide.

## Fonctionnalités développeur

- **/json** — Retourne le message actuel en JSON.
- **/dump** — Détail complet de l'update et JSON brut (chat privé uniquement). Utile pour déboguer les intégrations Bot API. Voir [inspecter le JSON d'update Telegram]({{< relref "telegram-json-update.md" "en" >}}).

## Pages connexes

- [Obtenir le Telegram user ID (méthodes sûres)]({{< relref "get-telegram-user-id.md" "en" >}})
- [Comment obtenir le chat_id d'un groupe Telegram]({{< relref "get-telegram-chat-id.md" "en" >}})
- [Comment trouver votre Telegram ID]({{< relref "how-to-find-telegram-id.md" "en" >}})

## FAQ

### Le bot fonctionne-t-il dans les canaux ?
Le bot fonctionne en chat privé et dans les groupes/supergroupes. Pour les canaux, l'ID de canal provient d'un autre flux (ex. publier en tant que canal et utiliser un bot qui reçoit les updates). Voir [obtenir l'ID de canal Telegram pour Bot API]({{< relref "how-to-get-channel-id-bot-api.md" "en" >}}).

### Puis-je obtenir le Telegram user ID de quelqu'un d'autre ?
Le bot affiche votre propre ID ou le chat_id des chats où vous êtes. Pour les messages transférés, il affiche l'ID de l'expéditeur uniquement s'il autorise le transfert ; sinon « ID hidden ». Vous ne pouvez pas rechercher un ID par numéro de téléphone ou username. Voir [Telegram ID vs username]({{< relref "telegram-id-vs-username.md" "en" >}}).

### Pourquoi le bot ne répond-il pas dans mon groupe ?
Le bot ne répond que lorsque vous lui répondez, envoyez /id ou /help, ou mentionnez @print_id_bot. Voir [bot ne répond pas en groupe]({{< relref "bot-not-responding-in-group.md" "en" >}}) pour une liste complète.

### Le bot est-il gratuit ?
Oui. Aucune inscription ni paiement requis.

### Quelle est la différence entre user ID et chat_id ?
**User ID** identifie un compte Telegram. **chat_id** identifie une conversation (chat privé, groupe, supergroupe, canal). Voir [Telegram ID vs username]({{< relref "telegram-id-vs-username.md" "en" >}}).
