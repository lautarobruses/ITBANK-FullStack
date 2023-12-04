import Head from 'next/head'

import { useEffect } from 'react'

import { useDispatch, useSelector } from 'react-redux'

import { initializeUserData } from '@/store/reducers/userReducer'
import { initializeCuentas } from '@/store/reducers/cuentasReducer'
import { initializeTarjetas } from '@/store/reducers/tarjetasReducer'

import SummaryAccount from '@/components/Main/SummaryAccount'
import Layout from '@/components/layout'

const Home = () => {
    const dispatch = useDispatch()
    const cuentas = useSelector((state) => state.cuentas)
    const tarjetas = useSelector((state) => state.tarjetas)
    const userInfo = useSelector((state) => state.user)

    //info
    useEffect(() => {
        dispatch(initializeUserData())
    }, [dispatch])

    //Cuentas
    useEffect(() => {
        if (userInfo) {
            dispatch(initializeCuentas(userInfo.customer_id))
        }
    }, [dispatch, userInfo])

    //tarjetas
    useEffect(() => {
        if (userInfo) {
            dispatch(initializeTarjetas(userInfo.customer_id))
        }
    }, [dispatch, userInfo])

    const nombreCompleto = `${userInfo?.customer_name} ${userInfo?.customer_surname}`
    
    return (
        <>
            <Head>
                <title>Nexus Bank - Inicio</title>
                <meta name="description" content="Pagina principal del sitio" />
                <link rel="shortcut icon" href="favicon.ico" />

                {/* Etiqueta meta para especificar el juego de caracteres */}
                <meta charSet="UTF-8" /> 

                {/* Etiqueta meta para controlar la vista móvil */}
                <meta name="viewport" content="width=device-width, initial-scale=1.0" /> 
                
                {/* Etiqueta meta para el autor */}
                <meta name="author" content="Grupo 3" />
                
                {/* Etiqueta meta para palabras clave (keywords) */}
                <meta name="keywords" content="Nexus Bank, Homebanking, Banca en línea, Préstamos personales, Pagos en línea, Transferencias seguras, Tarjetas de crédito" />
                
                {/* Etiqueta meta para el idioma de la página */}
                <meta httpEquiv="Content-Language" content="es" />
                
                {/* Etiqueta meta para el robot de rastreo (crawlers) */}
                <meta name="robots" content="index, follow" /> {/*index | follow | noindex | nofollow*/}

                {/* Etiqueta meta para la traduccion de google*/}
                <meta name="google" content="notranslate" key="notranslate" />
            </Head>
            <Layout>
                <SummaryAccount nombreCompleto={nombreCompleto} cuentas={cuentas} tarjetas={tarjetas}/>
            </Layout>
        </>
    )
}

export default Home
