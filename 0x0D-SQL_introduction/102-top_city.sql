-- Display the top 3 cities for July and August temperatures, ordered by descending temperature
SELECT city, AVG(temperature) AS avg_temp FROM temperatures WHERE month IN ('07', '08') GROUP BY city ORDER BY avg_temp DESC LIMIT 3;
