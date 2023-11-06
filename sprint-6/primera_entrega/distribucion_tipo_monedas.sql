WITH monedasAleatorias AS (
    SELECT tipo_moneda.moneda_id, cuenta.account_id
    FROM tipo_moneda, cuenta
    ORDER BY RANDOM()
)

-- Actualizo la tabla tarjeta con las marcas aleatoriamente
UPDATE cuenta
SET tipo_moneda_id = (
    SELECT moneda_id
    FROM monedasAleatorias
	WHERE cuenta.account_id = monedasAleatorias.account_id
);