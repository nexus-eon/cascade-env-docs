#!/bin/bash
set -e  # Exit on error

# Start the documentation server in the background
echo "Starting documentation server..."
mkdocs serve &
SERVER_PID=$!

# Wait for server to start
echo "Waiting for server to be ready..."
sleep 5

# Generate screenshots
echo "Generating screenshots..."
./tools/generate_screenshots.sh

# Kill the server
echo "Cleaning up..."
kill $SERVER_PID

# Build the documentation
echo "Building documentation..."
mkdocs build

echo "Documentation build complete with fresh screenshots!"
