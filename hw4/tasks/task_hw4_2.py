"""
Write a function that gets file path as an argument.
Read the first line of the file.
If first line is a number return true if number in an interval [1, 3)*
and false otherwise.
In case of any error, a ValueError should be thrown.

Write a test for that function using pytest library.

Definition of done:
 - function is created
 - function is properly formatted
 - function has positive and negative tests
 - all temporary files are removed after test run

You will learn:
 - how to test Exceptional cases
 - how to clean up after tests
 - how to check if file exists**
 - how to handle*** and raise**** exceptions in test. Use sample from the documentation.

* https://en.wikipedia.org/wiki/Interval_(mathematics)#Terminology
** https://docs.python.org/3/library/os.path.html
*** https://docs.python.org/3/tutorial/errors.html#handling-exceptions
**** https://docs.python.org/3/tutorial/errors.html#raising-exceptions
"""

import os.path


def read_magic_number(path: str) -> bool:
    try:
        while os.path.exists(path): #The exists() function of the os.path module returns True if the path refers to an existing path in the file system
            with open(path) as function:
                lines = function.readlines()
                number = float(lines[0]) #line by line we read the file and select 1 line
                if 1 <= number < 3: #If first line is a number return true if number in an interval [1, 3)
                    return True
                else:
                    return False
    except ValueError as path: #handling a nonexistent path error
        print("ERROR IN VALUE:"+ path + "this path don't exist")

