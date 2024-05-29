from Object import *


class Marshal:
    def python_to_lora(self, value):
        if isinstance(value, float):
            return Number(ObjectType.FLOAT, value)
        if isinstance(value, int):
            return Number(ObjectType.FLOAT, value)
        if isinstance(value, tuple):
            return Tuple([self.python_to_lora(el) for el in value])
        if isinstance(value, bool):
            return Boolean(value)
