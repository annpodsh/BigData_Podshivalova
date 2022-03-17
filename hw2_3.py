"""
Some of the functions have a bit cumbersome behavior when we deal with
positional and keyword arguments.

Write a function that accept any iterable of unique values and then
it behaves as range function:


import string


assert = custom_range(string.ascii_lowercase, 'g') == ['a', 'b', 'c', 'd', 'e', 'f']
assert = custom_range(string.ascii_lowercase, 'g', 'p') == ['g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o']
assert = custom_range(string.ascii_lowercase, 'p', 'g', -2) == ['p', 'n', 'l', 'j', 'h']

"""
from typing import Any


def custom_range(mas: str, *args: Any):
    if len(args) == 1:#длина строки равна 1
        index = mas.index(args[0])
        if index == -1:
            return mas#возвращаем строку, если индекс = -1
        else:
            return mas[:index]
    elif len(args) == 2:#длина строки равна 2
        start_index = mas.index(args[0])#начальный индекс
        end_index = mas.index(args[1])#конечный индекс
        if start_index == -1 or end_index == -1:
            return mas#возвращаем строку, если начальный или конечный индекс = -1
        else:
            return mas[start_index:end_index]
    elif len(args) > 2:#длина строки больше 2
        start_index = mas.index(args[0])#начальный индекс
        end_index = mas.index(args[1])#конечный индекс
        if start_index == -1 or end_index == -1 or type(args[2]) == isinstance(args[2], int):
            return mas#возвращаем строку, если начальный или конечный индекс = -1 или args[2] является int
        else:
            return mas[start_index:end_index:args[2]]#возвращаем строку от start_index до end_index с шагом args[2]
    else:
        return mas#возвращаем строку


print(custom_range("abcdef", "a", "f", 2))