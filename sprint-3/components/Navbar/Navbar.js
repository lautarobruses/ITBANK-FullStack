import Link from 'next/link'

import { useContext } from 'react'

import { useDispatch } from 'react-redux'

import styles from '@/styles/Navbar/NavBar.module.css'

import HomeIcon from "@/public/svg/home.svg";
import AccountIcon from "@/public/svg/account.svg";
import TranfersIcon from "@/public/svg/transfers.svg";
import PaymentsIcon from "@/public/svg/payment.svg";
import LoansIcon from "@/public/svg/loans.svg";
import LogoutIcon from "@/public/svg/logout.svg";

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
                    <HomeIcon />
                    Inicio
                </Link>
                <Link href="/cuenta">
                    <AccountIcon />
                    Cuenta
                </Link> 
                <Link href="/transferencias">
                    <TranfersIcon />
                    Transferencias
                </Link>
                <Link href="/pagos">
                    <PaymentsIcon />
                    Pagos
                </Link>
                 <Link href="/prestamos">
                    <LoansIcon />
                    Prestamos
                </Link>
                <Link href="/login">
                    <LogoutIcon />
                    Cerrar Sesion
                </Link>
            </div>
        </nav>
    )
}

export default Navbar