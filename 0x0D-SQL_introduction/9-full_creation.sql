-- this is a sql script that creates a table second_table in the database hbtn_0c_0 and adds multiple rows and adds records in them
-- database name is passed as a argument in the mysql command
CREATE TABLE IF NOT EXISTS second_table (
    id INT,
    name VARCHAR(256),
    score INT
);
INSERT INTO `second_table` VALUES(1, 'John', 10), (2, 'Alex', 3), (3, 'Bob', 14), (4, 'Geroge', 8);