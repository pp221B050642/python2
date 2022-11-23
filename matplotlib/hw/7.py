import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
fig = plt.figure()
ax = fig.add_subplot(projection='3d')
x1 = np.random.randint(45,size=(5))
y1 = np.random.randint(26, size=(5))
z1 = np.random.randint(49, size=(5))

plt.show()

