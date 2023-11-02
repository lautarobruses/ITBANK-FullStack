
SELECT * FROM Cuenta WHERE account_balance < 0;

--Seleccionar el nombre, apellido y edad de los clientes que tengan en el apellido la letra Z:

SELECT customer_name, customer_surname --falta la edad
FROM Cliente
WHERE customer_surname LIKE '%Z%';

--Seleccionar de la tabla de préstamos los préstamos con un importe mayor a $80,000 y los préstamos prendarios:

SELECT * FROM Prestamo WHERE loan_total > 80000 OR tipo =; --Falta tipo prendario

--Seleccionar los préstamos cuyo importe sea mayor que el importe medio de todos los préstamos:

SELECT * FROM Prestamo WHERE loan_total > (SELECT AVG(loan_total) FROM Prestamo);

--Contar la cantidad de clientes menores a 50 años:

SELECT COUNT(*) FROM Cliente WHERE --Falta la edad < 50;

--Seleccionar las primeras 5 cuentas con saldo mayor a $8,000:

SELECT * FROM Cuenta WHERE account_balance > 8000 LIMIT 5;

--Seleccionar los préstamos que tengan fecha en abril, junio y agosto, ordenándolos por importe:

SELECT * FROM Prestamo WHERE strftime('%m', loan_date) IN ('04', '06', '08') ORDER BY loan_total;
