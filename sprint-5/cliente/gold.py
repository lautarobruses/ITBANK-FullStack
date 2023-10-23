
from cliente.cliente import Cliente

class Gold(Cliente):
    def __init__(self, numero, nombre, apellido, dni, transacciones):
        super().__init__(numero, nombre, apellido, dni, transacciones)
        self.limite_retiro_efectivo = 20.000
        self.porcentaje_comision_envio = 0.5
        self.porcentaje_comision_recibo = 0.1

    def retiro_efectivo_cajero_automatico():
        '''descripcion'''
    
    def retiro_efectivo_por_caja():
        '''descripcion'''

    def alta_tarjeta_debito():
        '''descripcion'''

    def alta_caja_ahorros_pesos():
        '''descripcion'''

    def venta_dolar(self, monto) -> bool:
        return super().venta_dolar(monto)
    
    def comprar_dolar(self, monto) -> bool:
        return super().comprar_dolar(monto)
    
    def transferencia_recibida_pesos(self, monto, es_transferencia_enviada=False):
        return super().transferencia_recibida_pesos(monto, es_transferencia_enviada)
    
    def transferencia_recibida_dolares(self, monto, es_transferencia_enviada=False):
        return super().transferencia_recibida_dolares(monto, es_transferencia_enviada)
    
    def transferencia_enviada_pesos(self, monto, cuenta_destino, es_transferencia_enviada=True):
        return super().transferencia_enviada_pesos(monto, cuenta_destino, es_transferencia_enviada)
    
    def transferencia_enviada_dolares(self, monto, cuenta_destino, es_transferencia_enviada=True):
        return super().transferencia_enviada_dolares(monto, cuenta_destino, es_transferencia_enviada)
    
    def alta_cuenta_inversion(self, transaccion) -> bool:
        return super().alta_cuenta_inversion(transaccion)