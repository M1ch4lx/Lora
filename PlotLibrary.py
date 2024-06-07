from Export import export
import matplotlib.pyplot as plt


@export
def plot(x: list, y: list):
    plt.plot(x, y)
    plt.xlabel('X Axis')
    plt.ylabel('Y Axis')
    plt.show()
