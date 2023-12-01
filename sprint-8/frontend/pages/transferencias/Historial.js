import React, { useContext, useEffect } from 'react'

import EncTabla from '@/components/Transferencia/EncTabla'
import Tabla from '@/components/Transferencia/Tabla'
import Layout from '@/components/layout'

import { FormContext } from '@/contexts/TransferContext'

const TransactionHistory =  ({ transferencias}) => {
    const [formulario, setFormulario] = useContext(FormContext)

    useEffect(() => {
        
    }, [formulario])

    return(
        <Layout>
            <div>
            <h2>{transferencias && transferencias.lenght>0 ? 'Transferencias Realizadas' : 'No hay transferencias'}</h2>
            <div>
                <table>
                    <EncTabla />
                    {transferencias && Array.isArray(transferencias) && transferencias.map((datos) => (
                        <Tabla 
                            key={datos.id}
                            datos={datos}
                        />
                    ))}
                </table>
            </div>
        </div>
        </Layout>
    )
}

export default TransactionHistory