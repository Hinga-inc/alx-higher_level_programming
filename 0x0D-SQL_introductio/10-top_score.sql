-- this is a sql script that lists all records in the second_table of the database hbtn_0c_0, the database willl be passed as an argument in the mysql command
-- the results displays both the score and name and the ordered by score
SELECT score, name FROM second_table ORDER BY score DESC;