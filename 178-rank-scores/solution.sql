SELECT
    Score,
    Rank
FROM
    Scores NATURAL JOIN
    (SELECT
        S1.Score AS Score,
        COUNT(S2.Score) AS Rank
    FROM
        (SELECT DISTINCT Score FROM Scores) AS S1,
        (SELECT DISTINCT Score FROM Scores) AS S2
    WHERE S1.Score <= S2.Score GROUP BY S1.Score) AS Ranks
ORDER BY Rank;