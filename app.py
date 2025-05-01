from flask import Flask, jsonify, send_from_directory
from database import db
from flask_migrate import Migrate
from flask_cors import CORS
import os

# Create Flask app
app = Flask(__name__, static_folder="client/dist", static_url_path="")


# Enable CORS for API routes only
CORS(app, resources={r"/api/*": {"origins": "http://localhost:5173"}})

# Database configuration
# app.config["SQLALCHEMY_DATABASE_URI"] = 'mysql+pymysql://root:password@localhost:3306/instagram_app'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize database
# db.init_app(app)
# from models import (
#     User, 
#     Post,
#     Comment,    
#     Like,
#     Message,
#     Notification
# )
# migrate = Migrate(app, db)



# Create tables (only during development)
# with app.app_context():
#     db.create_all()


# Serve the Vue app (Home page)
# @app.route('/', defaults={'path': ''})
@app.route('/')
def serve_vue():
    return send_from_directory('client/dist', 'index.html')

@app.route('/<path:path>')
def static_files(path):
    return send_from_directory('client/dist', path)

# @app.route('/<path:path>')
# def serve_vue(path):
#     if path != "" and os.path.exists(os.path.join(app.static_folder, path)):
#         return send_from_directory(app.static_folder, path)
#     else:
#         return send_from_directory(app.static_folder, 'index.html')
    
# ------------------- API ROUTES -------------------

# API to fetch posts
# @app.route('/api/posts', methods=['GET'])
# def get_posts():
#     posts = Post.query.join(User).all()  
#     posts_list = [{
#         'id': post.id,
#         'caption': post.caption,
#         'image_url': post.image_url,
#         'user': {
#             'id': post.author.id,
#             'username': post.author.username,
#             'profile': post.author.profile
           
#         }
#     } for post in posts]
    
#     return jsonify(posts_list)

# ------------------- FRONTEND ROUTES -------------------

# -------------------------------------------------------

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000)