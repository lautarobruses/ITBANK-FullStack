import json
import webbrowser

from cliente.classic import Classic
from cliente.gold import Gold
from cliente.black import Black
from transaccion import Transaccion
from salidaHTML import crearHTML

# Nombre del archivo JSON que se desea analizar
NOMBRE_ARCHIVO = 'ejemplo.json'

# Abre el archivo JSON en modo lectura
with open(NOMBRE_ARCHIVO, 'r') as archivo:
    datos = json.load(archivo)

    if datos["tipo"] == "Classic":
        cliente = Classic(datos["numero"], datos["nombre"],
                          datos["apellido"], datos["dni"], datos["transacciones"])
    elif datos["tipo"] == "Gold":
        cliente = Gold(datos["numero"], datos["nombre"],
                       datos["apellido"], datos["dni"], datos["transacciones"])
    else:
        cliente = Black(datos["numero"], datos["nombre"],
                        datos["apellido"], datos["dni"], datos["transacciones"])

    transacciones: list[Transaccion] = []

    for transaccion in cliente.transacciones:
        nueva_transaccion: Transaccion = Transaccion(transaccion['estado'], transaccion["tipo"], transaccion["permitidoActualParaTransccion"], 
                                                     transaccion["monto"], transaccion["fecha"], transaccion["numero"])
        
        if 'cuentaNumero' in transaccion:
            nueva_transaccion.cuentaNumero = transaccion['cuentaNumero']
        if 'saldoDisponibleEnCuenta' in transaccion:
            nueva_transaccion.saldoDisponibleEnCuenta = transaccion['saldoDisponibleEnCuenta']
            
        nombre_metodo = nueva_transaccion.tipo.lower()

        # Verifica si el método existe en el objeto antes de llamarlo
        if hasattr(cliente, nombre_metodo):
            # Obtén una referencia al método utilizando getattr
            metodo = getattr(cliente, nombre_metodo)

            # Llama al método
            razon = metodo()

            print(razon)

            nueva_transaccion.razon = razon

            transacciones.append(nueva_transaccion)

    print(transacciones)
    #html_output = crearHTML(transacciones)
    #borrar lo siguiente y descomentar lo de arriba
    html_output = crearHTML([{
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
    
    with open('html_output.html', 'w') as file:
        file.write(html_output)

    webbrowser.open('html_output.html')
