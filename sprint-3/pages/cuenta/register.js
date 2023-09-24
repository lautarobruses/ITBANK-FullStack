import styles from '@/styles/Login/Register.module.css'

import Head from 'next/head'
import Image from 'next/image'

import RegisterForm from '@/components/Login-Register/RegisterForm'
import Background from '@/components/Background'


const Register = () => {
    return (
        <>
            <Head>
                <title>Nexus Bank - Registrarse</title>
                <meta name="description" content="Pagina principal del sitio" />

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
                
                {/* Etiqueta meta para la URL canónica */}
                <link rel="canonical" href="https://www.tusitio.com/tu-pagina" />

                {/* Etiqueta meta para la traduccion de google*/}
                <meta name="google" content="notranslate" key="notranslate" />
            </Head>
            <Background />
            <div className={`${styles.registerContainer}`}>
                <header className={`${styles.header}`}>
                    <Image 
                        src='/images/nexusbanklogo3.png'
                        alt='Logo Nexus Bank'
                        width={100}
                        height={60}
                        className={styles.nexusLogo}
                        quality={100}
                        priority
                    />
                </header>
                <RegisterForm/>
            </div>
        </>
    )
}

export default Register