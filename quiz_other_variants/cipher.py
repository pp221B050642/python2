s = str(input())
coded = str(input())
number_of_chars = []
number_of_chars2 = []
for i in s:
    cnt = 0
    for j in s:
        if i == j:
            cnt+=1
    number_of_chars.append(cnt)
for i in coded:
    cnt = 0
    for j in coded:
        if i == j:
            cnt+=1
    number_of_chars2.append(cnt)
answer = True

number_of_chars.sort()
number_of_chars2.sort()
if number_of_chars2==number_of_chars:
    answer = True
else:
    answer = False

for i in range(len(s)):
    if s[i] == coded[i]:
        answer = False
if answer == True:
    print("yes")
else:
    print("no")