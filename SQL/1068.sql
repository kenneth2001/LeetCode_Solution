SELECT
    product_name,
    year,
    price
FROM
    sales
    LEFT JOIN Product USING (product_id)
