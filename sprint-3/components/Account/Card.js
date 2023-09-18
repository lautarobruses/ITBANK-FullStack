import React, { useState } from 'react'

import styles from '@/styles/Account/Card.module.css'

import Image from 'next/image'

const movimientosFicticios = [
    { fecha: '2023-09-01', descripcion: 'Ingreso de salario', cantidad: 1500 },
    { fecha: '2023-09-05', descripcion: 'Compra en tienda', cantidad: -50 },
    { fecha: '2023-09-10', descripcion: 'Transferencia recibida', cantidad: 200 },
]

export default function Card({ tipe='account', title='Cuenta', coin='$', closing='', expiration='', img='', color='var(--dark)' }) {
    const [mostrarMovimientos, setMostrarMovimientos] = useState(false)
    const [saldo, setSaldo] = useState(0) // Inicializa el saldo en 0

    function handleClick() {
        setMostrarMovimientos(!mostrarMovimientos)
        if (!mostrarMovimientos) {
            // Calcula el saldo actual sumando o restando los movimientos ficticios
            const nuevoSaldo = movimientosFicticios.reduce(
                (saldoAcumulado, movimiento) => saldoAcumulado + movimiento.cantidad, 0
            )
            setSaldo(nuevoSaldo)
        }
    }

    return (
        <div id={`${styles.card}`} style={{backgroundColor: tipe==='card'? color : 'var(--white)', color: tipe==='card'? 'white' : 'black'}} >
            <div id={`${styles.content}`}>
                <div id={`${styles.headerCard}`} style={{borderColor: tipe==='card'? '#d2d2d2' : 'var(--grey-font)'}}>
                    {tipe==='card' && (
                        <Image width='40' src={img} alt="logo de mastercard" />
                    )}
                    <h3 id={`${styles.cardTitle}`}>{title}</h3>
                </div>

                <h4 id={`${styles.cardSubtitle}`} style={{color: tipe==='card'? '#f0f0f0' : 'var(--grey-font)'}}>
                    {tipe==='card' ? (
                        'Cierra el ' + closing + ' - Vence el' + expiration
                    ) : (
                        'Saldo total'
                    )}
                </h4>
                <h3 id={`${styles.saldo}`}>
                    {coin} {saldo.toFixed(2)}
                </h3>
                <button id={`${styles.button}`} style={{color: tipe==='card'? 'var(--white)' : 'var(--dark)'}} onClick={handleClick}>Ver movimientos</button>
            </div>
            {mostrarMovimientos && (
                <div>
                    <ul id={`${styles.motionContainer}`} style={{borderColor: tipe==='card'? '#d2d2d2' : 'var(--grey-font)'}}>
                        {movimientosFicticios.map((movimiento, index) => (
                            <li className={`${styles.motion}`} key={index} >
                                {movimiento.descripcion} ({movimiento.fecha}):
                                <span style={{ color: movimiento.cantidad > 0 ? 'green' : 'red' }}>
                                    {movimiento.cantidad > 0 ? ' ':' -'}
                                    ${Math.abs(movimiento.cantidad.toFixed(2))} 
                                </span>
                            </li>
                        ))}
                    </ul>
                </div>
            )}
        </div>
    )
}