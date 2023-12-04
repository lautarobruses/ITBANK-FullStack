import React from 'react'

import Image from 'next/image'

import styles from '@/styles/Main/SummaryAccount.module.css'

const SummaryAccount = ({ nombreCompleto, cuentas, tarjetas }) => {
    return (
        <div className={styles.container}>
            <div className={styles.accountsContainer}>
                <h1 className={styles.tituloPrincipal}>Bienvenido {nombreCompleto}!</h1>
            </div>

            <div className={styles.accountsContainer}>
                <h2 className={styles.tituloSecundario}>Tus cuentas:</h2>
                <ul className={styles.list}>
                    {cuentas?.map((cuenta) => (
                        <li key={cuenta.account_id} className={styles.elements}>
                            <span>{cuenta.title}</span>
                            <span>{cuenta.tipo_moneda === 0 ? `ARS$${cuenta.balance}` : `USD$${cuenta.balance}`}</span>
                        </li>
                    ))}
                </ul>
            </div>

            <div className={styles.accountsContainer}>
                <h2 className={styles.tituloSecundario}>Tus tarjetas:</h2>
                <ul className={styles.list}>
                    {tarjetas.map((tarjeta) => (
                        <li key={tarjeta.tarjeta_numero} className={styles.elements}>
                            <span style={{ justifyContent: 'center', display: 'flex', gap: '5px' }}>
                                {tarjeta.marca_tarjeta === 1 && <Image width="25" height="25" src="/images/visa.webp" alt="logo visa" />}
                                {tarjeta.marca_tarjeta === 2 && <Image width="25" height="25" src="/images/mastercard.webp" alt="logo mastercard" />}
                                {tarjeta.marca_tarjeta !== 1 && tarjeta.marca_tarjeta !== 2 && <Image width="25" height="25" src="/images/american_express.webp" alt="logo american express" />}
                            </span>
                            <span>Tarjeta numero: {tarjeta.tarjeta_numero}</span>
                            <span>Vencimiento: {tarjeta.tarjeta_fecha_expiracion}</span>
                        </li>
                    ))}
                </ul>
            </div>
        </div>
    );
};

export default SummaryAccount;
