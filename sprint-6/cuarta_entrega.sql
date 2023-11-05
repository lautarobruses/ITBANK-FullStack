/*
ENUNCIADO 1:
Listar la cantidad de clientes por nombre de sucursal ordenando de mayor
a menor
*/
SELECT Sucursal.branch_name, COUNT(cliente.customer_id) AS customer_count
-- A partir del branch id se combinan los datos de sucursal y cliente, customer_count como contador de clientes
FROM cliente
INNER JOIN sucursal ON cliente.branch_id = sucursal.branch_id
GROUP BY sucursal.branch_name 
ORDER BY customer_count DESC;
-- cada nombre de sucursal se lista de manera descendente con la cantidad de clientes por sucursal

/*
ENUNCIADO 2:
Obtener la cantidad de empleados por cliente por sucursal en un número
real
*/
SELECT branch_name, COUNT(e.employee_id) / COUNT(c.customer_id) AS proporcion_empleados_clientes
FROM cliente c
INNER JOIN empleado e ON c.branch_id = e.branch_id
INNER JOIN sucursal s ON c.branch_id = s.branch_id
GROUP BY s.branch_name;
/*ENUNCIADO 3:
Obtener la cantidad de empleados por cliente por sucursal en un número
real
*/
SELECT branch_name, m.marca_tarjeta_nombre, COUNT(t.tarjeta_numero) AS cantidad_tarjetas_credito
FROM sucursal AS s
INNER JOIN cliente AS c ON S.branch_id = c.branch_id
INNER JOIN tarjeta AS t ON c.customer_id = t.customer_id
INNER JOIN marca_tarjeta AS m ON t.marca_tarjeta_id = m.marca_tarjeta_id
GROUP BY s.branch_name, m.marca_tarjeta_nombre;
/*ENUNCIADO 4:
 Obtener el promedio de créditos otorgado por sucursal
*/
SELECT branch_name, AVG(loan_total) AS credit_average
FROM sucursal AS s
JOIN cliente AS c ON s.branch_id = c.branch_id
JOIN prestamo AS p  ON c.customer_id = p.customer_id
GROUP BY s.branch_name;
/*

ENUNCIADO 5:
La información de las cuentas resulta critica para la compañía, por eso es
necesario crear una tabla denominada “auditoria_cuenta” para guardar los
datos movimientos, con los siguientes campos: old_id, new_id, old_balance,
new_balance, old_iban, new_iban, old_type, new_type, user_action,
created_at
o Crear un trigger que después de actualizar en la tabla cuentas los
campos balance, IBAN o tipo de cuenta registre en la tabla auditoria
o Restar $100 a las cuentas 10,11,12,13,14*/
CREATE TABLE auditoria_cuenta (
  id INT AUTOINCREMENT PRIMARY KEY,
  old_id INT,
  new_id INT,
  old_balance DECIMAL(10,2),
  new_balance DECIMAL(10,2),
  old_iban VARCHAR(34),
  new_iban VARCHAR(34),
  old_type VARCHAR(50),
  new_type VARCHAR(50),
  user_action VARCHAR(50),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TRIGGER IF NOT EXISTS trigger_auditoria
AFTER UPDATE OF balance, iban, type ON cuenta  --falta crear campo tipo de cuenta
BEGIN 
  INSERT INTO auditoria_cuenta (old_id, new_id, old_balance, new_balance, old_iban, new_iban, old_type, new_type, user_action)
  VALUES (old.account_id, new.account_id, old.balance, new.balance, old.iban, new.iban, old.type, new.type, 'update');
END;
UPDATE cuenta
SET balance = balance - 10000
WHERE account_id IN (10,11,12,13,14);

SELECT * FROM auditoria_cuenta;

/*ENUNCIADO 6:
Mediante índices mejorar la performance la búsqueda de clientes por DNI
*/
CREATE UNIQUE INDEX idx_customer_DNI ON cliente(customer_DNI);

/*ENUNCIADO 7:
 Crear la tabla “movimientos” con los campos de identificación del
movimiento, número de cuenta, monto, tipo de operación y hora
o Mediante el uso de transacciones, hacer una transferencia de 1000$
desde la cuenta 200 a la cuenta 400
o Registrar el movimiento en la tabla movimientos
o En caso de no poder realizar la operación de forma completa, realizar
un ROLLBACK*/

CREATE TABLE movimientos(
  id_movimiento INTEGER PRIMARY KEY AUTOINCREMENT,
  numero_cuenta INTEGER REFERENCES cuenta ON UPDATE CASCADE ON DELETE SET NULL,
  monto DECIMAL(10,2),
  tipo_operacion VARCHAR(50),
  hora TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
BEGIN; --se inicia la transacción

SELECT  balance FROM cuenta WHERE account_id IN (200,400); -- se consulta el saldo inicial
-- si es posible realizar la transferencia
UPDATE cuenta SET balance = balanace - 100000 WHERE account_id = 200;
UPDATE cuenta SET balance = balanace + 100000 WHERE account_id = 400;
--registrar los movimientos en la tabla movimientos
INSERT INTO movimientos (numero_cuenta, monto, tipo_operacion)
VALUES (200, -100000, 'transferencia  enviada');

INSERT INTO movimientos (numero_cuenta, monto, tipo_operacion)
VALUES (400, 100000, 'transferencia recibida');
-- consultar el saldo despues de la transferencia
SELECT  balance FROM cuenta WHERE account_id IN (200,400);
-- confirmar la transaccion
COMMIT;
-- ROLLBACK;
