from package import cliente as c, tarjeta as t
import json


# Abre el archivo JSON en modo lectura
with open('reporte.json', 'r') as archivo:
    datos = json.load(archivo)

    if datos["tipo"] == "Classic":
        cliente = c.Classic( datos["numero"], datos["nombre"], datos["apellido"], datos["dni"], datos["transacciones"])
    elif datos["tipo"] == "Gold":
        cliente = c.Gold( datos["numero"], datos["nombre"], datos["apellido"], datos["dni"], datos["transacciones"])
    else:
        cliente = c.Black( datos["numero"], datos["nombre"], datos["apellido"], datos["dni"], datos["transacciones"])

print(cliente)