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
while IFS= read -r file; do
    filename=$(basename "$file" .py)
    
    # Convert filename to title (replace underscores with spaces, capitalize each word)
    title=$(echo "$filename" | sed 's/_/ /g' | awk '{for(i=1;i<=NF;i++)$i=toupper(substr($i,1,1))substr($i,2)}1')
    
    if [ "$first" = false ]; then
        metadata="${metadata},"
    fi
    first=false
    
    # Add entry to metadata
    metadata="${metadata}
    \"$filename\": {
      \"title\": \"$title\",
      \"description\": \"Interactive notebook on $title\",
      \"url\": \"./python/$filename\"
    }"
    
    echo -e "${GREEN}✓${NC} Found: $filename"
done < <(find "$PYTHON_EXERCISES_DIR" -name "*.py" -type f ! -path "*/__pycache__/*" ! -path "*/__marimo__/*" | sort)

# Close the JSON structure
metadata="${metadata}
  }
}"

# Write to file
echo "$metadata" > "$METADATA_FILE"

echo -e "${GREEN}✅ Metadata file updated: $METADATA_FILE${NC}"
