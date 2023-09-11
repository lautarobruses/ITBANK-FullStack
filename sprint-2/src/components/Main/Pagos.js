import { React, useState } from 'react'
import './estilosMain/Cuenta.css'
import cuaderno from '../../assets/cuaderno.png'
import Modal from 'react-modal'

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
                    <div className='icono'>
                        <img src={cuaderno} className='iconCuaderno' alt='Cuaderno' />
                    </div>
                    <div className='contain'>
                        <p><strong>¡Genial!</strong></p>
                        <p>NO TENÉS SERVICIOS POR VENCER</p>
                        <p className='link' onClick={openModal}>AÑADIR SERVICIOS</p>
                    </div>
                </div>
            ) : (
                <div className='contenedor'>
                    <h3>Servicios A Pagar: </h3>
                    <ul>
                        {servicios.map((servicio, index) => (
                            <li key={index}>
                                {servicio.tipo}
                                {servicio.monto}
                                {servicio.fechaPago}
                            </li>
                        ))}
                    </ul>
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