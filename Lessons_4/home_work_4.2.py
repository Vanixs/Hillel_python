cases = [[0, 1, 7, 2, 4, 8], [1, 3, 5], [6], []]

for lst in cases:
    print(sum(lst[::2]) * lst[-1] if lst else 0)