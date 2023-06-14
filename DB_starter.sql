DROP DATABASE IF EXISTS tischler;
CREATE DATABASE tischler;

-- Use the database tischler
USE tischler;

-- Create the users table
CREATE TABLE users (id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY, 
    user_id INT(50) UNSIGNED NOT NULL UNIQUE, 
    user_money INT,
    user_level INT,
    user_exp INT,
    timestampdaily DATE,
    timestampwork DATETIME,
    timestamplevel DATETIME,
    working BOOLEAN
);

-- Create the requests table
CREATE TABLE requests (id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY, 
    requestee INT(50) UNSIGNED NOT NULL UNIQUE, 
    requested INT(50) UNSIGNED NOT NULL UNIQUE,
    betting_amount INT NOT NULL,
    request_state TInyint(1) NOT NULL
);

-- Create the stocks table
CREATE TABLE stocks (
    stock_id INT PRIMARY KEY AUTO_INCREMENT,
    stock_name VARCHAR(255),
    price INT UNSIGNED
);

-- Create the buyers table
CREATE TABLE buyers (
    buyer_id INT PRIMARY KEY AUTO_INCREMENT,
    stock_id INT,
    user_id INT(50) UNSIGNED NOT NULL UNIQUE,
    count INT,
    FOREIGN KEY (stock_id) REFERENCES stocks(stock_id)
);

-- Insert the values
INSERT INTO stocks (name, price)
VALUES
  ('CornHub.com', 1000),
  ('DeTisch', 10000),
  ('Tree', 110),
  ('Giovanni', 120),
  ('Statue Inc.', 70),
  ('REST gmbh', 30),
  ('Evian', 40),
  ('Jim', 100000000);

DESC users;
DESC requests;
DESC stocks;
DESC buyers;
