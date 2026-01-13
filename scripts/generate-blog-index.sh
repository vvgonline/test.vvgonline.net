#!/bin/bash

# This script builds and runs the C# indexer tool to generate the blog index.

set -e

# Get the directory of the script
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"
PROJECT_DIR="$SCRIPT_DIR/../tools/Indexer"
OUTPUT_DIR="$SCRIPT_DIR/../src/wwwroot/data"

echo "Building the indexer tool..."
dotnet build "$PROJECT_DIR" -c Release

echo "Running the indexer tool..."
dotnet run --project "$PROJECT_DIR" -c Release

echo "Blog index generation complete."

