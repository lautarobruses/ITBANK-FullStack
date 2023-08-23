/*Share redes */
const share=document.querySelector(".share");
const toggle=document.querySelector(".toggle");
toggle.addEventListener("click",()=>{
  share.classList.toggle("active");
})
/*DESPLEGAR*/

const botonServicio = document.getElementById("servicio");
const comprobanteDiv = document.getElementById("comprobantes");

const estadoGuardado = localStorage.getItem("comprobanteVisible");
if (estadoGuardado === "true") {
    comprobanteDiv.style.maxHeight = "500px"; 
} else {
    comprobanteDiv.style.maxHeight = "0"; 
}

botonServicio.addEventListener("click", function() {
    if (comprobanteDiv.style.maxHeight === "0px") {
        comprobanteDiv.style.maxHeight = "500px"; 
        localStorage.setItem("comprobanteVisible", "true");
    } else {
        comprobanteDiv.style.maxHeight = "0"; 
        localStorage.setItem("comprobanteVisible", "false");
    }
});