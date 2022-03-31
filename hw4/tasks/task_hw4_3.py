"""
Write a function that will receive a string and write it to stderr
if line starts with "error" and to the stdout otherwise.


#>>> my_precious_logger("error: file not found")
'error: file not found'


#>>> my_precious_logger("OK")
# stdout
'OK'

Definition of done:
 - function is created
 - function is properly formatted
 - function has positive tests

You will learn:
 - how to write to stderr
 - how to test output to the stderr and stdout


"""
import sys

def my_precious_logger(text: str):
    if text.startswith("error"):
        sys.stderr.write(text) #if the string starts with "error", then we write it to the standard error descriptor
    else:
        sys.stdout.write(text) #otherwise, we write to the standard output descriptor