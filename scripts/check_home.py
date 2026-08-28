"""Inspeciona o HTML servido pela home para conferir imagens e vídeo."""

import re
import urllib.request

html = urllib.request.urlopen("http://127.0.0.1:8088/", timeout=5).read().decode("utf-8", "replace")

print("css v4:", "style.css?v=4" in html)
print("spotlight:", "spotlight" in html)
print("img:", re.findall(r"<img[^>]*src=\"([^\"]+)\"", html))
print("source:", re.findall(r"<source[^>]*src=\"([^\"]+)\"", html))
print("hero style:", re.findall(r"hero-media\"[^>]*", html))
