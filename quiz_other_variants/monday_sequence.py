answer = 1

def n_until_2n(n, N):
    global answer
    for i in range(n, 2*n+1):
        if N == 0:
            return answer
        answer *= i
        
    return answer + n_until_2n(2*n, N-1)


N = int(input())

print(n_until_2n(1, N))

    
    
    