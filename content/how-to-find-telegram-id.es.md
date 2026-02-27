+++
title = "Cómo encontrar tu ID de Telegram"
description = "Formas paso a paso para obtener tu Telegram user ID y chat_id (grupos) de forma segura. El método más rápido es usar un bot de Telegram."
cta = { text = "La forma más rápida: abre el bot y te mostrará tu ID de Telegram al instante.", label = "Open @print_id_bot", url = "https://t.me/print_id_bot" }
+++

## La forma más rápida (1 segundo)

Abre el bot y pulsa **Iniciar**. Te devolverá:

- Tu **Telegram user ID**
- Tu **username** (si tienes uno)
- (En grupos) el **chat_id** del grupo o supergrupo

## Método 1 — Usar un bot de Telegram (recomendado)

1. Abre el bot: https://t.me/print_id_bot
2. Pulsa **Iniciar**
3. Copia tu ID de Telegram del mensaje

**Por qué este método es el mejor:** es sencillo, funciona en móvil y escritorio, y no requiere herramientas de desarrollo.

## Método 2 — Obtener chat_id de un grupo (para Bot API)

Si necesitas un **chat_id** de grupo para integraciones:

1. Añade el bot a tu grupo
2. Envía cualquier mensaje en el grupo (o usa el comando del bot como `/id`)
3. El bot responderá con el **chat_id** del grupo

> Nota: los ID de grupos y supergrupos suelen ser números negativos. Es normal.

## Problemas comunes

- **El bot no responde en mi grupo:** asegúrate de que el bot tenga permiso para leer mensajes y revisa la configuración del modo de privacidad (según cómo esté construido el bot).
- **Solo veo un username, no un ID:** los usernames no son IDs. Los IDs son numéricos.
- **Quiero el ID de otra persona:** esta herramienta sirve para obtener tu propio ID o el chat_id de los chats donde participas.

## FAQ

### ¿Es privado mi ID de Telegram?
Tu ID de Telegram no se muestra públicamente en la interfaz de Telegram, pero los bots y aplicaciones pueden leerlo cuando interactúas con ellos.

### ¿Puedo obtener un ID por número de teléfono o username?
Oficialmente, en general no puedes obtener de forma fiable el ID numérico de alguien solo con su número de teléfono o username sin interacción. Evita servicios que prometan «búsqueda de ID por teléfono»: suelen ser estafas o violaciones de privacidad.

### ¿Cuál es la diferencia entre user ID y chat_id?
- **User ID** identifica una cuenta de Telegram.
- **chat_id** identifica una conversación (chat privado, grupo, supergrupo, canal).
