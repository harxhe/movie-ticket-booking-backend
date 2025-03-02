from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Enum
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

# SQLite Database URL
DATABASE_URL = "sqlite:///movies.db"

# Create Database Engine
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

# Create Session
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)  # Hash later
    role = Column(Enum("user", "owner", name="role_enum"), nullable=False)

class Movie(Base):
    __tablename__ = "movies"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    genre = Column(String, nullable=False)
    duration = Column(Integer, nullable=False)  # Duration in minutes

class Booking(Base):
    __tablename__ = "bookings"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    movie_id = Column(Integer, ForeignKey("movies.id"))
    
    user = relationship("User")
    movie = relationship("Movie")

Base.metadata.create_all(engine)
