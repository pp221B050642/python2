import random

d = '0123456789'

s = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'

result1 = random.choices(s, k = 6)
result2 = random.choices(d, k = 4)

result = result1+result2
random.shuffle(result)

answer = ''

for i in result:
    answer += i

print(answer)