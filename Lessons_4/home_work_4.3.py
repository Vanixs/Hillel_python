import random

original_list = [random.randint(1, 10) for i in range(random.randint(3, 10))]
result_list = [original_list[0], original_list[2], original_list[-2]]
print(original_list, "==" , result_list)