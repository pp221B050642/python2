import random

#10 characters
#2 uppercase, 1 digit, 1 special symbol

upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
lower = 'abcdefghijklmnopqrstuvwxyz'
number = '0123456789'
special_symbols = './,*-_=&%$#@!~^'

u = random.choices(upper, k=2)
n = list(random.choice(number))
ss = list(random.choice(special_symbols))

all_of_them = upper+lower+number+special_symbols
aof = random.choices(all_of_them, k = 6)

result = u+n+ss+aof

random.shuffle(result)

answer = ''
for i in result:
    answer += i

print(answer)