# Task: Write a function called is_palindrome that takes a string as input and returns
# True if the string is a palindrome (reads the same forwards and backwards) and False otherwise.
# Ignore spaces, punctuation, and capitalization.

def is_palindrome(s: str) -> bool:
    normalize_string: str = ''
    for char in s:
        if char.isalnum():
            normalize_string += char.lower()

    return normalize_string == normalize_string[:: -1]


print(is_palindrome("A man, a plan, a canal, Panama"))
