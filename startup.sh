#!/bin/bash

# Navigate to project root
cd /home/site/wwwroot

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
         --pythonpath=. \
         app:app