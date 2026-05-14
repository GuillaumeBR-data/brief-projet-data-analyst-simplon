-- 2. Afficher toutes les ventes
SELECT * FROM ventes;

-- 3.a Chiffre d'affaires total
SELECT SUM(prix*qte) AS "chiffre d'affaires total"
FROM ventes;

-- 3.b Ventes par produit
SELECT produit,
       SUM(qte) AS "ventes par produit"
FROM ventes
GROUP BY produit;

-- 3.b BIS Chiffre d'affaires par produit
SELECT produit,
       SUM(prix*qte) AS "chiffre d'affaires par produit"
FROM ventes
GROUP BY produit;

-- 3.c Ventes par région
SELECT region,
       SUM(qte) AS "ventes par région"
FROM ventes
GROUP BY region;

-- 3.c BIS Chiffre d'affaires par région
SELECT region,
       SUM(prix*qte) AS "chiffre d'affaires par région"
FROM ventes
GROUP BY region;