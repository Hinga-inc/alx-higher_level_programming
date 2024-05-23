-- this is a sql script that list the numbeer of records with the same score in the table second_table of the database hbtn_0c_0 whis is passed as an argument in the my sql command
-- then it is sorted by the number of records descending
-- the result displays the score the number of records for this score with a label number
SELECT `score`, COUNT(`score`) AS number
FROM second_table
GROUP BY score
ORDER BY number DESC;