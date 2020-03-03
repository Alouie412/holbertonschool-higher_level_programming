-- This script creates table in the passed in argument
-- The id will default to 1 if no id is passed in. Otherwise, change the id to whatever is passed in

CREATE TABLE IF NOT EXISTS id_not_null (
    id INT DEFAULT 1,
    name VARCHAR(256)
);
