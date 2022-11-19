#f(10)=3
#f(50)=165
#f(100000)=?
import math

def median(a, b, c):
    m = (1/2)*math.sqrt(2*(b**2)+2*(a**2)-c**2)
    return m

n = int(input())
cnt=0
for c in range(1, n+1):
    for a in range(1, n):
        for b in range(1, n):
            if a+b>c and median(a, b, c) == int(median(a, b, c)) and a<=b<=c:
                # print(a, b, c, median(a, b, c))
                cnt+=1

print(cnt)
