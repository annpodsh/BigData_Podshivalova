import os
from hw7.homework7.task_04 import KeyValueStorage, storage
import pytest


def test_access_the_attributes():
    assert storage.name == 'kek'
    assert storage.last_name == 'top'
    assert storage.power == '9001'
    assert storage.song == 'shadilay'


def test_type_of_data():
    assert isinstance(storage.name, string)
    assert isinstance(storage.power, int)
    
