import copy
from enum import Enum
from Function import *
from Context import Context


class Object:
    def __init__(self):
        self.value = None
        self.type = ObjectType.USER
        self.context: Context = Context()
        self.prototype_name = 'Object'

    def additive_neutral_element(self):
        pass

    def multiplicative_neutral_element(self):
        pass

    def __str__(self):
        return str(self.context)

    def context_str_if_any(self):
        return '\n' + str(self.context) if not self.context.empty() else ''


class String(Object):
    def __init__(self, string):
        super().__init__()
        self.value = string
        self.type = ObjectType.STRING
        self.prototype_name = 'String'

    def __str__(self):
        return self.value + self.context_str_if_any()

    def __add__(self, other):
        return String(self.value + other.value)

    def __eq__(self, other):
        if other is None:
            return False
        return self.value == other.value


class Array(Object):
    def __init__(self, values):
        super().__init__()
        self.value = values
        self.type = ObjectType.ARRAY
        self.prototype_name = 'Array'

    def __str__(self):
        return f"[{', '.join(str(elem) for elem in self.value)}]" + self.context_str_if_any()

    def __getitem__(self, item):
        return self.value[item]

    def __setitem__(self, key, value):
        self.value[key] = value

    def __add__(self, other):
        return Array(self.value + other.value)


class Callback(Object):
    def __init__(self, function: Function):
        super().__init__()
        self.value = function
        self.type = ObjectType.CALLBACK
        self.prototype_name = 'Callback'

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
        self.prototype_name = 'Tuple'

    def __str__(self):
        return f'({", ".join(str(obj) for obj in self.value)})' + self.context_str_if_any()


class Boolean(Object):
    def __init__(self, value):
        super().__init__()
        self.type = ObjectType.BOOLEAN
        self.value = bool(value)
        self.prototype_name = 'Boolean'

    def __str__(self):
        return str(self.value) + self.context_str_if_any()

    def __bool__(self):
        return self.value

    def __eq__(self, other):
        if other is None:
            return False
        return self.value == other.value


class Number(Object):
    def __init__(self, value):
        super().__init__()
        self.type = ObjectType.NUMBER
        self.value = value
        self.prototype_name = 'Number'

    def additive_neutral_element(self):
        return Number(0)

    def multiplicative_neutral_element(self):
        return Number(1)

    def __str__(self):
        return str(self.value) + self.context_str_if_any()

    def __add__(self, other):
        return Number(self.value + other.value)

    def __sub__(self, other):
        return Number(self.value - other.value)

    def __mul__(self, other):
        return Number(self.value * other.value)

    def __truediv__(self, other):
        return Number(self.value / other.value)

    def __eq__(self, other):
        if other is None:
            return False
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
