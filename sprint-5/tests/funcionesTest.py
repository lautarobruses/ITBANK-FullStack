import unittest
import requests

import services.funciones as fn
from cliente.classic import Classic
from cliente.gold import Gold
from cliente.black import Black

URL = "https://dolarapi.com/v1/dolares/oficial"

class calcularMontoTotalTestCase(unittest.TestCase):
    def setUp(self):
        response = requests.get(URL)
        data = response.json()
        self.precio_dolar = data['venta']

        self.impuesto_pais, self.impuesto_ganancias = fn.get_impuestos()

        self.monto1 = 1000
        self.monto2 = 456.789
        self.montoMalo1 = -10
        self.montoMalo2 = "1000"

    def test_calcular_monto_entero(self):
        resultado = (self.precio_dolar * self.monto1) * \
            (1 + self.impuesto_pais + self.impuesto_ganancias)
        self.assertEqual(fn.calcular_monto_total(self.precio_dolar, self.monto1),
                         resultado, f"La funcion no devuelve el resultado esperado: {resultado}")

    def test_calcular_monto_flotante(self):
        resultado = (self.precio_dolar * self.monto2) * \
            (1 + self.impuesto_pais + self.impuesto_ganancias)
        self.assertEqual(fn.calcular_monto_total(self.precio_dolar, self.monto2),
                         resultado, f"La funcion no devuelve el resultado esperado: {resultado}")

    def test_calcular_monto_negativo(self):
        self.assertRaises(TypeError, fn.calcular_monto_total(
            self.precio_dolar, self.monto1), "La funcion deberia devolver una excepcion de tipo TypeError")

    def test_calcular_monto_cadena(self):
        self.assertRaises(TypeError, fn.calcular_monto_total(
            self.precio_dolar, self.monto1), "La funcion deberia devolver una excepcion de tipo TypeError")

    def test_calcula_impuestos_correctos(self):
        resultado1 = (self.precio_dolar * self.monto1) * \
            (1 + self.impuesto_pais + self.impuesto_ganancias)
        resultado2 = (self.precio_dolar * self.monto2) * \
            (1 + self.impuesto_pais + self.impuesto_ganancias)
        self.assertAlmostEqual(fn.calcular_monto_total(self.precio_dolar, self.monto1), resultado1,
                               f"La funcion no aplica correctamente el impuestos pais ({self.impuesto_pais}) y ganancias: {self.impuesto_ganancias}")
        self.assertAlmostEqual(fn.calcular_monto_total(self.precio_dolar, self.monto2), resultado2,
                               f"La funcion no aplica correctamente el impuestos pais ({self.impuesto_pais}) y ganancias: {self.impuesto_ganancias}")

class descontarComisionTestCase(unittest.TestCase):
    def setUp(self):
        self.clienteClassic = Classic("", "", "", "", "")
        self.clienteGold = Gold("", "", "", "", "")
        self.clienteBlack = Black("", "", "", "", "")

        self.porcentajeFicticio = 0.45

        self.porcentaje_comision_envio1 = self.clienteClassic.get_porcentaje_comision_envio()
        self.porcentaje_comision_envio2 = self.clienteGold.get_porcentaje_comision_envio()
        self.porcentaje_comision_envio3 = self.clienteBlack.get_porcentaje_comision_envio()

        self.porcentaje_comision_recibo1 = self.clienteClassic.get_porcentaje_comision_recibo()
        self.porcentaje_comision_recibo2 = self.clienteGold.get_porcentaje_comision_recibo()
        self.porcentaje_comision_recibo3 = self.clienteBlack.get_porcentaje_comision_recibo()

        self.monto = 456.789
        self.monto2 = 9999999999999999.23
        self.monto3 = 12.5555555555555
        self.montoMalo1 = -10
    
    def test_descontar_comision_correcto(self):
        resultado1 = self.monto - (self.monto * self.porcentajeFicticio) 
        resultado2 = self.monto2 - (self.monto2 * self.porcentajeFicticio) 
        resultado3 = self.monto3 - (self.monto3 * self.porcentajeFicticio) 

        self.assertEqual(resultado1, fn.descontar_comision(
            self.monto, self.porcentajeFicticio), f"La funcion no devuelve el resultado esperado: {resultado1}")
        self.assertEqual(resultado2, fn.descontar_comision(
            self.monto2, self.porcentajeFicticio), f"La funcion no devuelve el resultado esperado: {resultado2}")
        self.assertEqual(resultado3, fn.descontar_comision(
            self.monto3, self.porcentajeFicticio), f"La funcion no devuelve el resultado esperado: {resultado3}")

    def test_descontar_comision_envio(self):
        resultado1 = self.monto * (1 - self.porcentaje_comision_envio1)
        resultado2 = self.monto * (1 - self.porcentaje_comision_envio2)
        resultado3 = self.monto * (1 - self.porcentaje_comision_envio3)
        self.assertEqual(resultado1, fn.descontar_comision(
            self.monto, self.porcentaje_comision_envio1), f"La funcion no devuelve el resultado esperado: {resultado1}")
        self.assertEqual(resultado2, fn.descontar_comision(
            self.monto, self.porcentaje_comision_envio2), f"La funcion no devuelve el resultado esperado: {resultado2}")
        self.assertEqual(resultado3, fn.descontar_comision(
            self.monto, self.porcentaje_comision_envio3), f"La funcion no devuelve el resultado esperado: {resultado3}")

    def test_descontar_comision_recibo(self):
        resultado1 = self.monto * (1 - self.porcentaje_comision_recibo1)
        resultado2 = self.monto * (1 - self.porcentaje_comision_recibo2)
        resultado3 = self.monto * (1 - self.porcentaje_comision_recibo3)
        self.assertEqual(resultado1, fn.descontar_comision(
            self.monto, self.porcentaje_comision_recibo1), f"La funcion no devuelve el resultado esperado: {resultado1}")
        self.assertEqual(resultado2, fn.descontar_comision(
            self.monto, self.porcentaje_comision_recibo2), f"La funcion no devuelve el resultado esperado: {resultado2}")
        self.assertEqual(resultado3, fn.descontar_comision(
            self.monto, self.porcentaje_comision_recibo3), f"La funcion no devuelve el resultado esperado: {resultado3}")

    def test_descontar_comision_monto_negativo(self):
        self.assertRaises(TypeError, fn.descontar_comision(
            self.montoMalo1, self.porcentajeFicticio), "La funcion deberia devolver una excepcion de tipo TypeError")

class calcularMontoPlazoFijoTestCase(unittest.TestCase):
    def setUp(self):
        self.monto1 = 1000
        self.monto2 = 434.789
        self.monto3 = 1111111111111111.0
        self.monto4 = 33.7894444444
        self.montoMalo = -10

        self.tasa_interes_anual_ficticia1 = 30
        self.tasa_interes_anual_ficticia2 = 78.0

        self.anios1 = 2
        self.anios2 = 1.333

    def test_calcular_monto_correcto(self):
        resultado1 = self.monto1 * (1 + (self.tasa_interes_anual_ficticia1 / 100) * self.anios1)
        resultado2 = self.monto2 * (1 + (self.tasa_interes_anual_ficticia1 / 100) * self.anios1)
        resultado3 = self.monto3 * (1 + (self.tasa_interes_anual_ficticia1 / 100) * self.anios1)
        resultado4 = self.monto4 * (1 + (self.tasa_interes_anual_ficticia1 / 100) * self.anios1)

        self.assertEqual(resultado1, fn.calcular_monto_plazo_fijo(self.monto1, self.tasa_interes_anual_ficticia1, self.anios1),
                          f"La funcion no devuelve el resultado esperado: {resultado1}")
        self.assertEqual(resultado2, fn.calcular_monto_plazo_fijo(self.monto2, self.tasa_interes_anual_ficticia1, self.anios1),
                          f"La funcion no devuelve el resultado esperado: {resultado2}")
        self.assertEqual(resultado3, fn.calcular_monto_plazo_fijo(self.monto3, self.tasa_interes_anual_ficticia1, self.anios1),
                          f"La funcion no devuelve el resultado esperado: {resultado3}")
        self.assertEqual(resultado4, fn.calcular_monto_plazo_fijo(self.monto4, self.tasa_interes_anual_ficticia1, self.anios1),
                          f"La funcion no devuelve el resultado esperado: {resultado4}")

    def test_calcular_monto_negativo(self):
        self.assertRaises(TypeError, fn.calcular_monto_plazo_fijo(self.montoMalo, self.tasa_interes_anual_ficticia1, self.anios1),
                          "La funcion deberia devolver una excepcion de tipo TypeError")

    def test_calcular_plazo_fijo_tasa_interes(self):
        resultado1 = self.monto1 * (1 + (self.tasa_interes_anual_ficticia1 / 100) * self.anios1)
        resultado2 = self.monto4 * (1 + (self.tasa_interes_anual_ficticia2 / 100) * self.anios1)

        self.assertEqual(resultado1, fn.calcular_monto_plazo_fijo(self.monto1, self.tasa_interes_anual_ficticia1, self.anios1),
                          f"La funcion no devuelve el resultado esperado: {resultado1}")
        self.assertEqual(resultado2, fn.calcular_monto_plazo_fijo(self.monto4, self.tasa_interes_anual_ficticia2, self.anios1),
                          f"La funcion no devuelve el resultado esperado: {resultado2}")

    def test_calcular_plazo_fijo_anios(self):
        resultado1 = self.monto2 * (1 + (self.tasa_interes_anual_ficticia1 / 100) * self.anios1)
        resultado2 = self.monto3 * (1 + (self.tasa_interes_anual_ficticia2 / 100) * self.anios2)

        self.assertEqual(resultado1, fn.calcular_monto_plazo_fijo(self.monto2, self.tasa_interes_anual_ficticia1, self.anios1),
                          f"La funcion no devuelve el resultado esperado: {resultado1}")
        self.assertEqual(resultado2, fn.calcular_monto_plazo_fijo(self.monto3, self.tasa_interes_anual_ficticia2, self.anios2),
                          f"La funcion no devuelve el resultado esperado: {resultado2}")
    
if __name__ == '__main__':
    unittest.main()
