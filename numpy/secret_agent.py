#secret agent password

import numpy as np

letters = "abcdefghijklmnopqrstuvwxyz"
n = 1

alph = {}
for i in letters:
    alph[i]=n
    n+=1

def next_letter(s):
    t = ''
    for i in s:
        if ord(i)>=97 and ord(i)<122:
            i = chr(ord(i)+1)
        elif ord(i) == 122:
            i = 'a'
        t += i
    return t

message = input()

if len(message) != 9:
    print("BANG! BANG! BANG!")
else:
    for i in message:
        if i not in letters:
            print("BANG! BANG! BANG!")
            break
        else:
            part_1 = message[0:3]
            part_2= message[3:6]
            part_3 = message[-3:]
            part_1 = f"{alph[part_1[0]]}{part_1[1]}{alph[part_1[2]]}"
            part_2 = part_2[::-1]
            part_3 = next_letter(part_3)
            print(part_2+part_3+part_1)
    
    
    

