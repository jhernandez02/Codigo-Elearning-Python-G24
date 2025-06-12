import unittest

class TestUpDown(unittest.TestCase):

    def setUp(self):
        print('Ejecutamos setUp')
    
    def tearDown(self):
        print('Ejecutamos tearDown')
    
    def test_1(self):
        print('Test: test_1')
    
    def test_2(self):
        print('Test: test_2')
    