import hw4.tasks.task_hw4_2
import pytest
import os

#If the first line of the file contains a number from the range [1,3)
@pytest.mark.parametrize(
    ["number"],
    [
        [1.1], [0], [2.6], [0.8]
    ]
)
def succes_test_read_magic_number(number):
    path = "file_read_magic_number"
    with open(path) as function:
        function.write(str(number))
    assert hw4.tasks.task_hw4_2.read_magic_number(path)
    os.remove(path)


#If the first line contains a number not from the range [1,3) or non-numeric values
@pytest.mark.parametrize(
    ["value"],
    [
        ["number"], [7], ["abc"], [0.8], [-4]
    ]
)
def unsucces_test_read_magic_number(value):
    path = "file_read_magic_number"
    with open(path) as function:
        function.write(str(number))
    try:
        hw4.tasks.task_hw4_2.read_magic_number(path)
        assert False
    except ValueError:
        assert True
    os.remove(path)