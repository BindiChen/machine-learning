import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation

def main():
    numframes = 100
    numpoints = 10
    color_data = np.random.random((numframes, numpoints))
    x, y, c = np.random.random((3, numpoints))

    fig = plt.figure()
    scat = plt.scatter(x, y, c=c, s=100)

    ani = animation.FuncAnimation(fig, update_plot, frames=100, interval=5,
                                  fargs=(color_data, scat))
    plt.show()

def update_plot(i, data, scat):
    print('----->', data[i])
    scat.set_array(data[i])
    return scat,

main()