import hw4.tasks.task_hw4_5
#let n = 25
def test_fizzbuzz(n: int = 25):
    value = hw4.tasks.task_hw4_5.fizzbuzz(n)
    i = 1
    str = "" # An empty variable for recording list values
    while i <= 25:
        str = next(value) # When calling the next() function, the generator uses the given conditions.
        i += 1
    assert str == "fizz buzz" #Checking values equal to "fizz buzz"