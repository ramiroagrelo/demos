# Plantilla de carruseles de Instagram (@somosnewaves)

- `python3 ig_carrusel.py spec.json salida/` genera `slide-01.jpg`… (1080x1350, renderizado al doble y reducido, JPEG 95) y `vista-previa.jpg`.
- Necesita Playwright y Chrome (`/usr/bin/google-chrome`, o la variable CHROME) y Pillow.
- Tipos de lámina: `portada`, `texto`, `paso`, `frase`, `cta`. Extras: `chips`, `flujo`, `lista`, `chat`, `tarjeta`, `nota` (letra a mano), `oscuro: true` (fondo azul noche con letras blancas).
- Marcas: `<m>resaltado verde</m>`, `<b>negrita</b>`, `<v>verde</v>`, `<t>tachado</t>`.
- Ejemplo completo: `ejemplo-spec.json`.
- Las imágenes publicadas van en `ig/AAAA-MM/<slug>-<4 letras>/` y se ven en https://demos.somosnewaves.com/ig/...
