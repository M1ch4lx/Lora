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

    def create_copy(self):
        return copy.deepcopy(self)

    def __str__(self):
        print(self.variables)
