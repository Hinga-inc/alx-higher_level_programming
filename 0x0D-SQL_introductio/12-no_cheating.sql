-- this is a sql script that updates the score of bob to 10 in the table second_table
-- without using bobs id value only the name field
UPDATE second_table
SET `score`=10
WHERE `name`='bob';