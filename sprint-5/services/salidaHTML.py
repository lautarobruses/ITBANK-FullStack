from jinja2 import Template
from transaccion.transaccion import Transaccion

# Plantilla de HTML utilizando Jinja2
TEMPLATE_STR = """
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

template = Template(TEMPLATE_STR)

def crearHTML(transacciones: list[Transaccion]):
    # Renderizar la plantilla con los datos
    html_output = template.render(data=transacciones)

    return html_output
