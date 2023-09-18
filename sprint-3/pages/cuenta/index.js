import React, { useState } from 'react'

import styles from '@/styles/Account/Index.module.css'

import Head from 'next/head'

import Card from '@/components/Account/Card'

import mastercard from '../../public/Images/mastercard.png'
import visa from '../../public/Images/visa.png'
import Layout from '@/components/layout'

export default function Document() {

    return (
        <Layout>
            <Head>
                <title>Tus cuentas - NexusBank</title>
            </Head>
            <div id={`${styles.div}`}>
                <h1 id={`${styles.title}`}>Tus cuentas</h1>

                <h2 className={`${styles.subtitle}`}>Cuentas</h2>
                <section className={`${styles.section}`}>
                    <Card title='Cuenta corriente' number='23762668920802'></Card>
                    <Card title='Cuenta de ahorro' number='23762668920802' coin='US$'></Card>
                </section>

                <h2 className={`${styles.subtitle}`}>Tarjetas</h2>
                <section className={`${styles.section}`}>
                    <Card tipe='card' finished='2312' closing='00/00/00' expiration='00/00/00' img={mastercard}></Card>
                    <Card tipe='card' finished='1234' closing='00/00/00' expiration='00/00/00' img={visa} color='#dc2328'> </Card>
                    <Card tipe='card' finished='4321' closing='00/00/00' expiration='00/00/00' img={mastercard} color='#a3a4a8'></Card>
                </section>
            </div>
        </Layout>
    )
}