q, w, e = input().split()
a = int(q)
b = int(w)
c = int(e)

discriminant = b**2-4*a*c

if discriminant>=0:
    x1 = int((-b+discriminant*(1/2))/(2*a))
    x2 = int((-b-discriminant*(1/2))/(2*a))
    if x1 == x2:
        print(f"Solution: x = {x1}")
    else:
        print(f"Solution: x1 = {x1}, x2 = {x2}")
else:
    print("no roots")    