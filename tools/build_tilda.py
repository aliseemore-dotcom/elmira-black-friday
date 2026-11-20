#!/usr/bin/env python3
"""Собирает один файл для блока «HTML-код» (T123) в Tilda: tilda/bf-tilda.html.
Запуск из папки black-friday:  python3 tools/build_tilda.py
"""
import os
root = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
rd = lambda n: open(os.path.join(root, n), encoding='utf-8').read()
h, css, cfg, js = rd('index.html'), rd('styles.css'), rd('config.js'), rd('main.js')
# Боевая сборка: без заглушек, картинки с GitHub Pages
BASE = 'https://aliseemore-dotcom.github.io/elmira-black-friday/assets/'
cfg = cfg.replace('previewMode: true', 'previewMode: false')
cfg = __import__('re').sub(r"images: \{[^}]*\}", "images: { " + ", ".join("'%s': '%s%s.jpg'" % (n, BASE, n) for n in ['bride','bathroom','evening','vanity','dior','envelope','tablet','elmira-mirror','bg-flowers']) + " }", cfg)
body = h.split('<body>', 1)[1].split('<script src="config.js">', 1)[0]
out = '''<!-- Black Friday · Эльмира Первакова. Вставьте целиком в блок T123 «HTML-код» на ПУСТОЙ странице Tilda.
     Картинки подгружаются с GitHub Pages (должен быть включён). Настройки в блоке config ниже. -->
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400;600&family=Oranienbaum&display=swap&subset=cyrillic" rel="stylesheet">
<style>
''' + css + '''
</style>
<div id="bf-root">''' + body.strip() + '''</div>
<script>
''' + cfg + '''
</script>
<script>
''' + js + '''
</script>
'''
os.makedirs(os.path.join(root, 'tilda'), exist_ok=True)
open(os.path.join(root, 'tilda', 'bf-tilda.html'), 'w', encoding='utf-8').write(out)
print('OK', len(out) // 1024, 'KB')
