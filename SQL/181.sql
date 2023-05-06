SELECT E1.name AS "Employee"
FROM Employee AS E1
  LEFT JOIN Employee AS E2 ON E1.managerID = E2.ID
WHERE
  E1.salary > E2.salary
  