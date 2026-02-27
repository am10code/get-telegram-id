+++
title = "Obter Telegram user ID (métodos seguros)"
description = "Como obter seu Telegram user ID com segurança. Métodos passo a passo com @print_id_bot. Sem ferramentas de desenvolvedor. Funciona em mobile e desktop."
cta = { text = "Abra o bot e toque em Iniciar para ver seu Telegram user ID instantaneamente.", label = "Open @print_id_bot", url = "https://t.me/print_id_bot" }
+++

Seu **Telegram user ID** é um identificador numérico da sua conta. Não é exibido no app do Telegram, mas bots e integrações podem lê-lo quando você interage com eles. Aqui estão formas seguras de obtê-lo.

## Método 1: Usar @print_id_bot (mais rápido)

1. Abra [@print_id_bot](https://t.me/print_id_bot) no Telegram.
2. Toque em **Iniciar**.
3. O bot responde com seu **User ID** e **Chat ID** (no chat privado são iguais).
4. Toque no número para copiar.

O bot responde em 16 idiomas conforme a configuração de idioma do Telegram. Idiomas não suportados usam inglês.

## Método 2: Enviar qualquer mensagem ao bot

No chat privado com @print_id_bot, envie qualquer mensagem, foto, sticker ou documento. O bot responde com seu User ID e Chat ID. Você também pode usar `/id` para uma resposta curta.

## Método 3: Encaminhar uma mensagem (e limitações)

Se você encaminhar uma mensagem de outro usuário para @print_id_bot, o bot pode mostrar o User ID do remetente original. Porém, se o remetente tiver configurações de privacidade que ocultam o ID ao encaminhar, você verá "ID hidden". Você não pode obter de forma confiável o ID de outra pessoa por número de telefone ou username. Veja [mensagens encaminhadas e IDs ocultos]({{< relref "telegram-forwarded-message-id.md" "en" >}}) para detalhes.

## O que você não pode fazer

- **Buscar por número de telefone**: Você não pode obter um Telegram user ID apenas por número de telefone. Serviços que afirmam isso costumam ser golpes ou violar privacidade.
- **Buscar por username**: Usernames não são IDs. O usuário precisa interagir com um bot ou app para obter o ID.
- **Ver IDs de outros sem interação**: Você só pode obter IDs de chats em que participa ou de usuários que encaminham mensagens que você recebe (e que permitem encaminhamento).

## Páginas relacionadas

- [Telegram ID vs username: qual a diferença?]({{< relref "telegram-id-vs-username.md" "en" >}})
- [Por que o Telegram não mostra seu ID numérico]({{< relref "telegram-id-not-in-ui.md" "en" >}})
- [print_id_bot: comandos, idiomas, recursos]({{< relref "print-id-bot.md" "en" >}})

## FAQ

### Meu Telegram user ID é privado?
Não é exibido na interface do Telegram, mas bots e apps podem lê-lo quando você interage com eles. Não compartilhe com serviços não confiáveis.

### Posso alterar meu Telegram user ID?
Não. É atribuído uma vez e não muda.

### Por que o bot mostra "ID hidden" em mensagens encaminhadas?
O remetente ativou configurações de privacidade que ocultam o ID ao encaminhar. Veja [ID do remetente encaminhado oculto]({{< relref "telegram-privacy-forwarded-id-hidden.md" "en" >}}).

### É seguro usar @print_id_bot?
Sim. O bot só exibe IDs aos quais você já tem acesso (o seu ou de chats em que participa). Não armazena nem compartilha seus dados além do que o Telegram fornece.

### Como é um Telegram user ID?
É um valor numérico, geralmente de 9–10 dígitos. Exemplo: `123456789`.
