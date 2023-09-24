import React, { useState } from 'react'
import styles from'@/styles/Transferencia/Form.module.css'
import { ToastContainer, toast } from 'react-toastify'
import { generarId, formatearFecha } from '@/helpers'

function TransferForm() {
    const [addressee, setAdressee] = useState ('')
    const [motivo, setMotivo] = useState ('')
    const [amount, setAmount] = useState ([])
    const [transferencias, setTransferencias] = useState([])

    function exito(){
        toast.success('¡Transferencia Realizada con éxito!', {
            position: toast.POSITION.TOP_RIGHT
        })
    }
    function error(){
        toast.error("Ojo, campos vacíos o monto igual a $0", {
            position: toast.POSITION.TOP_RIGHT
        })
    }
    function handleSubmit(e){
        e.preventDefault();

        if([addressee, amount, motivo].includes("")){
            error()
            return
        }

        if(Number(amount)<=0){
            error()
            return
        }

        const objetoTransferencia={
            addressee,
            amount,
            fecha: formatearFecha(Date.now())
        }

        objetoTransferencia.id=generarId()
        setTransferencias([...transferencias, objetoTransferencia].reverse())
        exito()
        setAdressee("")
        setMotivo("")
        setAmount("")
    }


    return(
        <div>
            <ToastContainer />
            <div className={styles.transferForm}>
                <form onSubmit={handleSubmit}> 
                    <div>
                        <label className={styles.labelForm}>Enviar pago a: </label>
                        <input 
                            type='text'
                            value={addressee}
                            onChange={(e) => setAdressee(e.target.value)}
                            className={styles.formInput}
                            placeholder='Nombre, @nombreusuario o email'
                            required
                        />
                    </div>
                    <div>
                        <label className={styles.labelForm}>Motivo: </label>
                        <input 
                            type='text'
                            value={motivo}
                            onChange={(e) => setMotivo(e.target.value)}
                            className={styles.formInput}
                            placeholder='Motivo de la transacción'
                        />
                    </div>
                    <div>
                        <label className={styles.labelForm}>Monto de la transferencia: </label>
                        <input 
                            type='number'
                            value={amount}
                            onChange={(e) => setAmount(e.target.value)}
                            className={styles.formInput}
                            placeholder='Monto'
                            required
                        />
                    </div>
                    <button type='submit' className={styles.formButton}>Transferir</button>
                </form>
            </div>
        </div>
    )
}

export default TransferForm