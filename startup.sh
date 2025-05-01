#!/bin/bash

# Navigate to client and build
echo "Building starttt Vue..."
cd client
npm install
npm run build
cd ..


echo "Building enddd Vue..."

# Start Flask
gunicorn --bind=0.0.0.0:8000 app:app