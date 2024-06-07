from Export import export
import matplotlib.pyplot as plt
import numpy as np


@export
def plot(x: list, y: list):
    plt.plot(x, y)
    plt.xlabel('X Axis')
    plt.ylabel('Y Axis')
    plt.show()


@export
def numpy_array(values: list):
    return np.array(values)

@export
def vector(values: list):
    return np.array(values)

@export
def matrix(values: list):
    return np.array(values)


@export(np.ndarray.__name__)
class NumpyArray:
    @export
    def to_list(array: np.ndarray):
        return array.tolist()
