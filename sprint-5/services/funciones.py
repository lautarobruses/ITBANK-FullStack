import requests

URL = "https://dolarapi.com/v1/dolares/oficial"

response = requests.get(URL)
data = response.json()
precio_dolar_oficial = data['venta']

impuesto_pais = 0.30
impuesto_ganancias = 0.35

def get_valor_dolar() -> float:
    return precio_dolar_oficial

def get_impuestos() -> float:
    return impuesto_pais, impuesto_ganancias

def calcular_monto_total(precio_dolar:float, monto:float) -> float:
    '''Calcula el monto total que se tiene que gastar sumando el impuesto país y ganancias.'''
    precio_dolar = precio_dolar_oficial

    # Monto sin impuestos
    monto_sin_impuestos = monto * precio_dolar

    # Monto con impuestos
    monto_total = monto_sin_impuestos * (1 + impuesto_pais + impuesto_ganancias)

    return monto_total

def descontar_comision(monto:float, porcentaje:float) -> float:
    '''Devulve el monto descontando la comisión.'''

    comision = monto * porcentaje
    monto_descontado = monto - comision

    return monto_descontado

def calcular_monto_plazo_fijo(monto:float, tasa_interes_anual:float, anios:float) -> float:
    '''Devulve el monto según el interés que se indique.'''

    monto_final = monto * (1 + (tasa_interes_anual / 100) * anios)

    return monto_final
