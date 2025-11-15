#!/bin/bash
# Script to automatically generate metadata.json from Python notebooks

set -e

# Colors for output
BLUE='\033[0;34m'
GREEN='\033[0;32m'
NC='\033[0m' # No Color

SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
PYTHON_EXERCISES_DIR="$SCRIPT_DIR/../python/exercises"
METADATA_FILE="$SCRIPT_DIR/metadata.json"

echo -e "${BLUE}🔍 Scanning for Python notebooks in $PYTHON_EXERCISES_DIR${NC}"

# Start building the JSON structure
metadata=$(cat <<'EOF'
{
  "title": "Churuchuru - Interactive Learning Notebooks",
  "subtitle": "Learn Python programming with interactive Marimo notebooks",
  "description": "Explore interactive Python notebooks built with Marimo. Learn programming concepts through hands-on examples.",
  "notebooks": {
EOF
)

first=true

# Find all .py files and generate notebook entries
find "$PYTHON_EXERCISES_DIR" -name "*.py" -type f ! -path "*/__pycache__/*" ! -path "*/__marimo__/*" | sort | while read file; do
    filename=$(basename "$file" .py)
    
    # Convert filename to title (replace underscores with spaces, capitalize)
    title=$(echo "$filename" | sed 's/_/ /g' | sed 's/\b\(.\)/\U\1/g')
    
    if [ "$first" = false ]; then
        metadata="${metadata},"
    fi
    first=false
    
    # Add entry to metadata
    metadata="${metadata}
    \"$filename\": {
      \"title\": \"$title\",
      \"description\": \"Interactive notebook on $title\",
      \"icon\": \"📚\"
    }"
    
    echo -e "${GREEN}✓${NC} Found: $filename"
done

# Close the JSON structure
metadata="${metadata}
  }
}"

# Write to file
echo "$metadata" > "$METADATA_FILE"

echo -e "${GREEN}✅ Metadata file updated: $METADATA_FILE${NC}"
