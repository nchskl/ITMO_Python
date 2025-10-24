from collections import deque
from typing import Callable, Dict, List
from pprint import pprint


"""
    Построение бинарного дерева без рекурсии.

    Функция создаёт бинарное дерево заданной высоты, начиная с корневого узла ``root``.
    Для вычисления значений левого и правого потомков используются переданные функции
    ``left_branch`` и ``right_branch``. Построение выполняется итеративно при помощи очереди.

    :param height: Высота дерева (минимальное значение — 1). Определяет количество уровней.
    :type height: int
    :param root: Значение корня дерева.
    :type root: int
    :param left_branch: Функция для вычисления значения левого потомка.
    :type left_branch: Callable[[int], int]
    :param right_branch: Функция для вычисления значения правого потомка.
    :type right_branch: Callable[[int], int]

    :return: Вложенный словарь, представляющий бинарное дерево.
             Каждый узел имеет вид ``{<значение узла>: [<левое поддерево>, <правое поддерево>]}``.
    :rtype: Dict[str, List[int]]

    :raises ValueError: Если ``height < 1``.
    """


def NotRecBinTree(
        height: int = 6,
        root: int = 15,
        left_branch: Callable[[int], int] = lambda x: x + 1,
        right_branch: Callable[[int], int] = lambda x: x - 1
) -> Dict[str, List[int]]:
    if height < 1:
        return {}

    tree = {str(root): []}
    queue = deque([(root, 1, tree[str(root)])])

    while queue:
        node, level, container = queue.popleft()

        if level < height:
            left_val = left_branch(node)
            right_val = right_branch(node)

            left_subtree = {str(left_val): []}
            right_subtree = {str(right_val): []}

            container.extend([left_subtree, right_subtree])

            queue.append((left_val, level + 1, left_subtree[str(left_val)]))
            queue.append((right_val, level + 1, right_subtree[str(right_val)]))

    return tree


if __name__ == "__main__":
    tree = NotRecBinTree(height=3, root=13)
    pprint(tree)
