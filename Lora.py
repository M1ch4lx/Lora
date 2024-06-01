from Context import Context
from Function import *
from Operator import *
from Variable import *
from Object import *
from TypeMarshalling import *
import math
import copy


class Lora:
    def __init__(self):
        self.function_set: FunctionSet = FunctionSet()
        self.current_context: Context = Context()
        self.expression_stack: list = []
        self.marshal: Marshal = Marshal()
        self.breaking_loop = False
        self.call_level = 0

        self.add_python_function(
            'print', [ObjectType.ANY], lambda args: print(args[0]))

        self.add_python_function(
            'sin', [ObjectType.NUMBER], lambda args: math.sin(args[0]))

        self.add_python_function(
            'size', [ObjectType.ARRAY], lambda args: len(args[0]), prototype='Array')

    def add_python_function(self, name, args, callback, prototype=None):
        args = [FunctionArgument(i, str(i), prototype=object_type_prototype(type), type=type) for i, type in enumerate(args)]
        if prototype is not None:
            name = prototype + ':' + name
        signature = FunctionSignature(name, args)
        function = Function(signature, is_python_function=True, python_callback=callback)
        if self.function_set.function_exists(name):
            raise Exception(f"Function already exists: {name}")
        self.function_set.add_function(function)

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
        if self.function_set.function_exists(name):
            raise Exception(f"Variable name {name} shadows function")
        var = self.get_variable(name)
        if var is None:
            self.current_context.create_variable(Variable(name, copy.deepcopy(object)))
        else:
            var.object = copy.deepcopy(object)

        # print(name + ': ' + object.type.name + ' = ' + str(object))

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

    def add_id(self, id):
        self.expression_stack.append(id)

    def add_reference(self, name):
        function = self.function_set.find_function(name)
        if function is not None:
            callback = Callback(function)
            self.expression_stack.append(callback)
        else:
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

        operands_count = operator_operands_count(op)

        if operands_count == 1:
            operand = self.expression_stack[index + 1]
            if op == Operator.NOT:
                result = Boolean(not operand)

        elif operands_count == 2:
            left_operand = self.expression_stack[index + 1]
            right_operand = self.expression_stack[index + 2]

            if op in (Operator.AND, Operator.OR, Operator.NOT):
                if left_operand.type != ObjectType.BOOLEAN or right_operand.type != ObjectType.BOOLEAN:
                    raise Exception("Expected logical expressions in boolean expression")

            if op == Operator.ADD:
                result = left_operand + right_operand
            elif op == Operator.SUB:
                result = left_operand - right_operand
            elif op == Operator.MUL:
                result = left_operand * right_operand
            elif op == Operator.DIV:
                result = left_operand / right_operand
            elif op == Operator.EQ:
                result = Boolean(left_operand == right_operand)
            elif op == Operator.NEQ:
                result = Boolean(left_operand != right_operand)
            elif op == Operator.LT:
                result = Boolean(left_operand < right_operand)
            elif op == Operator.LTE:
                result = Boolean(left_operand <= right_operand)
            elif op == Operator.GT:
                result = Boolean(left_operand > right_operand)
            elif op == Operator.GTE:
                result = Boolean(left_operand >= right_operand)
            elif op == Operator.AND:
                result = Boolean(left_operand and right_operand)
            elif op == Operator.OR:
                result = Boolean(left_operand or right_operand)
            elif op == Operator.ATTR:
                variable = left_operand.context.find_variable(right_operand)
                if variable is None:
                    raise Exception(f"Property {right_operand} not found")
                result = variable.object
            elif op == Operator.INDEX:
                if left_operand.type != ObjectType.NUMBER or not isinstance(left_operand.value, int):
                    raise Exception("Index must be an integer value")
                if right_operand.type != ObjectType.ARRAY:
                    raise Exception("Index operator expects array object")
                result = right_operand[left_operand.value]
        else:
            raise Exception("Invalid operands count")

        for i in range(1 + operands_count):
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
            if not isinstance(elem, Object) and elem is not None:
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
