import { useState } from 'react';
import TransferHistory from '@/components/Transferencia/TransferHistory';
import TransferForm from '@/components/Transferencia/TransferForm';
import Layout from '@/components/layout';

const TransferenciasHome = () => {
  const [transfers, setTransfers] = useState([]);

  const handleTransferSubmit = (transferData) => {
    setTransfers([...transfers, transferData]);
  };

  return (
    <Layout>
        <div>
            <h1>Página de Transferencias</h1>
            <TransferForm onSubmit={handleTransferSubmit} />
            <TransferHistory transfers={transfers} />
        </div>
    </Layout>
        
  );
};

export default TransferenciasHome;