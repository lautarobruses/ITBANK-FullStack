from cliente.cliente import Cliente

class Classic(Cliente):
    def __init__(self, numero, nombre, apellido, dni, transacciones, caja_ahorros_pesos):
        super().__init__(numero, nombre, apellido, dni, transacciones)
        self.caja_ahorros_pesos = caja_ahorros_pesos
        self.limite_retiro_efectivo = 10.000

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
    
    def venta_dolar(self, monto) -> bool:
        return super().venta_dolar(monto)
    
    def comprar_dolar(self, monto) -> bool:
        return super().comprar_dolar(monto)
     