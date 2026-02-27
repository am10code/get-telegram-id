+++
title = "print_id_bot: Telegram ID e chat_id (comandos, idiomas, recursos)"
description = "Referência completa do @print_id_bot: comandos, 16 idiomas, gatilhos em grupos e recursos para desenvolvedores (/json, /dump). Obtenha seu Telegram user ID e chat_id em segundos."
cta = { text = "Abra o bot para obter seu Telegram user ID e chat_id instantaneamente.", label = "Open @print_id_bot", url = "https://t.me/print_id_bot" }
+++

@print_id_bot é um bot do Telegram que exibe seu **Telegram user ID**, **chat_id** (para grupos e supergrupos) e ID de canal. Funciona em chat privado e em grupos, com respostas em 16 idiomas conforme a configuração de idioma do Telegram.

## Comandos

| Comando | Função |
|---------|--------|
| `/start` | Mensagem de boas-vindas, seu User ID e Chat ID, botões inline para /id e /help |
| `/id` | Seu User ID e Chat ID (resposta curta) |
| `/help` | Texto de ajuda completo e lista de comandos |
| `/json` | Mensagem atual em JSON (para desenvolvedores) |
| `/dump` | Detalhamento completo do update e JSON bruto (apenas em chat privado) |

Em chat privado, enviar qualquer mensagem (texto, foto, sticker, etc.) também retorna seu User ID e Chat ID. Para mensagens encaminhadas, o bot mostra o ID do autor quando disponível, ou "ID hidden" quando as configurações de privacidade do remetente bloqueiam. Veja [mensagens encaminhadas e IDs ocultos]({{< relref "telegram-forwarded-message-id.md" "en" >}}) para detalhes.

## Idiomas suportados (16)

O bot escolhe o idioma da resposta pelo seu `language_code` no Telegram. Suportados: inglês, russo, persa, uzbeque, hindi, chinês, turco, português, espanhol, árabe, indonésio, alemão, urdu, francês, tagalo, amárico. Códigos não suportados usam inglês. Veja [como funciona a seleção de idioma]({{< relref "telegram-id-bot-languages.md" "en" >}}).

## Comportamento em grupos e supergrupos

Em grupos, o bot só responde quando você:

- Responde à mensagem do bot
- Envia `/id` ou `/help` (com ou sem @print_id_bot)
- Envia qualquer comando com @print_id_bot (ex. `/foo@print_id_bot`)
- Menciona @print_id_bot na mensagem

Caso contrário permanece em silêncio. Ao ser adicionado a um grupo, envia mensagem de boas-vindas com o nome do grupo e chat_id. Veja [adicionar um bot ao grupo para obter chat_id]({{< relref "add-bot-to-group-chat-id.md" "en" >}}) para um guia rápido.

## Recursos para desenvolvedores

- **/json** — Retorna a mensagem atual em JSON.
- **/dump** — Detalhamento completo do update e JSON bruto (apenas em chat privado). Útil para depurar integrações com Bot API. Veja [inspecionar JSON do update do Telegram]({{< relref "telegram-json-update.md" "en" >}}).

## Páginas relacionadas

- [Obter Telegram user ID (métodos seguros)]({{< relref "get-telegram-user-id.md" "en" >}})
- [Como obter chat_id de um grupo no Telegram]({{< relref "get-telegram-chat-id.md" "en" >}})
- [Como encontrar seu Telegram ID]({{< relref "how-to-find-telegram-id.md" "en" >}})

## FAQ

### O bot funciona em canais?
O bot funciona em chat privado e em grupos/supergrupos. Para canais, você precisa do ID do canal de outro fluxo (ex. publicar como canal e usar um bot que receba updates). Veja [obter ID de canal para Bot API]({{< relref "how-to-get-channel-id-bot-api.md" "en" >}}).

### Posso obter o Telegram user ID de outra pessoa?
O bot mostra seu próprio ID ou o chat_id de chats em que você participa. Para mensagens encaminhadas, mostra o ID do remetente apenas se ele permitir encaminhamento; caso contrário, "ID hidden". Não é possível buscar ID por número de telefone ou username. Veja [Telegram ID vs username]({{< relref "telegram-id-vs-username.md" "en" >}}).

### Por que o bot não responde no meu grupo?
O bot só responde quando você responde a ele, envia /id ou /help, ou menciona @print_id_bot. Veja [bot não responde no grupo]({{< relref "bot-not-responding-in-group.md" "en" >}}) para uma lista completa.

### O bot é gratuito?
Sim. Não requer cadastro nem pagamento.

### Qual a diferença entre user ID e chat_id?
**User ID** identifica uma conta do Telegram. **chat_id** identifica uma conversa (chat privado, grupo, supergrupo, canal). Veja [Telegram ID vs username]({{< relref "telegram-id-vs-username.md" "en" >}}).
