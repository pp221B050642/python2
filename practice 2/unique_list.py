#unique list

l = list(input().split())

l2 =[]
for i in l:
    if i not in l2:
        l2.append(i)

if l == l2:
    print("yes")
else:
    print("no")        
