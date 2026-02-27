+++
title = "Bot de Telegram ID em 16 idiomas: como funciona a seleção de idioma"
description = "Como @print_id_bot escolhe o idioma de resposta pelo seu language_code do Telegram. 16 idiomas suportados, fallback para inglês. Russo, persa, árabe e mais."
cta = { text = "Abra @print_id_bot — ele responde no idioma do seu Telegram.", label = "Open @print_id_bot", url = "https://t.me/print_id_bot" }
+++

@print_id_bot responde em **16 idiomas** com base na configuração de idioma do Telegram. Não é necessário seleção manual.

## Como funciona

O bot lê seu **language_code** do update (de `message.from.language_code`, `edited_message.from.language_code` ou `callback_query.from.language_code`). Usa a primeira parte do código (ex.: `pt-BR` → `pt`) e mapeia para um locale suportado. Códigos não suportados têm fallback para **inglês**.

## Idiomas suportados (16)

| Código | Idioma |
|--------|--------|
| `en` | Inglês |
| `ru` | Russo |
| `fa` | Persa |
| `uz` | Uzbeque |
| `hi` | Hindi |
| `zh` | Chinês |
| `tr` | Turco |
| `pt` | Português |
| `es` | Espanhol |
| `ar` | Árabe |
| `id` | Indonésio |
| `de` | Alemão |
| `ur` | Urdu |
| `fr` | Francês |
| `tl` | Tagalo (filipino; `fil` mapeia para `tl`) |
| `am` | Amárico |

## Casos especiais

- **Filipino** — Telegram envia `fil`; o bot mapeia para `tl` (tagalo).
- **Português (Brasil)** — `pt-BR` usa `pt` (português).
- **Chinês** — `zh-CN`, `zh-TW` usam `zh` (chinês).

## O que está localizado

Todas as respostas do bot: texto de boas-vindas, rótulos (User ID, Chat ID, nome do grupo), texto de ajuda, botões e mensagens como "ID hidden" ou "Toque no número para copiar". O JSON bruto em /json e /dump não muda; só os rótulos legíveis usam seu idioma.

## Páginas relacionadas

- [Usar @print_id_bot se você não fala inglês]({{< relref "telegram-id-bot-for-non-english.md" "en" >}})
- [print_id_bot: comandos, idiomas, recursos]({{< relref "print-id-bot.md" "en" >}})
- [Obter Telegram user ID (métodos seguros)]({{< relref "get-telegram-user-id.md" "en" >}})

## FAQ

### Como mudo o idioma do bot?
Altere o idioma do app Telegram em Configurações → Idioma. O bot usa isso. Não há seletor de idioma no bot.

### E se meu idioma não for suportado?
O bot faz fallback para inglês. Toda a funcionalidade funciona igual.

### O bot suporta idiomas da direita para a esquerda (RTL)?
Sim. Árabe, persa e urdu são suportados. O Telegram gerencia a renderização RTL.

### Posso solicitar um novo idioma?
O bot suporta 16 idiomas. Adicionar mais depende dos mantenedores. O fallback para inglês garante que todos possam usar.

### O idioma é armazenado ou enviado para outro lugar?
Não. O bot lê `language_code` de cada update e usa apenas para escolher as strings de resposta. Não é armazenado nem compartilhado.
