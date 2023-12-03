import styles from '@/styles/Pagos/Pagos.module.css'

const PaymentTable = ({ services }) => {
    return (
      <div>
        <h2>Lista de Servicios</h2>
        <table className={styles.tablePagos}>
          <thead>
            <tr>
              <th className={[styles.cell, styles.headerCell].join('')}>Tipo de Servicio</th>
              <th className={[styles.cell, styles.headerCell].join('')}>Monto</th>
              <th className={[styles.cell, styles.headerCell].join('')}>Fecha de Pago</th>
            </tr>
          </thead>
          <tbody>
            {services.map((service, index) => (
              <tr key={index}>
                <td className={styles.cell}>{service.tipoServicio}</td>
                <td className={styles.cell}>${service.monto}</td>
                <td className={styles.cell}>{service.fechaPago}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    );
  };
  
  export default PaymentTable;