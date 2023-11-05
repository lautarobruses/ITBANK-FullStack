-- Asigno aleatoriamente las tarjeta_credito entre cliente_gold y cliente_black

-- Selecciono tarjeta_credito aleatoriamente respetando las condiciones del SPRINT 5
WITH clientesAleatorios AS (
    SELECT tarjeta_credito.tarjeta_numero, cliente.customer_id
    FROM tarjeta, tarjeta_credito, cliente, marca_tarjeta
    WHERE cliente.customer_id NOT IN (SELECT customer_id 
	                                  FROM cliente_classic)
		  AND (cliente.customer_id IN (SELECT customer_id 
	                                   FROM cliente_gold) AND cantidad_extensiones <= 5 
													      AND (marca_tarjeta_nombre LIKE '%VISA%' OR marca_tarjeta_nombre LIKE '%Mastercard%')
														  AND tarjeta.marca_tarjeta_id = marca_tarjeta.marca_tarjeta_id
		       OR cliente.customer_id IN (SELECT customer_id 
	                                      FROM cliente_black) AND cantidad_extensiones <= 10)
	     AND tarjeta.tarjeta_numero = tarjeta_credito.tarjeta_numero
    ORDER BY RANDOM()
)

-- Actualizo la tabla tarjeta con las marcas aleatoriamente
UPDATE tarjeta
SET customer_id = (
    SELECT customer_id
    FROM clientesAleatorios
	WHERE tarjeta.tarjeta_numero = clientesAleatorios.tarjeta_numero
);