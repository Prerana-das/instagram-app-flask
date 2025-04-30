#!/bin/bash

# Install Python deps
pip install -r requirements.txt

# Build Vue app
cd client
npm install
npm run build
cd ..

# Apply DB migrations
flask db upgrade

# Start server on Azure's port
gunicorn --bind=0.0.0.0:${WEBSITES_PORT:-5000} --timeout 600 app:app