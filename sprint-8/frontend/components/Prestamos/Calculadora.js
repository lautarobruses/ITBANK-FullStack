import React, { useState } from 'react';

const Calculadora = ({ p, r, t }) => {
  const [resultado, setResultado] = useState(null);

  const cuota = (p, r, t) => {
    return p * (r / 100) * t;
  };

  const calcularCuota = () => {
    const resultadoCalculado = cuota(p, r, t).toFixed(2);
    setResultado(resultadoCalculado);
  };

  const cerrarModal = () => {
    setResultado(null);
  };

  return (
    <div className='calculadora'>
      <h2>Resultado</h2>
      <button onClick={calcularCuota}>Calcular</button>

      {resultado !== null && (
        <div className='modal'>
          <div className='modal-contenido'>
            <p>El valor de la cuota es: ${resultado}</p>
            <button onClick={cerrarModal}>Cerrar</button>
          </div>
        </div>
      )}
    </div>
  );
};

export default Calculadora;
