from enum import Enum


class ObjectType(Enum):
    NONE = 0,
    INT = 1,
    FLOAT = 2,
    BOOLEAN = 3
    STRING = 4,
    ARRAY = 5


class Object:
    def __init__(self):
        self.value = None
        self.type = ObjectType.NONE


class Boolean(Object):
    def __init__(self, value):
        super().__init__()
        self.type = ObjectType.BOOLEAN
        self.value = bool(value)


class Number(Object):
    def __init__(self, type, value_str):
        super().__init__()
        self.type = type
        self.value = float(value_str)

    def __add__(self, other):
        return Number(self.type, self.value + other.value)

    def __sub__(self, other):
        return Number(self.type, self.value - other.value)

    def __mul__(self, other):
        return Number(self.type, self.value * other.value)

    def __truediv__(self, other):
        return Number(self.type, self.value / other.value)

    def __eq__(self, other):
        return self.value == other.value

    def __lt__(self, other):
        return self.value < other.value

    def __gt__(self, other):
        return self.value > other.value
