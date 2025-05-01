#!/bin/bash

# Build Vue app
cd client
npm install
npm run build
cd ..

# Start Flask
gunicorn --bind=0.0.0.0:8000 --timeout 120 --workers=4 app:app