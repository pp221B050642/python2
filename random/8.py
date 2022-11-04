import random 
#random string of specific letters

n = int(input())
s = input()

answer = random.choices(s, k = n)

result = ''

for i in answer:
    result +=i

print(result)


