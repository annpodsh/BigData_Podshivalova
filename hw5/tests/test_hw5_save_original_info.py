from hw5.tasks.task_hw5_save_original_info import decorator_info


"""
Checking the correct operation of the decorator, which saves information from
the original function (__name__ and __doc__) and saves the
original function itself in the __original_func attribute
"""


def test_decorator_info():
    def func_is(func):
        @decorator_info(original_func=func)
        def wrapper(*args, **kwargs):
            """
            Wrong example of decorator_info __doc__
            """
            return False

        return wrapper
    return func_is

    @func_is
    def correct_func(*args) -> bool:
        """Decorator_info with correct name __doc__"""
        return True

    assert correct_func.__original_func()
    assert correct_func.__name__ == "correct_func"
    assert correct_func.__doc__ == "Example of decorator_info with correct name __doc__"
