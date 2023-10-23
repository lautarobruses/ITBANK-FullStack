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

def descontar_comision(self, monto, es_transferencia_enviada=True):
    '''descripcion'''
    if es_transferencia_enviada:
        porcentaje = self.porcentaje_comision_envio
    else:
        porcentaje = self.porcentaje_comision_recibo

    comision = monto * (porcentaje / 100)
    monto_descontado = monto - comision
    
    return monto_descontado