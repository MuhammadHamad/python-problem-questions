nested_loops = [[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11]]

for value in nested_loops:
    for sub_value in value:
        print(f"InnerLoop: {sub_value}")

    print(f"Outer loop: {value}")

print(f"Loop finished: {nested_loops}")

for i in range(2, 11):
    for j in range(1, 11):
        result = i * j
        print(f"{i} X {j} = {result}")
