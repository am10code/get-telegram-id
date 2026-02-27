+++
title = "Bot Telegram ID en 16 langues : comment fonctionne la sélection de langue"
description = "Comment @print_id_bot choisit la langue de réponse selon votre language_code Telegram. 16 langues supportées, repli sur l'anglais. Russe, persan, arabe et plus."
cta = { text = "Ouvrez @print_id_bot — il répond dans la langue de votre Telegram.", label = "Open @print_id_bot", url = "https://t.me/print_id_bot" }
+++

@print_id_bot répond en **16 langues** selon la langue configurée dans Telegram. Aucune sélection manuelle nécessaire.

## Comment ça marche

Le bot lit votre **language_code** dans l'update (`message.from.language_code`, `edited_message.from.language_code` ou `callback_query.from.language_code`). Il utilise la première partie du code (ex. `pt-BR` → `pt`) et le mappe à une locale supportée. Les codes non supportés basculent sur **l'anglais**.

## Langues supportées (16)

| Code | Langue |
|------|--------|
| `en` | Anglais |
| `ru` | Russe |
| `fa` | Persan |
| `uz` | Ouzbek |
| `hi` | Hindi |
| `zh` | Chinois |
| `tr` | Turc |
| `pt` | Portugais |
| `es` | Espagnol |
| `ar` | Arabe |
| `id` | Indonésien |
| `de` | Allemand |
| `ur` | Urdu |
| `fr` | Français |
| `tl` | Tagalog (filipino ; `fil` mappe vers `tl`) |
| `am` | Amharique |

## Cas particuliers

- **Filipino** — Telegram envoie `fil` ; le bot mappe vers `tl` (tagalog).
- **Portugais (Brésil)** — `pt-BR` utilise `pt` (portugais).
- **Chinois** — `zh-CN`, `zh-TW` utilisent `zh` (chinois).

## Ce qui est localisé

Toutes les réponses du bot : texte de bienvenue, libellés (User ID, Chat ID, nom du groupe), aide, boutons et messages comme "ID hidden" ou "Appuyez sur le nombre pour copier". Le JSON brut dans /json et /dump ne change pas ; seuls les libellés lisibles utilisent votre langue.

## Pages connexes

- [Utiliser @print_id_bot si vous ne parlez pas anglais]({{< relref "telegram-id-bot-for-non-english.md" "en" >}})
- [print_id_bot : commandes, langues, fonctionnalités]({{< relref "print-id-bot.md" "en" >}})
- [Obtenir le Telegram user ID (méthodes sûres)]({{< relref "get-telegram-user-id.md" "en" >}})

## FAQ

### Comment changer la langue du bot ?
Changez la langue de l'app Telegram dans Paramètres → Langue. Le bot l'utilise. Pas de sélecteur de langue dans le bot.

### Et si ma langue n'est pas supportée ?
Le bot bascule sur l'anglais. Toutes les fonctionnalités marchent pareil.

### Le bot supporte-t-il les langues droite-à-gauche (RTL) ?
Oui. Arabe, persan et urdu sont supportés. Telegram gère le rendu RTL.

### Puis-je demander une nouvelle langue ?
Le bot supporte 16 langues. En ajouter dépend des mainteneurs. Le repli sur l'anglais assure que tout le monde peut l'utiliser.

### La langue est-elle stockée ou envoyée ailleurs ?
Non. Le bot lit `language_code` dans chaque update et l'utilise uniquement pour choisir les chaînes de réponse. Ce n'est pas stocké ni partagé.
