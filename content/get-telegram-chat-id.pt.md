+++
title = "Como obter o chat_id de um grupo no Telegram"
description = "Obtenha o chat_id de um grupo ou supergrupo do Telegram em segundos. Adicione @print_id_bot, envie /id ou mencione-o e copie o chat_id. Guia passo a passo."
cta = { text = "Adicione o bot ao seu grupo e obtenha o chat_id em 10 segundos.", label = "Open @print_id_bot", url = "https://t.me/print_id_bot" }
+++

O **chat_id** de um grupo ou supergrupo do Telegram é necessário para integrações com a Bot API. Aqui está como obtê-lo rapidamente.

## Passo 1: Adicione o bot ao seu grupo

1. Abra [@print_id_bot](https://t.me/print_id_bot) no Telegram.
2. Toque em **Iniciar**.
3. Adicione o bot ao grupo: abra o grupo → Adicionar membros → procure por `print_id_bot` → Adicionar.

Quando o bot é adicionado, ele envia uma mensagem de boas-vindas com o nome do grupo e o **chat_id**. Você pode copiá-lo de lá.

## Passo 2: Se precisar obter novamente

O bot responde em grupos apenas quando:

- você responde à mensagem do bot;
- você envia `/id` ou `/help` (com ou sem @print_id_bot);
- você envia qualquer comando com @print_id_bot (ex.: `/foo@print_id_bot`);
- você menciona @print_id_bot em uma mensagem.

Envie `/id` ou mencione @print_id_bot, e o bot responderá com o nome do grupo e o chat_id. Toque no número para copiar.

## Grupo vs supergrupo: chat_id

Os IDs de grupos e supergrupos costumam ser **números negativos**. Isso é normal. Quando um grupo é atualizado para supergrupo, o chat_id pode mudar. Veja [chat_id de grupo vs supergrupo]({{< relref "telegram-group-chat-id-vs-supergroup.md" "en" >}}) para detalhes.

## Solução de problemas

Se o bot não responder, verifique:

- que o bot tenha permissão para ler mensagens;
- que você o tenha ativado corretamente (resposta, /id, /help ou @print_id_bot);
- que o bot não esteja em modo privacidade bloqueando mensagens de grupo (se aplicável).

Veja [bot não responde em grupo do Telegram]({{< relref "bot-not-responding-in-group.md" "en" >}}) para a lista completa.

## Páginas relacionadas

- [Adicionar um bot a um grupo para obter chat_id (10 segundos)]({{< relref "add-bot-to-group-chat-id.md" "en" >}})
- [Telegram Bot API: como obter chat_id]({{< relref "telegram-bot-api-chat-id.md" "en" >}})
- [Por que o chat_id do Telegram pode ser negativo]({{< relref "telegram-chat-id-negative.md" "en" >}})

## FAQ

### Por que o chat_id do meu grupo é negativo?
Os IDs de grupos e supergrupos costumam ser negativos na Telegram Bot API. É por design. Veja [formato de chat_id no Telegram]({{< relref "telegram-chat-id-format.md" "en" >}}).

### Posso obter o chat_id do grupo de outra pessoa?
Apenas de grupos dos quais você é membro. Adicione o bot ao grupo e envie /id ou mencione-o.

### O bot funciona em supergrupos?
Sim. Grupos e supergrupos são suportados. O bot mostra o nome do grupo e o chat_id. Veja [chat_id de grupo vs supergrupo]({{< relref "telegram-group-chat-id-vs-supergroup.md" "en" >}}).

### E se o bot foi removido do grupo?
Adicione-o novamente. Ao adicionar, ele envia uma mensagem de boas-vindas com o chat_id. Você também pode obtê-lo enviando /id ou mencionando @print_id_bot.

### O chat_id é o mesmo para grupo e supergrupo?
Após a migração para supergrupo, o chat_id pode mudar. Use sempre o valor atual do bot ou da API.
