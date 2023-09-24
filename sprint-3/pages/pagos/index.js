import Head from 'next/head'

import { React, useState } from 'react'

import Modal from 'react-modal'

import Layout from '@/components/layout'

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

    return (
        <>
            <Head>
                <title>Nexus Bank - Pagos</title>
                <meta name="description" content="Permite pagar diferentes servicios" />
                <link rel='icon' href='/favicon.ico' />

                {/* Etiqueta meta para especificar el juego de caracteres */}
                <meta charSet="UTF-8" /> 

                {/* Etiqueta meta para controlar la vista móvil */}
                <meta name="viewport" content="width=device-width, initial-scale=1.0" /> 
                
                {/* Etiqueta meta para el autor */}
                <meta name="author" content="Grupo 3" />
                
                {/* Etiqueta meta para palabras clave (keywords) */}
                <meta name="keywords" content="Nexus Bank, Homebanking, Banca en línea, Préstamos personales, Pagos en línea, Transferencias seguras, Tarjetas de crédito" />
                
                {/* Etiqueta meta para el idioma de la página */}
                <meta http-equiv="Content-Language" content="es" />
                
                {/* Etiqueta meta para el robot de rastreo (crawlers) */}
                <meta name="robots" content="index, follow" /> {/*index | follow | noindex | nofollow*/}

                {/* Etiqueta meta para la traduccion de google*/}
                <meta name="google" content="notranslate" key="notranslate" />
            </Head>
            <Layout>
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
                        <h2 className='add-servicios'>Añadir Servicios</h2>
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
            </Layout>
        </>
    )
}

export default Pagos