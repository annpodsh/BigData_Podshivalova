importstring

import HW3.hw3_1 as task1

import random

N = 2
range_of_values = 10
A = []
B = []
for i in range(0, N):
    A.append(random.randint(-range_of_values, range_of_values))
    B.append(random.randint(-range_of_values, range_of_values))

def test_task1():
    result = task1.cache_func(A[0], B[1])
    assert result != None, "Result is None"
    assert type(result) != str, "Result isn't a number"
    assert (A[0] ** B[1]) ** 2 == result, "Function doesn't work correctly"