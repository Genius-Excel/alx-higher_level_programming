-- This sql script creates a new table if it does not exist and avoid failures.
CREATE TABLE IF NOT EXISTS first_table (id INT, name VARCHAR(256));
