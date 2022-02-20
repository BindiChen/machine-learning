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
x_data = []
y_data = []

for i in range(len(x)):
    x_data.append(x[i])
    y_data.append(y[i])

    x_train = np.array(x_data).reshape(-1, 1)
    y_train = np.array(y_data).reshape(-1, 1)
    reg.fit(x_train, y_train)

    plt.clf()
    plt.xlim(30, 250)
    plt.ylim(5, 50)
    plt.scatter(x_data, y_data, color='teal', edgecolors='black', label='Horsepower vs. Miles_per_Gallon')
    plt.plot(list(range(250)), reg.predict(np.array([entry for entry in range(250)]).reshape(-1, 1)), color='red', linewidth=2)
    plt.legend()
    plt.pause(0.001)

plt.show()


# reg = LinearRegression()
#
# x_data = []
# y_data = []
#
# for _ in range(1000):
#     x_data.append(random.randint(0, 100))
#     y_data.append(random.randint(0, 100))
#
#     x = np.array(x_data)
#     x = x.reshape(-1,1)
#     y = np.array(y_data)
#     y = y.reshape(-1, 1)
#     reg.fit(x, y)
#     plt.clf()
#     plt.xlim(0, 100)
#     plt.ylim(0,100)
#     plt.scatter(x_data, y_data, color='teal', edgecolors='black', label='Horsepower vs. Miles_per_Gallon')
#     plt.plot(list(range(100)), reg.predict(np.array([x for x in range(100)]).reshape(-1, 1)))
#     plt.pause(0.001)
#
# plt.show()