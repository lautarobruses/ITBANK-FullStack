import React from 'react'
import UCA from '../../assets/UCA.png'
import USD from '../../assets/USD.png'
import './estilosMain/Cuenta.css'

const Cuenta = () => {
    return (
        <div className='container'>
            <h1>Tus cuentas</h1>
            <h3 className='transparente'>Cuentas</h3>
            <div className='tarjetas'>
                <div className='parte1'>
                    <div className='card'>
                        <h6 className='izquierda'>PRINCIPAL</h6>
                        <img src={UCA} alt='Caja de Ahorro' />
                        <h4 className='cardTitle'>Caja Ahorro Pesos</h4>
                        <h2 className="monto">$45.244,20</h2>
                        <p className='numCuenta'>N° 237626689-2 080-1</p>
                    </div>
                    <div className='card'>
                        <br />
                        <img src={USD} alt='Caja de Ahorro en dólares' />
                        <h4 className="cardTitle">Caja Ahorro Dólares</h4>
                        <h2 className="monto">U$D 726,00</h2>
                        <p className="numCuenta">N° 556844972-2 090-5</p>
                        <button className="button">Comprar</button>
                        <button className="button">Vender</button>
                    </div>
                </div>
                <h3 className="subtitle">Cheques</h3>
                <div className="tarjetas">
                    <div className='parte1'>
                        <div className="card">
                            <h4>Cheques electrónicos</h4>
                        </div>
                        <div className="card">
                            <h4>Cheques físicos</h4>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    )

}

export default Cuenta