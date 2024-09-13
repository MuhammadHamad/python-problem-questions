# Task: Write a function called count_vowels that takes a string as input
# and returns the total number of vowels(a, e, i, o, u) in that string. 
# The function should be case-insensitive and should ignore spaces and punctuation.


def count_vowels(s: str) -> int:
    # Define a set of vowels (both lowercase and uppercase)
    vowels: str = "aeiou"

    # Normalize the string to lowercase
    s = s.lower()

    # Initialize a counter for the vowels
    vowel_count: int = 0

    # Loop through each character in the string
    for char in s:
        if char in vowels:  # Check if the character is a vowel
            vowel_count += 1  # Increment the counter if it is a vowel

    return vowel_count  # Return the total count of vowels
