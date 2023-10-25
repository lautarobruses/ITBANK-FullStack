class Transaccion:
    def __init__(self, estado, tipo, permitidoActualParaTransaccion, monto, fecha, numero, cuentaNumero=None, saldoDisponibleEnCuenta=0):
        self.estado = estado
        self.tipo = tipo
        self.cuentaNumero = cuentaNumero
        self.saldoDisponibleEnCuenta = float(saldoDisponibleEnCuenta)
        self.permitidoActualParaTransaccion = float(permitidoActualParaTransaccion)
        self.monto = float(monto)
        self.fecha = fecha
        self.numero = float(numero)
        self.razon = ""