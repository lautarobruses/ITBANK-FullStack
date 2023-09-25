import React, { useState } from 'react'

import Head from 'next/head'

import TransferForm from '@/components/Transferencia/TransferForm'
import Balance from '@/components/Transferencia/Balance'
import TransactionHistory from '@/components/Transferencia/TransactionHistory'
import Layout from '@/components/layout'

const Transferencia = () => {
    const [transactions, setTransactions] = useState([])
    const [balance, setBalance] = useState(1000)

    const handleTransfer = (e) => {
      e.preventDefault()
    }

    return (
        <>
            <Head>
                <title>Nexus Bank - Transferencias</title>
                <meta name="description" content="Permite realizar tranferencias hacia otras cuentas" />
                <link rel="icon" href="favicon.ico" type="image/x-icon"></link>

                {/* Etiqueta meta para especificar el juego de caracteres */}
                <meta charSet="UTF-8" /> 

                {/* Etiqueta meta para controlar la vista móvil */}
                <meta name="viewport" content="width=device-width, initial-scale=1.0" /> 
                
                {/* Etiqueta meta para el autor */}
                <meta name="author" content="Grupo 3" />
                
                {/* Etiqueta meta para palabras clave (keywords) */}
                <meta name="keywords" content="Nexus Bank, Homebanking, Banca en línea, Préstamos personales, Pagos en línea, Transferencias seguras, Tarjetas de crédito" />
                
                {/* Etiqueta meta para el idioma de la página */}
                <meta http-equiv="Content-Language" content="es" />
                
                {/* Etiqueta meta para el robot de rastreo (crawlers) */}
                <meta name="robots" content="index, follow" /> {/*index | follow | noindex | nofollow*/}

                {/* Etiqueta meta para la traduccion de google*/}
                <meta name="google" content="notranslate" key="notranslate" />
            </Head>
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
        </>

    )
}

export default Transferencia