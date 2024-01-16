-- This SQL script contins a query that creates a database if does not exist.

USE mysql;
SET @new_db_name := 'hbtn_0c_0';
SET @db_present := (SELECT COUNT(*) FROM information_schema.SCHEMATA WHERE SCHEMA_NAME = @new_db_name);
SET @sql_query := IF(@db_present = 0, CONCAT('CREATE DATABASE ', @new_db_name), '');
PREPARE create_stmt FROM @sql_query;
EXECUTE create_stmt;
DEALLOCATE PREPARE create_stmt;

USE hbtn_0c_0;
