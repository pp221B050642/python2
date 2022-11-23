import matplotlib.pyplot as plt

figure, axes = plt.subplots()
circle1 = plt.Circle((125, 110), 10, fill=False)
circle2 = plt.Circle((125, 150), 50, fill=False)
circle3 = plt.Circle((125, 200), 100, fill=False)

axes.add_artist(circle1)
axes.add_artist(circle2)
axes.add_artist(circle3)
plt.xlim(0, 350)
plt.ylim(0, 350)
plt.show()