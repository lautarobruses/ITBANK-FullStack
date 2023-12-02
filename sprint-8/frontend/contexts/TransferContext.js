import React, { useState } from 'react'
import { createContext } from 'react'

export const FormContext = createContext()

const FormProvider = ({ children }) => {
    const [formulario, setFormulario] = useState({
        addressee:'',
        motivo: '',
        amount: 0,
    })

    console.log('Formulario en Formprovider: ', formulario)

    return (
        <FormContext.Provider value={{formulario, setFormulario}}>
            {children}
        </FormContext.Provider>
    )
}

export default FormProvider
