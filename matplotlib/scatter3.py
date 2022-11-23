import matplotlib.pyplot as plt
import random

fig = plt.figure()
fig.suptitle("Bike Rentals at Different Temperatures By Seasons", fontsize=14, fontweight='bold')

fig.supxlabel('Normalized Temperature')
fig.supylabel('Count of Total Rental Bikes')
x = [random.uniform(0,0.6) for i in range(100)]
y = [random.randint(0, 8000) for i in range(100)]

ax1 = fig.add_subplot(2, 2, 1)
ax1.set_title("Spring", fontsize=10, fontweight='bold', c='g')
plt.scatter(x,y, c='g', s=5)

x = [random.uniform(0,0.6) for i in range(100)]
y = [random.randint(0, 8000) for i in range(100)]

ax2 = fig.add_subplot(2, 2, 2)
ax2.set_title("Summer", fontsize=10, fontweight='bold', c='orange')
plt.scatter(x,y, c='orange', s=5)

x = [random.uniform(0,0.6) for i in range(100)]
y = [random.randint(0, 8000) for i in range(100)]


ax3 = fig.add_subplot(2, 2, 3)
ax3.set_title("Autumn", fontsize=10, fontweight='bold', c='r')
plt.scatter(x,y, c='r', s=5)

x = [random.uniform(0,0.65) for i in range(500)]
y = [random.randint(0, 8000) for i in range(500)]


ax4 = fig.add_subplot(2, 2, 4)
ax4.set_title("Winter", fontsize=10, fontweight='bold', c='b')
plt.scatter(x,y, c='b', s=5)

for a in [ax1, ax2, ax3, ax4]:
    for label in (a.get_xticklabels() + a.get_yticklabels()):
        label.set_fontsize(6)

plt.show()