SELECT
    ROUND(SUM((CASE WHEN order_date = customer_pref_delivery_date THEN 1 ELSE 0 END)) / COUNT(*) * 100, 2) AS immediate_percentage
FROM
    (
        SELECT 
            *, 
            ROW_NUMBER() OVER(PARTITION BY customer_id ORDER BY order_date) AS RK 
        FROM Delivery
    ) TMP
WHERE
    RK = 1
