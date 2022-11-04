import random

alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'

l = random.choices(alphabet, k=5)
s = ''
for i in l:
    s+=i

print(s)