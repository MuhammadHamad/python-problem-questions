
# /Matrix is a two-dimensional list

# zeros: list[int] = list(range(21))
# chars: list[str] = list("A list")
# print(len(chars))


letters = ["a", "b", "c", "d"]

# *ADD
letters.append("e")  # adds at the end of the list
letters.insert(0, "3")  # inserts an element at a specific position

# !REMOVE
letters.pop()  # pop method removes elements from the end of the list
letters.remove("c")  # remove method removes a specific element
letters.clear()  # clear method clears a given list
# del method removes elements by index and it can also remove a range of elements
del letters[0:3]

# ? SORTING LISTS

numbers = [2, 54, 10, 15]
# numbers.sort(reverse=True)

# sorted function takes an iterable and returns a new list unlike the sort method which modifies the original list
new_list = sorted(numbers)
# print(numbers, new_list)

# sorting complex data structures
items = [
    ("Product1", 12),
    ("Product3", 5),
    ("Product4", 8),
    ("Product2", 15)
]


def sort_items(item):
    return item[0]

# items.sort(key=sort_items)


# lambda function: shorter and cleaner way of writing a function that we are only going to use once as an argument to another function
items.sort(key=lambda item: item[1])
print(items)
