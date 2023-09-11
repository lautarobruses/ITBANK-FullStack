import React, { useState } from 'react'
import { createContext } from 'react'

export const NavbarContext = createContext()

const NavbarContextProvider = ({ children }) => {
    const [isOpen, setisOpen] = useState(false)

    const actualizarEstado = () => {
        console.log(isOpen)
        setisOpen(!isOpen)
    }

    return (
        <NavbarContext.Provider value={{ isOpen, actualizarEstado }}>
            {children}
        </NavbarContext.Provider>
    )
}

export default NavbarContextProvider