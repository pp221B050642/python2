#program which returns the indices
#where the monotonicity of a 1D array
#changes

l = list(str(input()).split())
l1 = []
for i in range(0, len(l)-1):

    if l[i]>l[i+1]:
        l1.append(i)

print(l1)        
     

