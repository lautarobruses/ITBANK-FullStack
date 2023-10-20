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