SELECT
    employee_id,
    department_id
FROM (
    SELECT
        employee_id,
        department_id,
        RANK() OVER(PARTITION BY employee_id ORDER BY primary_flag) AS rk
    FROM
        Employee
) Tmp
WHERE
    rk = 1