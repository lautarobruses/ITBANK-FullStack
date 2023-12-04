import styles from'@/styles/Transferencia/TransferForm.module.css'

import { useState } from 'react';

const TransferForm = ({ onSubmit }) => {
  const [destino, setDestino] = useState('');
  const [monto, setMonto] = useState('');
  const [motivo, setMotivo] = useState('');

  const handleSubmit = (e) => {
        e.preventDefault();
        onSubmit({ destino, monto, motivo });
        setDestino('');
        setMonto('');
        setMotivo('');
  };

  return (
    <form onSubmit={handleSubmit} className={styles.formContainer}>
      <label className={styles.labelContainer}>
        Alias, CBU o CVU de Destino:
        <input className={styles.inputContainer} type="text" value={destino} onChange={(e) => setDestino(e.target.value)} required/>
      </label>
      <br />
      <label className={styles.labelContainer}>
        Monto:
        <input className={styles.inputContainer} type="number" value={monto} onChange={(e) => setMonto(e.target.value)} required/>
      </label>
      <br />
      <label className={styles.labelContainer}>
        Motivo:
        <input className={styles.inputContainer} type="text" value={motivo} onChange={(e) => setMotivo(e.target.value)} />
      </label>
      <br />
      <button className={styles.buttonContainer}type="submit">Realizar Transferencia</button>
    </form>
  );
};

export default TransferForm

