+++
title = "Obtener Telegram user ID (métodos seguros)"
description = "Cómo obtener tu Telegram user ID de forma segura. Métodos paso a paso con @print_id_bot. Sin herramientas de desarrollador. Funciona en móvil y escritorio."
cta = { text = "Abre el bot y pulsa Iniciar para ver tu Telegram user ID al instante.", label = "Open @print_id_bot", url = "https://t.me/print_id_bot" }
+++

Tu **Telegram user ID** es un identificador numérico de tu cuenta. No se muestra en la app de Telegram, pero los bots e integraciones pueden leerlo cuando interactúas con ellos. Aquí tienes formas seguras de obtenerlo.

## Método 1: Usar @print_id_bot (el más rápido)

1. Abre [@print_id_bot](https://t.me/print_id_bot) en Telegram.
2. Pulsa **Iniciar**.
3. El bot responde con tu **User ID** y **Chat ID** (en chat privado coinciden).
4. Pulsa el número para copiarlo.

El bot responde en 16 idiomas según tu configuración de idioma en Telegram. Los idiomas no soportados usan inglés.

## Método 2: Enviar cualquier mensaje al bot

En chat privado con @print_id_bot, envía cualquier mensaje, foto, sticker o documento. El bot responde con tu User ID y Chat ID. También puedes usar `/id` para una respuesta corta.

## Método 3: Reenviar un mensaje (y limitaciones)

Si reenvías un mensaje de otro usuario a @print_id_bot, el bot puede mostrar el User ID del remitente original. Sin embargo, si el remitente tiene ajustes de privacidad que ocultan su ID al reenviar, verás "ID hidden". No puedes obtener de forma fiable el ID de otra persona por número de teléfono o username. Ver [mensajes reenviados e IDs ocultos]({{< relref "telegram-forwarded-message-id.md" "en" >}}) para más detalles.

## Lo que no puedes hacer

- **Buscar por número de teléfono**: No puedes obtener un Telegram user ID solo con un número de teléfono. Los servicios que lo prometen suelen ser estafas o violan la privacidad.
- **Buscar por username**: Los usernames no son IDs. Necesitas que el usuario interactúe con un bot o app para obtener su ID.
- **Ver IDs de otros sin interacción**: Solo puedes obtener IDs de chats en los que participas o de usuarios que reenvían mensajes que recibes (y que permiten el reenvío).

## Páginas relacionadas

- [Telegram ID vs username: ¿cuál es la diferencia?]({{< relref "telegram-id-vs-username.md" "en" >}})
- [Por qué Telegram no muestra tu ID numérico]({{< relref "telegram-id-not-in-ui.md" "en" >}})
- [print_id_bot: comandos, idiomas, funciones]({{< relref "print-id-bot.md" "en" >}})

## FAQ

### ¿Es privado mi Telegram user ID?
No se muestra en la interfaz de Telegram, pero los bots y apps pueden leerlo cuando interactúas con ellos. No lo compartas con servicios no confiables.

### ¿Puedo cambiar mi Telegram user ID?
No. Se asigna una vez y no cambia.

### ¿Por qué el bot muestra "ID hidden" en mensajes reenviados?
El remitente ha activado ajustes de privacidad que ocultan su ID al reenviar. Ver [ID del remitente reenviado oculto]({{< relref "telegram-privacy-forwarded-id-hidden.md" "en" >}}).

### ¿Es seguro usar @print_id_bot?
Sí. El bot solo muestra IDs a los que ya tienes acceso (el tuyo o de chats en los que estás). No almacena ni comparte tus datos más allá de lo que proporciona Telegram.

### ¿Cómo es un Telegram user ID?
Es un valor numérico, a menudo de 9–10 dígitos. Ejemplo: `123456789`.
