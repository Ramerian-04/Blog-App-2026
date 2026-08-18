# 📝 Blog App 2026

A command-line blog application built with **Python** and **MySQL**, following a clean layered architecture (Models → Repositories → Services → UI).

## ✨ Features

- **User Registration & Login** — Create an account and log in with a unique user ID
- **Create Posts** — Write blog posts with a title and description
- **List Posts** — View all recent posts with author name and timestamp
- **Update Posts** — Edit your own posts (ownership enforced)
- **Delete Posts** — Remove your own posts (ownership enforced)
- **Input Validation** — Blank fields and invalid user IDs are rejected

## 🏗️ Project Structure

```
Blog_app/
├── main.py                  # Application entry point
├── Config/
│   └── settings.py          # MySQL connection config
├── DB/
│   └── connection.py        # Database connection handler
├── Database/
│   └── schema.sql           # SQL schema for tables
├── Models/
│   ├── user.py              # User model
│   └── blog_post.py         # BlogPost model
├── Repositories/
│   ├── user_repository.py   # User DB operations
│   └── blog_repository.py   # Blog post DB operations
├── Services/
│   ├── auth_service.py      # Authentication logic
│   └── blog_service.py      # Blog business logic
├── UI/
│   └── menu.py              # CLI menu display
└── Utils/
    └── validators.py        # Input validation helpers
```

## 🔧 Prerequisites

- **Python 3.8+**
- **MySQL Server**
- **mysql-connector-python** package

## 🚀 Setup & Run

### 1. Clone the repository

```bash
git clone https://github.com/Ramerian-04/Blog-App-2026.git
cd Blog-App-2026
```

### 2. Install dependencies

```bash
pip install mysql-connector-python
```

### 3. Set up the database

Open MySQL and run the schema file:

```sql
SOURCE Blog_app/Database/schema.sql;
```

Or manually:

```sql
CREATE DATABASE IF NOT EXISTS blog_app_2026;
USE blog_app_2026;

CREATE TABLE users(
    user_id VARCHAR(50) PRIMARY KEY,
    password VARCHAR(255) NOT NULL,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL
);

CREATE TABLE blogposts(
    blog_id INT PRIMARY KEY AUTO_INCREMENT,
    auth_id VARCHAR(50) NOT NULL,
    title VARCHAR(200) NOT NULL,
    description TEXT NOT NULL,
    created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY(auth_id) REFERENCES users(user_id) ON DELETE CASCADE
);
```

### 4. Configure database credentials

Edit `Blog_app/Config/settings.py` with your MySQL credentials:

```python
DB_CONFIG = {
    "host": "localhost",
    "user": "root",
    "password": "your_password",
    "database": "blog_app_2026"
}
```

### 5. Run the app

```bash
cd Blog_app
python main.py
```

## 📖 Usage

```
-----------------BLOG APP-----------------
1. Login
2. Register
3. Exit
```

1. **Register** a new account (option 2)
2. **Login** with your credentials (option 1)
3. Once logged in, you can **Create**, **List**, **Update**, or **Delete** posts

## 🧱 Architecture

| Layer | Responsibility |
|-------|----------------|
| **Models** | Data classes (`User`, `BlogPost`) |
| **Repositories** | Direct database CRUD operations |
| **Services** | Business logic and orchestration |
| **UI** | CLI menus and display |
| **Utils** | Input validation helpers |
| **Config / DB** | Database connection management |

## 📄 License

This project is open source and available for educational purposes.
