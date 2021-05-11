
CREATE TABLE IF NOT EXISTS client (
idclient int(5) NOT NULL,
nom varchar(128) NOT NULL,
prenom varchar(128) NOT NULL,
ville varchar(128) NOT NULL,
PRIMARY KEY (idclient)

-------------------------------

CREATE TABLE T_CLIENT
(CLI_ID INTEGER NOT NULL PRIMARY KEY,
CLI_NOM CHAR(32) NOT NULL,
CLI_PRENOM VARCHAR(32))


-> clé primaire donne auto un index

-----------------------------------------------



INSERT INTO T_CLIENT VALUES (3, 'Marcel', NULL)
INSERT INTO T_CLIENT VALUES (3, 'test', 'test') -- doesn't work because same id
INSERT INTO T_CLIENT VALUES (4, 'test', 'test')
INSERT INTO T_CLIENT VALUES (5, NULL, 'test') --doesn't work: null constrained

--------------------------------------

SELECT DISTINCT cli_nom FROM T_CLIENT

--------------------------------------

SELECT montant FROM operation WHERE montant <= 300
SELECT * FROM operation WHERE montant >= 300 AND idcompte < 200
SELECT * FROM operation WHERE idop != 5
SELECT * FROM operation WHERE idop <> 5
SELECT * FROM operation WHERE informations NOT IN ('Guichet')
SELECT montant * idcompte / 100 * idop FROM operation
SELECT montant * idcompte / (100 * idop) FROM operation -- same thing

SELECT * FROM operation WHERE idop == 1 or idcompte == 269
SELECT * FROM operation WHERE idop = 1 or idcompte = 269 -- same thing


--------------------------------------

SELECT * FROM T_CLIENT
SELECT * FROM T_CLIENT WHERE cli_prenom is NULL
SELECT * FROM T_CLIENT WHERE cli_prenom is NOT NULL

--------------------------------------

SELECT montant as alias_montant FROM operation
SELECT montant as alias_montant FROM operation ORDER BY alias_montant ASC
SELECT montant as alias_montant FROM operation ORDER BY alias_montant DESC


SELECT nom FROM client ORDER by nom ASC
SELECT nom FROM client ORDER by nom -- b same thing


SELECT AVG(montant) as prix_moyen FROM operation 
SELECT MIN(montant) as min_prix FROM operation 
SELECT count(montant) FROM operation 
SELECT SUM(montant) FROM operation 

SELECT COUNT(idcompte) FROM operation 
SELECT COUNT(DISTINCT(idcompte)) FROM operation 

example regex
https://www.dba-expert.fr/index.php/le-developpement/sql/20-la-fonction-regexp-like

SELECT * FROM operation GROUP by idcompte

SELECT SUM(montant) FROM operation GROUP by idcompte
SELECT SUM(montant) AS somme_montant FROM operation GROUP by idcompte

having filtre avec max, avg, min...

SELECT *
FROM operation
WHERE montant >= 20
GROUP by idcompte
HAVING COUNT(idop) < 3


SELECT montant, idcompte,
CASE
    WHEN montant < 0 THEN 'valeur négative'
    ELSE 'valeur positive'
END as 'resultat'
FROM operation;



--------------------------------------
SELECT count (*)
FROM(
    SELECT nom, prenom, idcompte, type
    FROM client
    INNER JOIN compte ON idclient=idproprietaire
    WHERE type == 'Livret A'
    )



a tester:
SELECT compte.idcomte, idproprietaire, type, montant, informations
FROM compte AS c
INNER JOIN client ON idclient = c.idproprietaire
INNER JOIN operation ON operation.idcompte = c.idcompte 
WHERE montant > 0 AND montant < 100

Inner joins (keep rows with keys that exist in the left and right datasets)

Outer joins (keep rows with keys in either the left or right datasets)

Left outer joins (keep rows with keys in the left dataset)

Right outer joins (keep rows with keys in the right dataset)

Left semi joins (keep the rows in the left, and only the left, dataset where the key
appears in the right dataset)

Left anti joins (keep the rows in the left, and only the left, dataset where they do not
appear in the right dataset)

Natural joins (perform a join by implicitly matching the columns between the two
datasets with the same names)

Cross (or Cartesian) joins (match every row in the left dataset with every row in the
right dataset)


--------------------------------------

--------------------------------------

--------------------------------------

--------------------------------------

--------------------------------------

--------------------------------------

--------------------------------------

--------------------------------------

--------------------------------------



--------------------------------------




--------------------------------------

--------------------------------------

--------------------------------------

--------------------------------------

--------------------------------------

--------------------------------------

--------------------------------------

--------------------------------------

--------------------------------------

--------------------------------------

--------------------------------------

--------------------------------------



--------------------------------------




--------------------------------------

--------------------------------------

--------------------------------------

--------------------------------------

--------------------------------------

--------------------------------------

--------------------------------------

--------------------------------------

--------------------------------------

--------------------------------------

--------------------------------------

--------------------------------------



--------------------------------------




--------------------------------------

--------------------------------------

--------------------------------------

--------------------------------------

--------------------------------------

--------------------------------------

--------------------------------------

--------------------------------------

--------------------------------------

--------------------------------------

--------------------------------------

--------------------------------------



--------------------------------------




--------------------------------------

--------------------------------------

--------------------------------------

--------------------------------------

--------------------------------------

--------------------------------------

--------------------------------------

--------------------------------------

--------------------------------------

--------------------------------------

--------------------------------------

--------------------------------------



--------------------------------------




--------------------------------------

--------------------------------------

--------------------------------------

--------------------------------------

--------------------------------------

--------------------------------------

--------------------------------------

--------------------------------------

--------------------------------------

--------------------------------------

--------------------------------------

--------------------------------------



--------------------------------------




--------------------------------------

--------------------------------------

--------------------------------------

--------------------------------------

--------------------------------------

--------------------------------------

--------------------------------------

--------------------------------------

--------------------------------------

--------------------------------------

--------------------------------------

--------------------------------------



--------------------------------------




--------------------------------------

--------------------------------------

--------------------------------------

--------------------------------------

--------------------------------------

--------------------------------------

--------------------------------------

--------------------------------------

--------------------------------------

--------------------------------------

--------------------------------------

--------------------------------------



--------------------------------------




--------------------------------------