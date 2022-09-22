number = int(input())

a = number%10
number = int(number/10)
b = number%10
number = int(number/10)
c = number%10

if c>b or b>a:
    print("no")
else:
    print("yes")        