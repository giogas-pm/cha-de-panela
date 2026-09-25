# -*- coding: utf-8 -*-
"""Gera as páginas de SEO do Kit do Chá + sitemap.xml. Rodar: python tools/gen_seo.py"""
import os, json, html, datetime
from content import CONTENT, GUIAS
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE = "https://giogas-pm.github.io/cha-de-panela/"
HOJE = datetime.date.today().isoformat()

CSS = """
  :root{--rose:#b5576b;--rose2:#8f3f52;--gold:#c9a15b;--ink:#2d2327;--bg:#fbf7f4;--muted:#7a6a6f;--line:#ecdfe0;--ok:#4f7a5a;--soft:#f8e6e8}
  *{box-sizing:border-box}
  html{-webkit-text-size-adjust:100%}
  body{margin:0;font-family:Nunito,system-ui,sans-serif;background:var(--bg);color:var(--ink);line-height:1.65;font-size:17px}
  a{color:var(--rose2)}
  header{display:flex;align-items:center;justify-content:space-between;flex-wrap:wrap;gap:6px;padding:14px 16px;max-width:1100px;margin:0 auto}
  .logo{font-weight:800;font-size:19px;color:var(--rose2);text-decoration:none}
  .trust{font-size:13px;color:var(--ok);font-weight:700}
  .wrap{max-width:780px;margin:0 auto;padding:0 16px}
  .crumbs{font-size:13px;color:var(--muted);margin:4px 0 0}
  .crumbs a{color:var(--muted)}
  h1{font-family:'Cormorant Garamond',serif;font-size:clamp(32px,7vw,48px);line-height:1.08;margin:10px 0 12px;font-weight:600}
  .lead{font-size:18px;color:#4a3b40}
  h2{font-family:'Cormorant Garamond',serif;font-size:clamp(26px,5vw,32px);line-height:1.15;margin:38px 0 8px;font-weight:600}
  h3{font-size:18px;margin:18px 0 4px}
  .toc{background:#fff;border:1px solid var(--line);border-radius:16px;padding:12px 18px;margin:18px 0;font-size:15.5px}
  .toc b{display:block;margin-bottom:4px}
  .toc ol{margin:0;padding-left:20px}
  .card{background:#fff;border:1px solid var(--line);border-radius:16px;padding:14px 18px;margin:12px 0}
  ul.l,ol.l{padding-left:22px}
  ul.l li,ol.l li{margin:6px 0}
  ul.cols{columns:2;column-gap:26px;padding-left:20px}
  @media(max-width:560px){ul.cols{columns:1}}
  table{width:100%;border-collapse:collapse;background:#fff;border-radius:12px;overflow:hidden;font-size:15.5px;margin:12px 0}
  th,td{border:1px solid var(--line);padding:8px 10px;text-align:left;vertical-align:top}
  th{background:var(--soft)}
  .tbl{overflow-x:auto}
  .btn{display:inline-block;border:0;border-radius:14px;padding:14px 20px;font:800 16px Nunito,sans-serif;cursor:pointer;text-decoration:none;text-align:center}
  .btn-main{background:linear-gradient(180deg,#c56a7e,var(--rose2));color:#fff;box-shadow:0 8px 18px rgba(143,63,82,.25)}
  .cta{background:#fff;border:2px solid var(--gold);border-radius:18px;padding:18px;margin:26px 0;text-align:center}
  .cta .ct{font-family:'Cormorant Garamond',serif;font-size:25px;font-weight:600;line-height:1.2;margin:0 0 6px}
  .cta p{margin:0 0 12px}
  .cta .btn{width:100%;max-width:420px}
  .cta-end{background:#fff7f8}
  .price{font-size:13px;color:var(--muted);margin:10px 0 0!important}
  .note{font-size:14.5px;color:var(--muted)}
  .faq details{background:#fff;border:1px solid var(--line);border-radius:14px;padding:10px 16px;margin:10px 0}
  .faq summary{font-weight:800;cursor:pointer}
  .rel{margin:40px 0 10px}
  .rel ul{list-style:none;padding:0;margin:0;display:grid;gap:8px}
  .rel li a{display:block;background:#fff;border:1px solid var(--line);border-radius:12px;padding:11px 14px;text-decoration:none;font-weight:700}
  footer{text-align:center;color:var(--muted);font-size:13px;padding:30px 16px 40px}
  footer nav{display:flex;flex-wrap:wrap;justify-content:center;gap:6px 14px;margin-bottom:10px}
  footer nav a{color:var(--muted)}
"""

def page(c):
    slug, title, desc = c["slug"], c["title"], c["desc"]
    assert len(title) <= 62, (slug, len(title), title)
    assert 70 <= len(desc) <= 158, (slug, len(desc), desc)
    url = BASE + slug + "/"
    ld = [{"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Kit do Chá", "item": BASE},
            {"@type": "ListItem", "position": 2, "name": c["crumb"], "item": url}]},
          {"@context": "https://schema.org", "@type": "Article", "headline": c["h1"].replace("<em>", "").replace("</em>", ""),
           "description": desc, "inLanguage": "pt-BR", "dateModified": HOJE, "mainEntityOfPage": url,
           "image": BASE + "og.png", "author": {"@type": "Organization", "name": "Kit do Chá"}}]
    if c.get("faq"):
        ld.append({"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
            {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": html.unescape(a)}} for q, a in c["faq"]]})
    if c.get("howto"):
        h = c["howto"]
        ld.append({"@context": "https://schema.org", "@type": "HowTo", "name": h["name"], "inLanguage": "pt-BR",
                   "step": [{"@type": "HowToStep", "position": i + 1, "name": s[0], "text": s[1]} for i, s in enumerate(h["steps"])]})
    faq = ""
    if c.get("faq"):
        faq = '<section class="faq"><h2>Perguntas frequentes</h2>' + "".join(
            f"<details><summary>{html.escape(q)}</summary><p>{a}</p></details>" for q, a in c["faq"]) + "</section>"
    rel = "".join(f'<li><a href="/cha-de-panela/{s}/">{lab}</a></li>' for s, lab in GUIAS if s != slug)
    foot = "".join(f'<a href="/cha-de-panela/{s}/">{lab}</a>' for s, lab in GUIAS)
    lds = "\n".join(f'<script type="application/ld+json">{json.dumps(x, ensure_ascii=False)}</script>' for x in ld)
    return f"""<!doctype html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{html.escape(title, quote=False)}</title>
<meta name="description" content="{html.escape(desc)}">
<link rel="canonical" href="{url}">
<meta property="og:title" content="{html.escape(title)}">
<meta property="og:description" content="{html.escape(desc)}">
<meta property="og:type" content="article">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{BASE}og.png">
<meta property="og:locale" content="pt_BR">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'%3E%3Ctext y='.9em' font-size='90'%3E🎀%3C/text%3E%3C/svg%3E">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@600&family=Nunito:wght@400;700;800&display=swap" rel="stylesheet">
<style>{CSS}</style>
{lds}
</head>
<body>
<header><a class="logo" href="/cha-de-panela/">🎀 Kit do Chá</a><span class="trust">✓ brincadeiras prontas pra imprimir</span></header>
<main class="wrap">
<nav class="crumbs" aria-label="Você está em"><a href="/cha-de-panela/">Kit do Chá</a> › {c["crumb"]}</nav>
<h1>{c["h1"]}</h1>
{c["body"]}
{faq}
<section class="rel"><h2>Mais guias do chá</h2><ul>{rel}<li><a href="/cha-de-panela/?src=seo&amp;p={slug}">Montar o kit personalizado do meu chá</a></li></ul></section>
</main>
<footer><nav aria-label="Guias de chá de panela"><a href="/cha-de-panela/">Kit do Chá (início)</a>{foot}</nav>Kit do Chá · feito com carinho no Brasil</footer>
</body>
</html>
"""

urls = [(BASE, "1.0")]
for c in CONTENT:
    d = os.path.join(ROOT, c["slug"]); os.makedirs(d, exist_ok=True)
    with open(os.path.join(d, "index.html"), "w", encoding="utf-8", newline="\n") as f:
        f.write(page(c))
    words = len(html.unescape(c["body"]).split())
    urls.append((BASE + c["slug"] + "/", "0.8"))
    print(f'{c["slug"]:45} title={len(c["title"])} desc={len(c["desc"])} palavras~{words} ctas={c["body"].count("class=\"cta")}')
sm = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + "".join(
    f"  <url><loc>{u}</loc><lastmod>{HOJE}</lastmod><priority>{p}</priority></url>\n" for u, p in urls) + "</urlset>\n"
open(os.path.join(ROOT, "sitemap.xml"), "w", encoding="utf-8", newline="\n").write(sm)
open(os.path.join(ROOT, "robots.txt"), "w", encoding="utf-8", newline="\n").write(f"User-agent: *\nAllow: /\nSitemap: {BASE}sitemap.xml\n")
print("sitemap:", len(urls), "urls")
