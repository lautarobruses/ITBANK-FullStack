from cliente.cliente import Cliente
import services.funciones as fn

class Classic(Cliente):
    def __init__(self, numero, nombre, apellido, dni, transacciones):
        super().__init__(numero, nombre, apellido, dni, transacciones, 0.01, 0.05)
        self.limite_retiro_efectivo = 10.000
        self.contador_retiros = 0
        self.tarifa = 100
        self.limite_tarjeta_debito = 1
        self.tarjetas_debito = {}

    def retiro_efectivo_por_cajero_automatico(self, transaccion) -> str: #En esta y la siguiente funcion tomo a permitidoActualParaTransaccion como el limite de retiro diario que le queda a classic, lo mismo para el gold y el black.
        '''Este metodo toma la transaccion de tipo:'retiro_efectivo_cajero_automatico' que el cliente classic realizo y devuelve en un string la razon por las que fue aceptada o rechazada teniendo en cuenta que tiene hasta 5 retiros de dinero en efectivo sin comisiones y luego se aplica una tarifa, y que el límite diario de retiro es de $10,000 por cajero.'''
        
        self.contador_retiros += 1

        if self.contador_retiros > 5:
            montoTotal = transaccion.monto + self.tarifa
        else:
            montoTotal = transaccion.monto

        try:
            if transaccion.saldoDisponibleEnCuenta <= 0:
                return f"Monto Inválido: El monto ingresado es un numero, pero debe ser mayor que cero."
            else:
                if transaccion.permitidoActualParaTransaccion < montoTotal:
                    return f"Supera el Limite Diario: No es posible retirar {montoTotal} ya que superarias tu limite de 10.000$ diario."
                elif transaccion.saldoDisponibleEnCuenta < montoTotal:
                    return f"Fondos Insuficientes: No es posible retirar {montoTotal}$ ya que excede tu saldo disponible de {transaccion.saldoDisponibleEnCuenta}$."
                else:
                    return f"Retiro Exitoso: El monto extraido es un numero y ademas no supera tu saldo disponible."
        except:
            return f"Formato Inválido: El monto debe ser un numero."

    def retiro_efectivo_por_caja(self, transaccion) -> str:
        '''Este metodo toma la transaccion de tipo:'retiro_efectivo_por_caja' que el cliente classic realizo y devuelve en un string la razon por las que fue aceptada o rechazada teniendo en cuenta que tiene hasta 5 retiros de dinero en efectivo sin comisiones y luego se aplica una tarifa.'''
        
        self.contador_retiros += 1

        if self.contador_retiros > 5:
            montoTotal = transaccion.monto + self.tarifa
        else:
            montoTotal = transaccion.monto

        try:
            if transaccion.saldoDisponibleEnCuenta <= 0:
                return f"Monto Inválido: El monto ingresado es un numero, pero debe ser mayor que cero."
            else:
                if transaccion.saldoDisponibleEnCuenta < montoTotal:
                    return f"Fondos Insuficientes: No es posible retirar {montoTotal}$ ya que excede tu saldo disponible de {transaccion.saldoDisponibleEnCuenta}$."
                else:
                    return f"Retiro Exitoso: El monto extraido es un numero y ademas no supera tu saldo disponible."
        except:
            return f"Formato Inválido: El monto debe ser un numero."

    def comprar_en_cuotas_tarjeta_credito_visa( self, transaccion ) -> str:
        '''Este metodo toma la transaccion de tipo:'comprar_en_cuotas_tarjeta_credito_visa' que el cliente classic realizo y devuelve en un string la razon por la cual classic no puede realizar compras en cuotas con tarjeta de credito visa.'''
        
        return "Cliente Classic: Los clientes classic no poseen tarjetas de crédito. Tu cuenta es de tipo 'Classic' y esta función está limitada para cuentas con un nivel de acceso más alto."

    def comprar_en_cuotas_tarjeta_credito_master( self, transaccion ) -> str:
        '''Este metodo toma la transaccion de tipo:'comprar_en_cuotas_tarjeta_credito_visa' que el cliente classic realizo y devuelve en un string la razon por la cual classic no puede realizar compras en cuotas con tarjeta de credito mastercard.'''
       
        return "Cliente Classic: Los clientes classic no poseen tarjetas de crédito. Tu cuenta es de tipo 'Classic' y esta función está limitada para cuentas con un nivel de acceso más alto."

    def comprar_en_cuotas_tarjeta_credito_amex( self, transaccion ) -> str:
        '''Este metodo toma la transaccion de tipo:'comprar_en_cuotas_tarjeta_credito_visa' que el cliente classic realizo y devuelve en un string la razon por la cual classic no puede realizar compras en cuotas con tarjeta de credito american express.'''
       
        return "Cliente Classic: Los clientes classic no poseen tarjetas de crédito. Tu cuenta es de tipo 'Classic' y esta función está limitada para cuentas con un nivel de acceso más alto."

    def comprar_tarjeta_credito_visa( self, transaccion ) -> str:
        '''Este metodo toma la transaccion de tipo:'comprar_en_cuotas_tarjeta_credito_visa' que el cliente classic realizo y devuelve en un string la razon por la cual classic no puede realizar compras con tarjeta de credito visa.'''
       
        return "Cliente Classic: Los clientes classic no poseen tarjetas de crédito. Tu cuenta es de tipo 'Classic' y esta función está limitada para cuentas con un nivel de acceso más alto."

    def comprar_tarjeta_credito_master( self, transaccion ) -> str:
        '''Este metodo toma la transaccion de tipo:'comprar_en_cuotas_tarjeta_credito_visa' que el cliente classic realizo y devuelve en un string la razon por la cual classic no puede realizar compras con tarjeta de credito mastercard.'''
       
        return "Cliente Classic: Los clientes classic no poseen tarjetas de crédito. Tu cuenta es de tipo 'Classic' y esta función está limitada para cuentas con un nivel de acceso más alto."

    def comprar_tarjeta_credito_amex( self, transaccion ) -> str:
        '''Este metodo toma la transaccion de tipo:'comprar_en_cuotas_tarjeta_credito_visa' que el cliente classic realizo y devuelve en un string la razon por la cual classic no puede realizar compras con tarjeta de credito american express.'''
       
        return "Cliente Classic: Los clientes classic no poseen tarjetas de crédito. Tu cuenta es de tipo 'Classic' y esta función está limitada para cuentas con un nivel de acceso más alto."
        
    def alta_tarjeta_debito(self, transaccion):
        razon = ""
        if self.limite_tarjeta_debito > 0:
            if transaccion.cuentaNumero in self.tarjetas_debito:
                razon = "Alta de la tarjeta ya aceptada anteriormente"
            else:
                self.tarjetas_debito[transaccion.cuentaNumero] = 1
                self.limite_tarjeta_debito -= 1
                razon = "Alta de la tarjeta aceptada"
        else:
            razon = "Has alcanzado el límite de tarjetas de débito permitidas."
        return razon

    def alta_caja_ahorros_pesos(self, transaccion) -> str:
        '''descripcion'''

    def alta_cuenta_inversion(self, transaccion) -> str:
        '''descripcion'''
        return "La cuenta Classic no tiene permitido el acceso a las inversiones."
    