#replace letters with position in alphabet

s = str(input())

alphabet = "abcdefghijklmnopqrstuvwxyz"
Alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

d = {}
D = {}

number = 1

for i in alphabet:
    d[i] = str(number)
    number += 1

Number = 1
for i in Alphabet:
    D[i] = str(Number)
    Number += 1

for i in s:
    if i in alphabet:
        print(d[i], end = " ")
    elif i in Alphabet:
        print(D[i], end = " ")