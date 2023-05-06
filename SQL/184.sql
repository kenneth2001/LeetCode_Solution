WITH TMP AS (
  SELECT departmentId, MAX(salary) AS highest
  FROM Employee
  GROUP BY departmentId
)

SELECT d.name AS "Department", E.name AS "Employee", E.salary AS "Salary"
FROM Employee E
  LEFT JOIN Department D ON E.departmentId = D.id
  LEFT JOIN TMP T ON E.departmentId = T.departmentId AND E.salary = T.highest
WHERE highest IS NOT NULL
