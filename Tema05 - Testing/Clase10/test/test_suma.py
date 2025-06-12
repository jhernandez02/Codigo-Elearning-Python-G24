import unittest

# Código a ser probado
def suma(a,b):
    return a + b

class TestSuma(unittest.TestCase):
    
    def test_suma(self):
        self.assertEqual(suma(2,2),4)
        self.assertEqual(suma(2,4),6)
        self.assertEqual(suma(6,3),9)

