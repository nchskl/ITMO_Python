import unittest
from unittest import TestCase
from BinTree import GetBinTree as f


'''функция покрывает все случаи неверного ввода данных, написание большого кол-ва тестов не требуется'''

class TestBinTree(TestCase):
    def test_1(self):
        self.assertEqual(f([]), 'Введен неверный тип данных')
    def test_2(self):
        self.assertEqual(f(height='sada'), 'Введен неверный тип данных')
    def test_3(self):
        self.assertEqual(f(height=f()), 'Введен неверный тип данных')


if __name__ == '__main__':
    unittest.main()
        