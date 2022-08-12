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
ax.plot(x + 4, y, color='blue', linestyle='-.', marker='o', label='y = x^2')
ax.plot(x / 3, y, c='pink', ls=':', marker='*', alpha=.5, lw = 2.5)  # color = c, linestyle = ls, linewidth
ax.plot(x + 1, y, color='red', linestyle='--')
ax.set_xticks(np.arange(-2, 11, 2))
ax.set_yticks(np.arange(-1, 5, 1))
ax.set_xlim(-2, 11)
ax.set_ylim(-1, 5)
ax.set_ylabel('axis Y')
ax.set_xlabel('axis X')
plt.legend(loc='best')
ax.grid(color='black', lw='0.5', ls='--', which='major')
plt.show()


# fig, axes = plt.subplots(1, 2)    #bar
# axes[0].bar([1, 2, 3, 4], [4, 2, 1, 5], color='black', label='vertical', alpha=1)
# axes[1].barh([0.5, 1, 2.5], [0, 1, 2], color='red', label='horizontal')
# axes[0].legend()
# axes[1].legend()
# plt.show()

# fig = plt.figure(figsize=(14,10)) #Stacked
# rect1 = plt.bar(np.arange(5), np.arange(5)**2,width = 0.3, color = 'red')
# rect2 = plt.bar(np.arange(5), np.arange(5)*2, width = 0.3, color = 'black')
# plt.legend((rect1[0], rect2[1]), ('support', 'freedom'))
# plt.grid(c='black')
# plt.show()

# fig, ax = plt.subplots() #hist boxplot
# np.random.seed(196868)
# mu, sigma = 100, 15
# x = mu + sigma * np.random.randn(10000)
# ax.hist(x, 50, density = True, facecolor = 'blue', alpha = 0.75)
# ax.grid(color= 'black')
# plt.show()

# fig, ax = plt.subplots() #area chart
# x = np.arange(0, 100, 1)
# y = x*2
# ax.fill_between(x,y,color = 'skyblue', alpha = 0.2)
# ax.plot(x,y, color = 'slateblue', alpha = 0.6)
# plt.show()
