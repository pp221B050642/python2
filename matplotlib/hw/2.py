import matplotlib.pyplot as plt
import numpy as np

x = np.array([0.03, 0.07, 0.05, 0.13, 0.15, 0.19, 0.24, 0.28, 0.29, 0.32, 0.36, 0.37, 0.39, 0.4, 0.43, 0.42, 0.47, 0.5, 0.52, 0.57, 0.6])
y = np.array([0.03, 0.1, 0.11, 0.12, 0.18, 0.17, 0.2, 0.23, 0.31, 0.29, 0.37, 0.41, 0.31, 0.39, 0.395, 0.48, 0.473, 0.57, 0.58, 0.5, 0.6])

plt.plot(x, y, 'o')

m, b = np.polyfit(x, y, 1)
plt.plot(x, m*x+b)
plt.show()