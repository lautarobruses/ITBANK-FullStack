import React, { useState, useEffect } from 'react'

import { useDispatch, useSelector } from 'react-redux'

import styles from '@/styles/Account/Index.module.css'

import { initializeCuentas } from '@/store/reducers/cuentasReducer'
import { initializeTarjetas } from '@/store/reducers/tarjetasReducer'

import Head from 'next/head'

import Layout from '@/components/layout'
import Card from '@/components/Cuenta/Card'

import Arrows from '@/public/svg/circularArrows.svg'
import mastercard from '@/public/Images/mastercard.webp'
import visa from '@/public/Images/visa.webp'
import american from '@/public/Images/american_express.webp'

const image_1 = { src: visa, alt: 'logo de visa' }
const image_2 = { src: mastercard, alt: 'logo de mastercard' }
const image_3 = { src: american, alt: 'logo de american' }

const Cuenta = () => {
    const dispatch = useDispatch()
    const cuentas = useSelector((state) => state.cuentas)
    const tarjetas = useSelector((state) => state.tarjetas)
  
    const userInfo = useSelector((state) => state.user)

    const [rates, setRates] = useState(null)
    const [input, setInput] = useState('')
    const [result, setResult] = useState('')
    const [coinInput, setCoinInput] = useState('ARG')
    const [coinResult, setCoinResult] = useState('USD')

    useEffect(() => {
        fetch('https://api.exchangerate.host/latest')
            .then(response => response.json())
            .then(data => {
                console.log(data)
                setRates({
                    base: data.base, rates: {
                        USD: data.rates.USD,
                        EUR: data.rates.EUR,
                        ARG: data.rates.ARS
                    },
                }) //aqui se pueden agregar mas monedas
            }, 10)
            .catch(error => {
                console.error('Error: ', error)
            })
    }, [])

    useEffect(() => {
        if (rates !== null && input > 0) {
            setResult((input / rates.rates[coinInput] * rates.rates[coinResult]).toFixed(2))
        }
    }, [input, coinInput, coinResult, rates])

    //Cuentas
    useEffect(() => {
        if (userInfo) {
            dispatch(initializeCuentas(userInfo.customer_id))
        }
    }, [dispatch, userInfo])

    //tarjetas
    useEffect(() => {
        if (userInfo) {
            dispatch(initializeTarjetas(userInfo.customer_id))
        }
    }, [dispatch, userInfo])

    const selectAccount = async (event) => {
        event.preventDefault()

        var idOption = event.target.value
        var input = document.getElementById('amount')
        var coinSelector = document.getElementById('coin-amount-selector')

        if (idOption !== 'otro') {
            var account = accountFake.find(account => account.number === idOption)

            if (account === undefined) {
                account = cardFake.find(card => card.number === idOption)
            }

            setInput(account.balance.toFixed(2))

            if (account.tipo_moneda === 0) {
                setCoinInput('ARG')
            } else if (account.tipo_moneda === 1) {
                setCoinInput('USD')
            } else {
                setCoinInput('EUR')
            }

            if (input.disabled === false) {
                input.disabled = true
                coinSelector.disabled = true
            }

        } else {
            if (input.disabled === true) {
                input.disabled = false
                coinSelector.disabled = false
            }
        }
    }

    return (
        <>
            <Head>
                <title>Nexus Bank - Cuenta</title>
                <meta name="description" content="Accede y administra tus cuentas y tarjetas bancarias en un solo lugar. Controla tus finanzas de manera sencilla y segura." />
                <link rel="icon" href="favicon.ico" type="image/x-icon"/>

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
                <div id={`${styles.div}`}>
                    <h1 id={`${styles.title}`}>Tus cuentas</h1>

                    <h2 className={`${styles.subtitle}`}>Cuentas</h2>
                    <section className={`${styles.section}`}>
                        {cuentas.map((account) => (<Card key={account.account_id} title={account.title} number={account.account_id} coin={account.tipo_moneda} balance={account.balance} />))}
                    </section>

                    <h2 className={`${styles.subtitle}`}>Tarjetas</h2>
                    <section className={`${styles.section}`}>
                        {tarjetas.map((card) => (<Card tipe="card" title={card.tarjeta_numero} closing={card.tarjeta_fecha_otorgamiento} expiration={card.tarjeta_fecha_expiracion} img={card.marca_tarjeta === 1? image_1 : card.marca_tarjeta=== 2? image_2 : image_3} color={card.color} balance={card.tarjeta_nombre_propietario} ></Card>))}
                    </section>

                    <div id={`${styles.converter}`}>
                        <h2 className={`${styles.subtitle}`} style={{ color: 'var(--black)' }} >Transforma tu dinero:</h2>

                        <div id={`${styles.converterOptions}`}>
                            <label id={`${styles.labelSelect}`}>Selecciona tu cuenta:</label>
                            <select id={`${styles.selectboxAccount}`} className={`${styles.selectbox}`} name='your-account' onChange={(event) => { selectAccount(event) }}>
                                <option value="" style={{ display: 'none' }}>Selecciona una cuenta</option>
                                {cuentas.map((account) => (<option value={account.number} disabled={account.balance > 0 ? false : true} key={account.number}>{account.title}</option>))}
                                {tarjetas.map((card) => (<option value={card.number} disabled={card.balance > 0 ? false : true} key={card.number}>{card.title}</option>))}
                                <option value="otro">Otro...</option>
                            </select>

                            <label className={`${styles.label}`}>De</label>
                            <div>
                                <input className={`${styles.selectbox}`} style={{ width: '71.7%' }} type='number' id='amount' name='amount' value={input} onChange={({ target }) => setInput(target.value)} />

                                <select className={`${styles.selectbox} ${styles.selectCoin}`} id='coin-amount-selector' value={coinInput} onChange={({ target }) => setCoinInput(target.value)} >
                                    {rates !== null && Object.keys(rates.rates).map(key => (
                                        <option value={key} key={key}>{key}</option>
                                    ))}
                                </select>
                            </div>

                            <div></div>
                            <Arrows id={`${styles.iconArrows}`} />

                            <label className={`${styles.label}`}>a</label>
                            <div>
                                <input className={`${styles.selectbox}`} style={{ width: '71.7%' }} type='number' name='result' disabled value={result} />

                                <select className={`${styles.selectbox} ${styles.selectCoin}`} id='coin-result-selector' value={coinResult} onChange={({ target }) => setCoinResult(target.value)} >
                                    {rates !== null && Object.keys(rates.rates).map(key => (
                                        <option value={key} key={key}>{key}</option>
                                    ))}
                                </select>
                            </div>
                        </div>
                    </div>
                </div>
            </Layout>
        </>
    )
}

export default Cuenta