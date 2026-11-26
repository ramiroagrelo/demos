# Arma los HTML de las láminas de imagen (02, 03, 04, 06, 08, 09, 10) con la base Noche en movimiento.
# Las láminas 01, 05 y 07 son animadas y tienen su propio HTML.
import os
AQUI = os.path.dirname(os.path.abspath(__file__))
TOTAL = 10

def pagina(n, css, cuerpo, pie="DESLIZÁ →"):
    return f"""<!doctype html><html><head><meta charset="utf-8">
<link rel="stylesheet" href="noche.css"><style>{css}</style></head><body>
<div class="top"><div>newaves<span class="dot">.</span></div><div class="c">{n:02d} / {TOTAL}</div></div>
{cuerpo}
<div class="foot"><div class="who"><img src="../../plantilla/newaves-isotipo-blanco.svg">@somosnewaves</div><div class="sw">{pie}</div></div>
</body></html>"""

FLECHA = '<svg viewBox="0 0 96 120" fill="none" stroke="#38E0A0" stroke-width="5" stroke-linecap="round" stroke-linejoin="round"><path d="M70 8 C 74 50, 50 84, 14 104"/><path d="M12 82 L12 106 L36 108"/></svg>'
CHECK = '<svg viewBox="0 0 24 24" fill="none" stroke="#070D1A" stroke-width="3.4" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12.5l4.5 4.5L19 7.5"/></svg>'

L = {}

# 02 · dolor
L[2] = pagina(2, """
.note{position:absolute;left:640px;top:170px;transform:rotate(-5deg)}
.note svg{position:absolute;left:-40px;top:52px;width:70px;height:90px;transform:scaleX(-1) rotate(30deg)}
.lead{position:absolute;left:80px;right:80px;top:345px}
.hist{position:absolute;left:80px;right:80px;top:470px;padding:30px 40px 18px}
.hist .h{display:flex;justify-content:space-between;font-size:24px;font-weight:700;color:#8D99AE;letter-spacing:1px;margin-bottom:8px}
.r{display:flex;gap:30px;align-items:baseline;padding:27px 0;border-top:1px solid #1E2B44;font-size:34px;font-weight:600}
.r .t{font-size:28px;color:#38E0A0;width:100px;flex:none;font-weight:700}
.r.last{color:#8D99AE}
.r.last .t{color:#F07A7A}
""", """
<h1>Abrís Canva<br>a las 22:00.</h1>
<div class="note"><span class="hand">¿te suena?</span></div>
<div class="lead">A las 00:40 seguís moviendo un cuadradito.<br><b>Y el carrusel no salió.</b></div>
<div class="hist card"><div class="h"><span>UNA NOCHE CUALQUIERA</span><span class="mono">hora a hora</span></div>
 <div class="r"><span class="t mono">22:00</span>Buscás una plantilla “que no parezca plantilla”.</div>
 <div class="r"><span class="t mono">22:25</span>Cambiás la letra. Otra vez.</div>
 <div class="r"><span class="t mono">22:50</span>El título no entra. Achicás todo.</div>
 <div class="r"><span class="t mono">23:30</span>Alineás un cuadradito dos píxeles.</div>
 <div class="r"><span class="t mono">00:10</span>Exportás. No te convence.</div>
 <div class="r last"><span class="t mono">00:40</span>Lo dejás para mañana.</div>
</div>""")

# 03 · giro
L[3] = pagina(3, """
h1{font-size:96px;line-height:1.0}
.lead{position:absolute;left:80px;right:80px;top:560px}
.cols{position:absolute;left:80px;right:80px;top:760px;display:grid;grid-template-columns:1fr 1fr;gap:28px}
.col{padding:30px 32px 34px}
.col .k{font-size:22px;font-weight:800;letter-spacing:4px;margin-bottom:22px}
.no .k{color:#F07A7A}.si .k{color:#38E0A0}
.si{border-color:#38E0A0}
.it{font-size:36px;font-weight:700;padding:18px 0}
.no .it{color:#AEB8C8}
.ar{font-size:28px;color:#5E6B82;line-height:1;padding-left:6px}
.si .ar{color:#38E0A0}
""", """
<h1>El problema<br>no es Canva.<br><span class="g">Es empezar<br>por el diseño.</span></h1>
<div class="lead">Si arrancás por la plantilla, tu idea se acomoda al dibujo. <b>Al revés sale mejor:</b> primero qué decís, después cómo se ve.</div>
<div class="cols">
 <div class="col card no"><div class="k">ASÍ NO</div><div class="it">Plantilla</div><div class="ar">↓</div><div class="it">Texto que no entra</div><div class="ar">↓</div><div class="it">Rehacer</div></div>
 <div class="col card si"><div class="k">ASÍ SÍ</div><div class="it">Idea</div><div class="ar">↓</div><div class="it">Guion</div><div class="ar">↓</div><div class="it">Diseño (lo hace la IA)</div></div>
</div>""")

# 04 · paso 01
L[4] = pagina(4, """
.step{position:absolute;left:80px;top:150px}
h1{top:215px}
.lead{position:absolute;left:80px;right:80px;top:420px}
.file{position:absolute;left:80px;right:80px;top:600px;overflow:hidden}
.bar{display:flex;align-items:center;gap:10px;padding:20px 28px;border-bottom:2px solid #22314C;font-size:24px;font-weight:700;color:#8D99AE}
.bar i{width:14px;height:14px;border-radius:50%;background:#2A3A57;display:block}
.bar span{margin-left:14px}
.code{padding:26px 34px 30px;font-size:28px;line-height:1.75;color:#DDE4EF}
.code .k{color:#38E0A0}.code .c{color:#5E6B82}
.note{position:absolute;right:90px;top:512px;transform:rotate(-4deg)}
.tip{position:absolute;left:80px;right:80px;top:1095px;font-size:32px;line-height:1.4;color:#AEB8C8;padding-left:28px;border-left:6px solid #38E0A0}
.tip b{color:#fff}
""", """
<div class="step">PASO 01</div>
<h1>Contale tu marca<br><span class="g">una sola vez.</span></h1>
<div class="lead">Un documento corto con tus colores, tu letra y <b>cómo hablás</b>. La IA lo lee antes de cada carrusel.</div>
<div class="note"><span class="hand">(este es el nuestro)</span></div>
<div class="file card"><div class="bar"><i></i><i></i><i></i><span class="mono">marca.md</span></div>
<div class="code mono"><span class="c"># newaves</span><br>
<span class="k">colores:</span> azul noche #070D1A · verde #38E0A0<br>
<span class="k">letra:</span> Figtree, títulos bien gruesos<br>
<span class="k">voz:</span> de vos, frases cortas, humor seco<br>
<span class="k">nunca:</span> "escalar", "hackear", emojis de más<br>
<span class="k">cierre:</span> siempre con una palabra clave</div></div>
<div class="tip"><b>Tip:</b> guardalo en un Proyecto de Claude y no lo volvés a pegar nunca más.</div>""")

# 06 · paso 03
L[6] = pagina(6, """
.step{position:absolute;left:80px;top:150px}
h1{top:215px}
.lead{position:absolute;left:80px;right:80px;top:420px}
.codebox{position:absolute;left:80px;top:590px;width:470px;height:430px;padding:28px 28px;font-size:22px;line-height:1.7;color:#DDE4EF}
.codebox .tg{color:#38E0A0}.codebox .a{color:#7FA7FF}.codebox .c{color:#5E6B82}
.arrow{position:absolute;left:560px;top:770px;width:60px;height:60px}
.mini{position:absolute;left:630px;top:575px;width:370px;height:462px;border-radius:22px;background:radial-gradient(90% 60% at 50% 55%,#0F1C33 0%,#070D1A 70%);border:2px solid #38E0A0;box-shadow:0 0 60px rgba(56,224,160,.18);padding:26px 26px}
.mini .mt{display:flex;justify-content:space-between;font-size:15px;font-weight:800}
.mini .mt span{opacity:.5;letter-spacing:2px;font-weight:700}
.mini h3{margin:30px 0 0;font-size:44px;line-height:1.0;letter-spacing:-1px;font-weight:800}
.mini .b{height:44px;border-radius:12px;background:#16233A;border:1px solid #2A3A57;margin-top:24px}
.mini .gr{display:grid;grid-template-columns:repeat(5,1fr);gap:7px;margin-top:16px}
.mini .gr i{display:block;height:46px;border-radius:6px;background:#111B2D;border:1px solid #2A3A57}
.prompt{position:absolute;left:80px;right:80px;top:1075px;padding:24px 32px;border-radius:30px 30px 30px 8px;background:#16233A;border:2px solid #2A3A57;font-size:30px;line-height:1.4;font-weight:600}
.prompt .who{font-size:18px;font-weight:800;letter-spacing:4px;color:#8D99AE;margin-bottom:6px}
""", """
<div class="step">PASO 03</div>
<h1>Pedile que lo<br><span class="g">dibuje en código.</span></h1>
<div class="lead">En HTML, el idioma de las páginas web. <b>Vos no lo tocás:</b> lo lee el navegador y cada lámina sale igual de prolija.</div>
<div class="codebox card mono"><span class="c">&lt;!-- lámina 01 --&gt;</span><br>
<span class="tg">&lt;h1&gt;</span>Este carrusel<br>no se diseñó.<br>
<span class="tg">&lt;span</span> <span class="a">class</span>="verde"<span class="tg">&gt;</span><br>&nbsp;&nbsp;Se conversó.<br><span class="tg">&lt;/span&gt;&lt;/h1&gt;</span><br>
<span class="tg">&lt;div</span> <span class="a">class</span>="chat"<span class="tg">&gt;</span>…<br>
<span class="tg">&lt;div</span> <span class="a">class</span>="laminas"<span class="tg">&gt;</span>…</div>
<svg class="arrow" viewBox="0 0 60 60" fill="none" stroke="#38E0A0" stroke-width="5" stroke-linecap="round" stroke-linejoin="round"><path d="M8 30h42M36 16l14 14-14 14"/></svg>
<div class="mini"><div class="mt">newaves.<span>01 / 10</span></div><h3>Este carrusel<br>no se diseñó.<br><span class="g">Se conversó.</span></h3><div class="b"></div><div class="gr"><i></i><i></i><i></i><i></i><i></i><i></i><i></i><i></i><i></i><i></i></div></div>
<div class="prompt"><div class="who">VOS</div>“Haceme cada lámina en HTML de 1080×1350, con mi marca. Letra grande, una idea por lámina.”</div>""")

# 08 · paso 05
L[8] = pagina(8, """
.step{position:absolute;left:80px;top:150px}
h1{top:215px}
.lead{position:absolute;left:80px;right:80px;top:420px}
.list{position:absolute;left:80px;right:80px;top:540px}
.li{display:flex;gap:28px;align-items:flex-start;padding:24px 0;border-top:1px solid #1E2B44}
.li:first-child{border-top:0}
.ck{flex:none;width:52px;height:52px;border-radius:50%;background:#38E0A0;display:flex;align-items:center;justify-content:center}
.ck svg{width:30px;height:30px}
.li b{display:block;font-size:38px;font-weight:800;letter-spacing:-.5px}
.li span{display:block;font-size:28px;color:#AEB8C8;margin-top:4px;line-height:1.3}
.note{position:absolute;left:80px;right:80px;top:1135px;transform:rotate(-2deg)}
.note .hand{font-size:46px}
""", f"""
<div class="step">PASO 05</div>
<h1>Exportalo en<br><span class="g">tamaño real.</span></h1>
<div class="lead">Lo que hace que un carrusel se vea <b>profesional</b> no es la plantilla. Es esto:</div>
<div class="list">
 <div class="li"><div class="ck">{CHECK}</div><div><b>1080 × 1350 píxeles</b><span>El vertical (4:5): el que más pantalla ocupa.</span></div></div>
 <div class="li"><div class="ck">{CHECK}</div><div><b>Letra grande</b><span>Que se lea sin hacer zoom, con el celular en la mano.</span></div></div>
 <div class="li"><div class="ck">{CHECK}</div><div><b>Aire en los bordes</b><span>Nada pegado al borde: en la grilla del perfil se recorta.</span></div></div>
 <div class="li"><div class="ck">{CHECK}</div><div><b>JPG o PNG en máxima calidad</b><span>Y si querés movimiento, la animación se graba como video.</span></div></div>
</div>
<div class="note"><span class="hand">Cómo pasarlo a imagen, paso a paso: en la guía ↓</span></div>""")

# 09 · cierre
L[9] = pagina(9, """
.wrap{position:absolute;left:80px;right:80px;top:0;bottom:0;display:flex;flex-direction:column;justify-content:center}
.big{font-size:104px;line-height:1.0;letter-spacing:-2.5px;font-weight:800}
.sub{font-size:36px;line-height:1.4;color:#AEB8C8;margin-top:56px;font-weight:500}
.sub b{color:#fff}
.glow{position:absolute;left:140px;top:560px;width:800px;height:260px;border-radius:120px;background:#38E0A0;filter:blur(90px);opacity:.14}
""", """
<div class="glow"></div>
<div class="wrap"><div class="big">Lo difícil nunca<br>fue el diseño.<br><span class="g">Era saber<br>qué decir.</span></div>
<div class="sub">Para eso no hay plantilla.<br><b>Para todo lo demás, alcanza con una buena conversación.</b></div></div>""")

# 10 · pedido
L[10] = pagina(10, """
h1{font-size:110px;top:170px}
.btn{position:absolute;left:80px;top:310px;display:inline-flex;align-items:center;gap:22px;background:#38E0A0;color:#070D1A;border-radius:120px;padding:28px 58px;font-size:104px;font-weight:800;letter-spacing:-1px;box-shadow:0 0 90px rgba(56,224,160,.35)}
.note{position:absolute;left:640px;top:180px;transform:rotate(-6deg)}
.note .hand{font-size:48px}
.lead{position:absolute;left:80px;right:80px;top:530px;font-size:40px;color:#fff;font-weight:700}
.box{position:absolute;left:80px;right:80px;top:620px;padding:16px 40px}
.li{display:flex;gap:26px;align-items:center;padding:26px 0;border-top:1px solid #1E2B44;font-size:36px;font-weight:700}
.li:first-child{border-top:0}
.li span{display:block;font-size:26px;color:#AEB8C8;font-weight:500;margin-top:4px}
.ck{flex:none;width:50px;height:50px;border-radius:50%;background:#38E0A0;display:flex;align-items:center;justify-content:center}
.ck svg{width:28px;height:28px}
.small{position:absolute;left:80px;right:80px;top:1130px;font-size:28px;color:#8D99AE;line-height:1.4}
.small b{color:#fff}
""", f"""
<h1>Comentá</h1>
<div class="btn">CARRUSEL</div>
<div class="note"><span class="hand">gratis, y sin Canva</span></div>
<div class="lead">y te mando por mensaje la guía completa:</div>
<div class="box card">
 <div class="li"><div class="ck">{CHECK}</div><div>Los 4 prompts que usamos<span>Listos para copiar y pegar.</span></div></div>
 <div class="li"><div class="ck">{CHECK}</div><div>La plantilla de tu documento de marca<span>Para que la IA escriba como vos.</span></div></div>
 <div class="li"><div class="ck">{CHECK}</div><div>Cómo exportar en máxima calidad<span>Sin programar nada.</span></div></div>
</div>
<div class="small">Si después querés que lo armemos con vos, <b>en la guía está el link para agendar.</b></div>""", pie="GUARDALO ↓")

for n, h in L.items():
    open(os.path.join(AQUI, f"lamina-{n:02d}.html"), "w").write(h)
print("ok", sorted(L))
