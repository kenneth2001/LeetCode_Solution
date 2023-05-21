WITH TMP AS (
    SELECT
        managerId
    FROM
        Employee
    GROUP BY
        managerId
    HAVING
        COUNT(*) >= 5
)

SELECT
    name
FROM
    Employee
WHERE
    id IN (SELECT * FROM TMP)
