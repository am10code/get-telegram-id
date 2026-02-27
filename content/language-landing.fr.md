+++
title = "Obtenir l'ID Telegram"
description = "Obtenez votre Telegram user ID et chat_id de groupe en quelques secondes. Le bot @print_id_bot fonctionne en chat privé et en groupes. Sûr et gratuit."
cta = { url = "https://t.me/print_id_bot", label = "Open @print_id_bot" }
+++

Le **Telegram user ID** est l'identifiant numérique de votre compte. Il est nécessaire pour les intégrations, les bots et le développement. Il n'apparaît pas dans l'interface Telegram, mais vous pouvez l'obtenir en quelques secondes avec le bot @print_id_bot. Plus de détails sur les méthodes sûres dans les [guides user ID]({{< relref "user-id-guides.md" >}}).

## Comment obtenir votre Telegram user ID en privé

Ouvrez le bot @print_id_bot en chat privé et appuyez sur **Démarrer**. Le bot renverra immédiatement votre **Telegram user ID**, votre nom d'utilisateur (si vous en avez un) et le chat_id. Rien d'autre n'est nécessaire : copiez simplement le nombre du message.

En privé, le bot répond à tout message : texte, photo, autocollant ou la commande `/id`. Envoyez ce que vous voulez et vous obtiendrez votre ID. C'est privé : seul vous voyez la réponse.

## Comment obtenir le chat_id d'un groupe

Pour obtenir le **chat_id** d'un groupe ou supergroupe, ajoutez @print_id_bot au groupe. Après l'ajout, le bot enverra un message de bienvenue avec le nom du groupe et le chat_id.

Dans les groupes, le bot ne répond **que lors de certaines actions**. Pour obtenir le chat_id, faites l'une des suivantes :

- Envoyez la commande **/id** ou **/help** (avec ou sans @print_id_bot)
- Répondez à un message du bot
- Mentionnez **@print_id_bot** dans votre message
- Envoyez n'importe quelle commande avec @print_id_bot (par ex. `/foo@print_id_bot`)

Les messages normaux sans mention du bot ne déclenchent pas de réponse : ainsi le bot évite le spam. Les ID des groupes et supergroupes sont souvent négatifs ; c'est normal.

## Par où commencer

- [Guides Telegram user ID]({{< relref "user-id-guides.md" >}}) — comment trouver, copier et comprendre votre user ID
- [Guides chat_id]({{< relref "chat-id-guides.md" >}}) — obtenir le chat_id des groupes et supergroupes
- [Guides Bot API]({{< relref "bot-api-guides.md" >}}) — intégration avec Telegram Bot API

## FAQ

### Mon ID Telegram est-il privé ?

Votre ID Telegram n'est pas affiché publiquement dans l'application. Les bots et applications ne l'obtiennent que lorsque vous interagissez avec eux — par exemple en ouvrant un bot et en appuyant sur Démarrer. Vous décidez à quels bots faire confiance.

### Pourquoi le bot ne répond-il pas dans le groupe ?

Le bot ne répond que lorsque vous répondez à son message, envoyez /id ou /help, ou mentionnez @print_id_bot. Les messages normaux sans ces déclencheurs sont ignorés. Vérifiez que le bot est dans le groupe et peut lire les messages.

### Quelle est la différence entre user ID et chat_id ?

Le **user ID** identifie votre compte Telegram. Le **chat_id** identifie le chat : privé, groupe, supergroupe ou canal. En chat privé, user ID et chat_id sont le même nombre. Pour les groupes, le chat_id est souvent négatif.
