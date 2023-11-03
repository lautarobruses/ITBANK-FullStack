/*
ENUNCIADO 1:
Listar la cantidad de clientes por nombre de sucursal ordenando de mayor
a menor
*/
SELECT Sucursales.branch_name, COUNT(Clientes.customer_id) AS customer_count
-- A partir del branch id se combinan los datos de sucursal y cliente, customer_count como contador de clientes
FROM Clientes
INNER JOIN Sucursales ON Clientes.branch_id = Sucursales.branch_id
GROUP BY Sucursales.branch_name 
ORDER BY customer_count DESC;
-- cada nombre de sucursal se lista de manera descendente con la cantidad de clientes por sucursal

/*
ENUNCIADO 2:
Obtener la cantidad de empleados por cliente por sucursal en un número
real
*/


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
  old_id INT,
  new_id INT,
  old_balance DECIMAL(10,2),
  new_balance DECIMAL(10,2),
  old_iban VARCHAR(34),
  new_iban VARCHAR(34),
  old_type VARCHAR(50),
  new_type VARCHAR(50),
  user_action VARCHAR(50),
  created_at TIMESTAMP
)
-- Falta crear el trigger
UPDATE cuentas
SET balance = balance - 100
WHERE id IN (10,11,12,13,14);
