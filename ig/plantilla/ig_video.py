# Graba una lámina animada (HTML con animaciones CSS) como video MP4 para un carrusel de Instagram.
# Uso: python3 ig_video.py lamina.html segundos salida.mp4 [fps=30]
# Calidad: cuadro por cuadro (sin perder cuadros), 1080x1350, H.264 High CRF 16 preset slow, audio mudo AAC, +faststart.
# También guarda salida.jpg (el último cuadro) para usar como portada o vista previa.
import sys, os, asyncio, subprocess, tempfile, shutil
from playwright.async_api import async_playwright
html, secs, out = sys.argv[1], float(sys.argv[2]), sys.argv[3]
fps = int(sys.argv[4]) if len(sys.argv) > 4 else 30
async def main(d):
    async with async_playwright() as p:
        b = await p.chromium.launch(executable_path=os.environ.get("CHROME", "/usr/bin/google-chrome"))
        pg = await (await b.new_context(viewport={"width": 1080, "height": 1350}, device_scale_factor=1)).new_page()
        await pg.goto("file://" + os.path.abspath(html)); await pg.evaluate("document.fonts.ready"); await pg.wait_for_timeout(400)
        await pg.evaluate("document.getAnimations().forEach(a=>a.pause())")
        n = int(secs * fps)
        for i in range(n):
            await pg.evaluate(f"document.getAnimations().forEach(a=>{{a.currentTime={i*1000/fps}}})")
            await pg.screenshot(path=f"{d}/f{i:05d}.png")
        await b.close()
    shutil.copy(f"{d}/f{n-1:05d}.png", out.rsplit('.',1)[0] + "-ultimo.png")
d = tempfile.mkdtemp(); asyncio.run(main(d))
subprocess.run(["ffmpeg","-y","-loglevel","error","-framerate",str(fps),"-i",f"{d}/f%05d.png",
  "-f","lavfi","-i","anullsrc=r=44100:cl=stereo","-shortest",
  "-c:v","libx264","-preset","slow","-crf","16","-profile:v","high","-pix_fmt","yuv420p","-r",str(fps),
  "-c:a","aac","-b:a","128k","-movflags","+faststart",out], check=True)
from PIL import Image
Image.open(out.rsplit('.',1)[0] + "-ultimo.png").convert("RGB").save(out.rsplit('.',1)[0] + ".jpg", "JPEG", quality=95, subsampling=0)
os.remove(out.rsplit('.',1)[0] + "-ultimo.png"); shutil.rmtree(d)
print("ok", out)
