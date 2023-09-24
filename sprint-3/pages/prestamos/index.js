import React, {useState} from 'react'
import Calculadora from './calculadora'
import Layout from '@/components/layout'
import styles from '@/styles/prestamos/pres.module.css'
import pres1 from '@/public/Images/pres1.jpg'



export default function Formulario() {
    const [Monto, setMonto] = useState(0);
    const [Interes, setInteres] = useState(0);
    const [Plazo, setPlazo] = useState(0);
  
    return (
      <Layout>
        <div className={`${styles.formContainer}`}>
            <div className={`${styles.formText}`}>
                <h1>Calculadora de Préstamos</h1>
                <p>Bienvenido a nuestra calculadora de préstamos, donde puedes calcular cuánto podrías pedir prestado y estimar tus pagos mensuales. Ingresa la información requerida a continuación para obtener una estimación.</p>
            </div>
        <div className={`${styles.calculatorContainer}`}>
        <form>
        <label htmlFor='monto'>Monto del préstamo:</label>
        <input
            type='number'
            name='monto'
            placeholder='Ingrese el monto'
            value={Monto}
            onChange={(e) => setMonto(e.target.value)}
        />

        <label htmlFor='interes'>Tasa de interés:</label>
        <input
            type='number'
            name='interes'
            placeholder='Ingrese la tasa de interés en %'
            value={Interes}
            onChange={(e) => setInteres(e.target.value)}
        />

        <label htmlFor='plazo'>Plazo anual:</label>
        <input
            type='number'
            name='plazo'
            placeholder='Ingrese el plazo en años'
            value={Plazo}
            onChange={(e) => setPlazo(e.target.value)}
        />
        </form>

        <h2>Resultados</h2>
        <p>Basado en la información proporcionada, aquí tienes una estimación de tus pagos:</p>
        <Calculadora p={Number(Monto)} r={Number(Interes)} t={Number(Plazo)} />
        </div>
        </div>
        <div className={styles.imagesContainer}>
            <img
                src={pres1}
                alt='Solicite su préstamo en nuestro banco'
            />
            <img
                src='imagen2.jpg'
                alt='Promociones especiales en préstamos'
            />
            <img
                src='imagen3.jpg'
                alt='Calculadora de préstamos en línea'
            />
        </div>
      </Layout>
    );
  }
