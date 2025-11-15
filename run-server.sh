#!/bin/bash
# Churuchuru Server - Build & Run Local Development Server

set -e

# Colors
BLUE='\033[0;34m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m'

SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
PYTHON_DIR="$SCRIPT_DIR/python"
HOMEPAGE_DIR="$SCRIPT_DIR/homepage"
BUILD_DIR="$SCRIPT_DIR/build"

echo -e "${BLUE}🚀 Churuchuru Server${NC}\n"

# Kill any existing process on port 8000
echo -e "${YELLOW}Cleaning up port 8000...${NC}"
lsof -i :8000 -t 2>/dev/null | xargs kill -9 2>/dev/null || true
sleep 1

# Check dependencies
if ! command -v python3 &> /dev/null; then
    echo -e "${RED}❌ Python 3 not found${NC}"
    exit 1
fi

if ! command -v uv &> /dev/null; then
    echo -e "${YELLOW}Installing uv...${NC}"
    curl -LsSf https://astral.sh/uv/install.sh | sh
fi

# Setup environment
echo -e "${YELLOW}Setting up...${NC}"
cd "$PYTHON_DIR" && uv sync > /dev/null 2>&1

# Generate metadata
cd "$HOMEPAGE_DIR" && bash generate-metadata.sh > /dev/null 2>&1

# Export notebooks
mkdir -p "$BUILD_DIR/python"
cd "$PYTHON_DIR"
find exercises -name "*.py" -type f | while read file; do
    filename=$(basename "$file" .py)
    notebook_dir="$BUILD_DIR/python/$filename"
    mkdir -p "$notebook_dir"
    uv run marimo export html-wasm "$file" -o "$notebook_dir/index.html" --mode edit > /dev/null 2>&1
done

# Copy files
cp "$HOMEPAGE_DIR"/{index.html,metadata.json,script.js,style.css} "$BUILD_DIR/"

echo -e "${GREEN}✓ Ready!${NC}\n"

# Find available port
find_available_port() {
    local port=8000
    while netstat -tuln 2>/dev/null | grep -q ":$port "; do
        port=$((port + 1))
    done
    echo $port
}

PORT=$(find_available_port)

# Start server
cd "$BUILD_DIR"
echo -e "${BLUE}📚 Server running at http://localhost:$PORT${NC}"
echo -e "${YELLOW}Press Ctrl+C to stop${NC}\n"

# Open browser
if [[ "$OSTYPE" == "darwin"* ]]; then
    open "http://localhost:$PORT" 2>/dev/null || true
elif command -v xdg-open &> /dev/null; then
    xdg-open "http://localhost:$PORT" 2>/dev/null || true
fi

python3 -m http.server $PORT
