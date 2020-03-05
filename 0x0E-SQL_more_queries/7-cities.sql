-- This script creates a table in the server
-- The foreign key state_id will reference the id from the states table
-- In other words, the table cities will check and verify that the id from states is valid before adding the entry,
-- otherwise an error message will be raised

CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS cities (
    id INT UNIQUE AUTO_INCREMENT NOT NULL,
    state_id INT NOT NULL,
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY (state_id) REFERENCES states(id)
);
