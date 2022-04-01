"""
Write a function that takes a number N as an input and returns N FizzBuzz numbers*
Write a doctest for that function.
Write a detailed instruction how to run doctests**.

That how first steps for the instruction may look like:
 - Install Python 3.8 (https://www.python.org/downloads/)
 - Install pytest `pip install pytest`
 - Clone the repository <path your repository>
 - Checkout branch <your branch>
 - Open terminal
 - ...

Definition of done:
 - function is created
 - function is properly formatted
 - function has doctests
 - instructions how to run doctest with the pytest are provided

You will learn:
 - the most common test task for developers
 - how to write doctests
 - how to run doctests
 - how to write instructions


Instruction:
- Install Python 3.8 (https://www.python.org/downloads/)
 - Install pytest `pip install pytest`
 - Clone the repository <path your repository>
 - Checkout branch <your branch>
 - Right-click on the doctest file
 - Click Run 'doctests in <filename>'

* https://en.wikipedia.org/wiki/Fizz_buzz
** Энциклопедия профессора Фортрана page 14, 15, "Робот Фортран, чисть картошку!"

"""
import doctest
from typing import List
import string



#in a list with a sequence of numbers from 1 to n+1, we make changes:
#divisible by 3, return the string 'Fizz';
#divisible by 5, return the string 'Buzz';
#divisible by both 3 and 5, return the string 'FizzBuzz';
#and if divisible by neither 3 nor 5, simply return x.




def fizzbuzz(n: int) -> List[str]:
    """
 >>> fizzbuzz(5)
 ['1', '2', 'fizz', '4', 'buzz']

 >>> fizzbuzz(8)
 ['1', '2', 'fizz', '4', 'buzz', 'fizz', '7', '8']

 >>> fizzbuzz(15)
 ['1', '2', 'fizz', '4', 'buzz', 'fizz', '7', '8', 'fizz', 'buzz', '11', 'fizz', '13', '14', 'fizzbuzz']

 :param n: numbers 1 to n
 :return: List[str] where each el % 3 == 0 = fizz and each el % 5 == 0 = buzz
    """
    list_fizzbuzz: List[str] = []
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            list_fizzbuzz.append("fizzbuzz")
        elif i % 3 == 0:
            list_fizzbuzz.append("fizz")
        elif i % 5 == 0:
            list_fizzbuzz.append("buzz")
        else:
            list_fizzbuzz.append(f"{i}")

    return list_fizzbuzz


if __name__ == '__main__':
    doctest.testmod()