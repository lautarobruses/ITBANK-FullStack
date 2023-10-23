
from cliente.cliente import Cliente

class Gold(Cliente):
    def __init__(self, numero, nombre, apellido, dni, transacciones):
        super().__init__(numero, nombre, apellido, dni, transacciones)
        self.limite_retiro_efectivo = 20.000
        self.porcentaje_comision_envio = 0.5
        self.porcentaje_comision_recibo = 0.1

    def retiro_efectivo_cajero_automatico(self, transaccion):
        '''Este metodo toma la transaccion de tipo:'retiro_efectivo_cajero_automatico' que el cliente gold realizo y especifica la razones por las que fue aceptada o rechazada teniendo en cuenta que el límite diario de retiro es de $20,000 por cajero.'''

        try:
            if transaccion.saldoDisponibleEnCuenta <= 0:
                transaccion.razon += "Monto Inválido: El monto ingresado es un numero, pero debe ser mayor que cero."
            else:
                if transaccion.permitidoActualParaTransaccion < transaccion.monto:
                    transaccion.razon += f"Supera el Limite Diario: No es posible retirar {transaccion.monto} ya que superarias tu limite de 20.000$ diario."
                elif transaccion.saldoDisponibleEnCuenta < transaccion.monto:
                    transaccion.razon += f"Fondos Insuficientes: No es posible retirar {transaccion.monto}$ ya que excede tu saldo disponible de {transaccion.saldoDisponibleEnCuenta}$."
                else:
                    transaccion.razon += "Retiro Exitoso: El monto extraido es un numero y ademas no supera tu saldo disponible."
        except:
            transaccion.razon += "Formato Inválido: El monto debe ser un numero."
    
    def retiro_efectivo_por_caja(self, transaccion):
        '''Este metodo toma la transaccion de tipo:'retiro_efectivo_cajero_automatico' que el cliente gold realizo y especifica la razones por las que fue aceptada o rechazada.'''

        try:
            if transaccion.saldoDisponibleEnCuenta <= 0:
                transaccion.razon += "Monto Inválido: El monto ingresado es un numero, pero debe ser mayor que cero."
            else:
                if transaccion.saldoDisponibleEnCuenta < transaccion.monto:
                    transaccion.razon += f"Fondos Insuficientes: No es posible retirar {transaccion.monto}$ ya que excede tu saldo disponible de {transaccion.saldoDisponibleEnCuenta}$."
                else:
                    transaccion.razon += "Retiro Exitoso: El monto extraido es un numero y ademas no supera tu saldo disponible."
        except:
            transaccion.razon += "Formato Inválido: El monto debe ser un numero."

    def comprar_en_cuotas_tarjeta_credito_visa(self, transaccion):
        '''Este metodo toma la transaccion de tipo:'comprar_en_cuotas_tarjeta_credito_visa' que el cliente gold realizo y especifica la razones por las que fue aceptada o rechazada.'''

        try:
            if transaccion.saldoDisponibleEnCuenta <= 0:
                transaccion.razon += "Monto Inválido: El monto ingresado es un numero, pero debe ser mayor que cero."
            else:
                if transaccion.saldoDisponibleEnCuenta < transaccion.monto:
                    transaccion.razon += f"Fondos Insuficientes: No es posible comprar en cuotas con tu tarjeta visa con el monto de {transaccion.monto}$ ya que excede tu saldo disponible de {transaccion.saldoDisponibleEnCuenta}$."
                else:
                    transaccion.razon += "Retiro Exitoso: El monto con el que desea comprar en cuotas es un numero y ademas no supera tu saldo disponible."
        except:
            transaccion.razon += "Formato Inválido: El monto debe ser un numero."
  

    def comprar_en_cuotas_tarjeta_credito_master(self, transaccion):
        '''Este metodo toma la transaccion de tipo:'comprar_en_cuotas_tarjeta_credito_master' que el cliente gold realizo y especifica la razones por las que fue aceptada o rechazada.'''

        try:
            if transaccion.saldoDisponibleEnCuenta <= 0:
                transaccion.razon += "Monto Inválido: El monto ingresado es un numero, pero debe ser mayor que cero."
            else:
                if transaccion.saldoDisponibleEnCuenta < transaccion.monto:
                    transaccion.razon += f"Fondos Insuficientes: No es posible comprar en cuotas con tu tarjeta mastercard con el monto de {transaccion.monto}$ ya que excede tu saldo disponible de {transaccion.saldoDisponibleEnCuenta}$."
                else:
                    transaccion.razon += "Retiro Exitoso: El monto con el que desea comprar en cuotas es un numero y ademas no supera tu saldo disponible."
        except:
            transaccion.razon += "Formato Inválido: El monto debe ser un numero."
       

    def comprar_en_cuotas_tarjeta_credito_amex(self, transaccion):
        '''descripcion'''

        transaccion.razon = "Cliente Gold: No puedes realizar compras en cuotas con tarjeta de crédito american express. Tu cuenta es de tipo 'Gold' y esta función está limitada para cuentas con un nivel de acceso más alto."

    def comprar_tarjeta_credito_visa(self, transaccion):
        '''Este metodo toma la transaccion de tipo:'comprar_tarjeta_credito_visa' que el cliente gold realizo y especifica la razones por las que fue aceptada o rechazada.'''

        try:
            if transaccion.saldoDisponibleEnCuenta <= 0:
                transaccion.razon += "Monto Inválido: El monto ingresado es un numero, pero debe ser mayor que cero."
            else:
                if transaccion.saldoDisponibleEnCuenta < transaccion.monto:
                    transaccion.razon += f"Fondos Insuficientes: No es posible comprar con tu tarjeta visa con el monto de {transaccion.monto}$ ya que excede tu saldo disponible de {transaccion.saldoDisponibleEnCuenta}$."
                else:
                    transaccion.razon += "Retiro Exitoso: El monto con el que desea comprar en cuotas es un numero y ademas no supera tu saldo disponible."
        except:
            transaccion.razon += "Formato Inválido: El monto debe ser un numero."
        

    def comprar_tarjeta_credito_master(self, transaccion):
        '''Este metodo toma la transaccion de tipo:'comprar_tarjeta_credito_master' que el cliente gold realizo y especifica la razones por las que fue aceptada o rechazada.'''

        try:
            if transaccion.saldoDisponibleEnCuenta <= 0:
                transaccion.razon += "Monto Inválido: El monto ingresado es un numero, pero debe ser mayor que cero."
            else:
                if transaccion.saldoDisponibleEnCuenta < transaccion.monto:
                    transaccion.razon += f"Fondos Insuficientes: No es posible comprar con tu tarjeta mastercard con el monto de {transaccion.monto}$ ya que excede tu saldo disponible de {transaccion.saldoDisponibleEnCuenta}$."
                else:
                    transaccion.razon += "Retiro Exitoso: El monto con el que desea comprar en cuotas es un numero y ademas no supera tu saldo disponible."
        except:
            transaccion.razon += "Formato Inválido: El monto debe ser un numero."   

    def comprar_tarjeta_credito_amex(self, transaccion):
        '''descripcion'''
        
        transaccion.razon = "Cliente Gold: No puedes realizar compras con tarjeta de crédito american express. Tu cuenta es de tipo 'Gold' y esta función está limitada para cuentas con un nivel de acceso más alto."
    
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