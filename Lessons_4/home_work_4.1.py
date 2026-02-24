numbers = [1, 0, 13, 0, 0, 0, 5]

non_zeros = [i for i in numbers if i != 0]
zeros_count = numbers.count(0)
result = non_zeros + [0] * zeros_count

print(result)