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


