from Jinja2 import Template

# Ejemplo de objetos de datos (puedes cambiar esto a tus datos)
data = [
    {"Nombre": "Juan", "Edad": 30, "Ciudad": "Madrid"},
    {"Nombre": "María", "Edad": 28, "Ciudad": "Barcelona"},
    {"Nombre": "Pedro", "Edad": 35, "Ciudad": "Sevilla"},
]

# Plantilla de HTML utilizando Jinja2
template_str = """
<table border="1">
    <tr>
        <th>Nombre</th>
        <th>Edad</th>
        <th>Ciudad</th>
    </tr>
    {% for item in data %}
    <tr>
        <td>{{ item.Nombre }}</td>
        <td>{{ item.Edad }}</td>
        <td>{{ item.Ciudad }}</td>
    </tr>
    {% endfor %}
</table>
"""

template = Template(template_str)

# Renderizar la plantilla con los datos
html_output = template.render(data=data)

# Imprimir o guardar el HTML
print(html_output)
