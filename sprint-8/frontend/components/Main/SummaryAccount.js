import React from 'react'

import Image from 'next/image'

import styles from '@/styles/Main/SummaryAccount.module.css'

import mastercard from '@/public/images/mastercard.webp'
import visa from '@/public/images/visa.webp'

const accountFake = [ //Esto en un futuro va a estar en una base de datos
    { number: '23762668920802', title: 'Cuenta corriente', balance: 1600 },
    { number: '23762668214893', title: 'Caja de ahorro', coin: { USD: 'US$' }, balance: 12300 }
]

const image_1 = { src: mastercard, alt: 'logo de mastercard' }
const image_2 = { src: visa, alt: 'logo de visa' }

const cardFake = [
    { number: '49725637101234', title: 'Terminada en 1234', coin: { EUR: '€' }, tipe: 'card', closing: '00/00/00', expiration: '00/00/00', img: image_1, balance: 1500 },
    { number: '94852039834321', title: 'Terminada en 4321', tipe: 'card', closing: '00/00/00', expiration: '00/00/00', img: image_2, color: '#dc2328', balance: 0 },
    { number: '30583485762134', title: 'Terminada en 2134', tipe: 'card', closing: '00/00/00', expiration: '00/00/00', img: image_1, color: '#a3a4a8', balance: 2890 },
]

export default function SummaryAccount() {

    return (
        <div id={`${styles.accountsContainer}`}>
            <h1 id={`${styles.title}`}>Tus cuentas:</h1>
            <ul id={`${styles.list}`}>
                {accountFake.map((account) => (<li key={account.number} className={`${styles.elements}`}>
                    <span>{account.title}</span>
                    <span>{account.coin ? Object.values(account.coin) : '$'}{account.balance}</span>
                </li>
                ))}
                {cardFake.map((card) => (<li key={card.number} className={`${styles.elements}`}>
                                            <span style={{justifyContent: 'center', display: 'flex', gap: '5px'}}>
                                                <Image
                                                    width={25}
                                                    src={card.img.src}
                                                    alt={card.img.alt}
                                                    quality={60}
                                                    loading="lazy"
                                                />
                                                {card.title}
                                            </span>
                                            <span>{card.coin ? Object.values(card.coin) : '$'}{card.balance}</span>
                                        </li>
                ))}
            </ul>
        </div>
    )
}