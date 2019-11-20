import random

a = list(range(10))
b = random.sample(a,1)
print(b)
print(type(a))
a.pop(b[0])
print(a)
print(a.index(1))
