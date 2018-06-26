-- Create a database but do not fail if already exists, then add a user.

CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.cities (id INT UNIQUE AUTO_INCREMENT NOT NULL PRIMARY KEY, 
state_id INT NOT NULL FOREIGN KEY(id) REFERENCES states(id),
name VARCHAR(256) NOT NULL);
