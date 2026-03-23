num = int(input())

while num > 9:
    result = 1
    for digit in str(num):
        result *= int(digit)
    num = result

print(num)