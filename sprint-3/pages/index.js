import { useEffect } from 'react'

import Head from 'next/head'

import { useDispatch } from 'react-redux'

import { initializeLoged } from '@/store/reducers/loginReducer'

import Layout from '@/components/layout'


export default function Home() {
    const dispatch = useDispatch()

    useEffect(() => {
        dispatch(initializeLoged())
    }, [dispatch])

    return (
        <>
            <Head>
                <title>Nexus Bank - Inicio</title>
                <meta name="description" content="Pagina principal del sitio" />
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
                <>
                    <h1>HOLA USUARIO</h1>
                </>
            </Layout>
        </>
    )
}
