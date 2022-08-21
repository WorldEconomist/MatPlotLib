import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0, 100)
y = x * 2
z = x ** 2

fig = plt.figure()
ax1 = fig.add_subplot(111)
ax2 = fig.add_subplot(222)
ax1.plot(x,z)
ax1.set_xlabel('Axis X')
ax1.set_ylabel('Axis Y')


ax2.plot(x,y)
ax2.set_xlabel('Axis X')
ax2.set_ylabel('Axis Y')
plt.show()