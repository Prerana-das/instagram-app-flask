from datetime import datetime
from app import app
from database import db
from models import User, Post, Like, Comment, Message, Notification

def seed_data():
    with app.app_context():
        # Clear existing data and create new tables
        db.drop_all()
        db.create_all()

        # Create sample users
        user1 = User(
            username='john_doe',
            email='john@example.com',
            profile='https://cdn.pixabay.com/photo/2015/04/23/22/00/new-year-background-736885_1280.jpg',
            address='New York, USA'
        )
        user2 = User(
            username='jane_smith',
            email='jane@example.com',
            profile='https://cdn.pixabay.com/photo/2015/04/23/22/00/new-year-background-736885_1280.jpg',
            address='London, UK'
        )

        db.session.add(user1)
        db.session.add(user2)
        db.session.commit()

        # Establish follower relationship (Jane follows John)
        user1.followers.append(user2)
        db.session.commit()

        # Create sample posts
        post1 = Post(
            caption='Beautiful sunset!',
            image_url='https://cdn.pixabay.com/photo/2015/04/23/22/00/new-year-background-736885_1280.jpg',
            user_id=user1.id
        )
        post2 = Post(
            caption='Mountain adventure',
            image_url='https://cdn.pixabay.com/photo/2015/04/23/22/00/new-year-background-736885_1280.jpg',
            user_id=user1.id
        )
        post3 = Post(
            caption='City vibes',
            image_url='https://cdn.pixabay.com/photo/2015/04/23/22/00/new-year-background-736885_1280.jpg',
            user_id=user2.id
        )

        db.session.add_all([post1, post2, post3])
        db.session.commit()

        # Create likes
        like1 = Like(user_id=user2.id, post_id=post1.id)
        like2 = Like(user_id=user2.id, post_id=post2.id)
        like3 = Like(user_id=user1.id, post_id=post3.id)

        db.session.add_all([like1, like2, like3])
        db.session.commit()

        # Create comments
        comment1 = Comment(
            content='Amazing shot, John!',
            user_id=user2.id,
            post_id=post1.id
        )
        comment2 = Comment(
            content='Love this city!',
            user_id=user1.id,
            post_id=post3.id
        )

        db.session.add_all([comment1, comment2])
        db.session.commit()

        # Create messages
        message1 = Message(
            content='Hi Jane, thanks for following!',
            sender_id=user1.id,
            receiver_id=user2.id
        )
        message2 = Message(
            content='Your photos are awesome, John!',
            sender_id=user2.id,
            receiver_id=user1.id
        )

        db.session.add_all([message1, message2])
        db.session.commit()

       # Create notifications
        notification1 = Notification(
            type='like',
            user_id=user1.id,
            post_id=post1.id,
            triggered_by_id=user2.id
        )
        notification2 = Notification(
            type='follow',
            user_id=user1.id,
            triggered_by_id=user2.id
        )
        db.session.add_all([notification1, notification2])
        db.session.commit()

        print("✅ Database seeded successfully!")

if __name__ == '__main__':
    seed_data()