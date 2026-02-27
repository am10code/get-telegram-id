+++
title = "Guias de Telegram user ID"
description = "Guias para encontrar, copiar e entender o seu Telegram user ID. Métodos seguros, dicas de privacidade e perguntas frequentes."
cta = { text = "Obtenha o seu Telegram user ID instantaneamente.", label = "Open @print_id_bot", url = "https://t.me/print_id_bot" }
+++

O seu **Telegram user ID** é um identificador numérico da sua conta. É estável, atribuído uma vez e não é mostrado em nenhum lugar na app do Telegram. Bots e integrações só podem lê-lo quando você interage com eles — por exemplo, ao abrir um bot e tocar em Iniciar, ou enviar uma mensagem. Este hub reúne guias para ajudá-lo a encontrar, copiar e entender o seu user ID em segurança.

Não é possível obter o ID de outra pessoa apenas pelo número de telefone ou username. Serviços que prometem «pesquisa de ID por telefone» são frequentemente fraudes ou violam a privacidade. Os ID são obtidos apenas através de interação: quando um utilizador abre um bot, reencaminha uma mensagem (se permitir) ou participa num chat a que tem acesso.

## Guias

- **[Como encontrar o seu Telegram ID]({{< relref "how-to-find-telegram-id.md" >}})** — Métodos passo a passo para obter o seu user ID. A forma mais rápida é usar um bot: abra-o, toque em Iniciar e copie o número.

- **[Obter Telegram user ID (métodos seguros)]({{< relref "get-telegram-user-id.md" >}})** — Formas seguras de obter o seu ID: via bot, enviando uma mensagem ou reencaminhando (com limites de privacidade). O que não pode fazer e porquê.

- **[Telegram ID vs username: qual é a diferença?]({{< relref "telegram-id-vs-username.md" >}})** — Os ID são numéricos e estáveis; os username são opcionais e alteráveis. Quando precisa de um ID para Bot API ou integrações.

- **[Como copiar e partilhar o seu Telegram ID em segurança]({{< relref "how-to-copy-telegram-id.md" >}})** — Toque para copiar do bot, partilhe com segurança e evite fraudes. Dicas de privacidade ao partilhar o seu ID.

- **[Por que o Telegram não mostra o seu ID numérico (e o que fazer)]({{< relref "telegram-id-not-in-ui.md" >}})** — O Telegram oculta o seu ID numérico na app. Por que está oculto e como obtê-lo quando precisar.

- **[Mensagens reencaminhadas no Telegram: por que os ID podem estar ocultos]({{< relref "telegram-forwarded-message-id.md" >}})** — Ao reencaminhar uma mensagem para um bot, o ID do remetente pode aparecer ou «ID hidden» se tiver definições de privacidade que bloqueiam o reencaminhamento.

## FAQ

### O meu Telegram ID é privado?

O seu Telegram ID não é mostrado publicamente na interface do Telegram, mas bots e apps podem lê-lo quando interage com eles. Você controla quem o obtém escolhendo quais bots e apps usa.

### Posso obter o ID de outra pessoa por número de telefone ou username?

Não. Não pode obter de forma fiável um Telegram user ID apenas pelo número de telefone ou username. Os ID são obtidos apenas quando o utilizador interage com um bot ou app, ou reencaminha uma mensagem (e permite o reencaminhamento). Evite serviços que afirmem o contrário.

### Qual é a diferença entre user ID e chat_id?

**User ID** identifica uma conta Telegram. **chat_id** identifica uma conversa (chat privado, grupo, supergrupo, canal). Num chat privado, user ID e chat_id são o mesmo número.
