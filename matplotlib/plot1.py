import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-1, 1,num = 25)
y = np.array([i**2 for i in x])

plt.plot(x, y, label = 'parabola')

plt.show()
