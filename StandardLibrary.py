import math

from Export import export


@export('print')
def lora_print(arg):
    print(arg)


@export('enumerate')
def lora_enumerate(array: list):
    return list(enumerate(array))


@export('range')
def lora_range(start: int, stop: int):
    return list(range(start, stop))


@export
def sin(angle: float):
    return math.sin(angle)


@export('Array')
class ArrayPrototype:
    @export
    def size(array: list):
        return len(array)
