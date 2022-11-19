import math

n = int(input())

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, 1 + math.floor(math.sqrt(n))):
        if n % i == 0:
            return False
    return True

def sum_of_squares(n):
    l = []
    for i in range(1, math.isqrt(n)+1):
        for j in range(1, math.isqrt(n)+1):
            if (i**2+j**2)==n:
                if i and j not in l:
                    l.append(i)
                    
    print(int(math.fsum(l)))

sum_of_squares(n)

prime = []
for i in range(n):
    if is_prime(i) and i%4==1:
        prime.append(i)

print(prime)


