SELECT
    name AS NAME,
    SUM(amount) AS BALANCE
FROM
    Users
    LEFT JOIN Transactions USING(account)
GROUP BY
    account
HAVING
    SUM(amount) > 10000
