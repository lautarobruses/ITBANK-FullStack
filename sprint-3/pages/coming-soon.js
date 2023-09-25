import styles from '@/styles/ComingSoon.module.css'

import Image from 'next/image'

const ComingSoon = () => {
    return (
        <div className={`${styles.container}`}>
            <h1>¡Página en construcción!</h1>
            <Image
                src="/construccion-page.gif"
                alt="Hombre construyendo una pagina web"
                width={300} 
                height={300} 
                quality={80}
            />
        </div>
    )
}

export default ComingSoon