SELECT
    U.product_id,
    ROUND(SUM(units * price) / SUM(units), 2) AS average_price
FROM
    UnitsSold U
    LEFT JOIN Prices P 
        ON U.product_id = P.product_id
        AND (U.purchase_date BETWEEN P.start_date AND P.end_date)
GROUP BY
    U.product_id
