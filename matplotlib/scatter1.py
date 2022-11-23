import matplotlib.pyplot as plt
import random

x_water = [random.uniform(0, 0.3) for i in range(50)]
y_water = [random.uniform(0, 0.3) for i in range(50)]
plt.scatter(x_water, y_water, c='b', s=10)

x_tea = [random.uniform(0.3, 0.75) for i in range(100)]
y_tea = [random.uniform(0, 0.5) for i in range(100)]
plt.scatter(x_tea, y_tea, c='g', s=10)

x_coffee = [random.uniform(0.5, 1.2) for i in range(30)]
y_coffee = [random.uniform(0, 1) for i in range(30)]
plt.scatter(x_coffee, y_coffee, c='r', s=10)

plt.xlim(-0.1, 1.4)
plt.ylim(-0.1, 1.2)
plt.show()
