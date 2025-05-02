#!/bin/bash
# Install Node.js
curl -fsSL https://deb.nodesource.com/setup_18.x | bash -
apt-get install -y nodejs

# Use appropriate Node.js version
nvm install 18
nvm use 18

cd client && npm install && npm run build
cd ..
gunicorn --bind=0.0.0.0:8000 --pythonpath=. app:app