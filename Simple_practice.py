import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0, 100)
y = x * 2
z = x ** 2

# fig = plt.figure()
fig, axes = plt.subplots(nrows=1, ncols=2)
# ax1 = fig.add_subplot(111)
# ax2 = fig.add_subplot(222)
axes[0].plot(x, y, ls='--', c='red', lw=2,)
axes[1].plot(x, z, ls='dotted', c='blue', lw=2)
# ax1.set_xlabel('Axis X')
# ax1.set_ylabel('Axis Y')
axes[0].set_xlabel('Axis X', fontsize=15)
axes[1].set_xlabel('Axis X', fontsize=15)
axes[0].set_ylabel('Axis Y', fontsize=15)
axes[1].set_ylabel('Axis Z', fontsize=15)
plt.suptitle('Random plots', fontsize=20, fontweight='bold')
axes[0].set_xticks(np.arange(0, 101, 25))
axes[1].set_xticks(np.arange(0, 101, 25))
# ax2.plot(x,y)
# ax2.set_xlabel('Axis X')
# ax2.set_ylabel('Axis Y')
plt.show()
