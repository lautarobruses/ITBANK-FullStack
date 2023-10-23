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

    def alta_cuenta_inversion():
        '''descripcion'''
        pass

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
        
        monto_con_comision = self.descontar_comision(monto)
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
        monto_con_comision = self.descontar_comision(monto_en_pesos)

        if cuenta_destino.transferencia_recibida_dolares(monto_con_comision, self):
            self.saldo_disponible_en_cuenta -= monto_con_comision
            return True

    def transferencia_recibida_pesos(self, monto, es_transferencia_enviada=False):
        '''descripcion'''
        monto_con_comision = self.descontar_comision(monto)
        self.saldo_disponible_en_cuenta += monto_con_comision
        return True

    def transferencia_recibida_dolares(self, monto, es_transferencia_enviada=False):
        '''descripcion'''
        if not self.caja_ahorro_dolar:
            return False  # No se permite la recepción de dólares

        # Realiza la recepción de la transferencia en dólares
        monto_en_pesos = monto * precio_dolar_oficial
        monto_con_comision = self.descontar_comision(monto_en_pesos)
        self.saldo_disponible_en_cuenta += monto_con_comision
        return True 