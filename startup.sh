# Start Gunicorn with explicit path
gunicorn --bind=0.0.0.0:8000 \
         --workers=4 \
         --pythonpath=/home/site/wwwroot \
         --access-logfile - \
         --error-logfile - \
         app:app