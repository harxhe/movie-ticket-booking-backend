from sqlalchemy.orm import Session
from database import SessionLocal, Booking, User, Movie

session = SessionLocal()

bookings = session.query(Booking).all()

print("\n🎟️ Bookings:")
for booking in bookings:
    user = session.query(User).filter_by(id=booking.user_id).first()
    movie = session.query(Movie).filter_by(id=booking.movie_id).first()
    print(f"User: {user.name} booked Movie: {movie.title}")

session.close()
