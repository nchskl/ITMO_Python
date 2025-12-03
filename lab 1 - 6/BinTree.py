from pprint import pprint #функция для более красивого вывода, в коде программы не задействована
from collections.abc import Callable #для проверки, являются ли переданные значения функциями

#left - функция, задающая шаг для левой ветви бинарного дерева
def left(root):
    return root + 1

#right - функция, задающая шаг для правой ветви бинарного дерева
def right(root):
    return root - 1

'''функция реализует построение бинарного дерева
в нее передаются 4 параметра, root - значения корня, height - требуемая высота,
l_b и r_b функции с шагом для левой и правой ветви соответственно
дерево строится рекурсивным методов'''
def GetBinTree(root=13, height=3, l_b=left, r_b=right):
    lb_t = l_b(1)
    rb_t = r_b(1)
    if not (type(root) == int and type(height) == int and isinstance(l_b, Callable) and isinstance(r_b, Callable)):
        return 'Введен неверный тип данных'
    elif not(type(lb_t) == int and type(rb_t) == int):
        return 'Введен неверный тип данных'
    else:
        left_branch = l_b
        right_branch = r_b
        if height > 0: #проверка, нужны ли еще ветви дерева
            return {root: [GetBinTree(left_branch(root), height - 1),   
                           GetBinTree(right_branch(root), height - 1)]}
        return 'конечный узел'
