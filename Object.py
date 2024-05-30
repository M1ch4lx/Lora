import copy
from enum import Enum
from Function import Function
from Context import Context


class ObjectType(Enum):
    USER = 0,
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
        self.type = ObjectType.USER
        self.context: Context = Context()
        self.prototype_name = None


class Array(Object):
    def __init__(self, values):
        super().__init__()
        self.value = values
        self.type = ObjectType.ARRAY

    def __str__(self):
        return str(self.value)


class Callback(Object):
    def __init__(self, function: Function):
        super().__init__()
        self.value = function
        self.type = ObjectType.CALLBACK

    def __deepcopy__(self, memo):
        if id(self) in memo:
            return memo[id(self)]

        new_instance = self.__class__.__new__(self.__class__)
        memo[id(self)] = new_instance

        new_instance.value = self.value
        new_instance.type = self.type
        new_instance.context = copy.deepcopy(self.context)
        new_instance.prototype_name = self.prototype_name

        return new_instance


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

    def __bool__(self):
        return self.value


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

    def __ne__(self, other):
        return self.value != other.value

    def __lt__(self, other):
        return self.value < other.value

    def __le__(self, other):
        return self.value <= other.value

    def __gt__(self, other):
        return self.value > other.value

    def __ge__(self, other):
        return self.value >= other.value
