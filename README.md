#  Movie Ticket Booking Backend

##  Project Overview
This is a **Flask-based backend system** for booking movie tickets. It supports two user roles:  
- **User** – Can view movies and book tickets.  
- **Theater Owner** – Can manage movie listings (to be implemented).  

The system currently includes **user authentication**, database setup, and API testing using Postman/cURL.

---

##  Tech Stack
- **Backend:** Flask  
- **Database:** SQLite (can switch to MySQL later)  
- **Security:** Flask-Bcrypt (password hashing), JWT

---

##  Features Implemented
###  Database Setup (SQLite)
- Created three tables using SQLAlchemy:
  - **Users** (`id`, `name`, `email`, `password`, `role`)
  - **Movies** (`id`, `title`, `duration`, `genre`)
  - **Bookings** (`id`, `user_id`, `movie_id`, `timestamp`)  

---

##  Features Added  

### 1️ User Authentication  
- **Signup** → `POST /signup` (Create user)  
- **Login** → `POST /login` (Get JWT token)  

### 2️ Movie Management (Owner Only)  
- **Add Movie** → `POST /movies` (Requires JWT, Only owners can access)  
- **Get Movies** → `GET /movies` (Anyone can access)  

### 3️ Show Management (Owner Only)  
- **Add Show** → `POST /shows` (Requires JWT,Only owners can access)  
- **Get Shows** → `GET /shows` (Anyone can access)  

### 4️ Ticket Booking (User Only)  
- **Book Ticket** → `POST /bookings` (Requires JWT,Only users can access)  
- **View Past Bookings** → `GET /bookings` (Requires JWT,Only users can access)  

