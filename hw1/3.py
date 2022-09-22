n = int(input())

age = 0

for i in range(n):
    if i == 0 or i == 1:
        age += 10.5
    else:
        age += 4

print("The dog's age in dog's years is", int(age) )
