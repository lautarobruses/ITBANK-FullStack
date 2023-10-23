import requests

url = "https://dolarapi.com/v1/dolares/oficial"

response = requests.get(url)
data = response.json()
precio_dolar_oficial = data['venta']

impuesto_pais = 0.30
impuesto_ganancias = 0.35

def get_valor_dolar() -> float:
    return precio_dolar_oficial

def get_impuestos() -> float:
    return impuesto_pais, impuesto_ganancias

def calcular_monto_total(self, precio_dolar, monto) -> float:
    '''Calcula el monto total que se tiene que gastar sumando el impuesto país y ganancias.'''
    precio_dolar = precio_dolar_oficial
    
    # Monto sin impuestos
    monto_sin_impuestos = monto * precio_dolar

    # Monto con impuestos
    monto_total = monto_sin_impuestos * (1 + impuesto_pais + impuesto_ganancias)

    return monto_total

def descontar_comision(self, monto, porcentaje) -> float:
    '''Devulve el monto descontando la comisión.'''

    comision = monto * (porcentaje / 100)
    monto_descontado = monto - comision
    
    return monto_descontado

def calcular_monto_plazo_fijo(self, monto, tasa_interes_anual, anios):
    '''Devulve el monto según el interés que se indique.'''

    monto_final = monto * (1 + (tasa_interes_anual / 100) * anios)

    return monto_final