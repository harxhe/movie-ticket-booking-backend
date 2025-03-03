# movie-ticket-booking-backend

## 📌 Project Overview
This is a **Flask-based backend system** for booking movie tickets. It supports two user roles:  
- **User** – Can view movies and book tickets.  
- **Theater Owner** – Can manage movie listings (to be implemented).  

The system currently includes **user authentication**, database setup, and API testing using Postman/cURL.

---

## 📂 Tech Stack
- **Backend:** Flask  
- **Database:** SQLite (can switch to MySQL later)  
- **Security:** Flask-Bcrypt (password hashing), JWT (coming soon)  

---

## 📌 Features Implemented
### ✅ Database Setup (SQLite)
- Created three tables using SQLAlchemy:
  - **Users** (`id`, `name`, `email`, `password`, `role`)
  - **Movies** (`id`, `title`, `duration`, `genre`)
  - **Bookings** (`id`, `user_id`, `movie_id`, `timestamp`)  

---

### ✅ User Authentication
- **Signup (`/signup`)**: Allows new users to register.  
- **Login (`/login`)**: Verifies user credentials and allows access.  
