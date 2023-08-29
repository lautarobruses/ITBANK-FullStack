const calcularButton = document.getElementById("calcular");

calcularButton.addEventListener("click", function () {
    const monto = parseFloat(document.getElementById("monto").value);
    const tasa = parseFloat(document.getElementById("tasa").value) / 100;
    const plazo = parseInt(document.getElementById("plazo").value);
    
    const mensual = (monto * tasa / 12) / (1 - Math.pow(1 + tasa / 12, -plazo));
    
    document.getElementById("resultado").innerHTML = `
        <p>Pago Mensual: $${mensual.toFixed(2)}</p>
    `;
    
    document.getElementById("resultado").style.display = "block";
});

