import matplotlib.pyplot as plt
import numpy as np
def append_exact_num(l,s, n):
    for i in range(n):
        l.append(s)

x = []
append_exact_num(x, "mon", 25)
append_exact_num(x, 'tue', 48)
append_exact_num(x, 'wed', 75)
append_exact_num(x, 'thu', 10)
append_exact_num(x, 'fri', 18)
append_exact_num(x, 'sat', 65)
append_exact_num(x, 'sun', 28)


week_days = ['mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun']
num_bins = 7
colors = ['AliceBlue', 'Aquamarine', 'YellowGreen', 'BurlyWood', 'DarkMagenta', 'MediumPurple', 'PaleGreen']
# plt.title("Weekday Data")
fig, ax = plt.subplots()
cnts, values, bars = ax.hist(x, edgecolor='w', rwidth=0.5, bins=week_days)
ax.set_xticks(week_days)

for i, (cnt, value, bar) in enumerate(zip(cnts, values, bars)):
    bar.set_facecolor(colors[i % len(colors)])


# plt.hist(x, 7, color='blue', rwidth=0.5,  alpha = 0.5)
# plt.ylim(0, 80)
plt.show()