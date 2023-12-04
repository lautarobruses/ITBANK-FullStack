import { useState } from 'react';
import Modal from 'react-modal';
import styles from '@/styles/Pagos/Pagos.module.css';

Modal.setAppElement('#__next'); // Necesario para evitar advertencias de accesibilidad

const PaymentFormModal = ({ isOpen, onRequestClose, onSubmit }) => {
    console.log('Renderizando PaymentFormModal. isOpen:', isOpen);
  const [tipoServicio, setTipoServicio] = useState('');
  const [monto, setMonto] = useState('');
  const [fechaPago, setFechaPago] = useState('');

  const handleSubmit = (e) => {
    e.preventDefault();
    onSubmit({ tipoServicio, monto, fechaPago });
    onRequestClose();
  };

  return (
    <Modal
      isOpen={isOpen}
      onRequestClose={onRequestClose}
      className={styles.modalContent}
      overlayClassName={styles.reactModalOverlay}
    >
      <span className={styles.close} onClick={onRequestClose}>&times;</span>
      <h2 className={styles.h2Modal}>Ingrese los detalles del pago</h2>
      <form onSubmit={handleSubmit} className={styles.formulario}>
        <label className={styles.labelForm}>
          Tipo de Servicio:
          <input
            type="text"
            value={tipoServicio}
            onChange={(e) => setTipoServicio(e.target.value)}
            className={styles.inputForm}
            required
          />
        </label>
        <br />
        <label className={styles.labelForm}>
          Monto:
          <input
            type="number"
            value={monto}
            onChange={(e) => setMonto(e.target.value)}
            className={styles.inputForm}
            required
          />
        </label>
        <br />
        <label className={styles.labelForm}>
          Fecha de Pago:
          <input
            type="date"
            value={fechaPago}
            onChange={(e) => setFechaPago(e.target.value)}
            className={styles.inputForm}
            required
          />
        </label>
        <br />
        <button className={styles.buttonForm} type="submit">Agregar Pago</button>
      </form>
    </Modal>
  );
};

export default PaymentFormModal;