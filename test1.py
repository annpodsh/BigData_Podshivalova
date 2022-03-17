from HW1.hw1_task_1 import check_sum_of_four
from HW1.hw1_task_2 import find_maximal_subarray_sum
import random

N = 10
range_of_values = 1000
A = []
B = []
C = []
D = []
for i in range(0, N):
    A.append(random.randint(-range_of_values, range_of_values))
    B.append(random.randint(-range_of_values, range_of_values))
    C.append(random.randint(-range_of_values, range_of_values))
    D.append(random.randint(-range_of_values, range_of_values))


def test_task1():
    result = check_sum_of_four(A, B, C, D)
    assert result != None, "Result is None"
    assert type(result) == type(1), "Result isn't number"
    assert result >= 0, "Result lower than zero"


n = random.randint(10, 100)
nums = []
k = random.randint(3, 10)
for i in range(0, n):
    nums.append(random.randint(-100, 100))


def test_task2():
    result = find_maximal_subarray_sum(nums, k)
    assert result != None, "Result is None"
    assert type(result) == type(1), "Result isn't number"
