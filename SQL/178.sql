SELECT score, DENSE_RANK() over(ORDER BY score desc) AS 'Rank'
FROM Scores
