import Background from '@/components/Background'
import styles from '@/styles/ComingSoon.module.css'

import Head from 'next/head'
import Image from 'next/image'

const ComingSoon = () => {
    return (
        <>
            <Head>
                <title>Nexus Bank - Coming Soon</title>
                <meta name="description" content="Proximamente" />
                <link rel="icon" href="favicon.ico" type="image/x-icon"></link>

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
            <Background/>
            <div className={`${styles.container}`}>
            <h1>¡Página en construcción!</h1>
            <Image
                src="/construccion-page.gif"
                alt="Hombre construyendo una pagina web"
                width={300} 
                height={300} 
                quality={80}
                loading="lazy"
            />
        </div>
        </> 
    )
}

export default ComingSoon