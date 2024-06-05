from Object import *


class Marshal:
    def lora_to_python(self, o: Object):
        if o is None:
            return None
        if o.type == ObjectType.NUMBER:
            return o.value
        if o.type == ObjectType.BOOLEAN:
            return o.value
        if o.type == ObjectType.STRING:
            return o.value
        if o.type == ObjectType.TUPLE or o.type == ObjectType.ARRAY:
            return [self.lora_to_python(el) for el in o.value]
        if o.type == ObjectType.CALLBACK:
            return o.value
        raise Exception(f'Cannot convert provided type to python object: {o.type.name}')

    def python_to_lora(self, value):
        if value is None:
            return None
        if isinstance(value, str):
            return String(value)
        if isinstance(value, float):
            return Number(float(value))
        if isinstance(value, int):
            return Number(int(value))
        if isinstance(value, tuple):
            return Tuple([self.python_to_lora(el) for el in value])
        if isinstance(value, bool):
            return Boolean(value)
        if isinstance(value, list):
            return Array([self.python_to_lora(el) for el in value])
        raise Exception(f'Cannot convert provided type to lora object: {type(value)}')
