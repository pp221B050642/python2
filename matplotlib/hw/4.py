import matplotlib.pyplot as plt
import numpy as np

y = np.array([27.7, 24.6, 18.8, 9.2, 3.1, 16.5])
labels = ["India", "UK", "US", "South Korea", "Australia", "Germany"]
plt.title("Population Density Index")
myexplode = [0, 0, 0.2, 0, 0, 0]



plt.pie(y, labels = labels, explode = myexplode, shadow = True, autopct='%.1f%%', textprops=dict(color='black'))
plt.show()
