WITH Tmp AS (
    SELECT
        id,
        name,
        salary,
        departmentId,
        DENSE_RANK() OVER(PARTITION BY departmentId ORDER BY salary DESC) AS rk
    FROM
        Employee
)

SELECT
    D.name AS Department,
    T.name AS Employee,
    T.salary AS Salary
FROM
    TMP T
    LEFT JOIN Department D ON T.departmentId = D.id
WHERE
    rk <= 3