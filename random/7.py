import random

n = int(input())

c1 = random.randint(1, 6)
print(c1)

l = []

while(len(l)<4):
    i = random.randint(1, 6)
    if i == c1:
        l.append(i)

# for i in l:
#     print(i)

if n-len(l)-1>0:
    for i in l:
        print(i)
    for i in range(n-len(l)-1):
        i = random.randint(1 ,6)
        print(i)
elif (n-len(l)-1)<0:
    for i in range(n-1):
        print(l[i])
else:
    for i in l:
        print(i)

