# Problem Question: Title Case Converter

# !Write a function called `title_case` that takes a sentence as input and converts it to title case. In title case, the first letter of each word is capitalized, and all other letters are in lowercase. However, certain short words (e.g., "and", "the", "in", "of") should be in lowercase unless they are the first or last word of the sentence.

# *Example:
# ?- Input: `"the quick brown fox jumps over the lazy dog"`
# /- Output: `"The Quick Brown Fox Jumps Over the Lazy Dog"`

# //- Input: `"to be or not to be, that is the question"`
# - Output: `"To Be or Not to Be, That Is the Question"`

# ### Hints:
# 1. **String Splitting**: Use the `split()` method to break the sentence into individual words.
# 2. **Capitalization**: Use the `capitalize()` method or string slicing to capitalize the first letter of each word.
# 3. **Conditional Logic**: Implement logic to check if a word is one of the short words that should remain in lowercase.
# 4. **Joining Words**: After processing the words, use the `join()` method to combine them back into a single string with spaces.

# Feel free to implement the function based on these hints! Let me know if you have any questions or need further assistance.

# / Solution: 01
# def title_case(sentence: str) -> str:
#     # List of short words that should be in lowercase unless they are the first or last word
#     short_words: set[str] = {"and", "the", "in", "of", "to",
#                              "a", "an", "for", "but", "nor", "on", "be", "at", "by", "with"}

#     # Split the sentence into words
#     words: list[str] = sentence.split()

#     # Initialize an empty list to hold the title-cased words
#     title_cased_words: list[str] = []

#     # Iterate through the words and apply title case rules
#     for i, word in enumerate(words):
#         # Capitalize the first letter of the word
#         if i == 0 or i == len(words) - 1 or word.lower() not in short_words:
#             title_cased_words.append(word.capitalize())
#         else:
#             title_cased_words.append(word.lower())

#     # Join the words back into a single string and return
#     return ' '.join(title_cased_words)


# / Solution: 02

def title_case(sentence: str) -> str:
    # Define the short words that should remain lowercase
    short_words = "and the in of to a an for but nor on at by with"

    # Split the sentence into words
    words = sentence.split()
    print(range(len(words)))

    title_cased_sentence = ''  # initialize an empty string for the new sentence

    for i in range(len(words)):
        word = words[i]
        if (i == 0 or i == len(words) - 1 or word.lower() not in short_words):
            title_cased_sentence += word.capitalize() + " "
        else:
            title_cased_sentence += word.lower() + " "

    return title_cased_sentence.strip()


# Output: "The Quick Brown Fox Jumps Over the Lazy Dog"
print(title_case("the quick brown fox jumps over The lazy dog and"))
# Output: "To Be or Not to Be, That Is the Question"
print(title_case("and to be or not to be, that is the question"))
