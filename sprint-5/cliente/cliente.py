import requests

url = "https://dolarapi.com/v1/dolares/oficial"

response = requests.get(url)
data = response.json()
precio_dolar_oficial = data['venta']
# print('El precio del dolar es: ',precio_dolar_oficial)

class Cliente:
    def __init__(self, numero, nombre, apellido, dni, transacciones, saldo_disponible_en_cuenta):
        self.numero = numero
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
        self.transacciones = transacciones
        self.saldo_disponible_en_cuenta = saldo_disponible_en_cuenta

    def retiro_efectivo_cajero_automatico():
        '''descripcion'''
        pass
    
    def retiro_efectivo_por_caja():
        '''descripcion'''
        pass

    def comprar_en_cuotas_tarjeta_credito_visa():
        '''descripcion'''
        pass

    def comprar_en_cuotas_tarjeta_credito_mastercard():
        '''descripcion'''
        pass

    def comprar_en_cuotas_tarjeta_credito_american():
        '''descripcion'''

    def comprar_tarjeta_credito_visa():
        '''descripcion'''
        pass

    def comprar_tarjeta_credito_mastercard():
        '''descripcion'''
        pass

    def comprar_tarjeta_credito_american():
        '''descripcion'''
        pass

    def alta_tarjeta_debito():
        '''descripcion'''
        pass

    def alta_cuenta_credito_visa():
        '''descripcion'''
        pass

    def alta_cuenta_credito_mastercard():
        '''descripcion'''
        pass

    def alta_cuenta_credito_american():
        '''descripcion'''
        pass

    def alta_caja_ahorros_pesos():
        '''descripcion'''
        pass

    def alta_caja_ahorros_dolares(self):
        '''descripcion'''
        self.caja_ahorro_dolar = True # Si es True, permite la compra y venta de dolares

    def alta_cuenta_inversion():
        '''descripcion'''
        pass
    
    def calcular_monto_total(self, precio_dolar, monto):
        precio_dolar = precio_dolar_oficial
        monto_total = monto * precio_dolar
        return monto_total

    def comprar_dolar(self, monto) -> bool:
        '''Compra una cantidad de dólares y devuelve el monto en pesos o False si la compra falla.'''
        if self.caja_ahorro_dolar:
            costo_en_pesos = self.calcular_monto_total(precio_dolar_oficial, monto)
            
            if costo_en_pesos > self.saldo_disponible_en_cuenta:
                return False  # No hay suficientes fondos en pesos para la compra de dólares

            return costo_en_pesos  # Devuelve el costo en pesos de la compra
        else:
            return False

    def vender_dolar(self, monto) -> bool:
        '''Vende una cantidad de dólares y devuelve el monto en pesos o False si la venta falla.'''
        if self.caja_ahorro_dolar:
            if monto > self.saldo_disponible_en_cuenta:
                return False  # No hay suficientes dólares para la venta
            
            monto_en_pesos = self.calcular_monto_total(precio_dolar_oficial, monto)
            
            return monto_en_pesos  # Devuelve el monto en pesos de la venta
        else:
            return False
        
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