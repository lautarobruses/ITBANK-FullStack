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
    comprobanteDiv.style.display = "block";
}

botonServicio.addEventListener("click", function() {
    if (comprobanteDiv.style.display === "block") {
        comprobanteDiv.style.display = "none";
        localStorage.setItem("comprobanteVisible", "false");
    } else {
        comprobanteDiv.style.display = "block";
        localStorage.setItem("comprobanteVisible", "true");
    }
});