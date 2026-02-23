mass = [1,2,3]
l = len(mass)
result = [mass[:l//2 + l%2],mass[l//2 + l%2:]] if l else [[],[]]
print(result)


