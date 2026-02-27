+++
title = "Obter ID do Telegram"
description = "Obtenha seu Telegram user ID e chat_id de grupo em segundos. O bot @print_id_bot funciona em chat privado e grupos. Seguro e gratuito."
cta = { url = "https://t.me/print_id_bot", label = "Open @print_id_bot" }
+++

O **Telegram user ID** é o identificador numérico da sua conta. Você precisa dele para integrações, bots e desenvolvimento. Ele não aparece na interface do Telegram, mas você pode obtê-lo em segundos com o bot @print_id_bot. Mais detalhes sobre métodos seguros nas [guias de user ID]({{< relref "user-id-guides.md" >}}).

## Como obter seu Telegram user ID no privado

Abra o bot @print_id_bot em um chat privado e toque em **Iniciar**. O bot retornará imediatamente seu **Telegram user ID**, seu username (se tiver) e o chat_id. Não é preciso mais nada: basta copiar o número da mensagem.

No privado, o bot responde a qualquer mensagem: texto, foto, figurinha ou o comando `/id`. Envie o que quiser e receberá seu ID. É privado: só você vê a resposta.

## Como obter o chat_id de um grupo

Para obter o **chat_id** de um grupo ou supergrupo, adicione @print_id_bot ao grupo. Após adicionar, o bot enviará uma mensagem de boas-vindas com o nome do grupo e o chat_id.

Em grupos, o bot só responde **quando você faz certas ações**. Para obter o chat_id, faça uma das seguintes:

- Envie o comando **/id** ou **/help** (com @print_id_bot ou sem)
- Responda a uma mensagem do bot
- Mencione **@print_id_bot** na sua mensagem
- Envie qualquer comando com @print_id_bot (por exemplo, `/foo@print_id_bot`)

Mensagens normais sem mencionar o bot não geram resposta: assim o bot evita spam. Os ID de grupos e supergrupos costumam ser negativos; é normal.

## Por onde começar

- [Guias de Telegram user ID]({{< relref "user-id-guides.md" >}}) — como encontrar, copiar e entender seu user ID
- [Guias de chat_id]({{< relref "chat-id-guides.md" >}}) — obter chat_id de grupos e supergrupos
- [Guias de Bot API]({{< relref "bot-api-guides.md" >}}) — integração com Telegram Bot API

## FAQ

### Meu Telegram ID é privado?

Seu Telegram ID não é exibido publicamente no app. Bots e aplicativos só o obtêm quando você interage com eles — por exemplo, ao abrir um bot e tocar em Iniciar. Você decide em quais bots confiar.

### Por que o bot não responde no grupo?

O bot só responde quando você responde à mensagem dele, envia /id ou /help, ou menciona @print_id_bot. Mensagens normais sem esses gatilhos ele ignora. Verifique se o bot está no grupo e pode ler mensagens.

### Qual a diferença entre user ID e chat_id?

O **user ID** identifica sua conta no Telegram. O **chat_id** identifica o chat: privado, grupo, supergrupo ou canal. No chat privado, user ID e chat_id são o mesmo número. Em grupos, o chat_id costuma ser negativo.
