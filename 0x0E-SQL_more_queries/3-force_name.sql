-- This script creates a table in the passed in database argument
-- Note that name cannot be empty. Something must be passed into name

CREATE TABLE IF NOT EXISTS force_name (
    id INT,
    name VARCHAR(256) NOT NULL
);
