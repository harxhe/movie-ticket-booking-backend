# 🎬 Movie Ticket Booking System  

A backend system for movie ticket booking, allowing users to book seats and theater owners to manage shows. Authentication is JWT-based for security.  

## 🚀 Features Implemented  

### 1️⃣ User Authentication  
- **Signup** → `POST /signup` (Create user)  
- **Login** → `POST /login` (Get JWT token)  

### 2️⃣ Movie Management (Owner Only)  
- **Add Movie** → `POST /movies` (Requires JWT, Only owners can access)  
- **Get Movies** → `GET /movies` (Anyone can access)  

### 3️⃣ Show Management (Owner Only)  
- **Add Show** → `POST /shows` (Requires JWT, Only owners can access)  
- **Get Shows** → `GET /shows` (Anyone can access)  

### 4️⃣ Ticket Booking (User Only)  
- **Book Ticket** → `POST /bookings` (Requires JWT,Only users can access)  
- **View Past Bookings** → `GET /bookings` (Requires JWT,Only users can access)  

---

## 🛠️ Technologies Used  

- **Backend:** Flask (Python)  
- **Database:** SQLite (Using Flask-SQLAlchemy)  
- **Authentication:** JWT (Flask-JWT-Extended)  
- **Password Hashing:** Bcrypt  
- **API Testing:** Postman / cURL  

---
## 📖 Implementation Details  

### 🗃️ 1️⃣ Database Schema  
The system consists of four main tables:  

#### **User Table (`users`)**  
| Column   | Type     | Description                       |  
|----------|---------|----------------------------------|  
| id       | Integer | Primary key, unique user ID     |  
| name     | String  | Full name of the user           |  
| email    | String  | Unique email address            |  
| password | String  | Hashed password                 |  
| role     | Enum    | Either `"user"` or `"owner"`    |  

#### **Movie Table (`movies`)**  
| Column   | Type     | Description                     |  
|----------|---------|--------------------------------|  
| id       | Integer | Primary key, unique movie ID   |  
| title    | String  | Movie title                    |  
| genre    | String  | Movie genre                    |  
| duration | Integer | Duration in minutes           |  

#### **Show Table (`shows`)**  
| Column          | Type     | Description                        |  
|---------------|---------|----------------------------------|  
| id            | Integer | Primary key, unique show ID      |  
| movie_id      | Integer | Foreign key linking to `movies.id` |  
| timing        | String  | Show date & time                 |  
| available_seats | Integer | Number of available seats        |  
| owner_id      | Integer | Foreign key linking to `users.id` (Only owners can add shows) |  

#### **Booking Table (`bookings`)**  
| Column   | Type     | Description                       |  
|----------|---------|----------------------------------|  
| id       | Integer | Primary key, unique booking ID  |  
| user_id  | Integer | Foreign key linking to `users.id` |  
| show_id  | Integer | Foreign key linking to `shows.id` |  
| num_seats| Integer | Number of seats booked          |  

---

### 🔐 2️⃣ JWT Authentication Flow  
Authentication is implemented using JSON Web Tokens (JWT).  

1️⃣ **User Signup (`/signup`)**  
   - Users provide name, email, password, and role (`user` or `owner`).  
   - Passwords are securely hashed using **Bcrypt** before storing.  

2️⃣ **User Login (`/login`)**  
   - Users log in with email and password.  
   - If valid, a **JWT access token** is generated.  

3️⃣ **Protected Routes**  
   - Owners require a valid JWT token to add movies/shows.  
   - Users require a JWT token to book tickets and view past bookings.  
   - Tokens are verified in headers using `Authorization: Bearer <token>`  

---

### 🔄 3️⃣ API Request Flow  

1️⃣ **Movies**  
   - Owners add movies → `POST /movies` (Requires JWT)  
   - Anyone can fetch movies → `GET /movies`  

2️⃣ **Shows**  
   - Owners add shows → `POST /shows` (Requires JWT)  
   - Anyone can view shows → `GET /shows`  

3️⃣ **Booking Tickets**  
   - Users book seats → `POST /bookings` (Requires JWT)  
   - Users view past bookings → `GET /bookings` (Requires JWT)  

---

### 🚀 4️⃣ How it Works  

1️⃣ **Owners add movies and shows**  
   - A theater owner logs in and gets a **JWT token**.  
   - The owner adds movies using the **`POST /movies`** API.  
   - The owner adds show timings using the **`POST /shows`** API.  

2️⃣ **Users book tickets**  
   - A user logs in and gets a **JWT token**.  
   - The user views available shows using **`GET /shows`**.  
   - The user books tickets using **`POST /bookings`**.  

3️⃣ **Viewing past bookings**  
   - Users can check their previous bookings using **`GET /bookings`**.  

---

This system ensures **secure authentication**, **role-based access**, and **smooth booking functionality**! 🚀  
