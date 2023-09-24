import styles from '@/styles/404.module.css'

import Image from 'next/image'
import Link from 'next/link'

import Background from '@/components/Background'

const PageNotFound = () => {
    return (
        <main className={`${styles.container}`}>
            <Background />
            <h1>404</h1>
            <h2>Pagina no encontrada</h2>
            <Image 
                src='/images/cableDesconectado.png'
                alt='Cable desconectado'
                width={600}
                height={100}
                quality={100}
                priority
            />
            <p>La pagina a la que intentas acceder no existe</p>
            <p>Intenta volver a la pagina principa.</p>
            <Link href="/">
                <button>Volver al inicio</button>
            </Link>
        </main>
    )
}

export default PageNotFound