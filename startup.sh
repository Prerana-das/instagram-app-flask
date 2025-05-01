#!/bin/bash

# Navigate to application root
cd /home/site/wwwroot

# Install Node.js (Azure-specific location)
curl -fsSL https://deb.nodesource.com/setup_18.x | bash -
apt-get install -y nodejs

# Build Vue app
echo "Building Vue app..."
cd client
npm install
npm run build
cd ..

# Start Gunicorn with explicit path
gunicorn --bind=0.0.0.0:8000 \
         --workers=4 \
         --pythonpath=/home/site/wwwroot \
         --access-logfile - \
         --error-logfile - \
         app:app