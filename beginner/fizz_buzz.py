""" 
!PARAMETERS are the inputs that you define for your functions
ARGUMENTS are the actual values that are passed to the function

Two types of functions
1- One that performs a task - performing a task means printing something
2- Other that returns value

Every function returns NONE by default
NONE is an object that represents the absence of a value
"""


def fizz_buzz(input: int):
    if (input % 3 == 0) and (input % 5 == 0):
        return "FizzBuzz"
    if input % 3 == 0:
        return "Fizz"
    if input % 5 == 0:
        return "Buzz"
    return input


print(fizz_buzz(30))
