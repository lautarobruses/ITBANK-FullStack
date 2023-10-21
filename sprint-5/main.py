import json
from jinja2 import Template
from cliente.classic import Classic
from cliente.gold import Gold
from cliente.black import Black

# Abre el archivo JSON en modo lectura
with open('ejemplo.json', 'r') as archivo:
    datos = json.load(archivo)

    if datos["tipo"] == "Classic":
        cliente = Classic( datos["numero"], datos["nombre"], datos["apellido"], datos["dni"], datos["transacciones"])
    elif datos["tipo"] == "Gold":
        cliente = Gold( datos["numero"], datos["nombre"], datos["apellido"], datos["dni"], datos["transacciones"])
    else:
        cliente = Black( datos["numero"], datos["nombre"], datos["apellido"], datos["dni"], datos["transacciones"])
    
    transacciones = cliente.transacciones
    # print(transacciones)

    for transaccion in transacciones:
        print(transaccion)

        # Nombre del método en forma de cadena
        nombre_metodo = "nombre_del_metodo"

        # Verifica si el método existe en el objeto antes de llamarlo
        if hasattr(cliente, nombre_metodo):
            # Obtén una referencia al método utilizando getattr
            metodo = getattr(cliente, nombre_metodo)

            # Llama al método
            resultado = metodo()
        
            transaccion.razon = resultado
            # transaccion.razon = "blablablaba"

print(cliente)