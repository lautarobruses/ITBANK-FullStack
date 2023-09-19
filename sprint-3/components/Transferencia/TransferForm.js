import React, { useState } from 'react'

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
        <div>
            <h2>TRANSFERENCIAS</h2>
            <form onSubmit={handleTransfer}>
                <div>
                    <label>Destinatario: </label>
                    <input 
                        type='text'
                        value={recipient}
                        onChange={(e) => setRecipient(e.target.value)}
                        required
                    />
                </div>
                <div>
                    <label>Monto: </label>
                    <input 
                        type='number'
                        value={amount}
                        onChange={(e) => setAmount(e.target.value)}
                        required
                    />
                </div>
                <button type='submit'>Transferir</button>
            </form>
        </div>
    )
}

export default TransferForm