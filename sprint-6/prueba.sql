SELECT loan_type, SUM(loan_total) AS loan_total_accu
FROM prestamo
GROUP BY loan_type;