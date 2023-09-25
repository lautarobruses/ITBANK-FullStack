import Image from 'next/image'

import styles from '@/styles/Header/Header.module.css'

import ButtonMenu from './ButtonMenu'

const Header = () => {
    return (
        <header className={`${styles.header}`}>
            <Image 
                src='/images/nexusbanklogo3.webp'
                alt='Logo Nexus Bank'
                width={220}
                height={72}
                quality={100}
                priority
            />
            <ButtonMenu />
        </header>
    )
}

export default Header