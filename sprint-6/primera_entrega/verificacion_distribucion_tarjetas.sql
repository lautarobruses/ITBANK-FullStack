--Verifico las tarjetas que no cumplen las condiciones de cliente_black y cliente_gold
SELECT SUM(total_count) as suma_total FROM (
    SELECT count(*) as total_count
    FROM tarjeta, tarjeta_credito
    WHERE customer_id IN (SELECT customer_id FROM cliente_gold)
        AND tarjeta.tarjeta_numero = tarjeta_credito.tarjeta_numero
        AND (tarjeta_credito.cantidad_extensiones > 5 OR tarjeta.marca_tarjeta_id = 3)
    UNION ALL
    SELECT count(*) as total_count
    FROM tarjeta, tarjeta_credito
    WHERE customer_id IN (SELECT customer_id FROM cliente_black)
        AND tarjeta.tarjeta_numero = tarjeta_credito.tarjeta_numero
        AND (tarjeta_credito.cantidad_extensiones > 10)
) as subconsulta;
