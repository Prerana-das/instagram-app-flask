#!/bin/bash
# Install Node.js
export NVM_DIR="/usr/local/nvm"
[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"

# Use appropriate Node.js version
nvm install 18
nvm use 18

cd client && npm install && npm run build
cd ..
gunicorn --bind=0.0.0.0:8000 --pythonpath=. app:app