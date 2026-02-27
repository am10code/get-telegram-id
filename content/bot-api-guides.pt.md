+++
title = "Guias de Telegram Bot API chat_id"
description = "Guias para desenvolvedores sobre Telegram Bot API chat_id: obter chat_id, corrigir 'chat not found', inspecionar updates e exemplos por biblioteca."
cta = { text = "Obtenha chat_id instantaneamente com @print_id_bot.", label = "Open @print_id_bot", url = "https://t.me/print_id_bot" }
+++

O **chat_id** é necessário para a maioria dos métodos da Telegram Bot API: sendMessage, sendPhoto, editMessageText e muitos outros. Identifica o destino — um chat privado (utilizador), grupo, supergrupo ou canal. Num chat privado, chat_id equivale ao Telegram user ID do utilizador (positivo). Para grupos e supergrupos, chat_id é tipicamente negativo. Este hub reúne guias para desenvolvedores sobre como obter chat_id, corrigir erros comuns e usá-lo em bibliotecas populares.

Pode obter chat_id fazendo os utilizadores interagirem com o seu bot (ou um bot auxiliar como @print_id_bot) e lendo-o dos updates. Para webhooks, inspecione o JSON do update recebido para extrair `chat.id`. O comando `/dump` no @print_id_bot mostra a estrutura completa do update para depuração.

## Guias

- **[Telegram Bot API: como obter chat_id]({{< relref "telegram-bot-api-chat-id.md" >}})** — Obter chat_id para chat privado, grupo, supergrupo e canal. Use @print_id_bot ou o seu próprio webhook.

- **[Telegram Bot API 'chat not found': causas comuns]({{< relref "chat-not-found-telegram-bot.md" >}})** — Bot removido do chat, chat_id errado, migração para supergrupo. Como corrigir e obter o chat_id correto.

- **[Telegram update JSON: como inspecionar a saída de /dump]({{< relref "telegram-json-update.md" >}})** — Inspecionar a estrutura bruta do update. Útil para depurar webhooks e entender os campos message, chat e user.

- **[Aiogram: obter chat_id e user ID (exemplos)]({{< relref "aiogram-get-chat-id.md" >}})** — Exemplos em Python Aiogram: extrair chat_id e user ID dos updates.

- **[Telegraf (Node.js): obter chat_id e user ID]({{< relref "telegraf-get-chat-id.md" >}})** — Exemplos em Node.js Telegraf: obter chat_id e user ID do contexto.

- **[python-telegram-bot: obter user ID e chat_id]({{< relref "python-telegram-bot-user-id.md" >}})** — Biblioteca python-telegram-bot: extrair user ID e chat_id dos updates.

- **[Go Telegram Bot API: obter chat_id]({{< relref "go-telegram-bot-api-chat-id.md" >}})** — Go: obter chat_id dos updates recebidos para o seu bot.

## FAQ

### Por que recebo "chat not found"?

Causas comuns: o bot foi removido do chat, está a usar um chat_id errado ou desatualizado, ou o grupo foi atualizado para supergrupo (chat_id pode mudar). Adicione o bot novamente, obtenha o chat_id atual com @print_id_bot e garanta que usa o valor correto.

### Como depuro os meus webhook updates?

Use o comando `/dump` no @print_id_bot (em chat privado) para ver o JSON completo do update. Mostra a estrutura de message, chat, user e outros campos. Compare com o payload do seu webhook para encontrar onde estão chat_id e user ID.

### Qual guia de biblioteca devo usar?

Escolha a guia que corresponde ao seu stack: Aiogram e python-telegram-bot para Python, Telegraf para Node.js, e a guia Go para Go. A guia geral da Bot API aplica-se a qualquer linguagem.
