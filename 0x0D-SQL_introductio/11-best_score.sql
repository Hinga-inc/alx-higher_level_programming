-- this is a script that lists records with a score >=10 in the table second_table in the db hbtn_0c_0 which will be passed as an argument in the mysql command
-- It displays the score and the name where the score is ordered as the top to be first
SELECT score, name
FROM second_table
HAVING `score` >= 10
ORDER BY score DESC;