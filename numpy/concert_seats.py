import numpy as np
import math

l = np.matrix('[1, 2, 3, 2, 1, 1; 2, 4, 4, 3, 2, 2; 5, 5, 5, 10, 4, 4; 6, 6, 7, 6, 5, 5]')
m = np.matrix('[1, 2, 3, 2, 1, 1; 2, 4, 4, 3, 2, 2; 5, 5, 5, 5, 4, 4; 6, 6, 7, 6, 5, 5]')

l2 = l.transpose()
print(l2)

l3 = np.sort(l2)
print(l3)
a = np.asarray(l2)
b = np.asarray(l3)

if np.array_equal(a, b):
    print("true")
else:
    print("false")



      