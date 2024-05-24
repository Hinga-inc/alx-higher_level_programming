-- this is a script that has imported a table dumb
-- this is a sql script that displays the average temperature by city ordered bu temperature in descending order
SELECT `city`, AVG(`value`) AS avg_temp
FROM temperatures
GROUP BY city
ORDER BY avg_temp DESC;