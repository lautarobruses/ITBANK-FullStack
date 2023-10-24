from cliente.cliente import Cliente


class Gold(Cliente):
    def __init__(self, numero, nombre, apellido, dni, transacciones):
        super().__init__(numero, nombre, apellido, dni, transacciones, 0.05, 0.001)
        self.limite_retiro_efectivo = 20.000
        self.cuenta_inversion = False
        self.limite_tarjeta_debito = 1
        self.tarjetas_debito = {}
        self.limite_tarjeta_credito_visa = 5
        self.limite_tarjeta_credito_mastercard = 5
        self.tarjetas_credito_visa = {}
        self.tarjetas_credito_mastercard = {}
        self.chequeras = {}
        self.limite_chequeras = 1

    def retiro_efectivo_cajero_automatico(self, transaccion) -> str:
        '''Este metodo toma la transaccion de tipo:'retiro_efectivo_cajero_automatico' que el cliente gold realizo y devuelve en un string la razon por las que fue aceptada o rechazada teniendo en cuenta que el límite diario de retiro es de $20,000 por cajero.'''

        try:
            if transaccion.monto <= 0:
                return "Monto Inválido: El monto ingresado es un numero, pero debe ser mayor que cero."
            else:
                if transaccion.permitidoActualParaTransaccion < transaccion.monto:
                    return f"Supera el Limite Diario: No es posible retirar {transaccion.monto} ya que superarias tu limite de 20.000$ diario."
                elif transaccion.saldoDisponibleEnCuenta < transaccion.monto:
                    return f"Fondos Insuficientes: No es posible retirar {transaccion.monto}$ ya que excede tu saldo disponible de {transaccion.saldoDisponibleEnCuenta}$."
                else:
                    return "Retiro Exitoso: El monto extraido es un numero y ademas no supera tu saldo disponible."
        except:
            return "Formato Inválido: El monto debe ser un numero."

    def retiro_efectivo_por_caja(self, transaccion) -> str:
        '''Este metodo toma la transaccion de tipo:'retiro_efectivo_cajero_automatico' que el cliente gold realizo y devuelve en un string la razon por las que fue aceptada o rechazada.'''

        try:
            if transaccion.monto <= 0:
                return "Monto Inválido: El monto ingresado es un numero, pero debe ser mayor que cero."
            else:
                if transaccion.saldoDisponibleEnCuenta < transaccion.monto:
                    return f"Fondos Insuficientes: No es posible retirar {transaccion.monto}$ ya que excede tu saldo disponible de {transaccion.saldoDisponibleEnCuenta}$."
                else:
                    return "Retiro Exitoso: El monto extraido es un numero y ademas no supera tu saldo disponible."
        except:
            return "Formato Inválido: El monto debe ser un numero."

    def comprar_en_cuotas_tarjeta_credito_visa(self, transaccion) -> str:
        '''Este metodo toma la transaccion de tipo:'comprar_en_cuotas_tarjeta_credito_visa' que el cliente gold realizo y devuelve en un string la razon por las que fue aceptada o rechazada.'''

        try:
            if transaccion.monto <= 0:
                return "Monto Inválido: El monto ingresado es un numero, pero debe ser mayor que cero."
            else:
                if transaccion.saldoDisponibleEnCuenta < transaccion.monto:
                    return f"Fondos Insuficientes: No es posible comprar en cuotas con tu tarjeta visa con el monto de {transaccion.monto}$ ya que excede tu saldo disponible de {transaccion.saldoDisponibleEnCuenta}$."
                else:
                    return "Retiro Exitoso: El monto con el que desea comprar en cuotas es un numero y ademas no supera tu saldo disponible."
        except:
            return "Formato Inválido: El monto debe ser un numero."

    def comprar_en_cuotas_tarjeta_credito_master(self, transaccion) -> str:
        '''Este metodo toma la transaccion de tipo:'comprar_en_cuotas_tarjeta_credito_master' que el cliente gold realizo y devuelve en un string la razon por las que fue aceptada o rechazada.'''

        try:
            if transaccion.monto <= 0:
                return "Monto Inválido: El monto ingresado es un numero, pero debe ser mayor que cero."
            else:
                if transaccion.saldoDisponibleEnCuenta < transaccion.monto:
                    return f"Fondos Insuficientes: No es posible comprar en cuotas con tu tarjeta mastercard con el monto de {transaccion.monto}$ ya que excede tu saldo disponible de {transaccion.saldoDisponibleEnCuenta}$."
                else:
                    return "Retiro Exitoso: El monto con el que desea comprar en cuotas es un numero y ademas no supera tu saldo disponible."
        except:
            return "Formato Inválido: El monto debe ser un numero."

    def comprar_en_cuotas_tarjeta_credito_amex(self, transaccion) -> str:
        '''descripcion'''

        return "Cliente Gold: No puedes realizar compras en cuotas con tarjeta de crédito american express. Tu cuenta es de tipo 'Gold' y esta función está limitada para cuentas con un nivel de acceso más alto."

    def comprar_tarjeta_credito_visa(self, transaccion) -> str:
        '''Este metodo toma la transaccion de tipo:'comprar_tarjeta_credito_visa' que el cliente gold realizo y devuelve en un string la razon por las que fue aceptada o rechazada.'''

        try:
            if transaccion.monto <= 0:
                return "Monto Inválido: El monto ingresado es un numero, pero debe ser mayor que cero."
            else:
                if transaccion.saldoDisponibleEnCuenta < transaccion.monto:
                    return f"Fondos Insuficientes: No es posible comprar con tu tarjeta visa con el monto de {transaccion.monto}$ ya que excede tu saldo disponible de {transaccion.saldoDisponibleEnCuenta}$."
                else:
                    return "Retiro Exitoso: El monto con el que desea comprar en cuotas es un numero y ademas no supera tu saldo disponible."
        except:
            return "Formato Inválido: El monto debe ser un numero."

    def comprar_tarjeta_credito_master(self, transaccion) -> str:
        '''Este metodo toma la transaccion de tipo:'comprar_tarjeta_credito_master' que el cliente gold realizo y devuelve en un string la razon por las que fue aceptada o rechazada.'''

        try:
            if transaccion.monto <= 0:
                return "Monto Inválido: El monto ingresado es un numero, pero debe ser mayor que cero."
            else:
                if transaccion.saldoDisponibleEnCuenta < transaccion.monto:
                    return f"Fondos Insuficientes: No es posible comprar con tu tarjeta mastercard con el monto de {transaccion.monto}$ ya que excede tu saldo disponible de {transaccion.saldoDisponibleEnCuenta}$."
                else:
                    return "Retiro Exitoso: El monto con el que desea comprar en cuotas es un numero y ademas no supera tu saldo disponible."
        except:
            return "Formato Inválido: El monto debe ser un numero."

    def comprar_tarjeta_credito_amex(self, _transaccion) -> str:
        '''descripcion'''
        return "Cliente Gold: No puedes realizar compras con tarjeta de crédito american express. Tu cuenta es de tipo 'Gold' y esta función está limitada para cuentas con un nivel de acceso más alto."

    def alta_tarjeta_debito(self, transaccion):
        '''descripcion'''
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

    def alta_tarjeta_credito_visa(self, transaccion) -> str:
        razon = ""
        if self.limite_tarjeta_credito_visa > 0:
            razon = "Alta de tarjeta de crédito VISA aceptada"
            # se supone que la alta y extension de tarjetas en diferentes cuentas influyen en limite total del ciente (5)
            self.limite_tarjeta_credito_visa -= 1
            self.tarjetas_credito_visa[transaccion.cuentaNumero] = 1
        else:
            razon = "Has alcanzado el límite de tarjetas de crédito VISA permitidas."
        return razon

    def alta_tarjeta_credito_master(self, transaccion) -> str:
        razon = ""
        if self.limite_tarjeta_credito_mastercard > 0:
            razon = "Alta de tarjeta de crédito Mastercard aceptada"
            # se supone que la alta y extension de tarjetas en diferentes cuentas influyen en limite total del ciente (5)
            self.limite_tarjeta_credito_mastercard -= 1
            self.tarjetas_credito_mastercard[transaccion.cuentaNumero] = 1
        else:
            razon = "Has alcanzado el límite de tarjetas de crédito Mastercard permitidas."
        return razon

    def alta_tarjeta_credito_amex(self, transaccion):
        return "RAZON"

    def alta_chequera(self, transaccion) -> str:
        razon = ""
        if self.limite_chequeras > 0:
            cuenta_numero = transaccion.cuentaNumero
            if cuenta_numero in self.chequeras:
                razon = "Ya tienes una chequera para esta cuenta."
            self.chequeras[cuenta_numero] = 1
            self.limite_chequeras -= 1
            razon = "Alta de chequera aceptada"
        else:
            razon = "Has alcanzado el límite de chequeras permitidas."
        return razon

    def alta_caja_ahorros_pesos(self, transaccion) -> str:
        '''descripcion'''

    def alta_cuenta_inversion(self, transaccion) -> str:
        if self.cuenta_inversion:
            return "El cliente ya posee una cuenta inversion."
        else:
            return "La creacion de la cuenta de inversion es correcta."
