#Create a program that takes a list 
#and return the most frequently occuring 
#element contained within it.

list1 = list(str(input()).split())

d = {}
for i in list1:
    if i not in d:
        d[i] = 1
    else: d[i] += 1    
max = 1
for j in d.keys():
    if d[j] > max:
        max = d[j] 

for t in d.keys():
    if d[t] == max:
        print(t, end = " ")


