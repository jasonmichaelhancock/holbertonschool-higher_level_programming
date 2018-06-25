-- Script lists number of records with same score, decending order.
SELECT score, COUNT(8) as number FROM second_table GROUP BY score ORDER BY number DESC;
