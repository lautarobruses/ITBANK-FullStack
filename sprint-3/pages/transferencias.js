import React, { useState } from 'react'
import TransferForm from '../components/Transferencia/TransferForm'
import Balance from '../components/Transferencia/Balance'
import TransactionHistory from '../components/Transferencia/TransactionHistory'
import Layout from '@/components/layout'

const Transferencia = () => {
    const [transactions, setTransactions] = useState([])
    const [balance, setBalance] = useState(1000)

    const handleTransfer = (e) => {
      e.preventDefault()
    }
    return(
        <Layout>
            <div className="container">
                <div className="titulo">
                    <h1>TRANSFERENCIAS</h1>
                    <h3>TODOS LOS CONTACTOS</h3>
                </div>
                <div>
                    <Balance balance={balance} />
                    <TransferForm onTransfer={handleTransfer} />
                    <TransactionHistory transactions={transactions}/>
                </div>
            </div>
        </Layout>
    )
}

export default Transferencia