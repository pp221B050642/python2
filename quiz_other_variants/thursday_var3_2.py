number = int(input())

a = number%10
number = int(number/10)
b = number%10
number = int(number/10)
c = number%10
number = int(number/10)
d = number%10

if a+b*10 == d+c*10:
    print("Yes")
else: print("No")    