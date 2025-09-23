"""
Модуль реализует игру 'Угадай число' с двумя способами поиска:
бинарный поиск и инкрементальный (последовательный) поиск.

Содержит класс guess_game и функцию run_game для получения
строкового результата игры.
"""

class guess_game:
    """
    Класс для симуляции игры угадывания числа с использованием
    бинарного или последовательного поиска.
    """

    def __init__(self, num1, num2, item, typegame):
        """
        Инициализирует объект игры и запускает соответствующий
        алгоритм поиска.

        Args:
            num1 (int): Начальное число диапазона.
            num2 (int): Конечное число диапазона.
            item (int): Число, которое нужно найти.
            typegame (str): Тип игры ('b' — бинарный поиск, 'i' — последовательный).
        """
        self.output = ''
        if type(num1) != int or type(num2) != int or type(item) != int or type(typegame) != str:
            self.output = 'Введен неверный тип данных'
        elif num2 <= num1:
            self.output = 'Введите корректный диапазон'
        else:
            self.nlist = [x for x in range(num1, num2 + 1)]
            self.item = item
            if typegame == 'b':
                self.binary_search(self.nlist, self.item)
            elif typegame == 'i':
                self.increment_search(self.nlist, self.item)
            else:
                self.output = 'Указан неверный тип игры, укажите b или i'

    def binary_search(self, nlist, item):
        """
        Выполняет бинарный поиск числа в списке.

        Args:
            nlist (list): Список чисел для поиска.
            item (int): Число, которое нужно найти.
        """
        low = 0
        high = len(nlist) - 1
        counter = 0
        loops = False
        while low <= high:
            counter += 1
            mid = (low + high) // 2
            guess = nlist[mid]
            if guess == item:
                loops = True
                self.output = f'Число: {guess}\nПотрачено попыток: {counter}'
                break
            elif guess > item:
                high = mid - 1
            else:
                low = mid + 1
        if loops is False:
            self.output = 'Нужное число не найдено'

    def increment_search(self, nlist, item):
        """
        Выполняет последовательный поиск числа в списке.

        Args:
            nlist (list): Список чисел для поиска.
            item (int): Число, которое нужно найти.
        """
        counter = 0
        loops = False
        for i in nlist:
            counter += 1
            if i == item:
                loops = True
                self.output = f'Число: {item}\nПотрачено попыток: {counter}'
                break
        if loops is False:
            self.output = 'Нужное число не найдено'

    def __str__(self):
        # Возвращает результат игры в виде строки.
        return self.output


def run_game(num1, num2, item, typegame):
    # Функция-обёртка, возвращающая результат игры в виде строки.
    return str(guess_game(num1, num2, item, typegame))

