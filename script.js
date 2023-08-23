const toggleButton = document.getElementById("button-menu")
const navWrapper = document.getElementById("nav")

console.log(document);
console.log(toggleButton);
console.log(navWrapper);

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