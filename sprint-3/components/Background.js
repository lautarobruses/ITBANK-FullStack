import styles from '@/styles/Background.module.css'

import Image from 'next/image'

const Background = () => {

    
    return (
        <div className={styles.background}>
            <Image
                src="/images/background.jpg"
                alt="Fondo principal del sitio"
                layout="fill"
                objectFit="cover"
                objectPosition="center top"
                quality={80}
            />
        </div>
    );
}

export default Background