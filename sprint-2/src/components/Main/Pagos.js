import React from 'react'
import './estilosMain/Cuenta.css'
import cuaderno from '../../assets/cuaderno.png'

const Pagos = () => {

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
                    <p className='link'>AÑADIR SERVICIOS</p>
                </div>
            </div>
        </div>
    )
}

export default Pagos