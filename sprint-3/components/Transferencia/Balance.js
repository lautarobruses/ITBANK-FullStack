import React from 'react'

const Balance = ({ balance }) => {
    return(
        <div>
            <h2>Saldo Actual</h2>
            <p>{balance}</p>
        </div>
    )
}

export default Balance