import React from 'react'

import Head from 'next/head'
import Link from 'next/link'

import TransferForm from '@/components/Transferencia/TransferForm'
import Layout from '@/components/layout'


const Transferencia = ({transferencias, setTransferencias}) => {

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
                    </div>
                    <div>
                        <TransferForm onTransfer={handleTransfer} transferencia={transferencias} setTransferencias={setTransferencias}/>
                        <Link href='transferencias/Historial'>Ver Historial</Link>
                    </div>
                </div>
            </Layout>
        </>

    )
}

export default Transferencia