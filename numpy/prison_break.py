import numpy as np

l = np.array([0, 1, 1, 1])  

cnt = 0
free = 1

if l[0]==0:
    print(cnt)
else:
    for i in range(len(l)):
        if l[i]==free:
            continue
        else:
            if free == 1:
                free = 0
            else:
                free=1
            cnt+=1
    print(cnt+1)
    