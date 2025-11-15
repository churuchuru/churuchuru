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
5. ✅ Start local web server
6. ✅ Open browser to http://localhost:8000

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
1. Export all notebooks (edit mode, Catppuccin Mocha theme)
2. Generate metadata
3. Deploy to GitHub Pages

## Technologies

- **Marimo**: Interactive Python notebooks
- **WASM**: Browser-based Python execution
- **Catppuccin**: Beautiful color schemes
- **Tailwind CSS**: Modern styling framework

## Core Maintainer
[Ritchie Ng](https://github.com/ritchieng)
