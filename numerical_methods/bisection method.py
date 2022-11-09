def f(x):
    return x**3+10*x-5

def bisection(p0,p1,e):
    step = 1
    answer = True
    while answer:
        p2 = (p0 + p1)/2
        print('%d.  x2 = %0.6f => f(x2) = %0.6f' % (step, p2, f(p2)))

        if f(p0) * f(p2) < 0:
            p1 = p2
        else:
            p0 = p2
        
        step = step + 1
        answer = abs(f(p2)) > e

    print('\nRoot is : %0.8f' % p2)
    print(f"Approximation at step {step-1}")


p0 = float(input('p0: '))
p1 = float(input('p1: '))
e = float(input('Tolerance: '))


if f(p0) * f(p1) > 0.0:
    print('p0 and p1 do not have opposite signs')
    print('Input another p0 and p1')
else:
    bisection(p0,p1,e)
