import React, { useState } from 'react'
import TransferForm from '../../components/Transferencia/TransferForm'
import TransactionHistory from './Historial'
import Layout from '@/components/layout'
import Link from 'next/link'

const Transferencia = ({transferencias, setTransferencias}) => {

    const handleTransfer = (e) => {
      e.preventDefault()
    }
    return(
        <Layout>
            <div className="container">
                <div className="titulo">
                    <h1>TRANSFERENCIAS</h1>
                </div>
                <div>
                    <TransferForm onTransfer={handleTransfer} transferencia={transferencias} setTransferencias={setTransferencias}/>
                    <Link href='transferencias/Historial'>Ver Historial</Link>
                </div>
            </div>
        </Layout>
    )
}

export default Transferencia