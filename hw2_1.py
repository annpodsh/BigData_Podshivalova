"""
Write a function that takes K lists as arguments and returns all possible
lists of K items where the first element is from the first list,
the second is from the second and so one.

You may assume that that every list contain at least one element

Example:

assert combinations([1, 2], [3, 4]) == [
    [1, 3],
    [1, 4],
    [2, 3],
    [2, 4],
]
"""
from itertools import permutations
from typing import List, Any
import itertools


def combinations(*args: List[Any]) -> List[list]:
    a = []#пустой лист
    for i in itertools.product(*args):#перебираем декартово произведение входных итерируемых последовательностей
        a.append(i)#добавляем элемент
    return a#возвращаем лист


print(combinations([1, 4], [7, 2], [9, 3]))#вызываем функцию
