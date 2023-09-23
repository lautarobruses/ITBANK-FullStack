import React from 'react'

const Calculadora = ({p,r,t,cuota}) => { 
      return (<div className='calculadora'>
                <h2>Resultado</h2> 
                <p>El valor de la cuota es: ${cuota(p,r,t).toFixed(2)}</p>     
            </div>) 
    }
export default Calculadora