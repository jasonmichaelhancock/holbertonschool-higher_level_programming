-- Create a database but do not fail if already exists, then add a user.

CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2';
GRANT SELECT ON `hbtn_0d_2`.* TO 'user_0d_2'@'localhost';
