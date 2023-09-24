import React, {useState} from 'react'
import Calculadora from './calculadora'

export default function Formulario(){
    const [Monto, setMonto] = useState (0)
    const [Interes, setInteres] = useState (0)
    const [Plazo, setPlazo] = useState (0)
    const [resultado, setResultado] = useState (null)
    const cuota = (p, r, t) => { return p * (1 + (r/100) * t) / t }
    return(
        <form>
            {<input
                type='number'
                name='monto'
                placeholder='Monto'
                value={Monto}
                onChange={(e) => setMonto(e.target.value)}
            />}
            {<input
                type='number'
                name='interes'
                placeholder='interés en %'
                value={Interes}
                onChange={(e) => setInteres(e.target.value)}
            />}
            {<input
                type='number'
                name='Plazo'
                placeholder='Plazo en Meses'
                value={Plazo}
                onChange={(e) => setPlazo(e.target.value)}
            />}
            {<button type='submit'
                onClick={(e) => {e.preventDefault()
                Resultado(<Calculadora p={Number(Monto)} r={Numberse(Interes)} t={Number(Plazo)}/>)}}>
                Calcular
            </button>}
        </form>
    )

}
