import random

l = []

for i in range(100, 1000):
    if i %5 == 0:
        l.append(i)

print(random.choice(l))
