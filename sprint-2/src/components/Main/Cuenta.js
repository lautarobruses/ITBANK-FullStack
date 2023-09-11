import React, { useState } from 'react'

import UCA from '../../assets/UCA.png'
import USD from '../../assets/USD.png'

import './estilosMain/Cuenta.css'

const Cuenta = () => {
    const [pesos] = useState({
        monto:45246,
        numCuenta:23762668920802,
    })

    const [dolar] = useState({
        monto:727,
        numCuenta:55684497220905,
    })

    const [saldoVisible, setSaldoVisible] = useState(true)
    const toggleVisibilidadSaldo = () => {
        setSaldoVisible(!saldoVisible)
    }

    // const comprarDolares = () => {
    //     const valorDolar = 710
    //     const cantidadDolares = prompt('Ingrese la cantidad que desea comprar: ')
    //     const totalCompra = valorDolar * cantidadDolares
    //     if (pesos.monto >= totalCompra && cantidadDolares > 0){
    //         setPesos({ pesos, monto: pesos.monto - totalCompra })
    //         setDolar({ dolar, monto: dolar.monto + parseInt(cantidadDolares) })
    //     } else {
    //         alert('Saldo insuficiente para comprar dólares.')
    //     }
    // }
    // const venderDolares = () => {
    //     const valorDolar = 710
    //     const cantidadDolares = prompt('Ingrese la cantidad de dólares que desea vender: ')
    //     if(dolar.monto >= cantidadDolares && cantidadDolares > 0){
    //         const totalVenta = valorDolar * cantidadDolares
    //         setDolar({ dolar, monto: dolar.monto - parseInt(cantidadDolares) })
    //         setPesos({ pesos, monto: pesos.monto + totalVenta })
    //     } else {
    //         alert('Saldo insuficiente para vender dólares')
    //     }
    // }

    return (
        <div className='container'>
            <h1>Tus cuentas</h1>
            <div className='tarjetas'>
                <h3>Cuentas</h3>
                <div className='card'>
                    <h4 className='izquierda'>PRINCIPAL</h4>
                    <img src={UCA} alt='Caja de Ahorro' />
                    <h4 className='cardTitle'>Caja Ahorro Pesos</h4>
                    {saldoVisible ? (
                        <h2 className="monto">$ {pesos.monto}</h2>
                    ) : (
                        <h2 className='monto'>$ *****</h2>
                    )}
                    <button className='button' onClick={toggleVisibilidadSaldo}>
                        {saldoVisible ? 'Ocultar Saldo' : 'Mostrar Saldo' }
                    </button>
                    <p>N°{pesos.numCuenta}</p>
                </div>
                <div className='card'>
                    <img src={USD} alt='Caja de Ahorro en dólares' />
                    <h4 className="cardTitle">Caja Ahorro Dólares</h4>
                    {saldoVisible ? (
                        <h2 className="monto">U$D {dolar.monto}</h2>
                    ) : (
                        <h2 className="monto">U$D *****</h2>
                    )
                    }
                    <button className='button' onClick={toggleVisibilidadSaldo}>
                        {saldoVisible ? 'Ocultar Saldo' : 'Mostrar Saldo' }
                    </button>
                    <hr />
                    <p>N°{dolar.numCuenta}</p>
                    {/* <button className="button" onClick={comprarDolares}>Comprar</button>
                    <button className="button" onClick={venderDolares}>Vender</button> */}
                </div>
            </div>
        </div>
    )
}

export default Cuenta