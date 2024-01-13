WITH Tmp AS (
    SELECT
        visited_on,
        SUM(amount) OVER (ORDER BY visited_on ROWS 6 PRECEDING) amount,
        AVG(amount) OVER (ORDER BY visited_on ROWS 6 PRECEDING) average_amount,
        ROW_NUMBER() OVER (ORDER by visited_on) row_n
    FROM
        (
            SELECT
                visited_on,
                SUM(amount) AS amount
            FROM
                Customer
            GROUP BY
                visited_on
        ) T
)

SELECT
    visited_on,
    ROUND(amount, 2) AS amount,
    ROUND(average_amount, 2) AS average_amount
FROM
    Tmp
WHERE
    row_n > 6