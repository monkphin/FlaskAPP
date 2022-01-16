START TRANSACTION;

-- Use (swtich to) webapp_db 
USE webapp_db;

-- Drop the Persons table if it exists
DROP TABLE IF EXISTS Minis;
DROP TABLE IF EXISTS Persons;
DROP TABLE IF EXISTS Credentials;

-- Create the Credentias table and set the uniqe auto_incrementing ID
CREATE TABLE Credentials (
    credId int NOT NULL AUTO_INCREMENT,
    username varchar(255) NOT NULL,
    userpwd varchar(255) NOT NULL,

    PRIMARY KEY (credId)
);

-- Create the Persons table and set the uniqe auto_incrementing ID
CREATE TABLE Persons (
    PersonID int NOT NULL AUTO_INCREMENT,
    LastName varchar(255) NOT NULL,
    FirstName varchar(255),
    email varchar(255) NOT NULL,
    addr varchar(1024),

    PRIMARY KEY (PersonID),
);

-- Create the orders table
CREATE TABLE Minis (
    MiniID int NOT NULL AUTO_INCREMENT,
    MiniName VARCHAR(255) NOT NULL,
    MiniNum int NOT NULL,
    MiniPoint int,
    MiniCost int,

    PRIMARY KEY (MiniID),

);

