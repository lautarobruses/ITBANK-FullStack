import styles from '@/styles/Login/Login.module.css'

import { useEffect } from 'react'

import { useRouter } from 'next/router'

import Head from 'next/head'
import Link from 'next/link'
import Image from 'next/image'

import { useSelector } from 'react-redux'

import Background from '@/components/Background'
import LoginForm from '@/components/Login-Register/LoginForm'


const Login = () => {
    const router = useRouter();
    const loggedUser = useSelector((state) => state.loggedUser)

    useEffect(() => {
        if (loggedUser) {
            router.replace('/');
        }
    }, [loggedUser, router]);

    return (
        <>
            <Head>
                <title>Nexus Bank - Login</title>
                <meta name="description" content="Permite a los usuarios ingresar al home banking" />
                <link rel="icon" href="favicon.ico" type="image/x-icon"/>

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
            <Background />
            <div className={`${styles.loginContainer}`}>
                <header className={`${styles.header}`}>
                    <Image 
                        src='/images/nexusbanklogo3.webp'
                        alt='Logo Nexus Bank'
                        width={100}
                        height={100}
                        className={styles.nexusLogo}
                        quality={100}
                        priority
                    />
                </header>
                <LoginForm />
                <div className={`${styles.footerRegister}`}>
                    <p>¿No tienes una cuenta? </p>
                    <Link href="/cuenta/register">Registrate!</Link>
                </div>
                <div className={`${styles.footerTerms}`}>
                    <Link href="/coming-soon">Terminos</Link>
                    <span>|</span>
                    <Link href="/coming-soon">Privacidad</Link>
                </div>
            </div>
        </>
    )
}

export default Login