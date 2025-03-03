from sqlalchemy.orm import Session
from database import SessionLocal, Booking, User, Movie

session = SessionLocal()

user1 = session.query(User).filter_by(email="john@example.com").first()  # Regular user
user2 = session.query(User).filter_by(email="bob@example.com").first()  # Another regular user
movie1 = session.query(Movie).filter_by(title="Inception").first()
movie2 = session.query(Movie).filter_by(title="The Dark Knight").first()

test_bookings = [
    Booking(user_id=user1.id, movie_id=movie1.id),
    Booking(user_id=user1.id, movie_id=movie2.id),
    Booking(user_id=user2.id, movie_id=movie1.id),
]

session.add_all(test_bookings)
session.commit()
session.close()

print("✅ Test bookings inserted successfully!")
