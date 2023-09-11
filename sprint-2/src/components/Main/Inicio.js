import React, { useState } from 'react'

import styled from 'styled-components'

import Mastercard from '../../assets/Mastercard.png'

const StyledCuenta = styled.div`
    padding: 24px;
    display: flex;
    text-align: center;

    h2 {
        font-size: 14px;
        padding: 8px;
    }

    & > div {
        color: ${(props) => props.$fontColor};
        padding: 10px;
        width: 300px;
        margin: 16px;
        border-radius: 10px;
        flex-direction: row;
        border: 1px;
        display: flex;
        box-shadow: 0 0 10px rgba(0, 0, 0, 0.2);
        background-color: ${(props) => props.$bgColor || 'transparent'};
    }

    h3 {
        font-size: 12px;
        float: left;
    }

    button {
        float:left;
        margin-top: 50px;
        color: var(--dark);
        font-size: 9px;

        background-color: transparent;
        border: none;
        font-size: inherit;
        font-family: inherit;
        cursor: pointer;
    }

    img{
        width: 60px;
        height: 40px;
        float:left;
    }
`

function Cuenta({ text1, text2, mostrarImagen }) {
    const [mostrarMovimientos, setMostrarMovimientos] = useState(false)
    const [saldo, setSaldo] = useState(0) // Inicializa el saldo en 0

    function handleClick() {
        setMostrarMovimientos(!mostrarMovimientos)
        if (!mostrarMovimientos) {
            // Calcula el saldo actual sumando o restando los movimientos ficticios
            const nuevoSaldo = movimientosFicticios.reduce(
                (saldoAcumulado, movimiento) => saldoAcumulado + movimiento.cantidad,
                0
            )
            setSaldo(nuevoSaldo)
        }
    }

    return (
        <div>
            <div>
                {mostrarImagen && <img src={Mastercard} alt="logo" />}
                <h2>{text1}</h2>
                <h3>{text2}</h3>
                <div style={{ clear: 'both' }}></div>
                <h3 style={{ fontSize: '18px', marginTop: '10px', float: 'left' }}>
                    ${saldo.toFixed(2)}
                </h3>
                <button onClick={handleClick}>Ver Movimientos</button>
            </div>
            {mostrarMovimientos && (
                <div>
                    <h4>Movimientos:</h4>
                    <ul>
                        {movimientosFicticios.map((movimiento, index) => (
                            <li key={index} style={{ color: movimiento.cantidad > 0 ? 'green' : 'red' }}>
                                {movimiento.descripcion} ({movimiento.fecha}): ${movimiento.cantidad.toFixed(2)}
                            </li>
                        ))}
                    </ul>
                </div>
            )}
        </div>
    )
}

const movimientosFicticios = [
    { fecha: '2023-09-01', descripcion: 'Ingreso de salario', cantidad: 1500 },
    { fecha: '2023-09-05', descripcion: 'Compra en tienda', cantidad: -50 },
    { fecha: '2023-09-10', descripcion: 'Transferencia recibida', cantidad: 200 },
]

function Inicio() {
    return (
        <div>
            <StyledCuenta $bgColor='white' $fontColor='Black'>
                <Cuenta text1='Cuentas' text2='Saldos totales' saldo={999.99999950}  mostrarImagen={false} />
            </StyledCuenta>
            <StyledCuenta $bgColor='#DB3F3F' $fontColor='white'>
                <Cuenta text1='Terminada en 1234' text2='Cierra el 01/01/2024 Vence el 05/10/2034' saldo={9.99999950}  mostrarImagen={true} />
            </StyledCuenta>
            <StyledCuenta $bgColor='silver' $fontColor='white'>
                <Cuenta text1='Terminada en 1234' text2='Cierra el 01/01/2024 Vence el 05/10/2034' saldo={9.99999950}  mostrarImagen={true}/>
            </StyledCuenta>
            <StyledCuenta $bgColor='#FFD700' $fontColor='white'>
                <Cuenta text1='Terminada en 1234' text2='Cierra el 01/01/2024 Vence el 05/10/2034' saldo={9.99999950}  mostrarImagen={true}/>
            </StyledCuenta>
        </div>
    )
}

export default Inicio