from Variable import *

class Context:
    def __init__(self):
        self.variables = {}
        self.loop_count = 0

    def find_variable(self, name) -> Variable:
        return self.variables.get(name)

    def create_variable(self, variable):
        self.variables[variable.name] = variable

    def variable_exists(self, name):
        return name in self.variables
