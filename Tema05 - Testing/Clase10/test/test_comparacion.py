import unittest

class TestComparacion(unittest.TestCase):
    
    def test_greater(self):
        # assertGreater(a,b) => Verifica que "a" sea myor a "b"
        self.assertGreater(8,6)

    def test_greater_equal(self):
        # assertGreaterEqual(a,b) => Verifica que "a" sea myor o igual a "b"
        self.assertGreaterEqual(8,6)
        self.assertGreaterEqual(8,8)
    
    def test_less(self):
        # assertLess(a,b) => Verifica que "a" sea menor a "b"
        self.assertLess(6,8)
    
    def test_less_equal(self):
        # assertLessEqual(a,b) => Verifica que "a" sea menor o igual a "b"
        self.assertLessEqual(6,8)
        self.assertLessEqual(6,6)

    def test_count_equal(self):
        # assertCountEqual(a,b) => Verifica que "a" tenga los mismos elementos que "b"
        #                          con el mismo número de ocurrencias
        lista1 = [1,2,3,4]
        lista2 = [4,3,2,1]
        lista3 = [1,2,2,3]
        lista4 = [3,2,1,2]
        #self.assertEqual(lista1, lista2)
        self.assertCountEqual(lista1, lista2)
        self.assertCountEqual(lista3, lista4)

    
    