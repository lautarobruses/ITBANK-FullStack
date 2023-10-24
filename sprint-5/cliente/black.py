from cliente.cliente import Cliente

class Black(Cliente):
    def __init__(self, numero, nombre, apellido, dni, transacciones):
        super().__init__(numero, nombre, apellido, dni, transacciones)
        self.cuenta_inversion = False
        self.limite_tarjeta_debito = 5
        self.tarjetas_debito = {}
        self.limite_tarjeta_credito_visa = 10
        self.limite_tarjeta_credito_mastercard = 10
        self.limite_tarjeta_credito_amex = 10
        self.tarjetas_credito_visa = {}
        self.tarjetas_credito_mastercard = {}
        self.tarjetas_credito_amex = {}
        self.chequeras = {}
        self.limite_chequeras = 2
        
    proximo_numero_cuenta = 100 
    limite_cuentas_corrientes = 3
    cuentas_corrientes = {}   
    cajas_ahorro = {}  
    limite_cajas_ahorro = 5 
    cargo_mensual_cajas_ahorro = 100 
     
    def get_porcentaje_comision_envio(self) -> float:
        return self.porcentaje_comision_envio

    def get_porcentaje_comision_recibo(self) -> float:
        return self.porcentaje_comision_recibo

    def retiro_efectivo_cajero_automatico(self, transaccion) -> str:
        '''Este metodo toma la transaccion de tipo:'retiro_efectivo_cajero_automatico' que el cliente black realizo y devuelve en un string la razon por las que fue aceptada o rechazada teniendo en cuenta que el límite diario de retiro es de $100,000 por cajero.'''
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
        '''Este metodo toma la transaccion de tipo:'retiro_efectivo_cajero_automatico' que el cliente black realizo y devuelve en un string la razon por las que fue aceptada o rechazada.'''

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
        '''Este metodo toma la transaccion de tipo:'comprar_en_cuotas_tarjeta_credito_visa' que el cliente black realizo y devuelve en un string la razon por las que fue aceptada o rechazada.'''

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
        '''Este metodo toma la transaccion de tipo:'comprar_en_cuotas_tarjeta_credito_master' que el cliente black realizo y devuelve en un string la razon por las que fue aceptada o rechazada.'''

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
        '''Este metodo toma la transaccion de tipo:'comprar_en_cuotas_tarjeta_credito_amex' que el cliente black realizo y devuelve en un string la razon por las que fue aceptada o rechazada.'''

        try:
            if transaccion.monto <= 0:
                return "Monto Inválido: El monto ingresado es un numero, pero debe ser mayor que cero."
            else:
                if transaccion.saldoDisponibleEnCuenta < transaccion.monto:
                    return f"Fondos Insuficientes: No es posible comprar en cuotas con tu tarjeta american express con el monto de {transaccion.monto}$ ya que excede tu saldo disponible de {transaccion.saldoDisponibleEnCuenta}$."
                else:
                    return "Retiro Exitoso: El monto con el que desea comprar en cuotas es un numero y ademas no supera tu saldo disponible."
        except:
            return "Formato Inválido: El monto debe ser un numero."

    def comprar_tarjeta_credito_visa(self, transaccion) -> str:
        '''Este metodo toma la transaccion de tipo:'comprar_tarjeta_credito_visa' que el cliente black realizo y devuelve en un string la razon por las que fue aceptada o rechazada.'''

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
        '''Este metodo toma la transaccion de tipo:'comprar_tarjeta_credito_master' que el cliente black realizo y devuelve en un string la razon por las que fue aceptada o rechazada.'''

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

    def comprar_tarjeta_credito_amex(self, transaccion) -> str:
        '''Este metodo toma la transaccion de tipo:'comprar_tarjeta_credito_amex' que el cliente black realizo y devuelve en un string la razon por las que fue aceptada o rechazada.'''

        try:
            if transaccion.monto <= 0:
                return "Monto Inválido: El monto ingresado es un numero, pero debe ser mayor que cero."
            else:
                if transaccion.saldoDisponibleEnCuenta < transaccion.monto:
                    return f"Fondos Insuficientes: No es posible comprar con tu tarjeta american express con el monto de {transaccion.monto}$ ya que excede tu saldo disponible de {transaccion.saldoDisponibleEnCuenta}$."
                else:
                    return "Retiro Exitoso: El monto con el que desea comprar en cuotas es un numero y ademas no supera tu saldo disponible."
        except:
            return "Formato Inválido: El monto debe ser un numero."

    def alta_tarjeta_debito(self, transaccion):
        '''descripcion'''
        razon = ""
        if transaccion.cuentaNumero is None:
            razon = "No se ha proporcionado el número de cuenta"
        elif self.limite_tarjeta_debito > 0:
            if transaccion.cuentaNumero in self.tarjetas_debito:
                # suponiendo que una tarjeta de debito por cuenta
                razon = "Alta de la tarjeta ya aceptada anteriormente"
            else:
                self.tarjetas_debito[transaccion.cuentaNumero] = 1
                self.limite_tarjeta_debito -= 1
                razon = "Alta de la tarjeta aceptada"
        else:
            razon = "Has alcanzado el límite de tarjetas de débito permitidas."
        return razon

    # se contemplan limite de 10 en tarjetas y extenciones de cada tipo
    def alta_tarjeta_credito_visa(self, transaccion):
        razon = ""
        if transaccion.cuentaNumero is None:
            razon = "No se ha proporcionado el número de cuenta"
        elif self.limite_tarjeta_credito_visa > 0:
            razon = "Alta de tarjeta de crédito VISA aceptada"
            self.limite_tarjeta_credito_visa -= 1
            self.tarjetas_credito_visa[transaccion.cuentaNumero] = 1
        else:
            razon = "Has alcanzado el límite de tarjetas de crédito VISA permitidas."
        return razon

    def alta_tarjeta_credito_master(self, transaccion):
        razon = ""
        if transaccion.cuentaNumero is None:
            razon = "No se ha proporcionado el número de cuenta"
        elif self.limite_tarjeta_credito_mastercard > 0:
            razon = "Alta de tarjeta de crédito Mastercard aceptada"
            self.limite_tarjeta_credito_mastercard -= 1
            self.tarjetas_credito_mastercard[transaccion.cuentaNumero] = 1
        else:
            razon = "Has alcanzado el límite de tarjetas de crédito Mastercard permitidas."
        return razon

    def alta_tarjeta_credito_amex(self, transaccion):
        razon = ""
        if transaccion.cuentaNumero is None:
            razon = "No se ha proporcionado el número de cuenta"
        elif self.limite_tarjeta_credito_amex > 0:
            razon = "Alta de tarjeta de crédito American Express aceptada"
            self.limite_tarjeta_credito_amex -= 1
            self.tarjetas_credito_amex[transaccion.cuentaNumero] = 1
        else:
            razon = "Has alcanzado el límite de tarjetas de crédito American Express permitidas."
        return razon

    def alta_chequera(self, transaccion) -> str:
        razon = ""
        if transaccion.cuentaNumero is None:
            razon = "No se ha proporcionado el número de cuenta"
        elif self.limite_chequeras > 0:
            cuenta_numero = transaccion.cuentaNumero
            if cuenta_numero in self.chequeras:
                razon = "Ya tienes una chequera para esta cuenta."
            self.chequeras[cuenta_numero] = 1
            self.limite_chequeras -= 1
            razon = "Alta de chequera aceptada"
        else:
            razon = "Has alcanzado el límite de chequeras permitidas."
        return razon
    
    def alta_cuenta_cte_pesos(self):
        razon = ""
        dni_cliente = self.dni

        if dni_cliente not in Black.cuentas_corrientes:
            Black.cuentas_corrientes[dni_cliente] = [Black.proximo_numero_cuenta]
            numero_cuenta = Black.proximo_numero_cuenta
            Black.proximo_numero_cuenta += 1
            razon = f"Alta de cuenta corriente en pesos aceptada. Número de cuenta: {numero_cuenta}"
        else:
            cuentas_creadas = Black.cuentas_corrientes[dni_cliente]
            if len(cuentas_creadas) < Black.limite_cuentas_corrientes:
                numero_cuenta = Black.proximo_numero_cuenta
                Black.proximo_numero_cuenta += 1
                cuentas_creadas.append(numero_cuenta)
                razon = f"Alta de cuenta corriente en pesos aceptada. Número de cuenta: {numero_cuenta}"
            else:
                razon = "Has superado el límite de cuentas corrientes."

        return razon

    def alta_cuenta_cte_dolares(self):
        razon = ""
        dni_cliente = self.dni

        if dni_cliente not in Black.cuentas_corrientes:
            Black.cuentas_corrientes[dni_cliente] = [Black.proximo_numero_cuenta]
            numero_cuenta = Black.proximo_numero_cuenta
            Black.proximo_numero_cuenta += 1
            razon = f"Alta de cuenta corriente en dólares aceptada. Número de cuenta: {numero_cuenta}"
        else:
            cuentas_creadas = Black.cuentas_corrientes[dni_cliente]
            if len(cuentas_creadas) < Black.limite_cuentas_corrientes:
                numero_cuenta = Black.proximo_numero_cuenta
                Black.proximo_numero_cuenta += 1
                cuentas_creadas.append(numero_cuenta)
                razon = f"Alta de cuenta corriente en dólares aceptada. Número de cuenta: {numero_cuenta}"
            else:
                razon = "Has superado el límite de cuentas corrientes."

        return razon


    def alta_caja_ahorro_pesos(self):
        razon = ""
        dni_cliente = self.dni

        if dni_cliente in Black.cajas_ahorro:
            cuentas_creadas = len(Black.cajas_ahorro[dni_cliente])
        else:
            cuentas_creadas = 0

        if cuentas_creadas < Black.limite_cajas_ahorro:
            numero_cuenta = Black.proximo_numero_cuenta_caja_ahorro
            Black.proximo_numero_cuenta_caja_ahorro += 1
            if dni_cliente not in Black.cajas_ahorro:
                Black.cajas_ahorro[dni_cliente] = [numero_cuenta]
            else:
                Black.cajas_ahorro[dni_cliente].append(numero_cuenta)
            if cuentas_creadas > 0:
                razon = f"Alta de caja de ahorro en pesos aceptada. Número de cuenta: {numero_cuenta}, Se aplicará un cargo mensual de ${Black.cargo_mensual_cajas_ahorro} a partir de la segunda cuenta."
            else:
                razon = f"Alta de caja de ahorro en pesos aceptada. Número de cuenta: {numero_cuenta}"
        else:
            razon = "Has superado el límite de caja de ahorro en pesos permitidas."

        return razon

    def alta_caja_ahorro_dolares(self):
        razon = ""
        dni_cliente = self.dni

        if dni_cliente in Black.cajas_ahorro:
            cuentas_creadas = len(Black.cajas_ahorro[dni_cliente])
        else:
            cuentas_creadas = 0

        if cuentas_creadas < Black.limite_cajas_ahorro:
            numero_cuenta = Black.proximo_numero_cuenta_caja_ahorro
            Black.proximo_numero_cuenta_caja_ahorro += 1
            if dni_cliente not in Black.cajas_ahorro:
                Black.cajas_ahorro[dni_cliente] = [numero_cuenta]
            else:
                Black.cajas_ahorro[dni_cliente].append(numero_cuenta)
            if cuentas_creadas > 0:
                razon = f"Alta de caja de ahorro en dólares aceptada. Número de cuenta: {numero_cuenta}, Se aplicará un cargo mensual de ${Black.cargo_mensual_cajas_ahorro} a partir de la segunda cuenta."
            else:
                razon = f"Alta de caja de ahorro en dólares aceptada. Número de cuenta: {numero_cuenta}"
        else:
            razon = "Has superado el límite de caja de ahorro en dólares permitidas."

        return razon
    
    def alta_cuenta_inversion(self, transaccion) -> str:
        if self.cuenta_inversion:
            return "El cliente ya posee una cuenta inversion."
        else:
            return "La creacion de la cuenta de inversion es correcta."
