from flask import Flask, jsonify, send_from_directory
from database import db
from flask_migrate import Migrate
from flask_cors import CORS
import os

app = Flask(__name__, static_folder="client/dist", static_url_path="/")

# Enable CORS for API routes only
CORS(app, resources={r"/api/*": {"origins": "http://localhost:5173"}})

# ------------------ Database Config ------------------
# Use environment variable or direct connection string
# app.config["SQLALCHEMY_DATABASE_URI"] = 'mysql+pymysql://root:password@localhost:3306/instagram_app'
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get(
    'DATABASE_URL',
    'mysql+pymysql://preranaadmin:helloworld123%40@instagram.mysql.database.azure.com/instagram_app'
)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# SSL Required for Azure MySQL
app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {
    'connect_args': {
        'ssl': {
            'ssl_ca': '/etc/ssl/certs/ca-certificates.crt'
        }
    }
}

# Initialize database
db.init_app(app)
from models import (
    User, 
    Post,
    Comment,    
    Like,
    Message,
    Notification
)
migrate = Migrate(app, db)

# Serve Static Files
# @app.route('/<path:path>')
# # def serve_static(path):
# #     if path.startswith('api/'):
# #         return "Not Found", 404
# #     if os.path.exists(os.path.join(app.static_folder, path)):
# #         return send_from_directory(app.static_folder, path)
# #     return send_from_directory(app.static_folder, 'index.html')
# def serve_vue(path):
#     if path.startswith('api/'):
#         return "Not Found", 404
    
#     file_path = os.path.join(app.static_folder, path)
#     if os.path.exists(file_path):
#         return send_from_directory(app.static_folder, path)
#     else:
#         # Catch-all: return index.html for Vue routes like /profile
#         return send_from_directory(app.static_folder, 'index.html')
    

# # Catch Root Route
# @app.route('/')
# def serve_root():
#     return send_from_directory(app.static_folder, 'index.html')

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    # if path.startswith('api/'):
    #     return "Not Found", 404

    # Serve index.html for all frontend routes (Vue will handle them)
    return send_from_directory(app.static_folder, 'index.html')


# API Route Example
# ------------------ API Route ------------------
@app.route('/api/posts')
def get_posts():
    posts = Post.query.join(User).all()
    post_list = [{
        'id': post.id,
        'caption': post.caption,
        'image_url': post.image_url,
        'user': {
            'id': post.author.id,
            'username': post.author.username,
            'profile': post.author.profile
        }
    } for post in posts]
    return jsonify(post_list)

@app.route('/api/dbtest')
def db_test():
    try:
        users = User.query.all()
        return {"status": "success", "user_count": len(users)}
    except Exception as e:
        return {"status": "error", "message": str(e)}, 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)