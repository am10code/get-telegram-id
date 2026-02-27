+++
title = "print_id_bot: Telegram ID y chat_id (comandos, idiomas, funciones)"
description = "Referencia completa de @print_id_bot: comandos, 16 idiomas, disparadores en grupos y funciones para desarrolladores (/json, /dump). Obtén tu Telegram user ID y chat_id en segundos."
cta = { text = "Abre el bot para obtener tu Telegram user ID y chat_id al instante.", label = "Open @print_id_bot", url = "https://t.me/print_id_bot" }
+++

@print_id_bot es un bot de Telegram que muestra tu **Telegram user ID**, **chat_id** (para grupos y supergrupos) e ID de canal. Funciona en chat privado y en grupos, con respuestas en 16 idiomas según la configuración de idioma de Telegram.

## Comandos

| Comando | Función |
|---------|---------|
| `/start` | Mensaje de bienvenida, tu User ID y Chat ID, botones inline para /id y /help |
| `/id` | Tu User ID y Chat ID (respuesta breve) |
| `/help` | Texto de ayuda completo y lista de comandos |
| `/json` | Mensaje actual en JSON (para desarrolladores) |
| `/dump` | Desglose completo del update y JSON crudo (solo en chat privado) |

En chat privado, enviar cualquier mensaje (texto, foto, sticker, etc.) también devuelve tu User ID y Chat ID. Para mensajes reenviados, el bot muestra el ID del autor cuando está disponible, o "ID hidden" cuando la privacidad del remitente lo bloquea. Ver [mensajes reenviados e IDs ocultos]({{< relref "telegram-forwarded-message-id.md" "en" >}}) para más detalles.

## Idiomas soportados (16)

El bot elige el idioma de respuesta según tu `language_code` de Telegram. Soportados: inglés, ruso, persa, uzbeko, hindi, chino, turco, portugués, español, árabe, indonesio, alemán, urdu, francés, tagalo, amárico. Los códigos no soportados usan inglés. Ver [cómo funciona la selección de idioma]({{< relref "telegram-id-bot-languages.md" "en" >}}).

## Comportamiento en grupos y supergrupos

En grupos, el bot solo responde cuando:

- Respondes al mensaje del bot
- Envías `/id` o `/help` (con o sin @print_id_bot)
- Envías cualquier comando con @print_id_bot (ej. `/foo@print_id_bot`)
- Mencionas @print_id_bot en tu mensaje

En caso contrario permanece en silencio. Al añadirlo a un grupo, envía un mensaje de bienvenida con el nombre del grupo y chat_id. Ver [añadir un bot al grupo para obtener chat_id]({{< relref "add-bot-to-group-chat-id.md" "en" >}}) para una guía rápida.

## Funciones para desarrolladores

- **/json** — Devuelve el mensaje actual en JSON.
- **/dump** — Desglose completo del update y JSON crudo (solo en chat privado). Útil para depurar integraciones con Bot API. Ver [inspeccionar JSON del update de Telegram]({{< relref "telegram-json-update.md" "en" >}}).

## Páginas relacionadas

- [Obtener Telegram user ID (métodos seguros)]({{< relref "get-telegram-user-id.md" "en" >}})
- [Cómo obtener chat_id de un grupo en Telegram]({{< relref "get-telegram-chat-id.md" "en" >}})
- [Cómo encontrar tu Telegram ID]({{< relref "how-to-find-telegram-id.md" "en" >}})

## FAQ

### ¿Funciona el bot en canales?
El bot funciona en chat privado y en grupos/supergrupos. Para canales necesitas el ID del canal de otro flujo (ej. publicar como canal y usar un bot que reciba updates). Ver [obtener ID de canal para Bot API]({{< relref "how-to-get-channel-id-bot-api.md" "en" >}}).

### ¿Puedo obtener el Telegram user ID de otra persona?
El bot muestra tu propio ID o el chat_id de chats en los que participas. Para mensajes reenviados muestra el ID del remitente solo si permite el reenvío; si no, verás "ID hidden". No puedes buscar el ID por número de teléfono o username. Ver [Telegram ID vs username]({{< relref "telegram-id-vs-username.md" "en" >}}).

### ¿Por qué el bot no responde en mi grupo?
El bot solo responde cuando le respondes, envías /id o /help, o mencionas @print_id_bot. Ver [bot no responde en grupo]({{< relref "bot-not-responding-in-group.md" "en" >}}) para una lista completa.

### ¿El bot es gratuito?
Sí. No requiere registro ni pago.

### ¿Cuál es la diferencia entre user ID y chat_id?
**User ID** identifica una cuenta de Telegram. **chat_id** identifica una conversación (chat privado, grupo, supergrupo, canal). Ver [Telegram ID vs username]({{< relref "telegram-id-vs-username.md" "en" >}}).
