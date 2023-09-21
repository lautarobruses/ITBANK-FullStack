import React, { useState } from 'react'
import Modal from 'react-modal'
import styles from'@/styles/Transferencia/Form.module.css'

const TransferForm = () => {
    const [addressee, setAdressee] = useState ('')
    const [amount, setAmount] = useState ('')
    const [balance, setBalance] = useState(1000)
    const [transactions, setTransactions] = useState([])
    const [modalIsOpen, setModalIsOpen] = React.useState(false)
    const [modalMessage, setModalMessage] = useState('')

    const handleTransfer = (e) => {
        e.preventDefault()

        if (!/^\d*\.?\d*$/.test(amount) || parseFloat(amount) <= 0) {
            setModalMessage('El monto de la transferencia debe ser un número positivo.')
            setModalIsOpen(true)
            return
          }

          if (parseFloat(amount) > balance) {
            setModalMessage('Saldo insuficiente para realizar la transferencia.')
            setModalIsOpen(true)
            return
          }
        
          const newBalance = balance - parseFloat(amount)
        

          const newTransaction = {
            id: Date.now(),
            addressee,
            amount: parseFloat(amount),
          }
        
          setTransactions([...transactions, newTransaction])
          setBalance(newBalance);
        
  
          setModalMessage('Transferencia exitosa', newTransaction)
          setModalIsOpen(true)
    }
    function openModal() {
        setModalIsOpen(true)
    }
    function closeModal() {
        setModalIsOpen(false)
    } 

    return(
        <div className={styles.transferForm}>
            <form onSubmit={handleTransfer}>
                <div>
                    <label className={styles.labelForm}>Enviar pago a: </label>
                    <input 
                        type='text'
                        value={addressee}
                        onChange={(e) => setAdressee(e.target.value)}
                        className={styles.formInput}
                        placeholder='Nombre, @nombreusuario o email'
                        required
                    />
                </div>
                <div>
                    <label className={styles.labelForm}>Monto de la transferencia: </label>
                    <input 
                        type='number'
                        value={amount}
                        onChange={(e) => setAmount(e.target.value)}
                        className={styles.formInput}
                        placeholder='Monto'
                        required
                    />
                </div>
                <button type='submit' className={styles.formButton}>Transferir</button>
            </form>
            <Modal
            isOpen={modalIsOpen}
            onRequestClose={closeModal}
            >
                <button onClick={closeModal}>Cerrar</button>
                <h1>{modalMessage}</h1>
            </Modal>
        </div>
    )
}

export default TransferForm