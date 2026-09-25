# -*- coding: utf-8 -*-
"""QA: gera o PDF A4 do kit liberado (sem pagar) via Chrome headless, pra conferir impressão.
Uso: python tools/pdftest.py <saida.pdf> [noiva] [noivo] [n] [estilo] [pal] [tipo] [free]
Precisa do servidor local em http://localhost:8137 (apps/)."""
import sys, os, subprocess, json
CH = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(HERE)
out = os.path.abspath(sys.argv[1]); a = sys.argv + [None]*9
cfg = dict(noiva=a[2] or 'Mariana', noivo=a[3] if a[3] is not None else 'Rafael', n=int(a[4] or 40), estilo=a[5] or 'moderno', pal=a[6] or 'rose', tipo=a[7] or 'panela', data='2026-11-14')
free = (a[8] == 'free')
s = open(os.path.join(ROOT, 'index.html'), encoding='utf-8').read()
boot = "load();bindForm();render();"
assert boot in s
inj = f"load();Object.assign(D,{json.dumps(cfg)});UNLOCKED={'false' if free else 'true'};window.print=()=>{{}};bindForm();render();" + ("imprimirGratis();" if free else "printPages(PAGES(V()),false);")
s = s.replace(boot, inj).replace("function track(e,m){", "function track(e,m){return;")
tmp = os.path.join(ROOT, '_pdftest.html'); open(tmp, 'w', encoding='utf-8').write(s)
try:
    subprocess.run([CH, "--headless=new", "--disable-gpu", "--no-pdf-header-footer", "--virtual-time-budget=8000",
                    f"--print-to-pdf={out}", "http://localhost:8137/cha-de-panela/_pdftest.html"], check=True,
                   stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
finally:
    os.remove(tmp)
print("ok", out)
