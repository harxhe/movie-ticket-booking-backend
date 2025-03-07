from flask import Flask, request, jsonify
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
from database import db, User , Movie , Show , Booking
import json

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///movies.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = 'this-is-top-secret'  

db.init_app(app)  
bcrypt = Bcrypt(app)
jwt = JWTManager(app)

#signup route
@app.route('/signup', methods=['POST'])
def signup():
    data = request.get_json() #get user data in json format 
    name = data.get('name')
    email = data.get('email')
    password = data.get('password')
    role = data.get('role') 

    if not name or not email or not password or role not in ["user", "owner"]: #check if all fields are filled
        return jsonify({"error": "Missing or invalid fields"}), 400

    if User.query.filter_by(email=email).first(): #check if email already exists
        return jsonify({'message': 'Email already registered'}), 400 

    new_user = User(name=name, email=email, role=role) #make a new object and add it to your table
    new_user.set_password(password)  
    db.session.add(new_user)
    db.session.commit()

    return jsonify({'message': 'User created successfully'}), 201

#login route
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json() #get login credentials in json format
    email = data.get('email')
    password = data.get('password')

    user = User.query.filter_by(email=email).first() #search for the user using his email and then check if the password is correct

    if user and user.check_password(password): 
        access_token = create_access_token(identity=json.dumps({'id': user.id, 'role': user.role}))
        return jsonify({'token': access_token}), 200

    return jsonify({'message': 'Invalid email or password'}), 401


@app.route('/movies', methods=['POST'])
@jwt_required() 
def add_movie():
    current_user = json.loads(get_jwt_identity()) 

    if current_user['role'] != 'owner': #only owners can access, check using jwt 
        return jsonify({"message": "Only theater owners can add movies"}), 403

    data = request.get_json() #get movie data in json format
    title = data.get('title')
    genre = data.get('genre')
    duration = data.get('duration')

    if not title or not genre or not duration: #check if all fields are filled
        return jsonify({"message": "All fields are required"}), 400

    new_movie = Movie(title=title, genre=genre, duration=duration) #add new movie in the database
    db.session.add(new_movie)
    db.session.commit()

    return jsonify({"message": "Movie added successfully"}), 201

@app.route('/movies', methods=['GET'])
def get_movies():
    movies = Movie.query.all() 
    movies_list = [
        {"id": movie.id, "title": movie.title, "genre": movie.genre, "duration": movie.duration}
        for movie in movies
    ]
    return jsonify(movies_list), 200 #return all movies in json format 

@app.route('/shows', methods=['POST'])
@jwt_required()
def add_show():
    current_user = json.loads(get_jwt_identity()) 

    if current_user['role'] != 'owner': #check if the current user is owner using his jwt identity
        return jsonify({'message': 'Only owners can add shows'}), 403

    data = request.get_json() #get show data in json format 
    movie_id = data.get('movie_id')
    theater_name = data.get('theater_name')
    show_time = data.get('show_time')
    available_seats = data.get('available_seats')

    if not all([movie_id, theater_name, show_time, available_seats]): #check if all fields are filled 
        return jsonify({'message': 'All fields are required'}), 400

    new_show = Show(movie_id=movie_id, theater_name=theater_name, show_time=show_time, available_seats=available_seats) #make a new object using Show class and add it to the database
    db.session.add(new_show)
    db.session.commit()

    return jsonify({'message': 'Show added successfully'}), 201

@app.route('/shows', methods=['GET'])
def get_shows():
    shows = Show.query.all() #make a get request to the /shows endpoint and return all available shows data in json format 
    
    result = []
    for show in shows:
        result.append({
            'id': show.id,
            'movie_title': show.movie.title,  
            'theater_name': show.theater_name,
            'show_time': show.show_time,
            'available_seats': show.available_seats
        })

    return jsonify(result), 200

@app.route('/book', methods=['POST'])
@jwt_required()
def book_ticket():
    current_user = json.loads(get_jwt_identity()) 
    data = request.get_json() #get booking data such as show_id and number of seats to be booked 
    show_id = data.get('show_id')
    num_seats = data.get('num_seats', 1) 

    show = Show.query.get(show_id) #check if the show_id is valid and it exists 
    if not show:
        return jsonify({'message': 'Show not found'}), 404

    if show.available_seats < num_seats: #check if there are enough seats for the show
        return jsonify({'message': 'Not enough seats available'}), 400

    booking = Booking(user_id=current_user['id'], show_id=show_id, num_seats=num_seats) #create a booking and add it to the database 
    show.available_seats -= num_seats  #decrease the available seats

    db.session.add(booking)
    db.session.commit()

    return jsonify({'message': 'Booking successful'}), 201

@app.route('/my-bookings', methods=['GET'])
@jwt_required()
def my_bookings():
    current_user = json.loads(get_jwt_identity())
    bookings = Booking.query.filter_by(user_id=current_user['id']).all() #show all bookings made by a user using his user_id and then return it in json format 

    result = []
    for booking in bookings:
        result.append({
            'booking_id': booking.id,
            'movie_title': booking.show.movie.title,
            'theater_name': booking.show.theater_name,
            'show_time': booking.show.show_time,
            'num_seats': booking.num_seats
        })

    return jsonify(result), 200

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  
    app.run(debug=True)
