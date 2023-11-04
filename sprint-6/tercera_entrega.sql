--Selecciona los regristros de cuentas con saldos negativos.
SELECT * FROM cuenta WHERE balance < 0;

--Seleccionar el nombre, apellido y edad de los clientes que tengan en el apellido la letra Z:

SELECT customer_name, customer_surname, strftime('%Y', 'now') - strftime('%Y', dob) - (strftime('%m-%d', 'now') < strftime('%m-%d', dob)) AS edad 
FROM cliente
WHERE customer_surname LIKE '%Z%';

--Seleccionar el nombre, apellido, edad y nombre de sucursal de las personas cuyo nombre sea “Brendan” y el resultado ordenarlo por nombre de sucursal

SELECT cliente.customer_name, cliente.customer_surname, 
       STRFTIME('%Y', 'now') - STRFTIME('%Y', cliente.dob) - (STRFTIME('%m-%d', 'now') < STRFTIME('%m-%d', cliente.dob)) AS edad, 
       sucursal.branch_name
FROM cliente
JOIN sucursal ON cliente.branch_id = sucursal.branch_id
WHERE cliente.customer_name = 'Brendan'
ORDER BY sucursal.branch_name ASC;

--Seleccionar de la tabla de préstamos, los préstamos con un importe mayor a $80.000 y los préstamos prendarios utilizando la unión de tablas/consultas (recordar que en las bases de datos la moneda se guarda como integer, en este caso con 2 centavos)

SELECT loan_type, loan_date, loan_total
FROM prestamo
WHERE loan_total > 8000000

UNION

-- Seleccionar préstamos prendarios
SELECT loan_type, loan_date, loan_total
FROM prestamo
WHERE loan_type = 'PRENDARIO';

--Seleccionar los préstamos cuyo importe sea mayor que el importe medio de todos los préstamos

SELECT * FROM Prestamo WHERE loan_total > (SELECT AVG(loan_total) FROM Prestamo);

--Contar la cantidad de clientes menores a 50 años:

SELECT COUNT(*)
FROM cliente
WHERE strftime('%Y', 'now') - strftime('%Y', dob) < 50;

--Seleccionar las primeras 5 cuentas con saldo mayor a $8,000:

SELECT * FROM cuenta WHERE balance > 800000 LIMIT 5;

--Seleccionar los préstamos que tengan fecha en abril, junio y agosto, ordenándolos por importe

SELECT * FROM Prestamo WHERE strftime('%m', loan_date) IN ('04', '06', '08') ORDER BY loan_total;

--Obtener el importe total de los prestamos agrupados por tipo de préstamos. Por cada tipo de préstamo de la tabla préstamo, calcular la suma de sus importes. Renombrar la columna como loan_total_accu

SELECT loan_type, SUM(loan_total) AS loan_total_accu
FROM prestamo
GROUP BY loan_type;