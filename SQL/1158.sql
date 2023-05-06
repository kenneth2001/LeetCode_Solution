SELECT
    U.user_id AS buyer_id,
    join_date,
    COUNT(DISTINCT order_id) AS orders_in_2019
FROM
    Users U
    LEFT JOIN Orders O ON U.user_id = O.buyer_id AND YEAR(O.order_date) = 2019
GROUP BY
    user_id
