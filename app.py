from flask import Flask, jsonify, send_from_directory, request, session
from database import db
from flask_migrate import Migrate
from flask_cors import CORS
import os
import uuid
from werkzeug.utils import secure_filename
from flask_session import Session
from flask_bcrypt import Bcrypt
from sqlalchemy import func, or_, and_, case


app = Flask(__name__, static_folder="client/dist", static_url_path="/")

app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['MAX_CONTENT_LENGTH'] = 50 * 1024 * 1024  # 50 MB limit
app.config['ALLOWED_EXTENSIONS'] = {'png', 'jpg', 'jpeg', 'gif', 'mp4', 'mov', 'avi'}

# Enable CORS for API routes only
CORS(app, resources={r"/api/*": {"origins": "http://localhost:5173"}})

# ------------------ Database Config ------------------
# Use environment variable or direct connection string
# app.config["SQLALCHEMY_DATABASE_URI"] = 'mysql+pymysql://root:password@localhost:3306/instagram_app'
# live database
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get(
    'DATABASE_URL',
    'mysql+pymysql://preranaadmin:helloworld123%40@instagram.mysql.database.azure.com/instagram_app'
)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#  SSL Required for Azure MySQL
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
bcrypt = Bcrypt(app)
app.config['SESSION_TYPE'] = 'filesystem'
Session(app)

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


# API Route Example
# ------------------ API Route  ------------------
@app.route('/api/posts')
def get_posts():
    user_id = session.get('user_id')  # Get current logged-in user
    if not user_id:
        return jsonify({'error': 'Unauthorized'}), 401

    posts = Post.query.join(User).order_by(Post.id.desc()).all()
    
    post_list = []
    for post in posts:
        # Total likes
        like_count = len(post.likes)

        # Check if current user has liked this post
        user_liked = any(like.user_id == user_id for like in post.likes)

        post_list.append({
            'id': post.id,
            'caption': post.caption,
            'image_url': post.image_url,
            'likes': like_count,
            'user_liked': user_liked,
            'user': {
                'id': post.author.id,
                'username': post.author.username,
                'profile': post.author.profile
            }
        })

    return jsonify(post_list)


@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

@app.route('/api/posts', methods=['POST'])
def create_post():
    caption = request.form.get('caption')
    location = request.form.get('location')
    user_id = request.form.get('user_id')
    file = request.files.get('file')

    # if not file or not allowed_file(file.filename):
    #     return jsonify({'error': 'Invalid or missing file'}), 400

    filename = secure_filename(file.filename)
    unique_filename = f"{uuid.uuid4().hex}_{filename}"
    save_path = os.path.join(app.config['UPLOAD_FOLDER'], unique_filename)

    # Create the uploads directory if it doesn't exist
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
    file.save(save_path)

    # Save post to the database
    post = Post(
        caption=caption,
        location=location,
        image_url=f"/{save_path}",
        user_id=user_id
    )
    db.session.add(post)
    db.session.commit()

    return jsonify({
        'message': 'Post created',
        'file_url': f"/{save_path}",
        'caption': caption,
        'location': location,
        'user_id': user_id
    })

# ------------------ followers Routes ------------------
@app.route('/api/followers/<int:user_id>', methods=['GET'])
def get_followers(user_id):
    user = User.query.get(user_id)
    if not user:
        return jsonify({'error': 'User not found'}), 404
    
    followers = user.followers.all()  # Get all followers
    followers_data = [{
        'id': follower.id,
        'username': follower.username,
        'profile': follower.profile
    } for follower in followers]
    
    return jsonify({'followers': followers_data}), 200

@app.route('/api/following/<int:user_id>', methods=['GET'])
def get_following(user_id):
    user = User.query.get(user_id)
    if not user:
        return jsonify({'error': 'User not found'}), 404
    
    following = user.following.all()  # Get all users that the user is following
    following_data = [{
        'id': followed.id,
        'username': followed.username,
        'profile': followed.profile
    } for followed in following]
    
    return jsonify({'following': following_data}), 200

@app.route('/api/follow/<int:user_id>', methods=['POST'])
def follow_user(user_id):
    data = request.get_json()
    followed_id = data.get('followed_id')
    
    user = User.query.get(user_id)
    followed_user = User.query.get(followed_id)
    
    if not user or not followed_user:
        return jsonify({'error': 'User(s) not found'}), 404
    
    if user.id == followed_user.id:
        return jsonify({'error': 'You cannot follow yourself'}), 400
    
    # Check if already following
    if followed_user in user.following:
        return jsonify({'error': 'Already following this user'}), 400
    
    user.following.append(followed_user)
    db.session.commit()
    
    return jsonify({'message': f'You are now following {followed_user.username}'}), 200


# ------------------ Authentication Routes ------------------
@app.route('/api/register', methods=['POST'])
def register():
    data = request.json
    name = data.get('name')
    username = data.get('username')
    email = data.get('email')
    password = data.get('password')

    if User.query.filter_by(email=email).first():
        return jsonify({'error': 'Email already exists'}), 400

    hashed_pw = bcrypt.generate_password_hash(password).decode('utf-8')

    user = User(name=name, username=username, email=email, password=hashed_pw)
    db.session.add(user)
    db.session.commit()

    session['user_id'] = user.id  # Create session
    return jsonify({'message': 'User registered successfully', 'user': {
        'id': user.id,
        'name': user.name,
        'username': user.username,
        'email': user.email
    }})

@app.route('/api/login', methods=['POST'])
def login():
    data = request.json
    email = data.get('email')
    password = data.get('password')

    user = User.query.filter_by(email=email).first()
    if not user or not bcrypt.check_password_hash(user.password, password):
        return jsonify({'error': 'Invalid credentials'}), 401

    session['user_id'] = user.id
    return jsonify({'message': 'Login successful', 'user': {
        'id': user.id,
        'name': user.name,
        'username': user.username,
        'email': user.email
    }})

@app.route('/api/logout', methods=['POST'])
def logout():
    session.pop('user_id', None)
    return jsonify({'message': 'Logged out'})



@app.route('/api/session', methods=['GET'])
def get_session_user():
    # Retrieve user ID from session (ensure the user is logged in)
    user_id = session.get('user_id')

    if not user_id:
        return jsonify({'error': 'User not logged in'}), 401

    # Fetch the user from the database
    user = User.query.get(user_id)

    if not user:
        return jsonify({'error': 'User not found'}), 404

    # Return the user data
    return jsonify({
        'id': user.id,
        'name': user.name,
        'bio': user.bio,
        'username': user.username,
        'email': user.email,
        'profile': user.profile,
        'followers': user.followers.count(),
        'following': user.following.count()
    })


@app.route('/api/users/<int:user_id>/posts', methods=['GET'])
def get_user_posts(user_id):
    # Fetch the user from the database
    user = User.query.get(user_id)

    if not user:
        return jsonify({'error': 'User not found'}), 404

    # Get posts for the user, ordered by most recent
    posts = Post.query.filter_by(user_id=user.id).order_by(Post.id.desc()).all()

    # Return the posts with user information
    post_list = [{
        'id': post.id,
        'caption': post.caption,
        'image_url': post.image_url,
        'location': post.location,
        'user': {
            'id': post.author.id,
            'username': post.author.username,
            'profile': post.author.profile
        }
    } for post in posts]

    return jsonify(post_list)

# ------------------ Profile Update Route Settings ------------------
@app.route('/api/update-profile', methods=['POST'])
def update_profile():
    user_id = session.get('user_id')
    if not user_id:
        return jsonify({'error': 'Not logged in'}), 401

    user = User.query.get(user_id)
    if not user:
        return jsonify({'error': 'User not found'}), 404

    user.name = request.form.get('name')
    user.location = request.form.get('location')

    if 'profile' in request.files:
        file = request.files['profile']

        filename = secure_filename(file.filename)
        unique_filename = f"{uuid.uuid4().hex}_{filename}"
        save_path = os.path.join(app.config['UPLOAD_FOLDER'], unique_filename)
        # Create the uploads directory if it doesn't exist
        os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
        file.save(save_path)
        user.profile=f"/{save_path}",

    db.session.commit()
    return jsonify({'success': True})


# ------------------ Message Route ------------------
@app.route('/api/messages')
def get_messages():
    user_id = session.get('user_id')
    if not user_id:
        return jsonify({'error': 'Not logged in'}), 401

    messages = Message.query.filter(
        (Message.sender_id == user_id) | (Message.receiver_id == user_id)
    ).order_by(Message.created_at.desc()).all()

    result = []
    for msg in messages:
        result.append({
            'id': msg.id,
            'content': msg.content,
            'created_at': msg.created_at.isoformat(),
            'sender': {
                'id': msg.sender.id,
                'username': msg.sender.username
            },
            'receiver': {
                'id': msg.receiver.id,
                'username': msg.receiver.username
            }
        })
    return jsonify(result)

@app.route('/api/conversations')
def get_conversations():
    user_id = session.get('user_id')
    if not user_id:
        return jsonify({'error': 'Unauthorized'}), 401

    # Get distinct users who have conversed with current user
    distinct_users = db.session.query(
        Message.receiver_id.label('other_user_id')
    ).filter(Message.sender_id == user_id).union_all(
        db.session.query(
            Message.sender_id.label('other_user_id')
        ).filter(Message.receiver_id == user_id)
    ).distinct().subquery()

    # Get latest message for each conversation
    conversations = db.session.query(
        User.id,
        User.username,
        User.profile,
        Message.content,
        Message.created_at
    ).join(
        Message,
        or_(
            and_(
                Message.sender_id == user_id,
                Message.receiver_id == User.id
            ),
            and_(
                Message.receiver_id == user_id,
                Message.sender_id == User.id
            )
        )
    ).filter(
        User.id.in_(db.session.query(distinct_users.c.other_user_id))
    ).order_by(
        Message.created_at.desc()
    ).all()

    # Group messages by user
    grouped = {}
    for conv in conversations:
        other_user_id = conv.id
        if other_user_id not in grouped:
            grouped[other_user_id] = {
                'user': {
                    'id': conv.id,
                    'username': conv.username,
                    'profile': conv.profile
                },
                'latest_message': {
                    'content': conv.content,
                    'timestamp': conv.created_at.isoformat()
                }
            }

    return jsonify(list(grouped.values()))


@app.route('/api/posts/<int:post_id>/like', methods=['POST'])
def like_post(post_id):
    user_id = session.get('user_id')
    if not user_id:
        return jsonify({'error': 'Unauthorized'}), 401

    # Check if user already liked this post
    existing_like = Like.query.filter_by(user_id=user_id, post_id=post_id).first()
    if existing_like:
        db.session.delete(existing_like)
        message = 'unliked'
    else:
        new_like = Like(user_id=user_id, post_id=post_id)
        db.session.add(new_like)
        message = 'liked'

    db.session.commit()

    # Return the new like count
    like_count = Like.query.filter_by(post_id=post_id).count()

    return jsonify({'likes': like_count, 'message': message})


@app.route('/api/dbtest')
def db_test():
    try:
        users = User.query.all()
        return {"status": "success", "user_count": len(users)}
    except Exception as e:
        return {"status": "error", "message": str(e)}, 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)