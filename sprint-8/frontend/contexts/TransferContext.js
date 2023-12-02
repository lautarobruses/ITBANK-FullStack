import React, { useState } from 'react'
import { createContext } from 'react'

export const FormContext = createContext()

const FormProvider = ({ children }) => {
    const [formulario, setFormulario] = useState([])

    const actualizarEstado = (newForm) => {
        setFormulario(newForm)
    }

    console.log('Formulario en Formprovider: ', formulario)

    return (
        <FormContext.Provider value={{formulario, actualizarEstado}}>
            {children}
        </FormContext.Provider>
    )
}

export default FormProvider
