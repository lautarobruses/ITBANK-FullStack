import Link from 'next/link'
import Image from 'next/image'

import { useContext } from 'react'

import { useDispatch } from 'react-redux'

import styles from '@/styles/Navbar/NavBar.module.css'

import { NavbarContext } from '@/contexts/NavbarContext'

import { logoutUser } from '../../store/reducers/loginReducer'

const Navbar = () => {
    const { isOpen, actualizarEstado } = useContext(NavbarContext)
    const dispatch = useDispatch()

    const handleToggle = () => {
        actualizarEstado(!isOpen)
    }

    const handleLogout = () => {
        dispatch(logoutUser())
    }

    return (
        <nav 
            className={`${styles.navbar} ${isOpen ? styles.show : ''}`}
            onClick={handleToggle}
        >
            <div className={`${styles.navlinks}`}>
                <Link href="/">
                    <Image 
                        src="/svg/home.svg"
                        alt="Home icon"
                        width={48}
                        height={48}
                        className='svg'
                    />
                    Inicio
                </Link>
                <Link href="/cuenta">
                    <Image 
                        src="/svg/account.svg"
                        alt="Account icon"
                        width={48}
                        height={48}
                        className={styles.svg}
                    />
                    Cuenta
                </Link> 
                <Link href="/transferencias">
                    <Image 
                        src="/svg/transfers.svg"
                        alt="Home icon"
                        width={48}
                        height={48}
                        className={styles.svg}
                    />
                    Transferencias
                </Link>
                <Link href="/pagos">
                    <Image 
                        src="/svg/payment.svg"
                        alt="Payments icon"
                        width={48}
                        height={48}
                        className={styles.svg}
                    />
                    Pagos
                </Link>
                 {/*  */}
                 <Link href="/prestamos">
                    <Image 
                        src="/svg/loans.svg"
                        alt="Loans icon"
                        width={48}
                        height={48}
                        className={styles.svg}
                    />
                    Prestamos
                </Link>
                <Link href="/login">
                    <Image 
                        src="/svg/logout.svg"
                        alt="Logout icon"
                        width={48}
                        height={48}
                        className={styles.svg}
                        onClick={handleLogout}
                    />
                    Cerrar Sesion
                </Link>
            </div>
        </nav>
    )
}

export default Navbar