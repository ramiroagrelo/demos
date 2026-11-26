# Plantilla de carruseles de Instagram (@somosnewaves)

- `python3 ig_carrusel.py spec.json salida/` genera `slide-01.jpg`… (1080x1350, renderizado al doble y reducido, JPEG 95) y `vista-previa.jpg`.
- Necesita Playwright y Chrome (`/usr/bin/google-chrome`, o la variable CHROME) y Pillow.
- Tipos de lámina: `portada`, `texto`, `paso`, `frase`, `cta`. Extras: `chips`, `flujo`, `lista`, `chat`, `tarjeta`, `nota` (letra a mano), `oscuro: true` (fondo azul noche con letras blancas).
- Marcas: `<m>resaltado verde</m>`, `<b>negrita</b>`, `<v>verde</v>`, `<t>tachado</t>`.
- Ejemplo completo: `ejemplo-spec.json`.
- Las imágenes publicadas van en `ig/AAAA-MM/<slug>-<4 letras>/` y se ven en https://demos.somosnewaves.com/ig/...

## Láminas animadas (estilo "noche en movimiento", como el carrusel de Evenly)
- `python3 ig_video.py lamina.html 9 salida.mp4` graba la lámina cuadro por cuadro (1080x1350, 30 fps, H.264 CRF 16, audio mudo) y deja `salida.jpg` con el último cuadro.
- La lámina es un HTML con animaciones SOLO en CSS (keyframes con delays; las infinitas para flujos que se mueven). Nada de JavaScript con tiempo real: el grabador adelanta las animaciones de CSS.
- Ejemplo: `ejemplo-lamina-animada.html` (canales → agente → agenda). Fondo azul noche, letras blancas, verde #38E0A0, contador "01 / 08", "DESLIZÁ →".
- Ideas que lucen en movimiento: agentes que reciben y responden, embudos que se llenan, gráficos de crecimiento que suben, calendarios que se completan, antes/después.
