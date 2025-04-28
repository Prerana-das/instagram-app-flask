from flask import Flask,jsonify, send_from_directory
from models import db, Post, User
from flask_cors import CORS
import os


# app = Flask(__name__, static_folder="client/dist", static_url_path="")
app = Flask(__name__, static_folder="path/to/static/files")


# Enable CORS for the entire app
# CORS(app, origins="http://localhost:5173")
# CORS(app, resources={r"/api/*": {"origins": "http://localhost:5173"}})

# Sample posts data
posts = [
    {"id": 1, "username": "prerana", "image": "https://via.placeholder.com/150", "caption": "Hello world!"},
    {"id": 2, "username": "alice", "image": "https://via.placeholder.com/150", "caption": "Beautiful day!"}
]

# 1. Configure your database
app.config["SQLALCHEMY_DATABASE_URI"] = 'mysql+pymysql://root:password@localhost:3306/instagram_app'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# 2. Initialize db with app
db.init_app(app)


# 3. Create the database tables
# This is a temporary block to create the database tables
# and should be removed in production.
with app.app_context():
    db.create_all()

# # API route
# @app.route("/api/posts")
# def get_posts():
#     return jsonify(posts)


# API route to get posts from the database
@app.route('/api/posts', methods=['GET'])
def get_posts():
    posts = Post.query.join(User).all()  # Assuming a relationship between Post and User
    posts_list = [{
        'id': post.id,
        # 'username': post.user.username,  # Get username from User model
        'image_url': post.image_url,
        'caption': post.caption
    } for post in posts]
    return jsonify(posts_list)

@app.route("/")
def serve_vue():
    return send_from_directory(app.static_folder, "index.html")

# Optional: handle Vue Router URLs
@app.route("/<path:path>")
def serve_vue_path(path):
    file_path = os.path.join(app.static_folder, path)
    if os.path.exists(file_path):
        return send_from_directory(app.static_folder, path)
    else:
        return send_from_directory(app.static_folder, "index.html")

if __name__ == "__main__":
    app.run(port=5001, debug=True) 
