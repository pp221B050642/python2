step1 = list(input().split())
step2 = list(input().split())
step3 = list(input().split())
step4 = list(input().split())
l = [step1, step2, step3, step4]

x = 0
y = 0
for i in l:
    if i[0] == "up":
        y += int(i[1])
    elif i[0] == "down":
        y -= int(i[1])
    elif i[0] == "left":
        x -= int(i[1])
    elif i[0] == "right":
        x += int(i[1])

answer = round((x**2 + y**2)**(1/2))
print(answer)