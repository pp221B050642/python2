# from secret_agent import alph
import numpy as np

letters = "abcdefghijklmnopqrstuvwxyz"
n = 1

alph = {}
for i in letters:
    alph[i]=n
    n+=1

message = input()

part_2 = message[0:3]
part_3 = message[3:6]
part_1 = message[6:]

def previuos_letter(s):
    t = ''
    for i in s:
        if ord(i)>=97 and ord(i)<122:
            i = chr(ord(i)-1)
        elif ord(i) == 97:
            i = 'z'
        t += i
    return t

new_part_2 = part_2[::-1]
# print(new_part_2)
new_part_3 = previuos_letter(part_3)
# print(new_part_3)


first = ''
third = ''
second = ''
for i in range(len(part_1)):
    if part_1[i].isalpha():
        first+=part_1[0:i]
        second += part_1[i]
        third+=part_1[i+1:]

first = int(first)
third = int(third)

for i in alph.keys():
    if alph[i] == first:
        first = i
    elif alph[i] == third:
        third = i

new_part_1 = first+second+third
answer = new_part_1+new_part_2+new_part_3
print(answer)