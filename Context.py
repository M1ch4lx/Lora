from Variable import *
import copy


class Context:
    BUILTIN_PROTOTYPES = {'Object', 'Number', 'Any', 'String', 'Array', 'Boolean', 'Callback', 'Tuple'}

    def __init__(self):
        self.variables = {}
        self.loop_count = 0

    def find_variable(self, name) -> Variable:
        return self.variables.get(name)

    def create_variable(self, variable):
        if variable.name in Context.BUILTIN_PROTOTYPES:
            raise Exception('Variable name is reserved')
        self.variables[variable.name] = variable

    def variable_exists(self, name):
        return name in self.variables

    def empty(self):
        return len(self.variables) == 0

    def create_copy(self):
        return copy.deepcopy(self)

    def __str__(self):
        if self.empty():
            return '{ }'
        return '{\n   ' + '\n   '.join(f'{key}: {val.object}' for key, val in self.variables.items()) + '\n}'
