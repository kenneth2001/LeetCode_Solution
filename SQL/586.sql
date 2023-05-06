SELECT 
  customer_number 
FROM
  Orders
GROUP BY
  customer_number
ORDER BY
  COUNT(0) DESC
LIMIT 1
