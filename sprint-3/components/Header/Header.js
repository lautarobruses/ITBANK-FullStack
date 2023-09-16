import Image from 'next/image'

import styles from '@/styles/Header/Header.module.css'

import ButtonMenu from './ButtonMenu'

const Header = () => {
    return (
        <header className={`${styles.header}`}>
            <Image 
                src='/images/nexusbanklogo3.png'
                alt='Logo Nexus Bank'
                width={0}
                height={0}
                className={styles.nexusLogo}
                priority
            />
            <ButtonMenu />
        </header>
    )
}

export default Header