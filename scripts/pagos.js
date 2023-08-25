/*Share redes */
const share=document.querySelector(".share");
const toggle=document.querySelector(".toggle");
toggle.addEventListener("click",()=>{
  share.classList.toggle("active");
})

/*DESPLEGAR*/
function desplegarArticulos() {
    const comprobantesHistoria = document.getElementById("comprobantes");
    if (comprobantesHistoria.style.display === "none") {
      comprobantesHistoria.style.display = "grid";
    } else {
      comprobantesHistoria.style.display = "none";
    }
}