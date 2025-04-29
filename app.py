from flask import Flask, jsonify, send_from_directory
from models import db, Post, User
from flask_cors import CORS
import os

# Create Flask app
app = Flask(__name__, static_folder="client/dist", static_url_path="")

# Enable CORS for API routes only
CORS(app, resources={r"/api/*": {"origins": "http://localhost:5173"}})

# Database configuration
app.config["SQLALCHEMY_DATABASE_URI"] = 'mysql+pymysql://root:password@localhost:3306/instagram_app'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize database
db.init_app(app)

# Create tables (only during development)
with app.app_context():
    db.create_all()

# ------------------- API ROUTES -------------------

# API to fetch posts
@app.route('/api/posts', methods=['GET'])
def get_posts():
    posts = Post.query.join(User).all()  # Assuming Post is related to User
    posts_list = [{
        'id': post.id,
        # 'username': post.user.username,  # Uncomment if you have a relation
        'image_url': post.image_url,
        'caption': post.caption
    } for post in posts]
    return jsonify(posts_list)

# ------------------- FRONTEND ROUTES -------------------

# Serve the Vue app (Home page)
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def serve_vue(path):
    if path != "" and os.path.exists(os.path.join(app.static_folder, path)):
        return send_from_directory(app.static_folder, path)
    else:
        return send_from_directory(app.static_folder, 'index.html')

# -------------------------------------------------------

if __name__ == "__main__":
    app.run(port=5001, debug=True)
