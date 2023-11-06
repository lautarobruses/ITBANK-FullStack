DROP TABLE IF EXISTS PKUnicas;
DELETE FROM cliente_classic;
DELETE FROM cliente_gold;
DELETE FROM cliente_black;

CREATE TEMPORARY TABLE PKUnicas AS
	SELECT ROW_NUMBER() OVER () AS customer_id
	FROM cliente
	LIMIT 500;

-- Asigno aleatoriamente las customer_id entre los tipos de clientes
INSERT INTO cliente_classic (customer_id)
SELECT customer_id
FROM PKUnicas
ORDER BY RANDOM()
LIMIT 300;

INSERT INTO cliente_gold (customer_id)
SELECT customer_id
FROM PKUnicas
WHERE customer_id NOT IN cliente_classic
ORDER BY RANDOM()
LIMIT 150;

INSERT INTO cliente_black (customer_id)
SELECT customer_id
FROM PKUnicas
WHERE customer_id NOT IN (SELECT customer_id FROM cliente_classic
						  UNION
						  SELECT customer_id FROM cliente_gold)
ORDER BY RANDOM()
LIMIT 50;

DROP TABLE IF EXISTS PKUnicas;