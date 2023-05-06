SELECT w1.id AS Id
FROM Weather w1
    LEFT JOIN Weather w2 
    ON w1.recordDate = w2.recordDate + INTERVAL 1 DAY
WHERE w1.temperature > w2.temperature
