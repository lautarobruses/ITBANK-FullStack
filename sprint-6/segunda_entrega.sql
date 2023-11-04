-- 1. Crear una vista con las columnas id, numero sucursal, nombre, apellido, DNI
-- y edad de la tabla cliente calculada a partir de la fecha de nacimiento

CREATE VIEW IF NOT EXISTS VistaClientes AS
SELECT
    customer_id, branch_id, customer_name, customer_surname, customer_DNI,
    strftime( '%Y', 'now' ) - strftime( '%Y', dob ) AS age
FROM Cliente;

-- Mostrar las columnas de los clientes, ordenadas por el DNI de menor
-- a mayor y cuya edad sea superior a 40 años

SELECT customer_id, branch_id, customer_name, customer_surname, customer_DNI, age
FROM VistaClientes
WHERE age > 40
ORDER BY customer_DNI;

-- Mostrar todos los clientes que se llaman “Anne” o “Tyler” ordenados
-- por edad de menor a mayo

SELECT customer_id, branch_id, customer_name, customer_surname, customer_DNI, age
FROM VistaClientes
WHERE customer_name IN ('Anne', 'Tyler')
ORDER BY age;

-- 2. Dado el siguiente JSON. Insertar 5 nuevos clientes en la base de datos y
-- verificar que se haya realizado con éxito la inserción

INSERT INTO Cliente ( customer_name, customer_surname, customer_DNI, branch_id, dob)
SELECT
  json_extract(value, '$.customer_name'),
  json_extract(value, '$.customer_surname'),
  json_extract(value, '$.customer_DNI'),
  json_extract(value, '$.branch_id'),
  json_extract(value, '$.dob')
FROM json_each('
    [
        {
            "customer_name": "Lois",
            "customer_surname": "Stout",
            "customer_DNI": 47730534,
            "branch_id": 80,
            "dob": "1984-07-07"
        },
        {
            "customer_name": "Hall",
            "customer_surname": "Mcconnell",
            "customer_DNI": 52055464,
            "branch_id": 45,
            "dob": "1968-04-30"
        },
        {
            "customer_name": "Hilel",
            "customer_surname": "Mclean",
            "customer_DNI": 43625213,
            "branch_id": 77,
            "dob": "1993-03-28"
        },
        {
            "customer_name": "Jin",
            "customer_surname": "Cooley",
            "customer_DNI": 21207908,
            "branch_id": 96,
            "dob": "1959-08-24"
        },
        {
            "customer_name": "Gabriel",
            "customer_surname": "Harmon",
            "customer_DNI": 57063950,
            "branch_id": 27,
            "dob": "1976-04-01"
        }
    ]
');


-- DELETE FROM Cliente
-- WHERE customer_id > 500

-- 3. Actualizar 5 clientes recientemente agregados en la base de datos dado que
-- hubo un error en el JSON que traía la información, la sucursal de todos es la 10

UPDATE Cliente
SET branch_id = 10
WHERE customer_id IN (
    SELECT customer_id
    FROM Cliente 
    ORDER BY customer_id DESC
    LIMIT 5
);

-- 4. Eliminar el registro correspondiente a “Noel David” realizando la selección
-- por el nombre y apellido

DELETE FROM Cliente
WHERE customer_name || ' ' || customer_surname = 'Noel David'

--INSERT INTO Cliente ( customer_name, customer_surname, customer_DNI, branch_id, dob)
--VALUES ('Noel', 'David', 9999999, 10, '0002-02-02')

-- 5. Consultar sobre cuál es el tipo de préstamo de mayor importe

SELECT loan_type
FROM prestamo
WHERE loan_total IN (
    SELECT MAX(loan_total)
    FROM prestamo
);