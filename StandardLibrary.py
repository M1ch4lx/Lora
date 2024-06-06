from Lora import *
import math
import matplotlib.pyplot as plt
from Object import *

class StandardLibrary:
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

        lora.add_python_function(
            'print', [ObjectType.ANY], lambda arg: print(arg))

        lora.add_python_function(
            'enumerate', [ObjectType.ARRAY], lambda iterable: list(enumerate(iterable)))

        lora.add_python_function(
            'range', [ObjectType.NUMBER, ObjectType.NUMBER], lambda start, stop: list(range(start, stop)))

        lora.add_python_function(
            'sin', [ObjectType.NUMBER], lambda angle: math.sin(angle))

        lora.add_python_function(
            'size', [ObjectType.ARRAY], lambda array: len(array), prototype='Array')
