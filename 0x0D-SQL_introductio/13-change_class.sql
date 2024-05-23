-- this is a sql script that deletes records with a score <= 5 in the table second_table of the database hbtn_0c_0 which is passed as an argument in the my sql command
DELETE FROM second_table
WHERE `score`<=5;