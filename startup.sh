#!/bin/bash
cd client && npm install && npm run build
cd ..
gunicorn --bind=0.0.0.0:8000 --pythonpath=. app:app