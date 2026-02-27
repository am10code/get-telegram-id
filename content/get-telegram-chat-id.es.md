+++
title = "Cómo obtener el chat_id de un grupo en Telegram"
description = "Obtén el chat_id de un grupo o supergrupo de Telegram en segundos. Añade @print_id_bot, envía /id o menciónalo y copia el chat_id. Guía paso a paso."
cta = { text = "Añade el bot a tu grupo y obtén el chat_id en 10 segundos.", label = "Open @print_id_bot", url = "https://t.me/print_id_bot" }
+++

El **chat_id** de un grupo o supergrupo de Telegram es necesario para integraciones con la Bot API. Aquí cómo obtenerlo rápido.

## Paso 1: Añade el bot a tu grupo

1. Abre [@print_id_bot](https://t.me/print_id_bot) en Telegram.
2. Pulsa **Iniciar**.
3. Añade el bot al grupo: abre el grupo → Añadir miembros → busca `print_id_bot` → Añadir.

Cuando el bot se añade, envía un mensaje de bienvenida con el nombre del grupo y el **chat_id**. Puedes copiarlo desde ahí.

## Paso 2: Si necesitas obtenerlo de nuevo

El bot responde en grupos solo cuando:

- respondes al mensaje del bot;
- envías `/id` o `/help` (con o sin @print_id_bot);
- envías cualquier comando con @print_id_bot (ej. `/foo@print_id_bot`);
- mencionas @print_id_bot en un mensaje.

Envía `/id` o menciona @print_id_bot y el bot responderá con el nombre del grupo y el chat_id. Pulsa el número para copiar.

## Grupo vs supergrupo: chat_id

Los ID de grupos y supergrupos suelen ser **números negativos**. Es normal. Cuando un grupo se convierte en supergrupo, el chat_id puede cambiar. Ver [chat_id de grupo vs supergrupo]({{< relref "telegram-group-chat-id-vs-supergroup.md" "en" >}}) para más detalles.

## Solución de problemas

Si el bot no responde, comprueba:

- que el bot tenga permiso para leer mensajes;
- que lo hayas activado correctamente (respuesta, /id, /help o @print_id_bot);
- que el bot no esté en modo privacidad bloqueando mensajes de grupo (si aplica).

Ver [el bot no responde en un grupo de Telegram]({{< relref "bot-not-responding-in-group.md" "en" >}}) para la lista completa.

## Páginas relacionadas

- [Añadir un bot a un grupo para obtener chat_id (10 segundos)]({{< relref "add-bot-to-group-chat-id.md" "en" >}})
- [Telegram Bot API: cómo obtener chat_id]({{< relref "telegram-bot-api-chat-id.md" "en" >}})
- [Por qué el chat_id de Telegram puede ser negativo]({{< relref "telegram-chat-id-negative.md" "en" >}})

## FAQ

### ¿Por qué el chat_id de mi grupo es negativo?
Los ID de grupos y supergrupos suelen ser negativos en la Telegram Bot API. Es así por diseño. Ver [formato de chat_id en Telegram]({{< relref "telegram-chat-id-format.md" "en" >}}).

### ¿Puedo obtener el chat_id del grupo de otro?
Solo de grupos en los que eres miembro. Añade el bot al grupo y envía /id o menciónalo.

### ¿Funciona el bot en supergrupos?
Sí. Se admiten grupos y supergrupos. El bot muestra el nombre del grupo y el chat_id. Ver [chat_id de grupo vs supergrupo]({{< relref "telegram-group-chat-id-vs-supergroup.md" "en" >}}).

### ¿Y si el bot fue eliminado del grupo?
Añádelo de nuevo. Al añadirlo, envía un mensaje de bienvenida con el chat_id. También puedes obtenerlo enviando /id o mencionando @print_id_bot.

### ¿El chat_id es igual para grupo y supergrupo?
Tras la migración a supergrupo, el chat_id puede cambiar. Usa siempre el valor actual del bot o la API.
