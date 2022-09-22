number = int(input())
digits = []
for i in range(1, 6):
    d = number%10
    digits.append(int(d))
    number = number/10
answer = 0
for i in range(len(digits)):
    if i%2==1:
        answer += digits[i]*(10**(i))*2
    else:    
        answer += digits[i]*(10**(i))

print(answer)

