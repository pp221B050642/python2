#numbers [0, 6] except 3 and 6

for i in range(0, 7):
    if i == 3 or i == 6:
        continue
    else:
        print(i, end = " ")