# Carruseles de Instagram de newaves (@somosnewaves) en maxima calidad.
# Uso: python3 ig_carrusel.py spec.json carpeta_salida
#   -> slide-01.jpg ... (1080x1350, renderizado al doble y reducido = texto muy nitido, JPEG calidad 95)
#   -> vista-previa.jpg (todas las laminas en grilla, para Telegram)
# Marcas dentro de los textos: <m>resaltado verde</m>, <b>negrita</b>, <v>texto verde</v>, <t>tachado</t>, \n = salto de linea.
import sys, os, json, asyncio, html, re
from playwright.async_api import async_playwright
from PIL import Image

AQUI = os.path.dirname(os.path.abspath(__file__))
F = "file://" + AQUI + "/fonts/"
LOGO = open(os.path.join(AQUI, "newaves-isotipo-blanco.svg")).read()

CSS = f"""
@font-face{{font-family:Figtree;font-weight:400;src:url({F}figtree-latin-400-normal.woff2)}}
@font-face{{font-family:Figtree;font-weight:500;src:url({F}figtree-latin-500-normal.woff2)}}
@font-face{{font-family:Figtree;font-weight:700;src:url({F}figtree-latin-700-normal.woff2)}}
@font-face{{font-family:Figtree;font-weight:800;src:url({F}figtree-latin-800-normal.woff2)}}
@font-face{{font-family:Caveat;font-weight:700;src:url({F}caveat-latin-700-normal.woff2)}}
*{{box-sizing:border-box}}
html,body{{margin:0;width:1080px;height:1350px;overflow:hidden}}
body{{font-family:Figtree;color:#0B1424;background:#F3F1EB;position:relative}}
body:before{{content:"";position:absolute;inset:0;opacity:.35;pointer-events:none;
 background-image:url("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='300' height='300'><filter id='n'><feTurbulence type='fractalNoise' baseFrequency='.9' numOctaves='3' stitchTiles='stitch'/><feColorMatrix values='0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 .09 0'/></filter><rect width='100%' height='100%' filter='url(%23n)'/></svg>")}}
body.dark{{background:#070D1A;color:#fff}}
body.dark:before{{opacity:.6}}
.wrap{{position:absolute;left:96px;right:96px;top:150px;bottom:170px;display:flex;flex-direction:column}}
.center{{justify-content:center}}
.tag{{display:inline-block;align-self:flex-start;font-weight:800;font-size:30px;letter-spacing:2px;text-transform:uppercase;border:3px solid currentColor;border-radius:40px;padding:10px 26px;margin-bottom:46px}}
h1{{font-weight:800;font-size:104px;line-height:1.0;letter-spacing:-2.5px;margin:0}}
h2{{font-weight:800;font-size:84px;line-height:1.05;letter-spacing:-1.5px;margin:0}}
p{{font-size:46px;line-height:1.35;font-weight:500;margin:34px 0 0}}
m{{background:linear-gradient(transparent 12%,#38E0A0 12%,#38E0A0 88%,transparent 88%);padding:0 10px;margin:0 -4px;-webkit-box-decoration-break:clone;box-decoration-break:clone;color:#0B1424}}
v{{color:#0A7A52}} body.dark v{{color:#38E0A0}}
t{{text-decoration:line-through;text-decoration-thickness:6px;text-decoration-color:#E5484D;opacity:.65}}
.hand{{font-family:Caveat;font-weight:700;color:#0A7A52;font-size:64px;line-height:1.05}}
body.dark .hand{{color:#38E0A0}}
.num{{font-family:Caveat;font-weight:700;color:#0A7A52;font-size:120px;line-height:.8;margin-bottom:18px}}
body.dark .num{{color:#38E0A0}}
.foot{{position:absolute;left:96px;right:96px;bottom:70px;display:flex;align-items:center;justify-content:space-between;font-size:30px;font-weight:700}}
.who{{display:flex;align-items:center;gap:16px}}
.logo{{width:64px;height:64px;border-radius:50%;background:#0B1424;display:flex;align-items:center;justify-content:center}}
body.dark .logo{{background:#16305F}}
.logo svg{{width:38px;height:auto}}
.swipe{{font-family:Caveat;font-size:50px;color:#0A7A52}} body.dark .swipe{{color:#38E0A0}}
.count{{position:absolute;top:70px;right:96px;font-weight:700;font-size:28px;opacity:.55}}
.brand{{position:absolute;top:70px;left:96px;font-weight:800;font-size:28px;letter-spacing:1px;opacity:.55}}
.chips{{display:flex;flex-wrap:wrap;gap:22px;margin-top:56px}}
.chip{{font-size:48px;font-weight:700;border:4px solid #0B1424;border-radius:60px;padding:16px 34px;background:#fff}}
body.dark .chip{{border-color:#fff;background:transparent}}
.chip.ok{{background:#38E0A0;color:#0B1424}}
.flow{{display:flex;flex-direction:column;gap:0;margin-top:56px}}
.box{{border:4px solid #0B1424;border-radius:24px;padding:32px 38px;font-size:50px;font-weight:700;background:#fff;box-shadow:8px 8px 0 #0B1424}}
.box.g{{background:#38E0A0}}
body.dark .box{{background:#111B2D;border-color:#fff;box-shadow:8px 8px 0 #38E0A0;color:#fff}}
.arrowdown{{height:100px;display:flex;align-items:center;padding-left:60px}}
.list{{margin:50px 0 0;padding:0;list-style:none}}
.list li{{font-size:50px;font-weight:600;line-height:1.3;padding:20px 0 20px 76px;position:relative;border-bottom:3px dashed rgba(11,20,36,.18)}}
body.dark .list li{{border-color:rgba(255,255,255,.18)}}
.list li:before{{content:"";position:absolute;left:0;top:28px;width:44px;height:44px;border-radius:50%;background:#38E0A0;box-shadow:inset 0 0 0 4px #0B1424}}
.chat{{margin-top:44px;background:#E9E4DA;border-radius:34px;padding:34px;display:flex;flex-direction:column;gap:18px;border:4px solid #0B1424}}
.msg{{max-width:80%;font-size:42px;line-height:1.3;padding:18px 24px;border-radius:24px;background:#fff;font-weight:500}}
.msg.yo{{align-self:flex-end;background:#C9F5DF}}
.msg small{{display:block;font-size:24px;opacity:.55;margin-top:6px;text-align:right}}
.chat .sep{{align-self:center;font-family:Caveat;font-size:46px;color:#E5484D;margin:4px 0}}
.nota{{font-size:24px;opacity:.5;margin-top:16px}}
.card{{margin-top:60px;background:#fff;border:4px solid #0B1424;border-radius:30px;padding:48px 52px;box-shadow:10px 10px 0 #38E0A0}}
.card .k{{font-size:32px;font-weight:700;opacity:.6;text-transform:uppercase;letter-spacing:1px}}
.card .t{{font-size:68px;font-weight:800;margin-top:8px}}
.card .s{{font-size:40px;font-weight:500;margin-top:10px;opacity:.75}}
.big{{font-size:118px;font-weight:800;line-height:.98;letter-spacing:-3px}}
svg.d{{position:absolute;overflow:visible}}
"""

def fmt(s):
    s = html.escape(s, quote=False)
    for t in ("m", "b", "v", "t"):
        s = s.replace(f"&lt;{t}&gt;", f"<{t}>").replace(f"&lt;/{t}&gt;", f"</{t}>")
    return s.replace("\n", "<br>")

ARROW_DOWN = '<svg width="70" height="80" viewBox="0 0 70 80"><path d="M30 6 C 40 30, 22 46, 34 70" fill="none" stroke="#0A7A52" stroke-width="6" stroke-linecap="round"/><path d="M18 54 L 34 72 L 50 52" fill="none" stroke="#0A7A52" stroke-width="6" stroke-linecap="round" stroke-linejoin="round"/></svg>'
def arrow_curva(x, y, w=230, rot=0):
    return (f'<svg class="d" style="left:{x}px;top:{y}px;transform:rotate({rot}deg)" width="{w}" height="{int(w*.6)}" viewBox="0 0 230 140">'
            '<path d="M10 20 C 60 0, 150 10, 200 100" fill="none" stroke="#0A7A52" stroke-width="7" stroke-linecap="round"/>'
            '<path d="M168 86 L 202 104 L 210 66" fill="none" stroke="#0A7A52" stroke-width="7" stroke-linecap="round" stroke-linejoin="round"/></svg>')
def circulo(x, y, w, h):
    return (f'<svg class="d" style="left:{x}px;top:{y}px" width="{w}" height="{h}" viewBox="0 0 100 60" preserveAspectRatio="none">'
            '<path d="M8 32 C 6 8, 80 2, 95 22 C 104 44, 60 58, 24 54 C 4 50, 2 34, 14 16" fill="none" stroke="#E5484D" stroke-width="2.4" stroke-linecap="round"/></svg>')

def extra(s):
    out = ""
    if "chips" in s:
        out += '<div class="chips">' + "".join(f'<div class="chip{" ok" if c.startswith("+") else ""}">{fmt(c.lstrip("+"))}</div>' for c in s["chips"]) + "</div>"
    if "flujo" in s:
        partes = []
        for i, c in enumerate(s["flujo"]):
            if i: partes.append(f'<div class="arrowdown">{ARROW_DOWN}</div>')
            partes.append(f'<div class="box{" g" if i == len(s["flujo"])-1 else ""}">{fmt(c)}</div>')
        out += '<div class="flow">' + "".join(partes) + "</div>"
    if "lista" in s:
        out += '<ul class="list">' + "".join(f"<li>{fmt(x)}</li>" for x in s["lista"]) + "</ul>"
    if "chat" in s:
        items = []
        for c in s["chat"]:
            if c.get("sep"): items.append(f'<div class="sep">{fmt(c["sep"])}</div>'); continue
            items.append(f'<div class="msg{" yo" if c.get("yo") else ""}">{fmt(c["txt"])}<small>{c.get("hora","")}</small></div>')
        out += '<div class="chat">' + "".join(items) + "</div>"
        out += f'<div class="nota">{fmt(s.get("aclaracion","Conversación de ejemplo."))}</div>'
    if "tarjeta" in s:
        k = s["tarjeta"]
        out += f'<div class="card"><div class="k">{fmt(k.get("k",""))}</div><div class="t">{fmt(k.get("t",""))}</div><div class="s">{fmt(k.get("s",""))}</div></div>'
    if "nota" in s:
        out += f'<div class="hand" style="margin-top:44px;transform:rotate(-2deg)">{fmt(s["nota"])}</div>'
    return out

def slide_html(s, i, n):
    dark = s.get("oscuro")
    tipo = s.get("tipo", "texto")
    body = ""
    deco = ""
    if tipo == "portada":
        body = ""
        if s.get("etiqueta"): body += f'<div class="tag">{fmt(s["etiqueta"])}</div>'
        body += f'<h1 style="font-size:{s.get("tam",104)}px">{fmt(s["titulo"])}</h1>'
        if s.get("bajada"): body += f'<p>{fmt(s["bajada"])}</p>'
        if s.get("nota"):
            body += f'<div class="hand" style="margin-top:60px;margin-left:300px;transform:rotate(-4deg);font-size:72px">{fmt(s["nota"])}</div>'
            deco += arrow_curva(150, 0, 220, 0).replace('top:0px', 'bottom:330px;top:auto')
        wrap = "wrap center"
    elif tipo == "paso":
        body = f'<div class="num">{fmt(s.get("n", str(i)))}</div><h2>{fmt(s["titulo"])}</h2>'
        if s.get("cuerpo"): body += f'<p>{fmt(s["cuerpo"])}</p>'
        body += extra(s)
        wrap = "wrap center"
    elif tipo == "frase":
        body = f'<div class="big">{fmt(s["titulo"])}</div>'
        if s.get("cuerpo"): body += f'<p>{fmt(s["cuerpo"])}</p>'
        body += extra(s)
        wrap = "wrap center"
    elif tipo == "cta":
        body = f'<h2 style="font-size:80px">{fmt(s["titulo"])}</h2>'
        if s.get("palabra"):
            body += f'<div style="margin-top:56px;display:flex;align-items:center;gap:26px"><span style="font-size:40px;font-weight:700">Comentá</span><span class="box g" style="font-size:64px;font-weight:800;letter-spacing:2px;padding:18px 40px">{fmt(s["palabra"])}</span></div>'
        if s.get("cuerpo"): body += f'<p>{fmt(s["cuerpo"])}</p>'
        body += extra(s)
        wrap = "wrap center"
    else:
        body = f'<h2>{fmt(s["titulo"])}</h2>' if s.get("titulo") else ""
        if s.get("cuerpo"): body += f'<p>{fmt(s["cuerpo"])}</p>'
        body += extra(s)
        wrap = "wrap"
    if s.get("circulo"): deco += circulo(*s["circulo"])
    ultima = i == n
    foot = (f'<div class="foot"><div class="who"><div class="logo">{LOGO}</div>@somosnewaves</div>'
            f'<div class="swipe">{"" if ultima else "deslizá →"}</div></div>')
    return (f'<!doctype html><html><head><meta charset="utf-8"><style>{CSS}</style></head>'
            f'<body class="{"dark" if dark else ""}"><div class="brand">newaves</div><div class="count">{i}/{n}</div>'
            f'<div class="{wrap}">{body}</div>{deco}{foot}</body></html>')

async def render(spec, out):
    os.makedirs(out, exist_ok=True)
    slides = spec["slides"]; n = len(slides)
    paths = []
    async with async_playwright() as p:
        b = await p.chromium.launch(executable_path=os.environ.get("CHROME", "/usr/bin/google-chrome"))
        pg = await (await b.new_context(viewport={"width": 1080, "height": 1350}, device_scale_factor=2)).new_page()
        for i, s in enumerate(slides, 1):
            h = os.path.join(out, f"slide-{i:02d}.html")
            open(h, "w").write(slide_html(s, i, n))
            await pg.goto("file://" + os.path.abspath(h)); await pg.evaluate("document.fonts.ready"); await pg.wait_for_timeout(300)
            big = h.replace(".html", "@2x.png"); await pg.screenshot(path=big)
            img = Image.open(big).convert("RGB").resize((1080, 1350), Image.LANCZOS)
            jp = h.replace(".html", ".jpg"); img.save(jp, "JPEG", quality=95, subsampling=0, optimize=True)
            os.remove(big); paths.append(jp)
        await b.close()
    cols = 5 if n > 6 else n
    rows = (n + cols - 1) // cols
    tw, th = 432, 540
    sheet = Image.new("RGB", (cols * tw + (cols + 1) * 12, rows * th + (rows + 1) * 12), (30, 30, 30))
    for k, pth in enumerate(paths):
        im = Image.open(pth).resize((tw, th), Image.LANCZOS)
        sheet.paste(im, (12 + (k % cols) * (tw + 12), 12 + (k // cols) * (th + 12)))
    sheet.save(os.path.join(out, "vista-previa.jpg"), "JPEG", quality=90)
    print("\n".join(paths))

if __name__ == "__main__":
    asyncio.run(render(json.load(open(sys.argv[1])), sys.argv[2]))
