import numpy as np
import matplotlib.pyplot as plt

fig, axes = plt.subplots(2, 2)

x = [-3, -2, -1, 0, 1, 2, 3]
y = [9, 4, 1, 0, 1, 4, 9]

axes[1, 0].plot(x,y)
plt.show()