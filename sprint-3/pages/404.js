import styles from '@/styles/404.module.css'

import Head from 'next/head'
import Image from 'next/image'
import Link from 'next/link'

import Background from '@/components/Background'

const PageNotFound = () => {
    return (
        <>
            <Head>
                <title>Nexus Bank - Error 404</title>
                <meta name="description" content="ERROR: La pagina no existe" />

                {/* Etiqueta meta para especificar el juego de caracteres */}
                <meta charSet="UTF-8" /> 

                {/* Etiqueta meta para controlar la vista móvil */}
                <meta name="viewport" content="width=device-width, initial-scale=1.0" /> 
                
                {/* Etiqueta meta para el autor */}
                <meta name="author" content="Grupo 3" />
                
                {/* Etiqueta meta para el idioma de la página */}
                <meta http-equiv="Content-Language" content="es" />
                
                {/* Etiqueta meta para el robot de rastreo (crawlers) */}
                <meta name="robots" content="noindex, nofollow" /> {/*index | follow | noindex | nofollow*/}

                {/* Etiqueta meta para la traduccion de google*/}
                <meta name="google" content="notranslate" key="notranslate" />
            </Head>
            <div className={`${styles.container}`}>
                <Background />
                <h1>404</h1>
                <h2>Pagina no encontrada</h2>
                <Image 
                    src='/images/cableDesconectado.webp'
                    alt='Cable desconectado'
                    width={710}
                    height={94}
                    quality={80}
                />
                <p>La pagina a la que intentas acceder no existe</p>
                <Link href="/">
                    <button>Volver al inicio</button>
                </Link>
            </div>
        </>
    )
}

export default PageNotFound