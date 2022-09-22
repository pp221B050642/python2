a, b, c = input().split()
x, y, z = int(a), int(b), int(c)

if x+y == z or x+z == y or y+z == x:
    print("yes")
else:
    print("no")    