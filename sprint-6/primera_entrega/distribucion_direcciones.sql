-- Asumo que empleado, cliente y sucursal no pueden tener la mismas direccion
-- Asigno aleatoriamente las direcciones entre clientes y empleados

-- Selecciono direcciones aleatoriamente que no se encuentren en sucursal
WITH DireccionesAleatorias AS (
    SELECT direccion_id, cliente.customer_id
    FROM direccion, cliente
    WHERE direccion_id NOT IN (SELECT branch_address_id 
	                           FROM sucursal)
    ORDER BY RANDOM()
    LIMIT 500
),
-- Selecciono direcciones aleatoriamente que no se encuentren en sucursal ni en cliente
DireccionesAleatorias2 AS (
    SELECT direccion_id, empleado.employee_id
    FROM direccion, empleado
    WHERE direccion_id NOT IN (SELECT direccion_id 
	                           FROM DireccionesAleatorias
							   UNION
							   SELECT branch_address_id 
	                           FROM sucursal)
    ORDER BY RANDOM()
)

-- Actualizo la tabla direccion con las nuevas asignaciones
UPDATE direccion
SET customer_id = (
    SELECT customer_id
    FROM DireccionesAleatorias
    WHERE direccion.direccion_id = DireccionesAleatorias.direccion_id
	),
	employee_id = (
		SELECT employee_id
		FROM DireccionesAleatorias2
		WHERE direccion.direccion_id = DireccionesAleatorias2.direccion_id
	);