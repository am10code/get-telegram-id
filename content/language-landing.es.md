+++
title = "Obtener ID de Telegram"
description = "Obtenga su Telegram user ID y chat_id de grupo en segundos. El bot @print_id_bot funciona en chat privado y grupos. Seguro y gratuito."
cta = { url = "https://t.me/print_id_bot", label = "Open @print_id_bot" }
+++

El **Telegram user ID** es el identificador numérico de tu cuenta. Lo necesitas para integraciones, bots y desarrollo. No aparece en la interfaz de Telegram, pero puedes obtenerlo en segundos con el bot @print_id_bot. Más información sobre métodos seguros en las [guías de user ID]({{< relref "user-id-guides.md" >}}).

## Cómo obtener tu Telegram user ID en privado

Abre el bot @print_id_bot en un chat privado y pulsa **Iniciar**. El bot devolverá al instante tu **Telegram user ID**, tu username (si tienes uno) y el chat_id. No hace falta nada más: solo copia el número del mensaje.

En privado, el bot responde a cualquier mensaje: texto, foto, sticker o el comando `/id`. Envía lo que quieras y obtendrás tu ID. Es privado: solo tú ves la respuesta.

## Cómo obtener el chat_id de un grupo

Para obtener el **chat_id** de un grupo o supergrupo, añade @print_id_bot al grupo. Tras añadirlo, el bot enviará un mensaje de bienvenida con el nombre del grupo y el chat_id.

En grupos, el bot solo responde **cuando haces ciertas acciones**. Para obtener el chat_id, haz una de estas cosas:

- Envía el comando **/id** o **/help** (con @print_id_bot o sin)
- Responde a un mensaje del bot
- Menciona **@print_id_bot** en tu mensaje
- Envía cualquier comando con @print_id_bot (por ejemplo, `/foo@print_id_bot`)

Los mensajes normales sin mencionar al bot no provocan respuesta: así evita el spam. Los ID de grupos y supergrupos suelen ser negativos; es normal.

## Por dónde empezar

- [Guías de Telegram user ID]({{< relref "user-id-guides.md" >}}) — cómo encontrar, copiar y entender tu user ID
- [Guías de chat_id]({{< relref "chat-id-guides.md" >}}) — obtener chat_id de grupos y supergrupos
- [Guías de Bot API]({{< relref "bot-api-guides.md" >}}) — integración con Telegram Bot API

## FAQ

### ¿Es privado mi Telegram ID?

Tu Telegram ID no se muestra públicamente en la app. Los bots y aplicaciones solo lo obtienen cuando interactúas con ellos — por ejemplo, al abrir un bot y pulsar Iniciar. Tú decides a qué bots confiar.

### ¿Por qué el bot no responde en el grupo?

El bot solo responde cuando respondes a su mensaje, envías /id o /help, o mencionas @print_id_bot. Los mensajes normales sin estos disparadores los ignora. Asegúrate de que el bot está en el grupo y puede leer mensajes.

### ¿Cuál es la diferencia entre user ID y chat_id?

El **user ID** identifica tu cuenta de Telegram. El **chat_id** identifica el chat: privado, grupo, supergrupo o canal. En chat privado, user ID y chat_id son el mismo número. En grupos, el chat_id suele ser negativo.
