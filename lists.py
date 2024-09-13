
# /Matrix is a two-dimensional list

# zeros: list[int] = list(range(21))
# chars: list[str] = list("A list")
# print(len(chars))


letters = ["a", "b", "c", "d"]

# ADD
letters.append("e") # adds at the end of the list
letters.insert(0, "3")  # inserts an element at a specific position

# REMOVE
letters.pop() # pop method removes elements from the end of the list
letters.remove("c") # remove method removes a specific element
letters.clear() # clear method clears a given list
del letters[0:3] # del method removes elements by index and it can also remove a range of elements
print(letters)