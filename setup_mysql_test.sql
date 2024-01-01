-- create test database

-- create database
CREATE DATABASE IF NOT EXISTS hbnb_test_db;

-- create new user
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY "hbnb_test_pwd";

-- give user all privileges
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_dev'@'localhost';

-- give user select privilege on the database performance_schema 
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';

