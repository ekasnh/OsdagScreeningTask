CREATE DATABASE prismdb;
USE prismdb;

CREATE TABLE rectangular_prism (
    id INT AUTO_INCREMENT PRIMARY KEY,
    designation VARCHAR(100) UNIQUE NOT NULL,
    length FLOAT NOT NULL,
    width FLOAT NOT NULL,
    height FLOAT NOT NULL
);

INSERT INTO rectangular_prism (designation, length, width, height) VALUES 
('L40B20H100', 40.0, 20.0, 100.0),
('L60B30H150', 60.0, 30.0, 150.0),
('L80B40H200', 80.0, 40.0, 200.0);
