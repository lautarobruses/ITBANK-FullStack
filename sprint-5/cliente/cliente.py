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
    
    def descontar_comision(self, monto, porcentaje_comision):
        comision = monto * (porcentaje_comision / 100)
        monto_descontado = monto - comision
        return monto_descontado
    
    def comprar_dolar(self, monto) -> bool:
        '''descripcion'''
        if self.caja_ahorro_dolar == True:
            costo_en_pesos = monto * precio_dolar_oficial
            costo_con_comision = self.descontar_comision(costo_en_pesos)
            
            if costo_con_comision > monto:
                return False  # No hay suficientes fondos en pesos para la compra de dólares
            else:
                return True  # Devuelve True si la compra se realiza con éxitocosto_en_pesos = monto * precio_dolar_oficial
        else:
            return False

    def venta_dolar(self, monto) -> bool:
        '''descripcion'''
        if self.caja_ahorro_dolar == True:
            if precio_dolar_oficial > monto:
                return False  
            
            monto_en_pesos = monto * precio_dolar_oficial
            monto_con_comision = self.descontar_comision(monto_en_pesos)
            
            return monto_con_comision
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