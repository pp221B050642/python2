#create a program that takes a list of numbers and return the number that's unique
#3 3 3 7 3 -> 7
#0 0 0 0.77 0 0 -> 0.77
#0 1 1 1 1 1 -> 0

l = input().split()
s = set(l)

for i in s:
    cnt = 0
    for j in l:
        if j == i :
            cnt += 1
    if cnt == 1 : print(i, end = " ")        
