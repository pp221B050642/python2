import matplotlib.pyplot as plt
import numpy as np

# print(y)
fig = plt.figure()

x = np.arange(-0.5, 1, 0.001)
x2 = np.arange(-0.5, 1, 0.001)
y2 = x
y = 3*x**2+11*x


plt.plot(x,y, 'b', label='g(x) = 3x^2+11x')
plt.plot(x2, y2, 'c', label = 'y=x')
plt.axhline(y = 0)
plt.axvline(x = 0)

plt.legend(loc='upper left')

plt.show()