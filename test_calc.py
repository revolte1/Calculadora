import unittest
from calc import Calc

class TestStringMethods(unittest.TestCase):
    def setUp(self):
        self.calc = Calc()
    
    def test_suma(self):
        self.assertEqual(4, self.calc.sumar(2,2))
        self.assertEqual(13, self.calc.sumar(1,12))
        self.assertEqual(1100, self.calc.sumar(100,1000))
        self.assertEqual(0, self.calc.sumar(0,0))
        self.assertEqual("Invalid", self.calc.sumar(1,-1))

    def test_resta(self):
        self.assertEqual(0, self.calc.restar(2,2))
        self.assertEqual(2, self.calc.restar(5,3))
        self.assertEqual(500, self.calc.restar(1000,500))
        self.assertEqual(0, self.calc.restar(0,0))
        self.assertEqual("Invalid", self.calc.restar(1,-2))
        self.assertEqual("Invalid", self.calc.restar(0,5))

    def test_multiplicacion(self):
        self.assertEqual(2, self.calc.multiplicar(2,1))
        self.assertEqual(64, self.calc.multiplicar(8,8))
        self.assertEqual(300, self.calc.multiplicar(3,100))
        self.assertEqual(0, self.calc.multiplicar(0,0))
        self.assertEqual("Invalid", self.calc.multiplicar(1,-2))

    def test_division(self):
        self.assertEqual(2, self.calc.dividir(2,1))
        self.assertEqual(1, self.calc.dividir(8,8))
        self.assertEqual(2, self.calc.dividir(100,50))
        self.assertEqual("Invalid", self.calc.dividir(0,0))
        self.assertEqual("Invalid", self.calc.dividir(2,-2))

     def test_exponencial(self):
        self.assertEqual(2, self.calc.exponente(2,1))
        self.assertEqual(64, self.calc.exponente(8,2))
        self.assertEqual(27, self.calc.exponente(3,3))
        self.assertEqual("Invalid", self.calc.exponente(0,0))
        self.assertEqual("Invalid", self.calc.exponente(2,-2))

if __name__ == '__main__':
    unittest.main()