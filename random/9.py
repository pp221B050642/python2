#random string without repeating characters
import random

n = int(input())

s = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'
l = []

while(n!=0):
    i = random.choice(s)
    if i not in l:
        l.append(i)
        n -= 1

answer = '' 
for i in l:
    answer += i

print(answer)
