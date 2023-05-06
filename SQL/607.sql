SELECT name FROM SalesPerson
WHERE sales_id NOT IN (
    SELECT sales_id
    FROM Orders
        LEFT JOIN Company USING (com_id)
        LEFT JOIN SalesPerson USING (sales_id)
    WHERE Company.name = "RED"
)
