import Head from 'next/head'

import { useEffect } from 'react'

import { useDispatch, useSelector } from 'react-redux'

import { initializeUserData } from '@/store/reducers/userReducer'

import SummaryAccount from '@/components/Main/SummaryAccount'
import Layout from '@/components/layout'

const Home = () => {
    const dispatch = useDispatch()
    const cuentas = useSelector((state) => state.cuentas)
    const userInfo = useSelector((state) => state.user)

    useEffect(() => {
        dispatch(initializeUserData())
            .catch((error) => {
                console.log(error);
            });  
    }, [dispatch])

    console.log(userInfo);
    
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
                <SummaryAccount nombreCompleto={"lautaro"} cuentas={cuentas} tarjetas={null}/>
            </Layout>
        </>
    )
}

export default Home
