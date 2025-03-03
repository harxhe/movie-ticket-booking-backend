from flask import Flask, request, jsonify
from sqlalchemy.orm import Session
from database import SessionLocal, User
from flask_bcrypt import Bcrypt

app = Flask(__name__)
bcrypt = Bcrypt(app)


@app.route("/signup", methods=["POST"])
def signup():
    data = request.json
    name = data.get("name")
    email = data.get("email")
    password = data.get("password")
    role = data.get("role")

    session = SessionLocal()

    if session.query(User).filter_by(email=email).first():
        return jsonify({"error": "Email already exists"}), 400

    #create a new user
    new_user = User(name=name, email=email, role=role)
    new_user.set_password(password)

    session.add(new_user)
    session.commit()
    session.close()

    return jsonify({"message": "User registered successfully"}), 201

@app.route("/login", methods=["POST"])
def login():
    data = request.json
    email = data.get("email")
    password = data.get("password")

    session = SessionLocal()
    user = session.query(User).filter_by(email=email).first()

    if user and user.check_password(password):
        return jsonify({"message": "Login successful"}), 200
    else:
        return jsonify({"error": "Invalid credentials"}), 401

if __name__ == "__main__":
    app.run(debug=True)
