class Transaccion:
    def __init__(self, estado, tipo, permitidoActualParaTransccion, monto, fecha, numero, cuentaNumero=None, saldoDisponibleEnCuenta=0):
        self.estado = estado
        self.tipo = tipo
        self.cuentaNumero = cuentaNumero
        self.saldoDisponibleEnCuenta = float(saldoDisponibleEnCuenta)
        self.permitidoActualParaTransccion = float(permitidoActualParaTransccion)
        self.monto = float(monto)
        self.fecha = fecha
        self.numero = float(numero)
        self.razon = ""