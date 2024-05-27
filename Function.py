class FunctionArgument:
    def __init__(self, index, name, type):
        self.name = name
        self.type = type
        self.index = index


class FunctionSignature:
    def __init__(self, name, args):
        self.name = name
        self.args_count = len(args)
        self.args = args
        self.id = self.name + str(self.args_count)


class Function:
    def __init__(self, signature, is_built_in, parser_context):
        self.signature = signature
        self.parser_context = parser_context
        self.built_in = is_built_in


class FunctionsSet:
    def __init__(self):
        self.functions = {}

    def add_function(self, function):
        self.functions[function.signature.id] = function

    def function_exists(self, signature):
        return signature.id in self.functions

    def find_function(self, signature):
        return self.functions.get(signature.id)
