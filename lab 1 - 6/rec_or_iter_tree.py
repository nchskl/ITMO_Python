from pprint import pprint
from collections import deque
from typing import Callable, Dict, List
import timeit
import matplotlib.pyplot as plt


class RecBin:
    @staticmethod
    def left(root):
        return root + 1

    @staticmethod
    def right(root):
        return root - 1

    @staticmethod
    def GetBinTree(root=13, height=3, l_b=None, r_b=None):
        if l_b is None:
            l_b = RecBin.left
        if r_b is None:
            r_b = RecBin.right

        if not (isinstance(root, int) and isinstance(height, int) and callable(l_b) and callable(r_b)):
            return

        if height > 0:
            return {root: [
                RecBin.GetBinTree(l_b(root), height - 1, l_b, r_b),
                RecBin.GetBinTree(r_b(root), height - 1, l_b, r_b)
            ]}
        return {}


class NotRecTree:
    @staticmethod
    def get_bin_tree(
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


def benchmark(func, n, number=100, repeat=3):
    """Возвращает минимальное время выполнения func(n)"""
    times = timeit.repeat(lambda: func(n), number=number, repeat=repeat)
    return min(times)


def main():
    test_data = list(range(2, 15))  # уровни деревьев
    res_recursive = []
    res_iterative = []

    for n in test_data:
        res_recursive.append(benchmark(lambda h=n: RecBin.GetBinTree(13, h), n))
        res_iterative.append(benchmark(lambda h=n: NotRecTree.get_bin_tree(h, 13), n))

    # Визуализация
    plt.plot(test_data, res_recursive, label="Рекурсивный")
    plt.plot(test_data, res_iterative, label="Итеративный")
    plt.xlabel("Высота дерева")
    plt.ylabel("Время (сек)")
    plt.title("Сравнение рекурсивного и итеративного построения бинарного дерева")
    plt.legend()
    plt.show()


if __name__ == "__main__":
    main()
