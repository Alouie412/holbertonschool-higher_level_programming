-- This script creates table in the passed in argument
-- The id will default to 1 if no id is passed in. Otherwise, change the id to whatever is passed in
-- The id must also be unique. This script will not allow duplicate ids to be passed in

CREATE TABLE IF NOT EXISTS unique_id (
    id INT DEFAULT 1 UNIQUE,
    name VARCHAR(256)
);
