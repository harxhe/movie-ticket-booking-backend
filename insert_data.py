from sqlalchemy.orm import Session
from database import SessionLocal, User, Movie

session = SessionLocal()

test_users = [
    User(name="John Doe", email="john@example.com", password="hashed_pass1", role="user"),
    User(name="Alice Smith", email="alice@example.com", password="hashed_pass2", role="owner"),
    User(name="Bob Johnson", email="bob@example.com", password="hashed_pass3", role="user"),
]

test_movies = [
    Movie(title="Inception", genre="Sci-Fi", duration=148),
    Movie(title="The Dark Knight", genre="Action", duration=152),
    Movie(title="Interstellar", genre="Sci-Fi", duration=169),
]

session.add_all(test_users)
session.add_all(test_movies)
session.commit()
session.close()

print("✅ Test users and movies inserted successfully!")
