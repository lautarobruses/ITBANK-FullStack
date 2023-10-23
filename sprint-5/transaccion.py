class Transaccion:
    def __init__(self, estado, tipo, saldoDisponibleEnCuenta, permitidoActualParaTransccion, monto, fecha, numero, cuentaNumero=None):
        self.estado = estado
        self.tipo = tipo
        self.cuentaNumero = cuentaNumero
        self.saldoDisponibleEnCuenta = saldoDisponibleEnCuenta
        self.permitidoActualParaTransccion = permitidoActualParaTransccion
        self.monto = monto
        self.fecha = fecha
        self.numero = numero
        self.razon = ""