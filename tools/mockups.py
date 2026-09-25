# -*- coding: utf-8 -*-
"""Gera og.png (1200x630) e 3 pins (1000x1500) fotografando páginas reais do kit (PDF via tools/pdftest.py).
Rodar de apps/cha-de-panela com o servidor local no ar: python tools/mockups.py"""
import os, subprocess, pymupdf
CH = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(HERE); TMP = os.path.join(HERE, "_mock"); os.makedirs(TMP, exist_ok=True)
def kit(name, *args):
    pdf = os.path.join(TMP, name + ".pdf")
    subprocess.run(["python", os.path.join(HERE, "pdftest.py"), pdf, *args], check=True, stdout=subprocess.DEVNULL)
    d = pymupdf.open(pdf); out = []
    for i in range(len(d)):
        p = os.path.join(TMP, f"{name}-{i+1}.png"); d[i].get_pixmap(dpi=110).save(p); out.append(p)
    return out
A = kit("rose", "Mariana", "Rafael", "20", "moderno", "rose", "panela")
B = kit("salvia", "Beatriz", "Lucas", "12", "rustico", "salvia", "cozinha")
C = kit("cristao", "Débora", "Samuel", "12", "cristao", "serenity", "panela")
def u(p): return "file:///" + p.replace("\\", "/")
FONTS = '<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,600;1,600&family=Great+Vibes&family=Nunito:wght@700;800;900&display=swap" rel="stylesheet">'
BASE = """body{margin:0;overflow:hidden;font-family:Nunito,sans-serif}
.bg{position:absolute;inset:0;background:radial-gradient(circle at 25% 15%,#fff7f5,#f3dfe1 70%)}
.dots{position:absolute;inset:0;background-image:radial-gradient(rgba(181,87,107,.18) 1.5px,transparent 2px);background-size:34px 34px}
.hl{position:absolute;color:#2d2327;font-family:'Cormorant Garamond',serif;font-weight:600;line-height:1.02}
.hl em{font-family:'Great Vibes',cursive;font-style:normal;font-weight:400;color:#b5576b}
.sub{position:absolute;color:#5a4a4f;font-weight:700}
.pill{position:absolute;background:#8f3f52;color:#fff;font-weight:900;border-radius:999px;padding:14px 30px;box-shadow:0 10px 24px rgba(143,63,82,.3)}
.pg{position:absolute;box-shadow:0 24px 50px rgba(60,30,40,.28);border-radius:4px}"""
def shot(name, w, h, body):
    src = os.path.join(TMP, name + ".html"); out = os.path.join(ROOT, name + ".png")
    open(src, "w", encoding="utf-8").write(f'<!doctype html><html><head><meta charset="utf-8">{FONTS}<style>{BASE}</style></head><body style="width:{w}px;height:{h}px;position:relative">{body}</body></html>')
    subprocess.run([CH, "--headless=new", "--disable-gpu", "--hide-scrollbars", "--allow-file-access-from-files", f"--window-size={w},{h}",
                    "--virtual-time-budget=6000", f"--screenshot={out}", u(src)], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    print("ok", out)
def img(p, x, y, wd, rot=0): return f'<img class="pg" src="{u(p)}" style="left:{x}px;top:{y}px;width:{wd}px;transform:rotate({rot}deg)">'
shot("og", 1200, 630, '<div class="bg"></div><div class="dots"></div>'
     '<div class="hl" style="left:60px;top:80px;font-size:64px;width:560px">Brincadeiras de <em>chá de panela</em> com o nome da noiva</div>'
     '<div class="sub" style="left:62px;top:330px;font-size:25px;width:520px">Bingo com até 40 cartelas diferentes, quem conhece a noiva, stop e prendas — nas cores do chá.</div>'
     '<div class="pill" style="left:60px;top:480px;font-size:25px">Veja a prévia grátis ✨</div>'
     + img(A[2], 880, 70, 300, 6) + img(A[0], 640, 40, 320, -4))
PINS = [
  ("pin-kit-cha-de-panela", "Kit de brincadeiras do <em>chá de panela</em>", "com o nome da noiva e as cores da decoração", [img(A[5] if len(A) > 5 else A[2], 470, 470, 470, 5), img(A[0], 90, 430, 480, -4)], "Prévia grátis · imprima em casa"),
  ("pin-bingo-cartelas-unicas", "Bingo do chá com <em>cartelas diferentes</em>", "até 40 cartelas únicas, prontas pra recortar", [img(B[3], 470, 500, 450, 5), img(B[2], 80, 440, 500, -3)], "Chega de 3 bingos no mesmo presente"),
  ("pin-cha-de-panela-evangelico", "Chá de panela <em>cristão</em>, prontinho", "brincadeiras 100% família, com versículo na capa", [img(C[-1], 480, 500, 440, 5), img(C[0], 90, 440, 480, -4)], "Stop bíblico · quem conhece a noiva · prendas"),
]
for name, t1, t2, imgs, pill in PINS:
    shot(name, 1000, 1500, '<div class="bg"></div><div class="dots"></div>'
         f'<div class="hl" style="left:60px;top:80px;font-size:84px;width:880px;text-align:center">{t1}</div>'
         f'<div class="sub" style="left:80px;top:320px;font-size:32px;width:840px;text-align:center">{t2}</div>'
         + "".join(imgs) + f'<div class="pill" style="left:50%;transform:translateX(-50%);bottom:70px;font-size:32px;white-space:nowrap">{pill}</div>')
