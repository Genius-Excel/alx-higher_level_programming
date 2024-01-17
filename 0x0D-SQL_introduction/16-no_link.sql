-- This sql script lists all records tht only has a name value.
SELECT score, name FROM second_table WHERE name IS NOT NULL ORDER BY score DESC;
