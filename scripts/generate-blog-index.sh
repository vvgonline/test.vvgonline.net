#!/bin/bash

# Directory containing the blog posts
BLOG_DIR="src/wwwroot/assets/data/blogs"

# Output JSON file
OUTPUT_FILE="src/wwwroot/data/blog-index.json"

# Create or truncate the output file
echo "[]" > "$OUTPUT_FILE"

# Loop through all markdown files in the blog directory
for file in "$BLOG_DIR"/*.md; do
  # Extract front-matter using sed
  front_matter=$(sed -n '/^---$/,/^---$/p' "$file" | sed '1d;$d')

  # Parse front-matter and convert to JSON
  json_object=$(echo "$front_matter" | awk -F': ' '
    BEGIN {
      printf "{"
      first = 1
    }
    {
      key = $1
      # The rest of the line is the value
      value = substr($0, index($0, ":") + 2)
      # Remove leading/trailing whitespace from value
      gsub(/^[ \t]+|[ \t]+$/, "", value)
      # Remove quotes from value
      gsub(/