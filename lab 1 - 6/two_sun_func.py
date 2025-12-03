class my_solution():
    def __init__(self):
        pass
    def test_data(self, nums, target):
        print(nums, target)
        if type(nums) != list:
            return 'error1'
        if type(target) != int:
            return 'error1'
        elif len(nums) <= 1:
            return 'error2'
        elif not all(type(x) == int for x in nums):
            return 'error1'
        return True

    def two_sum(self, nums, target):
        y = my_solution.test_data(my_solution(), nums=nums, target=target)
        if y == True:
            print('!')
            for i in nums:
                for j in nums:
                    if i + j == target and nums.index(i) != nums.index(j):
                        return nums.index(i), nums.index(j)
            return 'Подходящих пар чисел не найдено'
        elif y == 'error1':
            return 'Введенные данные некорректны'
        elif y == 'error2':
            return 'Переданный список не имеет два или более чисел'

x = my_solution()
print(x.two_sum(['abc'], 3))

#print(x.test_data(['abc', 3, 4, 5], 3))