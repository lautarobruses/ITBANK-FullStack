import services.funciones as fn

precio_dolar_oficial = fn.get_valor_dolar()

class Cliente:
    def __init__(self, numero, nombre, apellido, dni, transacciones, saldo_disponible_en_cuenta, porcentaje_comision_envio, porcentaje_comision_recibo):
        self.numero = numero
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
        self.transacciones = transacciones
        self.saldo_disponible_en_cuenta = saldo_disponible_en_cuenta
        self.porcentaje_comision_envio = porcentaje_comision_envio
        self.porcentaje_comision_recibo = porcentaje_comision_recibo

    def retiro_efectivo_cajero_automatico():
        '''descripcion'''
        pass
    
    def retiro_efectivo_por_caja():
        '''descripcion'''
        pass

    def comprar_en_cuotas_tarjeta_credito_visa():
        '''descripcion'''
        pass

    def comprar_en_cuotas_tarjeta_credito_mastercard():
        '''descripcion'''
        pass

    def comprar_en_cuotas_tarjeta_credito_american():
        '''descripcion'''

    def comprar_tarjeta_credito_visa():
        '''descripcion'''
        pass

    def comprar_tarjeta_credito_mastercard():
        '''descripcion'''
        pass

    def comprar_tarjeta_credito_american():
        '''descripcion'''
        pass

    def alta_tarjeta_debito():
        '''descripcion'''
        pass

    def alta_cuenta_credito_visa():
        '''descripcion'''
        pass

    def alta_cuenta_credito_mastercard():
        '''descripcion'''
        pass

    def alta_cuenta_credito_american():
        '''descripcion'''
        pass

    def alta_caja_ahorros_pesos():
        '''descripcion'''
        pass

    def alta_caja_ahorros_dolares(self):
        '''descripcion'''
        self.caja_ahorro_dolar = True # Si es True, permite la compra y venta de dolares

    def calcular_monto_plazo_fijo(self, transaccion):

        monto_inicial = transaccion.monto

        tasa_interes_anual = transaccion.tasa_interes_anual
        tiempo_anios = transaccion.tiempo_anios
        monto_final = monto_inicial * (1 + (tasa_interes_anual / 100) * tiempo_anios)

        return monto_final

    def alta_cuenta_inversion(self, transaccion) -> bool:
        '''descripcion'''
        if transaccion.tipo == 'CLASSIC':
            razon = 'RECHAZADA La cuenta Classic no tiene permitido el acceso a las inversiones'
            return razon # no tiene acceso a la cuenta de inversion 
        else: 
            self.cuenta_inversion = transaccion
            monto_plazo_fijo = self.calcular_monto_plazo_fijo(transaccion)
            transaccion.monto_plazo_fijo = monto_plazo_fijo
            razon1 = 'Aceptada, tu cuenta cumple los requisitos para acceder a las inversiones'
            return razon1
        
        



    def comprar_dolar(self, transaccion) -> bool:
        '''Compra una cantidad de dólares y devuelve el monto en pesos o False si la compra falla.'''
        if self.caja_ahorro_dolar:
            costo_en_pesos = self.calcular_monto_total(precio_dolar_oficial, transaccion.monto)
            
            if costo_en_pesos > transaccion.saldoDisponibleEnCuenta:
                razon = 'RECHAZADA, no hay suficientes fondos para la compra' 
                return razon # No hay suficientes fondos en pesos para la compra de dólares
            razon1 = f'Aceptada, tus fondos: {costo_en_pesos} los tenes disponibles para la compra' 
            return razon1  # Devuelve el costo en pesos de la compra
        else:
            razon2 = 'RECHAZADA, No contas con una caja de ahorro en dólares'
            return razon2

    def vender_dolar(self, transaccion) -> bool:
        '''Vende una cantidad de dólares y devuelve el monto en pesos o False si la venta falla.'''
        if self.caja_ahorro_dolar:
            if transaccion.monto > transaccion.saldoDisponibleEnCuenta:
                razon = 'RECHAZADA, No hay suficientes dólares para la venta'
                return razon  # No hay suficientes dólares para la venta
            
            monto_en_pesos = self.calcular_monto_total(precio_dolar_oficial, transaccion.monto)
            razon1 = f'Aceptada, contas con : {monto_en_pesos} para la venta'
            return razon1 # Devuelve el monto en pesos de la venta
        else:
            razon2 = 'RECHAZADA, No contas con una caja de ahorro en dólares'
            return razon2

    def transferencia_enviada_pesos(self, transaccion, cuenta_destino, es_transferencia_enviada=True):
        '''descripcion'''
        if transaccion.monto > transaccion.saldoDisponibleEnCuenta:
            razon = 'RECHAZADA, el monto proporcionado es mayor que tu saldo disponible '
            return razon
        
        monto_con_comision = fn.descontar_comision(transaccion.monto, self.porcentaje_comision_envio)
        if cuenta_destino.transferencia_recibida_pesos(monto_con_comision, self):
            transaccion.saldoDisponibleEnCuenta -= monto_con_comision
            razon2 = 'Aceptada, el saldo está disponible para ser enviado'
            return razon2
        
    def transferencia_enviada_dolares(self, transaccion, cuenta_destino, es_transferencia_enviada=True):
        '''descripcion'''
        if not self.caja_ahorro_dolar:
            razon = 'RECHAZADA, No contas con una caja de ahorro en dólares'
            return razon # No se permita la transferencia en dolar
        
        if transaccion.monto > transaccion.saldoDisponibleEnCuenta:
            razon1 = 'REZHADA, El monto proporcionado es mayor que el saldo disponible'
            return razon1  # No hay suficientes dolares para la transferencia
        
        monto_en_pesos = transaccion.monto * precio_dolar_oficial
        monto_con_comision = fn.descontar_comision(monto_en_pesos, self.porcentaje_comision_envio)

        if cuenta_destino.transferencia_recibida_dolares(monto_con_comision, self):
            transaccion.saldoDisponibleEnCuenta -= monto_con_comision
            razon2 = 'Aceptada, contas con saldo disponible y cuenta de ahorro en dólares'
            return razon2

    def transferencia_recibida_pesos(self, transaccion, es_transferencia_enviada=False):
        '''descripcion'''
        monto_con_comision = fn.descontar_comision(transaccion.monto, self.porcentaje_comision_recibo)
        transaccion.saldoDisponibleEnCuenta += monto_con_comision
        razon = 'Aceptada, la transferencia fue exitosa.'
        return razon

    def transferencia_recibida_dolares(self, transaccion, es_transferencia_enviada=False):
        '''descripcion'''
        if not self.caja_ahorro_dolar:
            razon = 'Rechazada, No se permite la recepción de dólares. No contas con caja de ahorro.'
            return razon  # No se permite la recepción de dólares

        # Realiza la recepción de la transferencia en dólares
        monto_en_pesos = transaccion.monto * precio_dolar_oficial
        monto_con_comision = fn.descontar_comision(monto_en_pesos, self.porcentaje_comision_recibo)
        transaccion.saldoDisponibleEnCuenta += monto_con_comision
        razon1 = 'Aceptada, contás con caja de ahorro en dólares para recibir el dinero,'
        return razon1 