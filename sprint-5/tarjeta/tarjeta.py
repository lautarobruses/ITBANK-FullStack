class Tarjeta:
    def __init__( self, numero, tipo, fecha_vencimiento, codigo_seguridad ):
        self.numero = numero
        self.tipo = tipo
        self.fecha_vencimiento = fecha_vencimiento
        self.codigo_seguridad = codigo_seguridad

class Debito(Tarjeta):
    def __init__(self,):
        return

class Credito(Tarjeta):
    def __init__(self, limite_pago, limite_cuotas, cantidad):
        self.limite_pago = limite_pago
        self.limite_cuotas = limite_cuotas
        self.cantidad = cantidad
