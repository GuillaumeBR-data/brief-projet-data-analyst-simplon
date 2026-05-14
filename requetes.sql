-- 3) c. BIS chiffre d'affaire par région
SELECT region,
       SUM(prix*qte) AS "chiffre d'affaire par région"
FROM ventes
GROUP BY region;