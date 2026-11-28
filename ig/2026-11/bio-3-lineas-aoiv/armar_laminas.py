# Arma los HTML de las láminas de imagen (02-07, 09, 10) con la base Noche en movimiento.
# Las láminas 01 y 08 son animadas y tienen su propio HTML (se graban con ig_video.py).
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

CHECK = '<svg viewBox="0 0 24 24" fill="none" stroke="#070D1A" stroke-width="3.4" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12.5l4.5 4.5L19 7.5"/></svg>'
def flecha(w=80, h=100, rot=0, flip=False):
    t = f"rotate({rot}deg)" + (" scaleX(-1)" if flip else "")
    return f'<svg width="{w}" height="{h}" style="transform:{t}" viewBox="0 0 96 120" fill="none" stroke="#38E0A0" stroke-width="5" stroke-linecap="round" stroke-linejoin="round"><path d="M70 8 C 74 50, 50 84, 14 104"/><path d="M12 82 L12 106 L36 108"/></svg>'

PERFIL_MALO = """<div class="hd"><div class="av"><div>LF</div></div><div><div class="u">lucia.nutri</div><div class="bts"><span class="f">Seguir</span><span>Mensaje</span></div></div></div>
 <div class="nm">Lucía Ferrer</div><div class="cat">Nutricionista</div>
 <div class="bio"><div class="l l1">✨ Nutricionista | Mamá | Viajera ✨</div><div class="l l2">Apasionada por ayudarte a ser tu mejor versión 💚</div><div class="l l3">Link abajo 👇</div></div>
 <div class="lk">🔗 tusitio.com</div><div class="ejt ej">ejemplo · persona inventada</div>"""

L = {}

# 02 · dolor: lo que ve el que entra
L[2] = pagina(2, """
h1{font-size:80px}
.prof{top:370px;padding-bottom:56px}
.prof .bio{font-size:34px;line-height:1.5;margin-top:14px}
.prof .nm{font-size:34px;margin-top:34px}.prof .cat{font-size:26px}.av{width:140px;height:140px}.prof .u{font-size:38px}.prof .lk{margin-top:18px}
.prof .l{width:fit-content;position:relative}
.prof .l:after{content:"";position:absolute;left:-8px;right:-8px;bottom:-4px;height:4px;border-radius:2px;background:#F07A7A;opacity:.9}
.qs{position:absolute;left:80px;right:80px;top:975px;display:flex;justify-content:space-between}
.q{font-family:Caveat;font-weight:700;color:#F07A7A;font-size:50px;line-height:.95;transform:rotate(-4deg);text-align:center}
.q:nth-child(2){transform:rotate(3deg)}
.bottom{position:absolute;left:80px;right:80px;top:1125px;font-size:38px;font-weight:700;line-height:1.3}
.bottom span{color:#AEB8C8;font-weight:500}
""", f"""
<h1>Esto ve alguien<br>que entra a tu perfil:</h1>
<div class="prof card">{PERFIL_MALO}</div>
<div class="qs"><div class="q">¿qué hacés<br>por mí?</div><div class="q">¿por qué<br>vos?</div><div class="q">¿y ahora<br>qué toco?</div></div>
<div class="bottom">Tres segundos después: <span class="x">atrás.</span><br><span>Sin seguirte. Sin escribirte. Sin que te enteres.</span></div>
""")

# 03 · giro: tres preguntas, tres líneas
L[3] = pagina(3, """
h1{font-size:92px;line-height:1.0}
.lead{position:absolute;left:80px;right:80px;top:480px}
.rows{position:absolute;left:80px;right:80px;top:640px}
.r{display:flex;align-items:center;gap:26px;padding:26px 34px;margin-bottom:22px}
.r .n{flex:none;width:64px;height:64px;border-radius:50%;background:#38E0A0;color:#070D1A;font-size:32px;font-weight:800;display:flex;align-items:center;justify-content:center}
.r .q{font-size:40px;font-weight:800;letter-spacing:-.5px;flex:1}
.r .a{font-size:26px;font-weight:700;color:#38E0A0;letter-spacing:2px;white-space:nowrap}
.note{position:absolute;left:80px;top:1060px;transform:rotate(-2deg)}
.note .hand{font-size:48px}
""", """
<h1>Tu bio no es<br>para presentarte.<br><span class="g">Es para responder.</span></h1>
<div class="lead">El que entra se hace <b>3 preguntas</b>, aunque no lo sepa. Cada línea de tu bio contesta una:</div>
<div class="rows">
 <div class="r card"><div class="n">1</div><div class="q">¿Qué hacés y para quién?</div><div class="a">LÍNEA 1</div></div>
 <div class="r card"><div class="n">2</div><div class="q">¿Por qué vos?</div><div class="a">LÍNEA 2</div></div>
 <div class="r card"><div class="n">3</div><div class="q">¿Y ahora qué toco?</div><div class="a">LÍNEA 3</div></div>
</div>
<div class="note"><span class="hand">nada de “mamá, viajera y soñadora”:<br>eso va en tus historias.</span></div>
""")

# 04 · paso 01: el nombre
L[4] = pagina(4, """
.step{position:absolute;left:80px;top:150px}
h1{top:215px}
.lead{position:absolute;left:80px;right:80px;top:420px}
.search{position:absolute;left:80px;right:80px;top:590px;padding:26px 30px 14px}
.sb{display:flex;align-items:center;gap:18px;background:#1B2A44;border-radius:18px;padding:18px 24px;font-size:30px;font-weight:600}
.sb svg{flex:none}
.res{display:flex;align-items:center;gap:22px;padding:22px 6px;border-top:1px solid #1E2B44;margin-top:16px}
.res + .res{margin-top:0}
.res .av{width:84px;height:84px;padding:4px}
.res .av div{font-size:26px;border-width:4px}
.res b{display:block;font-size:30px}
.res span{display:block;font-size:26px;color:#AEB8C8}
.res.no{opacity:.5}
.mk{background:rgba(56,224,160,.18);color:#fff;border-radius:6px;padding:0 4px}
.cmp{position:absolute;left:80px;right:80px;top:905px;display:grid;grid-template-columns:1fr 1fr;gap:24px}
.cmp .c{padding:28px 32px;min-height:200px}
.cmp .k{font-size:20px;font-weight:800;letter-spacing:4px;margin-bottom:8px}
.cmp .no .k{color:#F07A7A}.cmp .si .k{color:#38E0A0}
.cmp .si{border-color:#38E0A0}
.cmp .v{font-size:36px;font-weight:800;line-height:1.25}
.note{position:absolute;right:80px;top:528px;transform:rotate(-4deg)}
.note .hand{font-size:42px}
""", """
<div class="step">PASO 01</div>
<h1>Antes de la bio:<br><span class="g">tu nombre.</span></h1>
<div class="lead">El campo <b>Nombre</b> (no tu @) también cuenta en el buscador de Instagram. <b>Usalo para lo que te buscarían.</b></div>
<div class="note"><span class="hand">esto busca tu cliente ↓</span></div>
<div class="search card">
 <div class="sb"><svg width="34" height="34" viewBox="0 0 24 24" fill="none" stroke="#8D99AE" stroke-width="2.6" stroke-linecap="round"><circle cx="10.5" cy="10.5" r="6.5"/><path d="M15.5 15.5L21 21"/></svg>nutrición para runners</div>
 <div class="res"><div class="av"><div>LF</div></div><div><b>lucia.nutri</b><span>Lucía Ferrer | <span class="mk" style="display:inline">Nutrición para runners</span></span></div></div>
</div>
<div class="cmp">
 <div class="c card no"><div class="k">ASÍ NO</div><div class="v">Lucía ✨🌿</div></div>
 <div class="c card si"><div class="k">ASÍ SÍ</div><div class="v">Lucía Ferrer | Nutrición para runners</div></div>
</div>
<div class="ej" style="position:absolute;left:80px;top:1135px">ejemplo · persona inventada</div>
""")

# 05 · paso 02: línea 1
L[5] = pagina(5, """
.step{position:absolute;left:80px;top:150px}
h1{top:215px}
.f{position:absolute;left:80px;right:80px;top:425px;padding:30px 38px;font-size:42px;font-weight:800;line-height:1.45;letter-spacing:-.5px;border-color:#38E0A0}
.f .s{display:inline-block;border-radius:12px;padding:0 14px;font-weight:800;line-height:1.25}
.s1{background:#38E0A0;color:#070D1A}.s2{background:#7FA7FF;color:#070D1A}.s3{background:#2A3A57;color:#fff}
.f .lab{font-size:20px;letter-spacing:4px;color:#8D99AE;margin-bottom:10px;font-weight:800}
.ex{position:absolute;left:80px;right:80px;top:705px}
.ex .h{font-size:22px;font-weight:800;letter-spacing:4px;color:#8D99AE;margin-bottom:12px}
.e{font-size:30px;line-height:1.3;padding:16px 0;white-space:nowrap;border-top:1px solid #1E2B44;font-weight:600}
.e .r{display:block;font-size:22px;font-weight:800;letter-spacing:3px;color:#5E6B82;margin-bottom:4px}
.e u{text-decoration:none;color:#38E0A0}.e em{font-style:normal;color:#7FA7FF}.e i{font-style:normal;color:#AEB8C8}
.tip{position:absolute;left:80px;right:80px;top:1135px;font-size:30px;line-height:1.35;color:#AEB8C8;padding-left:26px;border-left:6px solid #38E0A0}
.tip b{color:#fff}
""", """
<div class="step">PASO 02 · LÍNEA 1</div>
<h1>A quién ayudás<br><span class="g">a lograr qué.</span></h1>
<div class="f card"><div class="lab">LA FÓRMULA</div>Ayudo a <span class="s s1">quién</span> a <span class="s s2">resultado</span> sin <span class="s s3">lo que odian</span>.</div>
<div class="ex"><div class="h">TRES EJEMPLOS <span class="ej" style="letter-spacing:0;font-weight:600">(inventados)</span></div>
 <div class="e"><span class="r">COACH</span>Ayudo a <u>coaches</u> a <em>llenar su agenda</em> <i>sin vivir en Instagram.</i></div>
 <div class="e"><span class="r">CONTADORA</span>Ayudo a <u>monotributistas</u> a <em>dormir tranquilos</em> <i>sin planillas.</i></div>
 <div class="e"><span class="r">RESTAURANTE</span>Ayudamos a <u>oficinas</u> a <em>almorzar rico</em> <i>sin perder una hora.</i></div>
</div>
<div class="tip"><b>Si le sirve a cualquiera, no le habla a nadie.</b> Nombrá a una persona, no a “todos los que quieran crecer”.</div>
""")

# 06 · paso 03: línea 2
L[6] = pagina(6, """
.step{position:absolute;left:80px;top:150px}
h1{top:215px}
.lead{position:absolute;left:80px;right:80px;top:420px}
.cols{position:absolute;left:80px;right:80px;top:560px;display:grid;grid-template-columns:1fr 1.25fr;gap:26px}
.col{padding:30px 32px 26px}
.col .k{font-size:22px;font-weight:800;letter-spacing:4px;margin-bottom:12px}
.no .k{color:#F07A7A}.si .k{color:#38E0A0}
.si{border-color:#38E0A0}
.it{font-size:32px;font-weight:700;padding:16px 0;border-top:1px solid #1E2B44;line-height:1.25}
.it:first-of-type{border-top:0}
.no .it{color:#8D99AE;text-decoration:line-through;text-decoration-color:#F07A7A;text-decoration-thickness:4px}
.si .it span{display:block;font-size:22px;color:#AEB8C8;font-weight:500;margin-top:4px}
.note{position:absolute;left:80px;right:80px;top:1135px;transform:rotate(-2deg)}
.note .hand{font-size:50px}
""", """
<div class="step">PASO 03 · LÍNEA 2</div>
<h1>Por qué vos.<br><span class="g">Con algo comprobable.</span></h1>
<div class="lead">Elegí <b>uno o dos</b> datos que cualquiera podría verificar. Separalos con un punto (·).</div>
<div class="cols">
 <div class="col card no"><div class="k">ASÍ NO</div>
  <div class="it">La mejor</div><div class="it">Experta</div><div class="it">Apasionada</div><div class="it">Mentora de vida</div><div class="it">Tu mejor versión</div></div>
 <div class="col card si"><div class="k">ASÍ SÍ</div>
  <div class="it">9 años<span>de experiencia (los tuyos)</span></div>
  <div class="it">Dónde trabajaste<span>o dónde te formaste</span></div>
  <div class="it">Tu método con nombre<span>si de verdad lo tenés</span></div>
  <div class="it">Tu ciudad<span>si atendés en persona</span></div></div>
</div>
<div class="note"><span class="hand">si no lo podés probar, no va.</span></div>
""")

# 07 · paso 04: línea 3
L[7] = pagina(7, """
.step{position:absolute;left:80px;top:150px}
h1{top:215px}
.lead{position:absolute;left:80px;right:80px;top:420px}
.box{position:absolute;left:80px;right:80px;padding:28px 36px}
.b1{top:540px}.b2{top:815px;border-color:#38E0A0}
.box .k{font-size:22px;font-weight:800;letter-spacing:4px;margin-bottom:12px}
.b1 .k{color:#F07A7A}.b2 .k{color:#38E0A0}
.b1 .v{font-size:32px;line-height:1.5;color:#8D99AE;font-weight:600}
.b1 .v s{text-decoration-color:#F07A7A;text-decoration-thickness:4px}
.b2 .v{font-size:40px;line-height:1.3;font-weight:800}
.b2 .v b{color:#38E0A0}
.b2 .w{font-size:25px;color:#AEB8C8;margin-top:12px;line-height:1.4}
.rule{position:absolute;left:80px;right:80px;top:1085px;display:flex;align-items:center;gap:24px;font-size:31px;line-height:1.35;color:#AEB8C8}
.rule .ck{flex:none;width:54px;height:54px;border-radius:50%;background:#38E0A0;display:flex;align-items:center;justify-content:center}
.rule .ck svg{width:30px;height:30px}
.rule b{color:#fff}
.note{position:absolute;right:80px;top:752px;transform:rotate(-3deg)}
.note .hand{font-size:42px}
""", f"""
<div class="step">PASO 04 · LÍNEA 3</div>
<h1>Un solo pedido.<br><span class="g">No cuatro.</span></h1>
<div class="lead">Si le pedís todo, no hace nada. Decile <b>una</b> cosa y <b>qué gana</b> haciéndola.</div>
<div class="box b1 card"><div class="k">ASÍ NO</div><div class="v"><s>Seguime 👉 Escribime 💬 Mirá mis destacadas ⭐ Link abajo 👇</s></div></div>
<div class="note"><span class="hand">una acción + qué recibe</span></div>
<div class="box b2 card"><div class="k">ASÍ SÍ</div><div class="v">Escribime <b>PLAN</b> y te paso tu primera semana.</div><div class="w">Otras: “Agendá tu primera charla gratis ↓” · “Bajá la guía de 5 recetas ↓”</div></div>
<div class="rule"><div class="ck">{CHECK}</div><div><b>Y que el link lleve a ese mismo lugar.</b> Si la bio dice “agendá”, el link abre la agenda. No una página con 12 botones.</div></div>
<div class="ej" style="position:absolute;left:80px;top:1215px">ejemplos inventados</div>
""")

# 09 · cierre
L[9] = pagina(9, """
.wrap{position:absolute;left:80px;right:80px;top:0;bottom:0;display:flex;flex-direction:column;justify-content:center}
.big{font-size:116px;line-height:1.0;letter-spacing:-3px;font-weight:800}
.sub{font-size:38px;line-height:1.4;color:#AEB8C8;margin-top:56px;font-weight:500}
.sub b{color:#fff}
.glow{position:absolute;left:140px;top:560px;width:800px;height:260px;border-radius:120px;background:#38E0A0;filter:blur(90px);opacity:.14}
""", """
<div class="glow"></div>
<div class="wrap"><div class="big">Nadie sigue<br>lo que <span class="g">no<br>entiende.</span></div>
<div class="sub">Tu bio no tiene que ser ingeniosa.<br><b>Tiene que hacer que el que entra se quede.</b></div></div>""")

# 10 · pedido
L[10] = pagina(10, """
h1{font-size:110px;top:170px}
.btn{position:absolute;left:80px;top:310px;display:inline-flex;align-items:center;background:#38E0A0;color:#070D1A;border-radius:120px;padding:28px 70px;font-size:112px;font-weight:800;letter-spacing:-1px;box-shadow:0 0 90px rgba(56,224,160,.35)}
.note{position:absolute;left:450px;top:345px;transform:rotate(-6deg)}
.note .hand{font-size:50px}
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
<div class="btn">BIO</div>
<div class="note"><span class="hand">← y te llega<br>por mensaje</span></div>
<div class="lead">y te mando la plantilla para escribir la tuya:</div>
<div class="box card">
 <div class="li"><div class="ck">{CHECK}</div><div>Las 3 líneas, con 9 ejemplos<span>De rubros distintos, para que veas el patrón.</span></div></div>
 <div class="li"><div class="ck">{CHECK}</div><div>El prompt para la IA<span>Te propone 5 versiones con tu forma de hablar.</span></div></div>
 <div class="li"><div class="ck">{CHECK}</div><div>Un armador que cuenta los caracteres<span>Completás 3 casillas y la copiás tal cual.</span></div></div>
</div>
<div class="small">Si querés que la revisemos juntos, <b>en la plantilla está el link para agendar.</b></div>""", pie="GUARDALO ↓")

for n, h in L.items():
    open(os.path.join(AQUI, f"lamina-{n:02d}.html"), "w").write(h)
print("ok", sorted(L))
