-- this is a sql script that computes the score average in the table scond_table of the database hbtn_0c_0 that is passed as an argument in the mysql command
-- the result collumn is average
SELECT AVG(`score`) AS average
FROM second_table;