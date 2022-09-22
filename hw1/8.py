x, y, z = input().split()

if x == y and x == z:
    print("Equilateral triangle")
elif x != y and x!= z:
    print("Scalene triangle")
else:
    print("Isosceles triangle")        