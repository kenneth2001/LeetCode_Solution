SELECT
    stock_name,
    SUM(
        CASE
            WHEN operation = "buy" THEN -price
            ELSE price
        END
    ) capital_gain_loss
FROM
    Stocks
GROUP BY
    stock_name
