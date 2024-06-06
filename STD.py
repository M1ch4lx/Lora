from Lora import *
import math
import matplotlib.pyplot as plt
from Export import *


class STD:
    def __init__(self):
        pass

    def load(self, lora: Lora):
        def plot(x, y):
            plt.plot(x, y)
            plt.xlabel('X Axis')
            plt.ylabel('Y Axis')
            plt.show()

        lora.add_python_function(
            'plot', [ObjectType.ARRAY, ObjectType.ARRAY], plot)
