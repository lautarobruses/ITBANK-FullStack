import unittest
import requests

import services.funciones as fn

url = "https://dolarapi.com/v1/dolares/oficial"
    
class calcularMontoTotalTestCase(unittest.TestCase):
    def setUp(self):
        response = requests.get(url)
        data = response.json()
        self.precio_dolar = data['venta']

        self.impuesto_pais, self.impuesto_ganancias = fn.get_impuestos()

        self.monto1 = 1000
        self.monto2 = 456.789
        self.montoMalo1 = -10
        self.montoMalo2 = "1000"

    def test_calcular_monto_entero(self):
        resultado = (self.precio_dolar * self.monto1) * (1 + self.impuesto_pais + self.impuesto_ganancias)
        self.assertEqual(fn.calcular_monto_total(self, self.precio_dolar, self.monto1), resultado, f"La funcion no devuelve el resultado esperado: {resultado}")

    def test_calcular_monto_flotante(self):
        resultado = (self.precio_dolar * self.monto2) * (1 + self.impuesto_pais + self.impuesto_ganancias)
        self.assertEqual(fn.calcular_monto_total(self, self.precio_dolar, self.monto2), resultado, f"La funcion no devuelve el resultado esperado: {resultado}")

    def test_calcular_monto_negativo(self):
        self.assertRaises(TypeError, fn.calcular_monto_total(self, self.precio_dolar, self.monto1), f"La funcion deberia devolver una excepcion de tipo Exception")

    def test_calcular_monto_cadena(self):
        self.assertRaises(TypeError, fn.calcular_monto_total(self, self.precio_dolar, self.monto1), f"La funcion deberia devolver una excepcion de tipo Exception")

    def test_calcula_impuestos_correctos(self):
        resultado1 = (self.precio_dolar * self.monto1) * (1 + self.impuesto_pais + self.impuesto_ganancias)
        resultado2 = (self.precio_dolar * self.monto2) * (1 + self.impuesto_pais + self.impuesto_ganancias)
        self.assertAlmostEqual(fn.calcular_monto_total(self, self.precio_dolar, self.monto1), resultado1, f"La funcion no aplica correctamente el impuestos pais ({self.impuesto_pais}) y ganancias: {self.impuesto_ganancias}")
        self.assertAlmostEqual(fn.calcular_monto_total(self, self.precio_dolar, self.monto2), resultado2, f"La funcion no aplica correctamente el impuestos pais ({self.impuesto_pais}) y ganancias: {self.impuesto_ganancias}")

class descontarComisionTestCase(unittest.TestCase):
    def setUp(self):
        self.monto1 = 1000
        self.monto2 = 456.789
        self.montoMalo1 = -10
        self.montoMalo2 = "1000"

    def test_another_thing(self):
        fn.descontar_comision(self, )
        return

class calcularMontoPlazoFijoTestCase(unittest.TestCase):
    def test_another_thing(self):
        # Otra prueba que también utiliza el entorno de prueba configurado en 
        # fn.vender_dolar(self, )
        return
    
if __name__ == '__main__':
    unittest.main()