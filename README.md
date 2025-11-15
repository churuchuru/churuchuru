# Churuchuru - Interactive Learning Notebooks

A collection of interactive Python notebooks built with **Marimo**, served with a beautiful **Catppuccin Mocha** dark theme and **Hack Nerd Font** styling.

This is an experimental repo for me to have fun, teach my son, and hopefully other parents might find this useful.

## Quick Start

```bash
./run-server.sh
```

This will:
1. ✅ Check dependencies (Python, uv)
2. ✅ Setup Python environment
3. ✅ Generate notebook metadata
4. ✅ Export notebooks to HTML WASM (editable mode)
5. ✅ Regenerate minified CSS/JS for optimal performance ⚡
6. ✅ Start local web server
7. ✅ Open browser to http://localhost:8000

### Environment Setup (Optional but Recommended)

For best minification performance, install these tools once:

```bash
npm install -g cssnano-cli terser
```

Without them, the build script will use fallback sed-based minification.

## Developer Workflow

## Features

- 📚 **Interactive Notebooks**: Edit and run code directly in browser
- 🎨 **Catppuccin Mocha Theme**: Beautiful dark theme with 26-color palette
- 🖥️ **Terminal Style**: Hack Nerd Font for authentic coding experience
- 🔍 **Search**: Find notebooks by title, description, or filename
- 📱 **Responsive**: Works on desktop and mobile
- ⚡ **WASM Export**: Notebooks run in browser with full interactivity

## Project Structure

```
churuchuru/
├── run-server.sh              # Run this to test locally
├── README.md                  # This file
├── homepage/
│   ├── index.html            # Homepage
│   ├── script.js             # Homepage logic
│   ├── style.css             # Homepage styles
│   ├── marimo-theme.css      # Catppuccin Mocha theme
│   ├── metadata.json         # Notebook registry
│   └── generate-metadata.sh  # Generate metadata
├── python/
│   ├── exercises/            # Notebook .py files
│   ├── .marimo.toml          # Marimo config
│   └── pyproject.toml        # Python dependencies
├── build/                    # Generated (test only)
└── .github/
    └── workflows/
        └── publish-marimo.yml # GitHub Pages deployment
```

## Adding New Notebooks

1. Create a `.py` file in `python/exercises/`
2. Build with Marimo:
   ```bash
   uv run marimo create python/exercises/your_notebook.py
   ```
3. Re-run `./run-server.sh`

## Editing Homepage

When you edit `homepage/style.css` or `homepage/script.js`:

```bash
# 1. Make your changes
vim homepage/style.css

# 2. Run dev server (auto-regenerates minified files)
./run-server.sh

# 3. Test locally at http://localhost:8000

# 4. Commit your changes
git add homepage/style.* homepage/script.*
git commit -m "Update: description of changes"
```

**Note:** Minified files (`style.min.css`, `script.min.js`) are **automatically regenerated** by `run-server.sh`. You should commit them to ensure consistent production builds.

## Testing Checklist

- [ ] Homepage displays with search bar and notebook cards
- [ ] Click notebook opens in edit mode
- [ ] Dark theme (Catppuccin Mocha) applied
- [ ] Code is editable
- [ ] Run button executes code
- [ ] Search filters notebooks

## Deployment

Push to `main` branch to automatically deploy to GitHub Pages via GitHub Action.

The GitHub Action will:
1. Export all notebooks (edit mode)
2. Deploy to GitHub Pages

## Technologies

- **Marimo**: Interactive Python notebooks
- **WASM**: Browser-based Python execution
- **Catppuccin**: Beautiful color schemes
- **Tailwind CSS**: Modern styling framework

## Performance Optimization

### Overview

The homepage is optimized for speed with:

- **Inlined critical CSS** - Eliminates render-blocking styles
- **Deferred JavaScript** - Non-blocking script loading
- **Font optimization** - `font-display: swap` for instant text rendering
- **Minified assets** - 39% smaller files with automatic regeneration
- **Aggressive caching** - 30 days for CSS/JS, 1 year for fonts
- **CDN preconnect** - Faster connections to external resources

### Cache Headers

GitHub Pages automatically handles caching via their CDN:
- **CSS/JS**: Cached by GitHub's CDN
- **Fonts**: Long-lived cache (optimized via `font-display: swap`)
- **HTML**: Short-lived cache (allows quick updates)

All optimizations (minification, compression) work with GitHub's automatic caching.

### Automatic Regeneration

Optimization files are **automatically regenerated** every time you run:

```bash
./run-server.sh
```

This includes:
- `style.min.css` - Minified CSS
- `script.min.js` - Minified JavaScript
- Cache header configuration

### Core Maintainer

[Ritchie Ng](https://github.com/ritchieng)
