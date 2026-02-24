cases = [[0, 1, 7, 2, 4, 8], [1, 3, 5], [6], []]

for list in cases:
    print(sum(list[::2]) * list[-1] if list else 0)