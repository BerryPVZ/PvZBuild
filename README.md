# Plants vs. Zombies Builder 1.1

An offline-capable HTML5 builder for your own plants, zombies, lawns, levels and campaigns.

**[Open the builder](https://berrypvz.github.io/PvZBuild/)**

## New in 1.1

- Refreshed lawn, level, campaign, Play, pack, guide and seed-selection menus.
- Tabbed editors, collection search, campaign stage controls, Play search and filters, and larger touch controls.
- 100 new plant-only abilities and 100 new zombie-only abilities, in addition to the 210 existing shared recipes. Each maker now offers 310 choices; 410 distinct abilities in total.
- See [all 200 additions and their mechanics](ABILITIES_1.1.md).

## Build your own content

The workshop starts empty. Import PNG/GIF art and MP3/WAV audio as embedded base64. Add per-state animation and SFX, custom mower designs and sounds, NPC dialogue, plant unlocks, weighted zombie pools, weather, water and roof tiles, draggable map-grid alignment, and full-screen gameplay.

Changes save in this browser. Export `.pvzpack` backups to move work between devices or from an offline copy to this website. Pack imports preserve older edition data. Export standalone HTML to share an offline builder with your project inside.

## Offline and source

Download `index.html` and open it in a browser. No network dependencies are required.

Editable source is in `source/`. Run `python3 source/build.py` to rebuild `source/index.html`; copy that file to the repository root to publish. GitHub Actions deploys changes to `main` to GitHub Pages.

Fan-made project. Plants vs. Zombies belongs to EA / PopCap.
