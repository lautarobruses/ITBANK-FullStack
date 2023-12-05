import styles from '@/styles/Account/Card.module.css'

import React, { useState } from 'react'

import Image from 'next/image'

const Card = ({ tipe='account',
                title='Cuenta',
                coin=1,
                balance='0',
                closing='',
                expiration='',
                img='',
                color='var(--dark)'
}) => {
    const [mostrarMovimientos, setMostrarMovimientos] = useState(false)
    const [saldo, setSaldo] = useState(balance)

    function handleClick() {
        setMostrarMovimientos(!mostrarMovimientos)
    }

    return (
        <div id={`${styles.card}`} style={{backgroundColor: tipe==='card' ? color : 'var(--white)', color: tipe==='card'? 'white' : 'black'}} >
            <div id={`${styles.content}`}>
                <div id={`${styles.headerCard}`} style={{borderColor: tipe==='card'? '#d2d2d2' : 'var(--grey-font)'}}>
                    {tipe==='card' && (
                        <Image 
                            width={40} 
                            src={img.src} 
                            alt={img.alt}
                            quality={60}
                            loading="lazy"
                        />
                    )}
                    <h3 id={`${styles.cardTitle}`}>{tipe === 'card'? "Terminada en " + title: title}</h3>
                </div>

                <h4 id={`${styles.cardSubtitle}`} style={{color: tipe==='card'? '#f0f0f0' : 'var(--grey-font)'}}>
                    {tipe==='card' ? (
                        'Cierra el ' + closing + ' - Vence el ' + expiration
                    ) : (
                        'Saldo total'
                    )}
                </h4>
                <h3 id={`${styles.saldo}`}>
                    {tipe!=='card' ? 
                        coin == 0? "$" : "U$S"
                    : "" }
                    {saldo}
                </h3>
                {/* <button id={`${styles.button}`} style={{color: tipe==='card'? 'var(--white)' : 'var(--dark)'}} onClick={handleClick}>Ver movimientos</button> */}
            </div>
            {/* {mostrarMovimientos && (
                <div>
                    <ul id={`${styles.motionContainer}`} style={{borderColor: tipe==='card'? '#d2d2d2' : 'var(--grey-font)'}}>
                        {movimientosFicticios.map((movimiento) => (
                            <li key={movimientosFicticios.id} className={`${styles.motion}`} >
                                {movimiento.descripcion} ({movimiento.fecha}):
                                <span style={{ color: movimiento.cantidad > 0 ? 'green' : 'red' }}>
                                    {movimiento.cantidad > 0 ? ' ':' -'}
                                    ${Math.abs(movimiento.cantidad.toFixed(2))} 
                                </span>
                            </li>
                        ))}
                    </ul>
                </div>
            )} */}
        </div>
    )
}

export default Card