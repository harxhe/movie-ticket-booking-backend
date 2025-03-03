from sqlalchemy.orm import Session
from database import SessionLocal, User, Movie

session = SessionLocal()

users = session.query(User).all()
print("\n📌 Users:")
for user in users:
    print(f"ID: {user.id}, Name: {user.name}, Email: {user.email}, Role: {user.role}")

movies = session.query(Movie).all()
print("\n🎬 Movies:")
for movie in movies:
    print(f"ID: {movie.id}, Title: {movie.title}, Genre: {movie.genre}, Duration: {movie.duration} min")

session.close()
