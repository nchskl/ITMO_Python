import unittest
from unittest import TestCase
from gunu_game import run_game as f


class GuessGameTest(TestCase):
    def test_1(self):
        self.assertEqual(f(1, 6, 3, 'b'), f'Число: 3\nПотрачено попыток: 1')
    def test_2(self):
        self.assertEqual(f(1, 4, 8, 'i'), 'Нужное число не найдено')
    def test_3(self):
        self.assertEqual(f(-23, -4, 8, 'b'), 'Нужное число не найдено')
    def test_4(self):
        self.assertEqual(f('abc', 1, 3, 'b'), 'Введен неверный тип данных')
    def test_5(self):
        self.assertEqual(f(1, '1', 3, 'b'), 'Введен неверный тип данных')
    def test_6(self):
        self.assertEqual(f(6, 1, 'ee', 'b'), 'Введен неверный тип данных')
    def test_7(self):
        self.assertEqual(f(21, 1, 3, 12), 'Введен неверный тип данных')
    def test_8(self):
        self.assertEqual(f(1, 4, 3, 'c'), 'Указан неверный тип игры, укажите b или i')
    def test_9(self):
        self.assertEqual(f(100, 1, 50, 'i'), 'Введите корректный диапазон')
    def test_10(self):
        self.assertEqual(f(1, 4, 3, '🧠'), 'Указан неверный тип игры, укажите b или i')


if __name__ == '__main__':
    unittest.main()
