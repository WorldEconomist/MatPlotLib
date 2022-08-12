import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# #
# # fig, axes = plt.subplots(2, 2)
# #
# # x = np.array([-3, -2, -1, 0, 1, 2, 3])
# # y = np.array([9, 4, 1, 0, 1, 4, 9])
# # axes[1, 0].plot(x, y, lw=0.5)
# # axes[1, 1].plot(x, y, label='idi nahuy')
# # axes[0, 0].plot(x + 4, y / 3, c='red', ls='-', label='y=x^2')
# # axes[0, 0].set_xlim(2, 0)
# # axes[1, 0].set_ylim(-5, 4)
# # axes[0, 1].set_title('Tut snizu nichego net', fontsize=20)
# # plt.legend(loc='lower left')
# # plt.show()
# fig, ax = plt.subplots()
N = 100
x = np.random.rand(N)
y = np.random.rand(N)
colors = np.random.rand(N)
area = (30 * np.random.rand(N)) ** 2
# ax.set_title("Starry sky", fontsize='40', c='green')
fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111, projection='3d')
ax.scatter(x, y, s=area, c=colors, alpha=1, marker='*', cmap='plasma')
ax.grid(c='black', lw='0.5', ls='--', which='major')
ax.set_title("Starry sky", fontsize='40', c='black', fontweight='bold')
plt.show()
