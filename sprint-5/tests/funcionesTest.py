import unittest
import requests

import services.funciones as fn
import cliente.classic as classic
import cliente.gold as gold
import cliente.black as black

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
        self.assertRaises(TypeError, fn.calcular_monto_total(self, self.precio_dolar, self.monto1), f"La funcion deberia devolver una excepcion de tipo TypeError")

    def test_calcular_monto_cadena(self):
        self.assertRaises(TypeError, fn.calcular_monto_total(self, self.precio_dolar, self.monto1), f"La funcion deberia devolver una excepcion de tipo TypeError")

    def test_calcula_impuestos_correctos(self):
        resultado1 = (self.precio_dolar * self.monto1) * (1 + self.impuesto_pais + self.impuesto_ganancias)
        resultado2 = (self.precio_dolar * self.monto2) * (1 + self.impuesto_pais + self.impuesto_ganancias)
        self.assertAlmostEqual(fn.calcular_monto_total(self, self.precio_dolar, self.monto1), resultado1, f"La funcion no aplica correctamente el impuestos pais ({self.impuesto_pais}) y ganancias: {self.impuesto_ganancias}")
        self.assertAlmostEqual(fn.calcular_monto_total(self, self.precio_dolar, self.monto2), resultado2, f"La funcion no aplica correctamente el impuestos pais ({self.impuesto_pais}) y ganancias: {self.impuesto_ganancias}")

class descontarComisionTestCase(unittest.TestCase):
    def setUp(self):
        self.clienteClassic = classic.Classic("", "", "", "", "")
        self.clienteGold = gold.Gold("", "", "", "", "")
        self.clienteBlack = black.Black("", "", "", "", "")

        self.porcentajeFicticio = 0.45

        self.monto = 456.789
        self.montoMalo1 = -10
        self.montoMalo2 = "1000"

    def test_descontar_comision_envio(self):
        self.porcentaje_comision_envio1 = self.clienteClassic.get_porcentaje_comision_envio()
        self.porcentaje_comision_envio2 = self.clienteGold.get_porcentaje_comision_envio()
        self.porcentaje_comision_envio3 = self.clienteBlack.get_porcentaje_comision_envio()

        resultado1 = self.monto * (1 - self.porcentaje_comision_envio1)
        resultado2 = self.monto * (1 - self.porcentaje_comision_envio2)
        resultado3 = self.monto * (1 - self.porcentaje_comision_envio3)
        self.assertAlmostEqual(resultado1, fn.descontar_comision(self, self.monto, self.porcentaje_comision_envio1), f"La funcion no devuelve el resultado esperado: {resultado1}")
        self.assertAlmostEqual(resultado2, fn.descontar_comision(self, self.monto, self.porcentaje_comision_envio2), f"La funcion no devuelve el resultado esperado: {resultado2}")
        self.assertAlmostEqual(resultado3, fn.descontar_comision(self, self.monto, self.porcentaje_comision_envio3), f"La funcion no devuelve el resultado esperado: {resultado3}")

    def test_descontar_comision_recibo(self):
        self.porcentaje_comision_recibo1 = self.clienteClassic.get_porcentaje_comision_recibo()
        self.porcentaje_comision_recibo2 = self.clienteGold.get_porcentaje_comision_recibo()
        self.porcentaje_comision_recibo3 = self.clienteBlack.get_porcentaje_comision_recibo()

        print(self.porcentaje_comision_recibo1)
        print(self.porcentaje_comision_recibo2)
        print(self.porcentaje_comision_recibo3)

        resultado1 = self.monto * (1 - self.porcentaje_comision_recibo1)
        resultado2 = self.monto * (1 - self.porcentaje_comision_recibo2)
        resultado3 = self.monto * (1 - self.porcentaje_comision_recibo3)
        self.assertAlmostEqual(resultado1, fn.descontar_comision(self, self.monto, self.porcentaje_comision_recibo1), f"La funcion no devuelve el resultado esperado: {resultado1}")
        self.assertAlmostEqual(resultado2, fn.descontar_comision(self, self.monto, self.porcentaje_comision_recibo2), f"La funcion no devuelve el resultado esperado: {resultado2}")
        self.assertAlmostEqual(resultado3, fn.descontar_comision(self, self.monto, self.porcentaje_comision_recibo3), f"La funcion no devuelve el resultado esperado: {resultado3}")

    def test_descontar_comision_monto_negativo(self):
        self.assertRaises(TypeError, fn.descontar_comision(self, self.montoMalo1, self.porcentajeFicticio), f"La funcion deberia devolver una excepcion de tipo TypeError")

    def test_descontar_comision_monto_cadena(self):
        self.assertRaises(TypeError, fn.descontar_comision(self, self.montoMalo2, self.porcentajeFicticio), f"La funcion deberia devolver una excepcion de tipo TypeError")

class calcularMontoPlazoFijoTestCase(unittest.TestCase):
    def test_another_thing(self):
        # Otra prueba que también utiliza el entorno de prueba configurado en 
        # fn.vender_dolar(self, )
        return
    
if __name__ == '__main__':
    unittest.main()