import { useContext } from 'react'

import { NavbarContext } from '@/contexts/NavbarContext'

import styles from '@/styles/Header/ButtonMenu.module.css'

const ButtonMenu = () => {
    const { isOpen, actualizarEstado } = useContext(NavbarContext)

    const handleToggle = () => {
        actualizarEstado(!isOpen)
    }

    return (
        <button 
            className={`${styles.buttonMenu} ${isOpen ? styles.close : ''}`}
            onClick={handleToggle}
        >
            <span/>
            <span/>
            <span/>
        </button>
    )
}

export default ButtonMenu