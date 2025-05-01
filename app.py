from flask import Flask, send_from_directory
import os

app = Flask(__name__, static_folder="client/dist", static_url_path="/")

# API Test Endpoint
@app.route("/api/test")
def test():
    return {"status": "API working"}

# Serve Vue App
@app.route("/", defaults={"path": ""})
@app.route("/<path:path>")
def serve(path):
    if path.startswith("api/"):
        return "Not Found", 404
    if os.path.exists(os.path.join(app.static_folder, path)):
        return send_from_directory(app.static_folder, path)
    return send_from_directory(app.static_folder, "index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)