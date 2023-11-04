DROP TABLE IF EXISTS PKUnicas;
DELETE FROM caja_ahorro;
DELETE FROM cuenta_corriente;

CREATE TEMPORARY TABLE PKUnicas AS
	SELECT ROW_NUMBER() OVER () AS account_id
	FROM cuenta
	LIMIT 500;

-- Asigno aleatoriamente las customer_id entre los tipos de clientes
INSERT INTO caja_ahorro (account_id)
SELECT account_id
FROM PKUnicas
ORDER BY RANDOM()
LIMIT 300;

INSERT INTO cuenta_corriente (account_id)
SELECT account_id
FROM PKUnicas
WHERE account_id NOT IN (SELECT account_id
						 FROM caja_ahorro)
ORDER BY RANDOM()
LIMIT 200;

DROP TABLE IF EXISTS PKUnicas;