import styles from '@/styles/Transferencia/TransferHistory.module.css'

const TransferHistory = ({ transfers }) => {
    if (transfers.length === 0) {
      return <p className={styles.noTransfersMessage}>No tienes transferencias realizadas.</p>
    }
  
    return (
      <div className={styles.historyContainer}>
        <h2>Historial de Transferencias</h2>
        <table className={styles.tableContainer}>
          <thead>
            <tr>
              <th className={styles.headerCell}>Destino</th>
              <th className={styles.headerCell}>Monto</th>
              <th className={styles.headerCell}>Motivo</th>
            </tr>
          </thead>
          <tbody>
            {transfers.map((transfer, index) => (
              <tr key={index}>
                <td className={styles.cell}>{transfer.destino}</td>
                <td className={styles.cell}>${transfer.monto}</td>
                <td className={styles.cell}>{transfer.motivo}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    );
  };
  
  export default TransferHistory;