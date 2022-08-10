import numpy as np
import matplotlib.pyplot as plt

fig, ax = plt.subplots()
# figure = plt.figure()
# ax1 = figure.add_subplot (2, 2, 1)
# ax2 = figure.add_subplot (2, 2, 2)
# ax3 = figure.add_subplot (2, 2, 3)
x = np.array([-3, -2, -1, 0, 1, 2, 3])
y = np.array([9, 4, 1, 0, 1, 4, 9])
# x_abs = [3, 2, 1, 0, 1, 2, 3]
ax.plot(x, y, color='black', linestyle='solid')
# ax.plot(x, x_abs)
ax.plot(x + 4, y, color='blue', linestyle='-.', marker='o', label = 'y = x^2')
ax.plot(x / 3, y, c='pink', ls=':', marker='*', alpha=0.5, lw=2.5)  # color = c, linestyle = ls, linewidth
ax.plot(x + 44, y, color='red', linestyle='--')
ax.set_xlim(-2, 11)
ax.set_ylim(-1,5)
ax.set_ylabel('axis Y')
ax.set_xlabel('axis X')
plt.legend(loc = 'best')
plt.show()
