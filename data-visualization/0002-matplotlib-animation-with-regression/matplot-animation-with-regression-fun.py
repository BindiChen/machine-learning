import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression
from vega_datasets import data
df = data.cars()


# Get the data
df.dropna(subset=['Horsepower', 'Miles_per_Gallon'], inplace=True)
x = df['Horsepower'].to_numpy().reshape(-1, 1)
y = df['Miles_per_Gallon'].to_numpy().reshape(-1, 1)

reg = LinearRegression()

# Running animation
# x_data = []
# y_data = []


from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots()

# line, = ax.plot([])
scatter = ax.scatter([], [])

ax.set_xlim(30, 250)
ax.set_ylim(5, 50)

def animate(frame):
    x_data = x[:frame+1]
    y_data = y[:frame+1]

    x_train = np.array(x_data).reshape(-1, 1)
    y_train = np.array(y_data).reshape(-1, 1)
    reg.fit(x_train, y_train)

    scatter.set_array(x_data, y_data)
    # line.set_data((list(range(250)), reg.predict(np.array([entry for entry in range(250)]).reshape(-1, 1))))
    # ax.scatter(x_data, y_data)
    # ax.plot(list(range(250)), reg.predict(np.array([entry for entry in range(250)]).reshape(-1, 1)))

anim = FuncAnimation(fig, animate, frames=250, interval=5)

plt.show()
