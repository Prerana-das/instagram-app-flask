from app import app
from models import db, User, Post

def seed_data():
    with app.app_context():
        # Optional: Drop and recreate tables if needed
        # db.drop_all()
        # db.create_all()

        # Check if there's already data
        if User.query.first():
            print("Data already exists, skipping seeding.")
            return

        # Create a User
        user1 = User(
            username='john_doe',
            password='password123',
            name='John Doe',
            profile='https://example.com/john.jpg',
            bio='Love photography!'
        )

        db.session.add(user1)
        db.session.commit()

        # Create some Posts
        post1 = Post(
            caption='Beautiful sunset!',
            image_url='https://cdn.pixabay.com/photo/2015/04/23/22/00/new-year-background-736885_1280.jpg',
            user_id=user1.id
        )
        post2 = Post(
            caption='Adventure time!',
            image_url='https://cdn.pixabay.com/photo/2015/04/23/22/00/new-year-background-736885_1280.jpg',
            user_id=user1.id
        )

        db.session.add(post1)
        db.session.add(post2)
        db.session.commit()

        print("✅ Database seeded successfully!")

if __name__ == '__main__':
    seed_data()
