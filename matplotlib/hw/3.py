import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0, 15*np.pi, 0.1)   # start,stop,step
y = np.sin(x/10)
plt.plot(x, y, c='b')

x = np.arange(0, 15*np.pi, 0.1)   # start,stop,step
y = -np.sin(x/10)
plt.plot(x, y, c='g')

x = np.arange(0, 15*np.pi, 0.1)   # start,stop,step
y = np.cos(x/10)
plt.plot(x, y, c='orange')

x = np.arange(0, 15*np.pi, 0.1)   # start,stop,step
y = -np.cos(x/10)
plt.plot(x, y, c='r')

plt.xlim(0, 50)
plt.ylim(-1, 1)
plt.grid()
plt.show()