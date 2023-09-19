import React from 'react'

const TransactionHistory =  ({ transactions }) => {
    return(
        <div>
            <h2>Historial de transacciones</h2>
            <ul>
                {transactions.map((transaction) => (
                    <li key={transaction.id}>
                        {transaction.recipient}: ${transaction.amount}
                    </li>
                )
                )}
            </ul>
        </div>
    )
}

export default TransactionHistory