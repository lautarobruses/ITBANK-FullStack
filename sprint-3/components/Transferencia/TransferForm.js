import React, { useState } from 'react'
import styles from'@/styles/Transferencia/Form.module.css'

const TransferForm = () => {
    const [recipient, setRecipient] = useState ('')
    const [amount, setAmount] = useState ('')
    const [balance, setBalance] = useState(1000)
    const [transactions, setTransactions] = useState([])

    const handleTransfer = (e) => {
        e.preventDefault()

        if (!/^\d*\.?\d*$/.test(amount) || parseFloat(amount) <= 0) {
            console.error('El monto de la transferencia debe ser un número positivo.');
            return
          }

          if (parseFloat(amount) > balance) {
            console.error('Saldo insuficiente para realizar la transferencia.');
            return
          }
        
          const newBalance = balance - parseFloat(amount)
        

          const newTransaction = {
            id: Date.now(),
            recipient,
            amount: parseFloat(amount),
          }
        
          setTransactions([...transactions, newTransaction])
          setBalance(newBalance);
        
  
          console.log('Transferencia exitosa:', newTransaction)
    }

    return(
        <div className={styles.transferForm}>
            <form onSubmit={handleTransfer}>
                <div>
                    <label className={styles.labelForm}>Enviar pago a: </label>
                    <input 
                        type='text'
                        value={recipient}
                        onChange={(e) => setRecipient(e.target.value)}
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
        </div>
    )
}

export default TransferForm