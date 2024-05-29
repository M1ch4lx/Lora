from Context import Context
from Function import *
from Operator import Operator
from Variable import *
from Object import *


class Lora:
    def __init__(self):
        self.functions_set: FunctionsSet = FunctionsSet()
        self.current_context: Context = Context()
        self.expression_stack: list = []

    def swap_context(self, new_context):
        current_context = self.current_context
        self.current_context = new_context
        return current_context

    def swap_expression_stack(self, new_expression_stack):
        current_expression_stack = self.expression_stack
        self.expression_stack = new_expression_stack
        return current_expression_stack

    def get_variable(self, name):
        return self.current_context.find_variable(name)

    def assign_variable(self, name, object):
        var = self.get_variable(name)
        if var is None:
            self.current_context.create_variable(Variable(name, object))
        else:
            var.object = object

        print(name + ': ' + object.type.name + ' = ' + str(object))

    def variable_exists(self, name):
        return self.current_context.variable_exists(name)

    def variable_value(self, name):
        return self.get_variable(name).object.value

    def variable_type(self, name):
        return self.get_variable(name).object.type

    def start_expression(self):
        self.expression_stack = []

    def add_operator(self, operator):
        self.expression_stack.append(operator)

    def add_value(self, operand):
        self.expression_stack.append(operand)

    def add_reference(self, name):
        var = self.get_variable(name)

        if var == None:
            raise Exception('Variable not found: ' + name)

        self.expression_stack.append(var)

    def next_operator(self):
        for i, e in reversed(list(enumerate(self.expression_stack))):
            if isinstance(e, Operator):
                return i, e
        return None

    def evaluate_next_operator(self):
        pair = self.next_operator()

        if pair is None:
            return False

        index, op = pair

        left_operand = self.expression_stack[index + 1]
        right_operand = self.expression_stack[index + 2]
        result = None

        if op == Operator.ADD:
            result = left_operand + right_operand
        if op == Operator.SUB:
            result = left_operand - right_operand
        if op == Operator.MUL:
            result = left_operand * right_operand
        if op == Operator.DIV:
            result = left_operand / right_operand
        if op == Operator.EQ:
            result = Boolean(left_operand == right_operand)

        for i in range(3):
            self.expression_stack.pop(index)

        self.expression_stack.insert(index, result)

        return True

    def is_expression_stack_empty(self):
        return len(self.expression_stack) == 0

    def expression_result(self):
        if len(self.expression_stack) == 0:
            raise Exception("There is no expression result")

        if not self.is_expression_evaluated():
            raise Exception("Expression not yet evaluated")

        return self.expression_stack[0]

    def dereference_variables(self):
        for i, elem in enumerate(self.expression_stack):
            if isinstance(elem, Variable):
                self.expression_stack[i] = elem.object

    def is_expression_evaluated(self):
        for elem in self.expression_stack:
            if not isinstance(elem, Object):
                return False
        return True

    def pack_expression_result(self):
        if not self.is_expression_evaluated():
            raise Exception("Expression not yet evaluated")
        tuple = Tuple(self.expression_stack)
        self.expression_stack = [tuple]

    def evaluate_expression(self):
        self.dereference_variables()

        while self.evaluate_next_operator():
            pass
