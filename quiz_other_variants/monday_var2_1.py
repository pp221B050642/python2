x, y = input().split()
a, b = int(x), int(y)

c = int((a**2+b**2)**(1/2))
area = int(a*b/2)
perimeter = a+b+c

print(f"hypotenuse = {c}\narea = {area}\nperimeter = {perimeter}")