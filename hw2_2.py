"""
Write a function that accepts another function as an argument. Then it
should return such a function, so the every call to initial one
should be cached.


def func(a, b):
    return (a ** b) ** 2


cache_func = cache(func)

some = 100, 200

val_1 = cache_func(*some)
val_2 = cache_func(*some)

assert val_1 is val_2

"""
from collections.abc import Callable
from functools import lru_cache


def cache(func: Callable) -> Callable:
    """
 we use the decorator @lru_cache (wraps the function with the arguments passed to it
and remembers the returned result corresponding to this argument). passing the internal function,
which takes a function as an argument. Then it returns a function that has cached every call of the initial
function cached.
    """

    @lru_cache#декоратор
    def inner(*args):
        return func(*args)#возвращаем функцию от аргумента

    return inner#возвращаем функцию


# for example
# passing a function with arguments a and b
def func(a, b):
    return (a ** b) ** 2


# decorating our function
cache_func = cache(func)#хэш значения

some = 15, 34

val_1 = cache_func(*some)#хэш 1 значения(15)
val_2 = cache_func(*some)#хэш 2 значения(34)

assert val_1 is val_2#проверка, что val_1 = val_2

print(val_1)
print(val_2)
