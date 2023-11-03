-- primer inciso

CREATE VIEW IF NOT EXISTS VistaClientes AS
SELECT
    customer_id,
    branch_id,
    customer_name,
    customer_surname,
    customer_DNI
    -- falta poner la age calculada con la fecha de nacimiento
FROM Cliente;

SELECT
    customer_id,
    branch_id,
    customer_name,
    customer_surname,
    customer_DNI,
    age
FROM VistaClientes
WHERE age > 40
ORDER BY customer_DNI;

SELECT
    customer_id,
    branch_id,
    customer_name,
    customer_surname,
    customer_DNI,
    age
FROM VistaClientes
WHERE customer_name IN ('Anne', 'Tyler')
ORDER BY age;

-- segundo inciso



-- tercer inciso



-- cuarto inciso



-- quinto inciso