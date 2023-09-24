import styles from '@/styles/Login/Register.module.css'

import Image from 'next/image'

import RegisterForm from '@/components/Login-Register/RegisterForm'
import Background from '@/components/Background'

const Register = () => {

    return (
        <>
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