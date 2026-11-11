# LARP Games

A personal game library site for your HTML games — with search and favorites.

## Setup

1. **Drop your HTML games** into the `games/` folder.
2. **Run the scanner** to generate the game list:
   ```bash
   python scan.py
   # or, if you don't have Python:
   bash scan.sh
   ```
3. **Open `index.html`** in a browser (or serve it with a local server).

## Running locally

Because the site fetches `games/index.json`, you need a local HTTP server
(browsers block `fetch()` on bare `file://` URLs).

**Python (easiest):**
```bash
cd larp-games
python -m http.server 8080
# then open http://localhost:8080
```

**Node / npx:**
```bash
npx serve .
```

**VS Code:** install the "Live Server" extension and click "Go Live".

## Adding a new game

1. Copy `yourgame.html` into `games/`
2. Run `python scan.py` again
3. Refresh the browser — the game appears automatically

## Customising names

Edit `games/index.json` directly:
```json
[
  { "name": "Dragon Quest", "file": "dragonquest.html" },
  { "name": "Space Invaders Remix", "file": "space.html" }
]
```

## File structure

```
larp-games/
├── index.html      ← the site
├── style.css
├── app.js
├── scan.py         ← run after adding games
├── scan.sh         ← bash alternative
├── README.md
└── games/
    ├── index.json  ← auto-generated game list
    ├── game1.html
    └── game2.html
```
