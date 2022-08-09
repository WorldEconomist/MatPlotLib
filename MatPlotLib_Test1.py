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
ax.plot(x, y, color='black', linestyle = 'solid')
# ax.plot(x, x_abs)
ax.plot(x + 4, y, color='blue', linestyle='-.')
ax.plot(x / 3, y, color='g', linestyle=':')
ax.plot(x + 44, y, color='red', linestyle='--')
plt.show()
