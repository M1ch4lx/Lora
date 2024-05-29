from Object import *


class Marshal:
    def lora_to_python(self, o: Object):
        if o.type == ObjectType.FLOAT or o.type == ObjectType.INT:
            return o.value
        if o.type == ObjectType.BOOLEAN:
            return o.value
        if o.type == ObjectType.TUPLE or o.type == ObjectType.ARRAY:
            return [self.lora_to_python(el) for el in o.value]
        if o.type == ObjectType.CALLBACK:
            return o.value.python_callback
        raise Exception(f'Cannot convert provided type to python object: {o.type.name}')

    def python_to_lora(self, value):
        if isinstance(value, float):
            return Number(ObjectType.FLOAT, value)
        if isinstance(value, int):
            return Number(ObjectType.FLOAT, value)
        if isinstance(value, tuple):
            return Tuple([self.python_to_lora(el) for el in value])
        if isinstance(value, bool):
            return Boolean(value)
        if isinstance(value, list):
            return Array([self.python_to_lora(el) for el in value])
        raise Exception(f'Cannot convert provided type to lora object: {type(value)}')
