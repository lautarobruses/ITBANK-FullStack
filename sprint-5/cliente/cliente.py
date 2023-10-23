import services.funciones as fn

precio_dolar_oficial = fn.get_valor_dolar()

class Cliente:
    def __init__(self, numero, nombre, apellido, dni, transacciones, saldo_disponible_en_cuenta):
        self.numero = numero
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
        self.transacciones = transacciones
        self.saldo_disponible_en_cuenta = saldo_disponible_en_cuenta

    def retiro_efectivo_cajero_automatico(self, transaccion): 
        pass
    
    def retiro_efectivo_por_caja(self, transaccion):
        pass

    def comprar_en_cuotas_tarjeta_credito_visa(self, transaccion):
        pass

    def comprar_en_cuotas_tarjeta_credito_master(self, transaccion):
        pass

    def comprar_en_cuotas_tarjeta_credito_amex(self, transaccion):
        pass

    def comprar_tarjeta_credito_visa(self, transaccion):
        pass

    def comprar_tarjeta_credito_master(self, transaccion):
        pass

    def comprar_tarjeta_credito_amex(self, transaccion):
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
            return False # no tiene acceso a la cuenta de inversion 
        else: 
            self.cuenta_inversion = transaccion
            monto_plazo_fijo = self.calcular_monto_plazo_fijo(transaccion)
            transaccion.monto_plazo_fijo = monto_plazo_fijo
            return True
        



    def comprar_dolar(self, monto) -> bool:
        '''Compra una cantidad de dólares y devuelve el monto en pesos o False si la compra falla.'''
        if self.caja_ahorro_dolar:
            costo_en_pesos = self.calcular_monto_total(precio_dolar_oficial, monto)
            
            if costo_en_pesos > self.saldo_disponible_en_cuenta:
                return False  # No hay suficientes fondos en pesos para la compra de dólares

            return costo_en_pesos  # Devuelve el costo en pesos de la compra
        else:
            return False

    def vender_dolar(self, monto) -> bool:
        '''Vende una cantidad de dólares y devuelve el monto en pesos o False si la venta falla.'''
        if self.caja_ahorro_dolar:
            if monto > self.saldo_disponible_en_cuenta:
                return False  # No hay suficientes dólares para la venta
            
            monto_en_pesos = self.calcular_monto_total(precio_dolar_oficial, monto)
            
            return monto_en_pesos  # Devuelve el monto en pesos de la venta
        else:
            return False

    def transferencia_enviada_pesos(self, monto, cuenta_destino, es_transferencia_enviada=True):
        '''descripcion'''
        if monto > self.saldo_disponible_en_cuenta:
            return False
        
        monto_con_comision = fn.descontar_comision(monto, self.porcentaje_comision_envio)
        if cuenta_destino.transferencia_recibida_pesos(monto_con_comision, self):
            self.saldo_disponible_en_cuenta -= monto_con_comision
            return True
        
    def transferencia_enviada_dolares(self, monto, cuenta_destino, es_transferencia_enviada=True):
        '''descripcion'''
        if not self.caja_ahorro_dolar:
            return False # No se permita la transferencia en dolar
        
        if monto > self.saldo_disponible_en_cuenta:
            return False # No hay suficientes dolares para la transferencia
        
        monto_en_pesos = monto * precio_dolar_oficial
        monto_con_comision = fn.descontar_comision(monto_en_pesos, self.porcentaje_comision_envio)

        if cuenta_destino.transferencia_recibida_dolares(monto_con_comision, self):
            self.saldo_disponible_en_cuenta -= monto_con_comision
            return True

    def transferencia_recibida_pesos(self, monto, es_transferencia_enviada=False):
        '''descripcion'''
        monto_con_comision = fn.descontar_comision(monto, self.porcentaje_comision_recibo)
        self.saldo_disponible_en_cuenta += monto_con_comision
        return True

    def transferencia_recibida_dolares(self, monto, es_transferencia_enviada=False):
        '''descripcion'''
        if not self.caja_ahorro_dolar:
            return False  # No se permite la recepción de dólares

        # Realiza la recepción de la transferencia en dólares
        monto_en_pesos = monto * precio_dolar_oficial
        monto_con_comision = fn.descontar_comision(monto_en_pesos, self.porcentaje_comision_recibo)
        self.saldo_disponible_en_cuenta += monto_con_comision
        return True 