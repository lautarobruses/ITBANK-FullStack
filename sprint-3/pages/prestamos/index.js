import styles from '@/styles/prestamos/Prestamos.module.css'

import React, {useState} from 'react'

import Calculadora from '@/components/Prestamos/Calculadora'
import Layout from '@/components/layout'

import Head from 'next/head'

export default function Formulario() {
    const [Monto, setMonto] = useState(0);
    const [Interes, setInteres] = useState(0);
    const [Plazo, setPlazo] = useState(0);
  
    return (
        <>
            <Head>
                <title>Nexus Bank - Prestamos</title>
                <meta name="description" content="Permite calcular prestamos" />
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
                <div className={`${styles.formContainer}`}>
                    <div className={`${styles.formText}`}>
                        <h1>Calculadora de Préstamos</h1>
                        <p>Bienvenido a nuestra calculadora de préstamos, donde puedes calcular cuánto podrías pedir prestado y estimar tus pagos mensuales. Ingresa la información requerida a continuación para obtener una estimación.</p>
                    </div>
                    <div className={`${styles.calculatorContainer}`}>
                    <form>
                    <label htmlFor='monto'>Monto del préstamo:</label>
                    <input
                        type='number'
                        name='monto'
                        placeholder='Ingrese el monto'
                        value={Monto}
                        onChange={(e) => setMonto(e.target.value)}
                    />

                    <label htmlFor='interes'>Tasa de interés:</label>
                    <input
                        type='number'
                        name='interes'
                        placeholder='Ingrese la tasa de interés en %'
                        value={Interes}
                        onChange={(e) => setInteres(e.target.value)}
                    />

                    <label htmlFor='plazo'>Plazo anual:</label>
                    <input
                        type='number'
                        name='plazo'
                        placeholder='Ingrese el plazo en años'
                        value={Plazo}
                        onChange={(e) => setPlazo(e.target.value)}
                    />
                    </form>

                    <h2>Resultados</h2>
                    <p>Basado en la información proporcionada, aquí tienes una estimación de tus pagos:</p>
                    <Calculadora p={Number(Monto)} r={Number(Interes)} t={Number(Plazo)} />
                    </div>
                </div>
                {/* <div className={styles.imagesContainer}>
                    <img
                        src={pres1}
                        alt='Solicite su préstamo en nuestro banco'
                    />
                    <img
                        src='imagen2.jpg'
                        alt='Promociones especiales en préstamos'
                    />
                    <img
                        src='imagen3.jpg'
                        alt='Calculadora de préstamos en línea'
                    />
                </div> */}
            </Layout>
        </>
    )
}
