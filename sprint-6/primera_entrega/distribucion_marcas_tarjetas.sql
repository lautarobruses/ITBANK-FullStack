WITH marcasAleatorias AS (
    SELECT marca_tarjeta.marca_tarjeta_id, tarjeta.tarjeta_numero
    FROM marca_tarjeta, tarjeta
    ORDER BY RANDOM()
)

-- Actualizo la tabla tarjeta con las marcas aleatoriamente
UPDATE tarjeta
SET marca_tarjeta_id = (
    SELECT marca_tarjeta_id
    FROM marcasAleatorias
	WHERE tarjeta.tarjeta_numero = marcasAleatorias.tarjeta_numero
);
