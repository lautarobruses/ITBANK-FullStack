import requests

url = "https://dolarapi.com/v1/dolares/oficial"

response = requests.get(url)
data = response.json()
precio_dolar_oficial = data['venta']
# print('El precio del dolar es: ',precio_dolar_oficial)

class Cliente:
    def __init__(self, numero, nombre, apellido, dni, transacciones):
        self.numero = numero
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
        self.transacciones = transacciones

    def retiro_efectivo_cajero_automatico():
        '''descripcion'''
        pass
    
    def retiro_efectivo_por_caja():
        '''descripcion'''
        pass

    def comprar_en_cuotas_tarjeta_credito_pesos():
        '''descripcion'''
        pass

    def comprar_en_cuotas_tarjeta_credito_dolares():
        '''descripcion'''

    def comprar_tarjeta_credito_pesos():
        '''descripcion'''
        pass

    def comprar_tarjeta_credito_dolares():
        '''descripcion'''
        pass

    def alta_tarjeta_debito():
        '''descripcion'''
        pass

    def alta_cuenta_cte_pesos():
        '''descripcion'''
        pass

    def alta_cuenta_cte_dolares():
        '''descripcion'''
        pass

    def alta_caja_ahorros_pesos():
        '''descripcion'''
        pass

    def alta_caja_ahorros_dolares():
        '''descripcion'''
        pass

    def alta_cuenta_inversion():
        '''descripcion'''
        pass

    def comprar_dolar():
        '''descripcion'''
        pass

    def venta_dolar():
        '''descripcion'''
        pass
        
    def transferencia_enviada_pesos():
        '''descripcion'''
        pass
        
    def transferencia_enviada_dolares():
        '''descripcion'''
        pass

    def transferencia_recibida_pesos():
        '''descripcion'''
        pass

    def transferencia_recibida_dolares():
        '''descripcion'''
        pass