mass = [12, 3, 4, 10, 8]
if len(mass) > 1:
    last_element = mass.pop()
    mass.insert(0, last_element)
print(mass)
