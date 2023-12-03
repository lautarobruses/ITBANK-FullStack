import { useState } from 'react';
import TransferForm from '@/components/Transferencia/TransferForm';
import TransferHistory from '@/components/Transferencia/TransferHistory';
import Layout from '@/components/layout';
import styles from '@/styles/Transferencia/TransferForm.module.css'

const TransferenciasHome = () => {
  const [transfers, setTransfers] = useState([]);

  const handleTransferSubmit = (transferData) => {
    setTransfers([...transfers, transferData]);
  };

  return (
    <Layout>
        <div>
        <h1 className={styles.titulo1}>Realizá tus Transferencias</h1>
        <TransferForm onSubmit={handleTransferSubmit} />
        <TransferHistory transfers={transfers} />
        </div>
    </Layout>
  );
};

export default TransferenciasHome;