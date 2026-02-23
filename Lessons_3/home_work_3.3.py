mass = [1,2,3,4,5,6,7]
l = len(mass)
result = [mass[:l//2 + l%2],mass[l//2 + l%2:]] if l else [[],[]]
print(result)


