class FunctionArgument:
    def __init__(self, index, name, type=None):
        self.name = name
        self.type = type
        self.index = index


def get_function_id(name):
    return name


class FunctionSignature:
    def __init__(self, name, args: list[FunctionArgument]):
        self.name = name
        self.args_count = len(args)
        self.args = args
        self.id = get_function_id(self.name)


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

