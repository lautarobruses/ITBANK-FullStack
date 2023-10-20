from cliente.classic import Classic
from cliente.gold import Gold
from cliente.black import Black
import json

# Abre el archivo JSON en modo lectura
with open('ejemplo.json', 'r') as archivo:
    datos = json.load(archivo)

    if datos["tipo"] == "Classic":
        cliente = Classic( datos["numero"], datos["nombre"], datos["apellido"], datos["dni"], datos["transacciones"])
    elif datos["tipo"] == "Gold":
        cliente = Gold( datos["numero"], datos["nombre"], datos["apellido"], datos["dni"], datos["transacciones"])
    else:
        cliente = Black( datos["numero"], datos["nombre"], datos["apellido"], datos["dni"], datos["transacciones"])

print(cliente)