const toggleButton = document.getElementById("button-menu")
const navWrapper = document.getElementById("nav")

toggleButton.addEventListener('click',() => {
  toggleButton.classList.toggle('close')
  navWrapper.classList.toggle('show')
})

navWrapper.addEventListener('click',e => {
  if(e.target.id === 'nav'){
    navWrapper.classList.remove('show')
    toggleButton.classList.remove('close')
  }
})

//Funciones utilizadas en index.html

function ocultarSaldo(){
  let showBalance = document.getElementById('show-balance-container');
  let hiddenBalance = document.getElementById('hidden-balance-container');
  let icon = document.getElementById('eye-buttom');

  showBalance.id = 'hidden-balance-container';
  hiddenBalance.id = 'show-balance-container';

  if(icon.className === 'show-eye-buttom'){
    icon.className = "hidden-eye-buttom";
  } else{
    icon.className = "show-eye-buttom";
  }
}

//Funciones utilizadas en login.html y register.html

function showPassword(inputID, iconID){
  let password = document.getElementById(inputID);
  let icon = document.getElementById(iconID);

  if(password.type === 'password'){
    password.type = 'text';
    icon.src = "/resources/img/icons/ojo.svg";
  } else{
    password.type = 'password';
    icon.src = "/resources/img/icons/ojo-tachado.svg";
  }
}

//Funciones utilizadas en Transfer.html

document.addEventListener('DOMContentLoaded', function () {

  const entradaCantidad = document.getElementById('cantidad');
  const selectMonedaOrigen = document.getElementById('monedaOrigen');
  const selectMonedaDestino = document.getElementById('monedaDestino');
  const botonConvertir = document.getElementById('botonConvertir');
  const elementoResultado = document.getElementById('resultado');
  
  for (let moneda in tasasDeCambio) {
    const opcionOrigen = document.createElement('option');
    opcionOrigen.value = moneda;
    opcionOrigen.text = moneda;
    selectMonedaOrigen.appendChild(opcionOrigen);
  
    const opcionDestino = document.createElement('option');
    opcionDestino.value = moneda;
    opcionDestino.text = moneda;
    selectMonedaDestino.appendChild(opcionDestino);
  }
  
  function convertirMoneda() {
    const cantidad = parseFloat(entradaCantidad.value);
    const monedaOrigen = selectMonedaOrigen.value;
    const monedaDestino = selectMonedaDestino.value;
  
    if (!isNaN(cantidad)) {
        const cantidadConvertida = (cantidad / tasasDeCambio[monedaOrigen]) * tasasDeCambio[monedaDestino];
        elementoResultado.textContent = `Resultado: ${cantidadConvertida.toFixed(2)} ${monedaDestino}`;
    } else {
        elementoResultado.textContent = 'Por favor, introduce una cantidad válida.';
    }
  }
  
  botonConvertir.addEventListener('click', convertirMoneda);

  // Nuevo código para el buscador de cuentas
  const botonBuscar = document.getElementById('botonBuscar');
  const listaCuentasAsociadas = document.getElementById('listaCuentasAsociadas');
  const cuentasAsociadas = ['Cuenta 1', 'Cuenta 2', 'Cuenta 3'];

  function actualizarListaCuentas(busqueda) {
      const cuentasFiltradas = cuentasAsociadas.filter(cuenta => cuenta.toLowerCase().includes(busqueda.toLowerCase()));
      listaCuentasAsociadas.innerHTML = cuentasFiltradas.map(cuenta => `<li>${cuenta}</li>`).join('');
  }

  botonBuscar.addEventListener('click', function () {
      const inputBuscar = document.getElementById('buscarCuenta').value;
      actualizarListaCuentas(inputBuscar);
  });

  actualizarListaCuentas('');
});

