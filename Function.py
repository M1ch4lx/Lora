from enum import Enum


class ObjectType(Enum):
    USER = 0
    NUMBER = 1
    BOOLEAN = 3
    STRING = 4
    ARRAY = 5
    TUPLE = 6
    CALLBACK = 7
    ANY = 8
    NATIVE = 9


def object_type_prototype(type):
    if type == ObjectType.NUMBER:
        return 'Number'
    if type == ObjectType.BOOLEAN:
        return 'Boolean'
    if type == ObjectType.STRING:
        return 'String'
    if type == ObjectType.ARRAY:
        return 'Array'
    if type == ObjectType.TUPLE:
        return 'Tuple'
    if type == ObjectType.CALLBACK:
        return 'Callback'
    return 'Any'


class FunctionArgument:
    def __init__(self, index, name, prototype='Any', type=ObjectType.ANY):
        self.name = name
        self.prototype = prototype
        self.index = index
        self.type = type


def get_function_id(name):
    return name


class FunctionSignature:
    def __init__(self, name, args: list[FunctionArgument]):
        self.name = name
        self.args_count = len(args)
        self.args: list[FunctionArgument] = args
        self.id = get_function_id(self.name)
        self.return_type = 'Any'


class Function:
    def __init__(self, signature: FunctionSignature, is_python_function: bool, parser_context=None, python_callback=None):
        self.signature = signature
        self.parser_context = parser_context
        self.built_in = is_python_function
        self.python_callback = python_callback


class FunctionSet:
    def __init__(self):
        self.functions = {}

    def add_function(self, function):
        self.functions[function.signature.id] = function

    def function_exists(self, function_id):
        return function_id in self.functions

    def find_function(self, function_id) -> Function:
        return self.functions.get(function_id)

    def find_all_of_prototype(self, prototype) -> list[Function]:
        result = []
        for fun_id, function in self.functions.items():
            if fun_id.startswith(f'{prototype}:'):
                result.append(function)
        return result
