#!/bin/bash
# Install Node.js
curl -fsSL https://deb.nodesource.com/setup_18.x | sudo -E bash -
sudo apt-get install -y nodejs

cd client && npm install && npm run build
cd ..
gunicorn --bind=0.0.0.0:8000 --pythonpath=. app:app