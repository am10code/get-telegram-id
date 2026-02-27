+++
title = "Bot de Telegram ID en 16 idiomas: cómo funciona la selección de idioma"
description = "Cómo @print_id_bot elige el idioma de respuesta según tu language_code de Telegram. 16 idiomas soportados, fallback a inglés. Ruso, persa, árabe y más."
cta = { text = "Abre @print_id_bot — responde en el idioma de tu Telegram.", label = "Open @print_id_bot", url = "https://t.me/print_id_bot" }
+++

@print_id_bot responde en **16 idiomas** según la configuración de idioma de Telegram. No hace falta selección manual.

## Cómo funciona

El bot lee tu **language_code** del update (de `message.from.language_code`, `edited_message.from.language_code` o `callback_query.from.language_code`). Usa la primera parte del código (ej. `pt-BR` → `pt`) y lo mapea a una locale soportada. Los códigos no soportados fallan a **inglés**.

## Idiomas soportados (16)

| Código | Idioma |
|--------|--------|
| `en` | Inglés |
| `ru` | Ruso |
| `fa` | Persa |
| `uz` | Uzbeko |
| `hi` | Hindi |
| `zh` | Chino |
| `tr` | Turco |
| `pt` | Portugués |
| `es` | Español |
| `ar` | Árabe |
| `id` | Indonesio |
| `de` | Alemán |
| `ur` | Urdu |
| `fr` | Francés |
| `tl` | Tagalo (filipino; `fil` mapea a `tl`) |
| `am` | Amharic |

## Casos especiales

- **Filipino** — Telegram envía `fil`; el bot lo mapea a `tl` (tagalo).
- **Portugués (Brasil)** — `pt-BR` usa `pt` (portugués).
- **Chino** — `zh-CN`, `zh-TW` usan `zh` (chino).

## Qué está localizado

Todas las respuestas del bot: texto de bienvenida, etiquetas (User ID, Chat ID, nombre de grupo), texto de ayuda, botones y mensajes como "ID hidden" o "Pulsa el número para copiar". El JSON crudo en /json y /dump no cambia; solo las etiquetas legibles usan tu idioma.

## Páginas relacionadas

- [Usar @print_id_bot si no hablas inglés]({{< relref "telegram-id-bot-for-non-english.md" "en" >}})
- [print_id_bot: comandos, idiomas, funciones]({{< relref "print-id-bot.md" "en" >}})
- [Obtener Telegram user ID (métodos seguros)]({{< relref "get-telegram-user-id.md" "en" >}})

## FAQ

### ¿Cómo cambio el idioma del bot?
Cambia el idioma de la app Telegram en Ajustes → Idioma. El bot lo usa. No hay selector de idioma en el bot.

### ¿Y si mi idioma no está soportado?
El bot falla a inglés. Toda la funcionalidad funciona igual.

### ¿El bot soporta idiomas de derecha a izquierda (RTL)?
Sí. Árabe, persa y urdu están soportados. Telegram maneja el renderizado RTL.

### ¿Puedo solicitar un nuevo idioma?
El bot soporta 16 idiomas. Añadir más depende de los mantenedores. El fallback a inglés garantiza que todos puedan usarlo.

### ¿Se guarda o envía el idioma a algún sitio?
No. El bot lee `language_code` de cada update y lo usa solo para elegir las cadenas de respuesta. No se guarda ni comparte.
