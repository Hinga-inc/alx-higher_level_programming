-- this is a sql script that lists all records of the table second_table of the database hbtn_0c_0 that is passed as an argument in the mysql command
-- it doesn't list rows without a name value
-- results displays the score and name with the score ordered in descening order
SELECT `score`, `name`
FROM second_table
WHERE `name` IS NOT NULL
ORDER BY `score` DESC;