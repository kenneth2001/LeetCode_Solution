WITH Tmp AS (
    SELECT
        product_id,
        SUM(unit) AS unit
    FROM
        Orders
    WHERE
        YEAR(order_date) = 2020 AND MONTH(order_date) = 2
    GROUP BY
        product_id
)

SELECT
    product_name,
    unit
FROM
    Products P
    LEFT JOIN Tmp T ON P.product_id = T.product_id
WHERE
    T.unit >= 100