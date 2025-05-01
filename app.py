from flask import Flask, send_from_directory
import os

app = Flask(__name__, static_folder="client/dist", static_url_path="/")

# API Route (Test First)
@app.route("/api/test")
def test_api():
    return {"status": "working"}  # Simple test endpoint

# Serve Vue App
@app.route("/", defaults={"path": ""})
@app.route("/<path:path>")
def serve_vue(path):
    if path.startswith("api/"):
        return "Not Found", 404
    if os.path.exists(os.path.join(app.static_folder, path)):
        return send_from_directory(app.static_folder, path)
    return send_from_directory(app.static_folder, "index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)