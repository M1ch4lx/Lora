class FunctionArgument:
    def __init__(self, index, name, type=None):
        self.name = name
        self.type = type
        self.index = index


def get_function_id(name, args_count):
    return name + str(args_count)


class FunctionSignature:
    def __init__(self, name, args: list[FunctionArgument]):
        self.name = name
        self.args_count = len(args)
        self.args = args
        self.id = get_function_id(self.name, self.args_count)


class Function:
    def __init__(self, signature: FunctionSignature, is_built_in: bool, code_block):
        self.signature = signature
        self.code_block = code_block
        self.built_in = is_built_in


class FunctionsSet:
    def __init__(self):
        self.functions = {}

    def add_function(self, function):
        self.functions[function.signature.id] = function

    def function_exists(self, function_id):
        return function_id in self.functions

    def find_function(self, function_id) -> Function:
        return self.functions.get(function_id)

