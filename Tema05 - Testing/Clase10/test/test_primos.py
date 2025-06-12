import unittest
from modules.primo import es_primo

class TestPrimo(unittest.TestCase):

    def test_numeros_primos(self):
        self.assertTrue(es_primo(2))
        self.assertTrue(es_primo(3))
        self.assertTrue(es_primo(5))
        self.assertTrue(es_primo(7))

    def test_numeros_no_primos(self):
        self.assertFalse(es_primo(0))
        self.assertFalse(es_primo(4))
        self.assertFalse(es_primo(6))
        self.assertFalse(es_primo(8))
    
    def test_numeros_negativos(self):
        self.assertFalse(es_primo(-1))
        self.assertFalse(es_primo(-2))
        self.assertFalse(es_primo(-3))