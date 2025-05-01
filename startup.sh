#!/bin/bash

# Navigate to repository root
cd "$(dirname "$0")"  # Go to script's directory
cd ..                # Move up to project root

# Build Vue app
echo "Building Vue app..."
cd client
npm install
npm run build

# Start Flask
echo "Starting Gunicorn..."
cd ..
gunicorn --bind=0.0.0.0:8000 \
         --workers=4 \
         --timeout=120 \
         --pythonpath=. \
         app:app