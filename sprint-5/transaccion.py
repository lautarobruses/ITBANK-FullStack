class Transaccion:
    def __init__(self, estado, tipo, permitidoActualParaTransccion, monto, fecha, numero, cuentaNumero=None, saldoDisponibleEnCuenta=None):
        self.estado = estado
        self.tipo = tipo
        self.cuentaNumero = cuentaNumero
        self.saldoDisponibleEnCuenta = saldoDisponibleEnCuenta
        self.permitidoActualParaTransccion = permitidoActualParaTransccion
        self.monto = monto
        self.fecha = fecha
        self.numero = numero
        self.razon = ""