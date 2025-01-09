import re

def count_vowels(s: str) -> int:
    vowels = "aeiou"
    s = s.lower()
    return sum(1 for char in s if char in vowels)  # Count vowels


while True:
    input_string = input("Enter a string to check the number of vowels (or type 'quit' to exit): ")
    if input_string.lower() == "quit":
        break  # Exit the loop if the user types 'quit'

    # Remove non-alphabetic characters
    cleaned_string = re.sub(r'[^a-zA-Z]', '', input_string)

    if cleaned_string:  # Check if there's anything left after cleaning
        result = count_vowels(cleaned_string)
        print(f"The string has {result} vowels.")
    else:
        print("Invalid input. Please enter a valid string.")
