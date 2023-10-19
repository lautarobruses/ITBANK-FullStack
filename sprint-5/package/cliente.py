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

    def comprar_en_cuotas_tarjeta_credito_dolares():
        '''descripcion'''

    def comprar_tarjeta_credito_pesos():
        '''descripcion'''

    def comprar_tarjeta_credito_dolares():
        '''descripcion'''

    def alta_tarjeta_debito():
        '''descripcion'''
        pass

    def alta_cuenta_cte_pesos():
        '''descripcion'''

    def alta_cuenta_cte_dolares():
        '''descripcion'''

    def alta_caja_ahorros_pesos():
        '''descripcion'''
        pass

    def alta_caja_ahorros_dolares():
        '''descripcion'''

    def alta_cuenta_inversion():
        '''descripcion'''

    def comprar_dolar():
        '''descripcion'''

    def venta_dolar():
        '''descripcion'''
        
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


class Classic(Cliente):
    def __init__(self, numero, nombre, apellido, dni, transacciones):
        super().__init__(numero, nombre, apellido, dni, transacciones)

    def retiro_efectivo_cajero_automatico():
        '''descripcion'''
    
    def retiro_efectivo_por_caja():
        '''descripcion'''
        
    def alta_tarjeta_debito():
        '''descripcion'''

    def alta_caja_ahorros_pesos():
        '''descripcion'''

    def transferencia_enviada_pesos():
        '''descripcion'''
        
    def transferencia_enviada_dolares():
        '''descripcion'''

    def transferencia_recibida_pesos():
        '''descripcion'''

    def transferencia_recibida_dolares():
        '''descripcion'''

class Gold(Cliente):
    def __init__(self, numero, nombre, apellido, dni, transacciones):
        super().__init__(numero, nombre, apellido, dni, transacciones)

    def retiro_efectivo_cajero_automatico():
        '''descripcion'''
    
    def retiro_efectivo_por_caja():
        '''descripcion'''

    def alta_tarjeta_debito():
        '''descripcion'''

    def alta_caja_ahorros_pesos():
        '''descripcion'''

    def transferencia_enviada_pesos():
        '''descripcion'''
        
    def transferencia_enviada_dolares():
        '''descripcion'''

    def transferencia_recibida_pesos():
        '''descripcion'''

    def transferencia_recibida_dolares():
        '''descripcion'''

class Black(Cliente):
    def __init__(self, numero, nombre, apellido, dni, transacciones):
        super().__init__(numero, nombre, apellido, dni, transacciones)

    def retiro_efectivo_cajero_automatico():
        '''descripcion'''
    
    def retiro_efectivo_por_caja():
        '''descripcion'''
        
    def alta_tarjeta_debito():
        '''descripcion'''
        
    def alta_caja_ahorros_pesos():
        '''descripcion'''
        
    def transferencia_enviada_pesos():
        '''descripcion'''
        
    def transferencia_enviada_dolares():
        '''descripcion'''

    def transferencia_recibida_pesos():
        '''descripcion'''

    def transferencia_recibida_dolares():
        '''descripcion'''