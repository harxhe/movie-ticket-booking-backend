from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

db = SQLAlchemy() 
bcrypt = Bcrypt()  

#Make a new user class with all the parameters id,name,email,password and role
class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    role = db.Column(db.Enum("user", "owner", name="role_enum"), nullable=False) #role can be either user or owner

    def set_password(self, raw_password):
        """Hashes the password and stores it securely."""
        self.password = bcrypt.generate_password_hash(raw_password).decode("utf-8") #hashes the password before storing it to ensure security

    def check_password(self, raw_password):
        """Verifies a password against the stored hash."""
        return bcrypt.check_password_hash(self.password, raw_password) #checks if the password given matches with the hashed passowrd stored in db

#Make a new movie class with parameters as movie_id, title,genre and duration in minutes
class Movie(db.Model):
    __tablename__ = "movies"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    genre = db.Column(db.String(100), nullable=False)
    duration = db.Column(db.Integer, nullable=False)  

#Make a new booking class which will store the booking made by a user, it will have booking_id,user_id,movie_id and number of seats under that booking
class Booking(db.Model):
    __tablename__ = "bookings"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    show_id = db.Column(db.Integer, db.ForeignKey("shows.id"), nullable=False)
    num_seats = db.Column(db.Integer, nullable=False)

    user = db.relationship("User", backref="bookings")
    show = db.relationship("Show", backref="bookings")

#Make a new show class to store the available shows
#Parameters are show_id,movie_id,theater_name,show_time and available seats  
class Show(db.Model):
    __tablename__ = "shows"

    id = db.Column(db.Integer, primary_key=True)
    movie_id = db.Column(db.Integer, db.ForeignKey("movies.id"), nullable=False)
    theater_name = db.Column(db.String, nullable=False)
    show_time = db.Column(db.String, nullable=False)  # Example: "2025-03-04 18:00"
    available_seats = db.Column(db.Integer, nullable=False)

    movie = db.relationship("Movie", backref="shows")
