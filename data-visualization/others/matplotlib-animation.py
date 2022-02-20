import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 2*np.pi, 100)
y = np.sin(x)

# plt.plot(x, y)
# plt.show()

from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots()

line, = ax.plot([])

ax.set_xlim(0, 2 * np.pi)
ax.set_ylim(-1.1, 1.1)


def animate(frame):
    y = np.sin(x + 2 * np.pi * frame / 100)
    line.set_data((x, y))


anim = FuncAnimation(fig, animate, frames=100, interval=5)

plt.show()


# # Running animation
# x_data = []
# y_data = []
#
# for i in range(len(x)):
#     x_data.append(x[i])
#     y_data.append(y[i])
#
#     plt.clf()
#     plt.xlim(30, 250)
#     plt.ylim(5, 50)
#     plt.scatter(x_data, y_data, color='teal', edgecolors='black', label='Horsepower vs. Miles_per_Gallon')
#     plt.legend()
#     plt.pause(0.001)
#
# plt.show()
