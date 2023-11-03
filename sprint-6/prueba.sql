--Seleccionar de la tabla de préstamos, los préstamos con un importe mayor a $80.000 y los préstamos prendarios utilizando la unión de tablas/consultas (recordar que en las bases de datos la moneda se guarda como integer, en este caso con 2 centavos)

SELECT * FROM prestamo 
WHERE loan_total > 8000000 and loan_type = 'PRENDARIO';

