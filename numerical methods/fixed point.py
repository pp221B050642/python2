def f(x):
    return x**3 + 9*x - 6

def g1(x):
    return x**3+9*x-6

def g(x):
    return x-(x**3+9*x-6)/10

def derivative(x):
    return 3*x**2+11

def fixed_point_iteration(x0, e, N):
    step = 1
    number_of_iteration = True
    answer = True
    approx = 0
    if abs(derivative(x0))<1:
        while answer:
            x1 = g1(x0)
            print('Iteration-%d, x1 = %0.6f => f(x1) = %0.6f' % (step, x1, f(x1)))
    
            x0 = x1

            step = step + 1
            
            if step > N:
                number_of_iteration=False
                break
            
            answer = abs(f(x1)) > e
        if number_of_iteration==True:
            print(f'\nRoot: {x1}')
    else:
        while answer:
            x1 = g(x0)
            print('Iteration-%d, x1 = %0.6f => f(x1) = %0.6f' % (step, x1, f(x1)))
            if abs(x1-x0)<e:
                approx = step
                break
            x0 = x1

            step = step + 1
            
            if step > N:
                number_of_iteration=False
                break
            
            answer = abs(f(x1)) > e
        print(f'\nApproximation is at point {approx}')

x0 = float(input('p0: '))
e = float(input('Epsilon: '))
N = int(input('Max number of iterations: '))
print("\n")


fixed_point_iteration(x0,e,N)
