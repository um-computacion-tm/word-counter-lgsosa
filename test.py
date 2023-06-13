from contarpalabras import contar_palabras
from parameterized import parameterized, parameterized_class
import unittest

class TestContarPalabras(unittest.TestCase):
    @parameterized.expand([
        ("Hola mundo", {"hola":1, "mundo":1}),
        ("Me llamo Alma", {"me":1, "llamo":1, "alma": 1}),
        ("La casa de la mama", {"la":2, "casa":1, "de": 1, "mama":1}),
        ("Tres tristes tigres tragaban trigo en un trigal, en un trigal, tres tristes tigres tragaban trigo", {"tres":2, "tristes":2, "tigres": 2, "tragaban":2, "trigo":2, "en":2, "un":2, "trigal":2}),
        ("Pablito clavó un clavito en la calva de un calvito. En la calva de un calvito, un clavito clavó Pablito. Pablito clavó un clavito",
        {"pablito":3, "clavó":3, "un":5, "clavito":3, "en":2, "la":2,"calva":2, "de":2, "calvito":2})
    ])
    def test(self, sentence, nro_palabras):
        self.assertEqual(contar_palabras(sentence),nro_palabras)

if __name__ == '__main__':
    unittest.main()