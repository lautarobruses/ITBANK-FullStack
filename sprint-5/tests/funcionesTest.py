import unittest
import requests

import services.funciones as fn

url = "https://dolarapi.com/v1/dolares/oficial"
    
class calcularMontoTotalTestCase(unittest.TestCase):
    def setUp(self):
        response = requests.get(url)
        data = response.json()
        self.precio_dolar = data['venta']

        self.monto1 = 1000
        self.monto2 = 456.789
        self.montoMalo1 = -10
        self.montoMalo2 = "1000"

    def test_calcular_monto_entero(self):
        resultado = self.precio_dolar * self.monto1
        self.assertEqual(fn.calcular_monto_total(self, self.precio_dolar, self.monto1), resultado, f"La funcion no devuelve el resultado esperado: {resultado}")

    def test_calcular_monto_flotante(self):
        resultado = self.precio_dolar * self.monto2
        self.assertEqual(fn.calcular_monto_total(self, self.precio_dolar, self.monto2), resultado, f"La funcion no devuelve el resultado esperado: {resultado}")

    def test_calcular_monto_negativo(self):
        self.assertRaises(TypeError, fn.calcular_monto_total(self, self.precio_dolar, self.monto1), f"La funcion deberia devolver una excepcion de tipo Exception")

    def test_calcular_monto_cadena(self):
        self.assertRaises(TypeError, fn.calcular_monto_total(self, self.precio_dolar, self.monto1), f"La funcion deberia devolver una excepcion de tipo Exception")

    def test_calcula_impuesto_pais(self):
        return

    def test_calcula_impuesto_ganancias(self):
        return
    
class descontarComisionTestCase(unittest.TestCase):
    def test_another_thing(self):
        # Otra prueba que también utiliza el entorno de prueba configurado en 
        # fn.comprar_dolar(self, )
        return

class calcularMontoPlazoFijoTestCase(unittest.TestCase):
    def test_another_thing(self):
        # Otra prueba que también utiliza el entorno de prueba configurado en 
        # fn.vender_dolar(self, )
        return
    
if __name__ == '__main__':
    unittest.main()