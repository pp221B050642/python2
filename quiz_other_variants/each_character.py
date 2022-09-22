s = str(input())

print(len(s))
characters = []

for i in s:
    cnt = 0
    for j in s:
        if i == j:
            cnt+=1
    print(cnt, i)