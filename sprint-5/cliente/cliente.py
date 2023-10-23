import services.funciones as fn

precio_dolar_oficial = fn.get_valor_dolar()

class Cliente:
    def __init__(self, numero, nombre, apellido, dni, transacciones):
        self.numero = numero
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
        self.transacciones = transacciones
        self.tasa_interes_anual = 0.30
        self.anios = 2

    def retiro_efectivo_cajero_automatico(self, transaccion) -> str: 
        pass
    
    def retiro_efectivo_por_caja(self, transaccion) -> str:
        pass

    def comprar_en_cuotas_tarjeta_credito_visa(self, transaccion) -> str:
        pass

    def comprar_en_cuotas_tarjeta_credito_master(self, transaccion) -> str:
        pass

    def comprar_en_cuotas_tarjeta_credito_amex(self, transaccion) -> str:
        pass

    def comprar_tarjeta_credito_visa(self, transaccion) -> str:
        pass

    def comprar_tarjeta_credito_master(self, transaccion) -> str:
        pass

    def comprar_tarjeta_credito_amex(self, transaccion) -> str:
        pass

    def alta_tarjeta_debito(self, transaccion) -> str:
        '''descripcion'''
        pass

    def alta_cuenta_credito_visa(self, transaccion) -> str:
        '''descripcion'''
        pass

    def alta_cuenta_credito_mastercard(self, transaccion) -> str:
        '''descripcion'''
        pass

    def alta_cuenta_credito_american(self, transaccion) -> str:
        '''descripcion'''
        pass

    def alta_caja_ahorros_pesos(self, transaccion) -> str:
        '''descripcion'''
        pass

    def alta_caja_ahorros_dolares(self, transaccion) -> str:
        '''descripcion'''
        self.caja_ahorro_dolar = True # Si es True, permite la compra y venta de dolares

    def alta_cuenta_inversion(self, transaccion) -> str:
        pass
        
    def comprar_dolar(self, transaccion) -> str:
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

    def vender_dolar(self, transaccion) -> str:
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

    def transferencia_enviada_pesos(self, transaccion) -> str:
        '''descripcion'''
        if transaccion.monto > transaccion.saldoDisponibleEnCuenta:
            razon = 'RECHAZADA, el monto proporcionado es mayor que tu saldo disponible '
            return razon
        
        monto_con_comision = fn.descontar_comision(transaccion.monto, self.porcentaje_comision_envio)
        if cuenta_destino.transferencia_recibida_pesos(monto_con_comision, self):
            transaccion.saldoDisponibleEnCuenta -= monto_con_comision
            razon2 = 'Aceptada, el saldo está disponible para ser enviado'
            return razon2
        
    def transferencia_enviada_dolares(self, transaccion) -> str:
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

    def transferencia_recibida_pesos(self, transaccion) -> str:
        '''descripcion'''
        monto_con_comision = fn.descontar_comision(transaccion.monto, self.porcentaje_comision_recibo)
        transaccion.saldoDisponibleEnCuenta += monto_con_comision
        razon = 'La transferencia fue exitosa.'
        return razon

    def transferencia_recibida_dolares(self, transaccion) -> str:
        '''descripcion'''
        if not self.caja_ahorro_dolar:
            razon = 'No se permite la recepción de dólares. No contas con caja de ahorro.'
            return razon  # No se permite la recepción de dólares

        # Realiza la recepción de la transferencia en dólares
        monto_en_pesos = transaccion.monto * precio_dolar_oficial
        monto_con_comision = fn.descontar_comision(monto_en_pesos, self.porcentaje_comision_recibo)
        transaccion.saldoDisponibleEnCuenta += monto_con_comision
        razon1 = 'Contás con caja de ahorro en dólares para recibir el dinero,'
        return razon1 