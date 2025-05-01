#!/bin/bash

# Navigate to client and build
cd client
npm install
npm run build
cd ..

# Start Flask
gunicorn --bind=0.0.0.0:8000 app:app