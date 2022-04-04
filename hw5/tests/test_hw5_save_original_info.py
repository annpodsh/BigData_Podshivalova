from BigData_Podshivalova.hw5.tasks.task_hw5_save_original_info import custom_sum
import pytest


"""
Checking the correct operation of the decorator, which saves information from
the original function (__name__ and __doc__) and saves the
original function itself in the __original_func attribute
"""


@pytest.mark.parametrize("a, b, c, expected_result", [(1, 10, 100, 111),
                                                      ([1, 2], [9, 3, 8], [5, 4, 7], [1, 2, 3, 4, 5, 7, 8, 9]),
                                                      ('Hello,', 'me dear', 'friend!', 'Hello, my dear friend!')])
def test_custom_sum(a, b, c, expected_result):
    assert custom_sum(a, b, c) == expected_result


def test_custom_sum_name():
    assert custom_sum.__name__ == 'custom_sum'


def test_custom_sum_doc():
    assert custom_sum.__doc__ == 'This function can sum any objects which have __add___'


def test_custom_sum_orig_func():
    assert str(custom_sum.__original_func)[:20] == '<function custom_sum'
