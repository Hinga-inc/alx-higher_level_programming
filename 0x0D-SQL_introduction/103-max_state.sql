-- this is a sql script that displays the max temperature of each state orderded by state name
-- this is from an imporded table dump known as temperatures
SELECT DISTINCT `state`, MAX(`value`) AS max_temp
FROM temperatures
GROUP BY `state`
ORDER BY `state`;