import BigData_Podshivalova.hw6.tasks.task_hw6_counter.py as Task
import pytest

user = Task.User()


def test_classname():
    assert user.__class__.__name__ == 'Counter'


def test_instances():
    assert user.counter == 1


def test_instances_get():
    _, _, _ = Task.User(), Task.User(), Task.User()
    assert user.counter == 4


def test_instances_reset():
    user.reset_instances_counter()
    assert user.counter == 0
