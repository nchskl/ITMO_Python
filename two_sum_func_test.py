import unittest
from two_sun_func import my_solution as f

class TestTwoSum(unittest.TestCase):
    def test_1(self):
        self.assertEqual(f.two_sum(self,[1, 2, 3, 4, 5], 6), (0, 4))
    def test_2(self):
        self.assertEqual(f.two_sum(self,[11, 15, 4, 2], 9), 'Подходящих пар чисел не найдено')
    def test_3(self):
        self.assertEqual(f.two_sum(self,[], 8), 'Переданный список не имеет два или более чисел')
    def test_4(self):
        self.assertEqual(f.two_sum(self,[1], 3), 'Переданный список не имеет два или более чисел')
    def test_5(self):
        self.assertEqual(f.two_sum(self,[1], 1), 'Переданный список не имеет два или более чисел')
    def test_6(self):
        self.assertEqual(f.two_sum(self,[1, 4, 5, 2, 1, 132], 0), 'Подходящих пар чисел не найдено')
    def test_7(self):
        self.assertEqual(f.two_sum(self,'sdsdsdvvvss', 32), 'Введенные данные некорректны')
    def test_8(self):
        self.assertEqual(f.two_sum(self,[1.23, 1, 3, 2.742], 3), 'Введенные данные некорректны')
    def test_9(self):
        self.assertEqual(f.two_sum(self,[1, 2, 3, 4, 5], 'dsds'), 'Введенные данные некорректны')


if __name__ == '__main__':
    unittest.main()