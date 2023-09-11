import { React, useState } from 'react'

import Modal from 'react-modal'

import './estilosMain/Cuenta.css'

import cuaderno from '../../assets/cuaderno.png'


const Pagos = () => {
    const [modalIsOpen, setModalIsOpen] = useState(false)

    const openModal = () => {
        setModalIsOpen(true)
    }

    const closeModal = () => {
        setModalIsOpen(false)
    }

    return(
        <div className='container'>
            <h1>PAGOS DE SERVICIOS</h1>
            <h3>PRÓXIMOS VENCIMIENTOS</h3>
            <div className='contenedor'>
                <div className='icono'>
                    <img src = {cuaderno} className='iconCuaderno' />
                </div>
                <div className='contain'>
                    <p><strong>¡Genial!</strong></p>
                    <p>NO TENÉS SERVICIOS POR VENCER</p>
                    <p className='link' onClick={openModal}>AÑADIR SERVICIOS</p>
                </div>
            </div>
            <Modal
                isOpen={modalIsOpen}
                onRequestClose={closeModal}
                contentLabel='Añadir Servicios'
                className='modal'
            >
                <h2>Añadir Servicios</h2>
                <form>
                    <label>Tipo de servicio: </label>
                    <input type="text" placeholder="Escribe el tipo de servicio" />

                    <label>Monto a Pagar en pesos:</label>
                    <input type="number" placeholder="Ingresa el monto a pagar" />

                    <label>Fecha de pago:</label>
                    <input type="date" />

                    <button type='submit'>Guardar</button>
                </form>
                <button onClick={closeModal} className='close-button'>Cerrar</button>
            </Modal>
        </div>
    )
}

export default Pagos