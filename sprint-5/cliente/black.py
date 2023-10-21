from cliente.cliente import Cliente

class Black(Cliente):
    def __init__(self, numero, nombre, apellido, dni, transacciones):
        super().__init__(numero, nombre, apellido, dni, transacciones)

    def retiro_efectivo_cajero_automatico(hola):
        '''descripcion'''
        print(hola)
        return "hola"
    
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