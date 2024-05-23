-- this a=is a sql script that creates a table called first_table in MySQL server
-- the database name is passed as an argument in the mysql command 
-- if the table exist the script doesnt fail
CREATE TABLE IF NOT EXISTS first_table(
    id INT,
    name VARCHAR(256)
);