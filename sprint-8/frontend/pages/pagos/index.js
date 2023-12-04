import { useState } from 'react';
import PaymentFormModal from '@/components/Pagos/PaymentFormModal';
import PaymentTable from '@/components/Pagos/PaymentTable';
import Layout from '@/components/layout';
import styles from '@/styles/Pagos/Pagos.module.css'

const Pagos = () => {
  const [showModal, setShowModal] = useState(false);
  const [services, setServices] = useState([]);

  const handleFormSubmit = (service) => {
    setServices([...services, service]);
    setShowModal(false);
  };

  const handleButtonClick = () => {
    console.log('Antes de acutilizar modal: ', showModal)
    setShowModal(true)
    console.log('Despues de actualizar modal: ', showModal)
  }

  const closeModal = () => {
    setShowModal(false);
  };

  return (
    <Layout>
        <div>
        <h1 className={styles.h1Pagos}>Página de Pagos</h1>

        {services.length === 0 ? (
            <p className={styles.pPagos}>No hay servicios disponibles.</p>
        ) : (
            <PaymentTable services={services} />
        )}

        {showModal && (
            <PaymentFormModal
            onSubmit={handleFormSubmit}
            onRequestClose={closeModal}
            isOpen={showModal}
            />
        )}
        <button className={styles.buttonPagos} onClick={handleButtonClick}>Agregar Pago</button>
        </div>
    </Layout>
  );
};

export default Pagos;