WITH First AS (
    SELECT player_id, MIN(event_date) AS first_login
    FROM Activity
    GROUP BY player_id
)

SELECT ROUND(COUNT(*) / (SELECT COUNT(*) FROM First), 2) AS fraction
FROM First F INNER JOIN Activity A
ON A.player_id = F.player_id AND A.event_date = DATE_ADD(F.first_login, INTERVAL 1 DAY)
