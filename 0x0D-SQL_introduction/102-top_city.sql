-- this is a sql script that uses an importeded table dumb 
-- that displays the top 3 of citites temeperature  during july and august ordered by temperature in descending order
SELECT `city`, AVG(`value`) AS avg_temp
FROM temperatures
WHERE `month` IN (7, 8)
GROUP BY `city`
ORDER BY avg_temp DESC LIMIT 3;
