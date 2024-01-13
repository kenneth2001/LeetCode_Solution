WITH Tmp AS (
    SELECT
        person_name,
        SUM(weight) OVER(ORDER BY turn, person_id) AS ttl
    FROM
        Queue
)

SELECT
    person_name
FROM
    Tmp
WHERE
    ttl <= 1000
ORDER BY
    ttl DESC
LIMIT 1