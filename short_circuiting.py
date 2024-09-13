a = 0
b = 10

# Without short-circuiting, this would raise a ZeroDivisionError.
# if a != 0 and b / a > 5:
#     print("Result:", b / a)
# else:
#     print("Avoided division by zero!")


# Simulating no short-circuiting by separating the conditions
# if a != 0:
#     if b / a > 5:  # This will raise ZeroDivisionError when a is 0
#         print("Result:", b / a)
#     else:
#         print("Avoided division by zero!")


# Force both evaluations (though it will raise an error when a is 0)
# cond1 = a != 0
# cond2 = b / a > 5  # This will raise ZeroDivisionError when a is 0

# if cond1 and cond2:
#     print("Result:", b / a)
# else:
#     print("Avoided division by zero!")


# Define a custom function to mimic behavior where short-circuiting does not apply.
def check_b_div_a():
    print("Evaluating b / a")
    # return b / a > 5  # This will raise a ZeroDivisionError if a == 0


# Force evaluation of both conditions
cond1 = a != 0
cond2 = check_b_div_a()  # This will execute even if cond1 is False

if cond1 and cond2:
    print("Both conditions are True")
else:
    print("One or both conditions are False")
