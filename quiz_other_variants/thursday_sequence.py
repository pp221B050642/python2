def factorial(m):
    if m == 1:
        return 1
    return m*factorial(m-1)

answer = 3
def sequence(n):
    for i in range(3, n+1):
        global answer
        answer += factorial(i*2*i)

n = int(input())
sequence(n)
print(answer)