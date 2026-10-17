"""Rebuild the offline HTML. Standard-library only; no downloads needed."""
import base64,json
from pathlib import Path
root=Path(__file__).resolve().parent

js=(root/'app.js').read_text()
ui={k:'data:image/png;base64,'+base64.b64encode((root/'assets'/f).read_bytes()).decode() for k,f in [('logo','logo.png'),('menu','menubg.png'),('maker','makerbg.png')]}
js=js.replace("'use strict';","'use strict';\nconst UI_ASSETS="+json.dumps(ui,separators=(',',':'))+';',1)
js=js.replace('/* LAWN_EXTENSION */',(root/'lawn-tools.js').read_text())
js=js.replace('/* STATE_MEDIA_EXTENSION */',(root/'state-media.js').read_text())
js=js.replace('/* ABILITY_EXTENSION */',(root/'abilities.js').read_text().replace('/* CREATOR_EXPANSION */',(root/'expansion.js').read_text()))
js=js.replace('/* WORKSHOP_UI */',(root/'workshop-ui.js').read_text())
css=(root/'style.css').read_text()+'\n'+(root/'reference-ui.css').read_text()+'\n'+(root/'tablet.css').read_text()+'\n'+(root/'lawn-tools.css').read_text()+'\n'+(root/'workshop-ui.css').read_text()
css=':root{--menu-bg:url("'+ui['menu']+'");--maker-bg:url("'+ui['maker']+'")}\n'+css
font=root/'builder-heading.ttf'
if font.exists():
    css="@font-face{font-family:Garden;src:url(data:font/ttf;base64,"+base64.b64encode(font.read_bytes()).decode()+")}\n"+css+"\naside .logo span,.hero h1{font-family:Garden,system-ui,sans-serif;font-weight:400}"
html='''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1,interactive-widget=resizes-content"><title>Plants vs. Zombies Builder</title><style>CSS</style></head><body><div id="app"></div><div id="toast" role="status"></div><input id="packFile" type="file" accept=".json,.pvzpack" hidden><script id="embeddedProject" type="application/octet-stream"></script><script>JS</script></body></html>'''.replace('<style>CSS</style>','<style>'+css+'</style>').replace('<script>JS</script>','<script>'+js.replace('</script','<\\/script')+'</script>')
(root/'index.html').write_text(html)
print('Built index.html:',len(html.encode()),'bytes; empty project, no preset media.')
