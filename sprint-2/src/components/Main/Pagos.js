import { React, useState } from 'react'

import Modal from 'react-modal'

import './estilosMain/Cuenta.css'

const Pagos = () => {
    const [modalIsOpen, setModalIsOpen] = useState(false)
    const [servicios, setServicios] = useState([])
    const [tipoServicio, setTipoServicio] = useState('')
    const [monto, setMonto] = useState('')
    const [fechaPago, setFechaPago] = useState('')

    const openModal = () => {
        setModalIsOpen(true)
    }

    const closeModal = () => {
        setModalIsOpen(false)
    }

    const handleSubmit = (e) => {
        e.preventDefault()
        const nuevoServicio = {
            tipo: tipoServicio,
            monto: monto,
            fechaPago: fechaPago,
        }
        setServicios([ servicios, nuevoServicio])
        setTipoServicio('')
        setMonto('')
        setFechaPago('')
    }

    return(
        <div className='container'>
            <h1>PAGOS DE SERVICIOS</h1>
            <h3>PRÓXIMOS VENCIMIENTOS</h3>
            {servicios.length === 0 ? ( // Verifica si hay servicios en la lista
                <div className='contenedor'>
                    <svg className='cuaderno' stroke="currentColor" fill="currentColor" strokeWidth="0" viewBox="0 0 16 16" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path fillRule="evenodd" d="M6 1h6v7a.5.5 0 0 1-.757.429L9 7.083 6.757 8.43A.5.5 0 0 1 6 8V1z"></path><path d="M3 0h10a2 2 0 0 1 2 2v12a2 2 0 0 1-2 2H3a2 2 0 0 1-2-2v-1h1v1a1 1 0 0 0 1 1h10a1 1 0 0 0 1-1V2a1 1 0 0 0-1-1H3a1 1 0 0 0-1 1v1H1V2a2 2 0 0 1 2-2z"></path><path d="M1 5v-.5a.5.5 0 0 1 1 0V5h.5a.5.5 0 0 1 0 1h-2a.5.5 0 0 1 0-1H1zm0 3v-.5a.5.5 0 0 1 1 0V8h.5a.5.5 0 0 1 0 1h-2a.5.5 0 0 1 0-1H1zm0 3v-.5a.5.5 0 0 1 1 0v.5h.5a.5.5 0 0 1 0 1h-2a.5.5 0 0 1 0-1H1z"></path></svg>
                    <p><strong>¡Genial!</strong></p>
                    <p>NO TENÉS SERVICIOS POR VENCER</p>
                    <p className='link' onClick={openModal}>AÑADIR SERVICIOS</p>
                </div>
            ) : (
                <div className='contenedor'>
                    <h3>Servicios A Pagar: </h3>
                    <table className='servicios-table'>
                        <thead>
                            <tr>
                                <th>Tipo de Servicio</th>
                                <th>Monto a Pagar</th>
                                <th>Fecha de Pago</th>
                            </tr>
                        </thead>
                        <tbody>
                            {servicios.map((servicio, index) => (
                                <tr key={index}>
                                    <td>{servicio.tipo}</td>
                                    <td>${servicio.monto}</td>
                                    <td>{servicio.fechaPago}</td>
                                </tr>
                            ))}
                        </tbody>
                    </table>
                    <p className='link' onClick={openModal}>AÑADIR SERVICIOS</p>
                </div>
            )}
            <Modal
                isOpen={modalIsOpen}
                onRequestClose={closeModal}
                contentLabel='Añadir Servicios'
                className='modal'
            >
                <h2>Añadir Servicios</h2>
                <form onSubmit={handleSubmit}>
                    <label>Tipo de servicio: </label>
                    <input
                        type="text"
                        placeholder="Escribe el tipo de servicio"
                        value={tipoServicio}
                        onChange={(e) => setTipoServicio(e.target.value)}
                        required
                    />

                    <label>Monto a Pagar en pesos: </label>
                    <input
                        type="number"
                        placeholder="Ingresa el monto a pagar"
                        value={monto}
                        onChange={(e) => setMonto(e.target.value)}
                        required
                    />

                    <label>Fecha de pago:</label>
                    <input
                        type="date"
                        value={fechaPago}
                        onChange={(e) => setFechaPago(e.target.value)}
                        required
                    />

                    <button type='submit'>Guardar</button>
                </form>
                <button onClick={closeModal} className='close-button'>Cerrar</button>
            </Modal>
        </div>
    )
}

export default Pagos