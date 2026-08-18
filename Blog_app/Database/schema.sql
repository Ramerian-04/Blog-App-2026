CREATE DATABASE IF NOT EXISTS blog_app_2026;
USE blog_app_2026;

CREATE TABLE users(
    user_id varchar(50) PRIMARY KEY,
    password varchar(255) NOT NULL,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL
);

CREATE TABLE blogposts(
    blog_id INT PRIMARY_KEY AUTO_INCREMENT,
    auth_id VARCHAR(50) NOT NULL,
    title VARCHAR(200) NOT NULL,
    description TEXT NO NULL,
    created_at at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY(auth_id) REFERENCES users(user_id)
    ON DELETE CASCADE
)