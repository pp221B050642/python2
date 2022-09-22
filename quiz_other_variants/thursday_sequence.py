def factorial(m):
    if m == 1:
        return 1
    return m*factorial(m-1)

answer = 0
def sequence(n):
    global answer
    if n == 1:
        answer = 1
    elif n == 2:
        answer = 2        
    else:
        for i in range(3, n+1):
            answer = 3
            answer += factorial(i*2*i)

n = int(input())
sequence(n)
print(answer)