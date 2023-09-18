import styles from '@/styles/Login/Login.module.css'

import Link from 'next/link'
import Image from 'next/image'

import Background from '@/components/Background'
import LoginForm from '@/components/Login-Register/LoginForm'

const Login = () => {
    return (
        <>
            <Background />
            <div className={`${styles.loginContainer}`}>
                <header className={`${styles.header}`}>
                    <Image 
                        src='/images/nexusbanklogo3.png'
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
                    <Link href="/account/register">Registrate!</Link>
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