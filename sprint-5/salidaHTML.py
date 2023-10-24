from jinja2 import Template
import webbrowser
from transaccion import Transaccion

# Plantilla de HTML utilizando Jinja2
template_str = """
<table border="1">
    <tr>
        <th>Numero</th>
        <th>Estado</th>
        <th>tipo</th>
        <th>cuentaNumero</th>
        <th>permitidoActualParaTransccion</th>
        <th>monto</th>
        <th>fecha</th>
        <th>razon</th>
    </tr>
    {% for transaccion in data %}
    <tr>
        <td>{{ transaccion.numero }}</td>
        <td>{{ transaccion.estado }}</td>
        <td>{{ transaccion.tipo }}</td>
        <td>{{ transaccion.cuentaNumero }}</td>
        <td>{{ transaccion.permitidoActualParaTransccion }}</td>
        <td>{{ transaccion.monto }}</td>
        <td>{{ transaccion.fecha }}</td>
        <td>{{ transaccion.razon }}</td>
    </tr>
    {% endfor %}
</table>
"""

template = Template(template_str)

def crearHTML(transacciones: list[Transaccion]):
    # Renderizar la plantilla con los datos
    html_output = template.render(data = transacciones)

    with open('archivo_generado.html', 'w') as file:
        file.write(html_output)

    webbrowser.open('archivo_generado.html')

#borrar lo siguiente xdd
crearHTML([{
            "estado": "ACEPTADA",
            "tipo": "RETIRO_EFECTIVO_CAJERO_AUTOMATICO",
            "cuentaNumero": 190,
            "permitidoActualParaTransccion": 9000,
            "monto": 1000,
            "fecha": "10/10/2022 16: 00: 55",
            "numero": 1
        },
        {
            "estado": "RECHAZADA",
            "tipo": "COMPRA_EN_CUOTAS_TARJETA_VISA",
            "permitidoActualParaTransccion": 9000,
            "monto": 750000,
            "fecha": "10/10/2022 16: 14: 35",
            "numero": 2
        }])