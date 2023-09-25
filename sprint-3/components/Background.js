import styles from '@/styles/Background.module.css'

import Image from 'next/image'

const Background = () => {

    
    return (
        <div className={styles.background}>
            <Image
                src="/images/background.webp"
                alt="Fondo principal del sitio"
                layout="fill"
                quality={80}
            />
        </div>
    );
}

export default Background