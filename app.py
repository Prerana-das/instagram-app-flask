from flask import Flask, send_from_directory
import os

app = Flask(__name__, static_folder="client/dist", static_url_path="/")

# API Route Example
@app.route('/api/posts')
def get_posts():
    return {"status": "API working"}

# Serve Static Files
@app.route('/<path:path>')
def serve_static(path):
    if path.startswith('api/'):
        return "Not Found", 404
    if os.path.exists(os.path.join(app.static_folder, path)):
        return send_from_directory(app.static_folder, path)
    return send_from_directory(app.static_folder, 'index.html')

# Catch Root Route
@app.route('/')
def serve_root():
    return send_from_directory(app.static_folder, 'index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)