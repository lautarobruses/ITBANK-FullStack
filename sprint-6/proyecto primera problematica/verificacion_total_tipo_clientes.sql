SELECT COUNT(*) AS total_registros
FROM (
    SELECT * FROM cliente_classic
    UNION ALL
    SELECT * FROM cliente_gold
    UNION ALL
    SELECT * FROM cliente_black
) AS tablas_combinadas;