-- Actualizo la columna employee_hire_date con el formato YYYY-MM-DD
UPDATE empleado
SET employee_hire_date = SUBSTR(employee_hire_date, 7, 4) || '-' || SUBSTR(employee_hire_date, 4, 2) || '-' || SUBSTR(employee_hire_date, 1, 2)
WHERE LENGTH(employee_hire_date) = 10
  AND SUBSTR(employee_hire_date, 3, 1) = '/'
  AND SUBSTR(employee_hire_date, 6, 1) = '/';
