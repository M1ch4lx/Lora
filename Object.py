from enum import Enum
from Function import Function


class ObjectType(Enum):
    NONE = 0,
    INT = 1,
    FLOAT = 2,
    BOOLEAN = 3
    STRING = 4,
    ARRAY = 5,
    TUPLE = 6,
    CALLBACK = 7,
    ANY = 8


class Object:
    def __init__(self):
        self.value = None
        self.type = ObjectType.NONE


class Callback(Object):
    def __init__(self, function: Function):
        super().__init__()
        self.value = function
        self.type = ObjectType.CALLBACK


class Tuple(Object):
    def __init__(self, values):
        super().__init__()
        self.value = values
        self.type = ObjectType.TUPLE

    def __str__(self):
        return f'({", ".join(str(obj) for obj in self.value)})'


class Boolean(Object):
    def __init__(self, value):
        super().__init__()
        self.type = ObjectType.BOOLEAN
        self.value = bool(value)

    def __str__(self):
        return str(self.value)


class Number(Object):
    def __init__(self, type, value):
        super().__init__()
        self.type = type
        self.value = value

    def __str__(self):
        return str(self.value)

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

