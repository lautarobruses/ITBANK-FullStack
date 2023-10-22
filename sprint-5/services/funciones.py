import requests

url = "https://dolarapi.com/v1/dolares/oficial"

response = requests.get(url)
data = response.json()
precio_dolar_oficial = data['venta']

def calcular_monto_total(self, precio_dolar, monto) -> float:
    precio_dolar = precio_dolar_oficial
    impuesto_pais = 0.30
    impuesto_ganancias = 0.35

    # Monto sin impuestos
    monto_sin_impuestos= monto * precio_dolar

    # Monto con impuesto país
    monto_con_impuesto_pais = monto_sin_impuestos + (monto_sin_impuestos * impuesto_pais)

    # Monto con impuesto a las ganancias

    monto_total = monto_con_impuesto_pais + (monto_con_impuesto_pais * impuesto_ganancias)


    return monto_total

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