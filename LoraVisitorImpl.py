from LoraLexer import LoraLexer
from LoraVisitor import LoraVisitor
from antlr4 import *
if "." in __name__:
    from .LoraParser import LoraParser
else:
    from LoraParser import LoraParser

from Lora import Lora
from Object import *
from Operator import *
from Function import *
from Context import *
from Variable import *


class StopExecution(Exception):
    pass


class LoraVisitorImpl(LoraVisitor):

    def __init__(self, lora: Lora):
        self.lora = lora
        self.lora.visitor = self
        self.this: Object = None
        self.current_statement_line = ''

    # Visit a parse tree produced by LoraParser#program.
    def visitProgram(self, ctx: LoraParser.ProgramContext):
        self.visitChildren(ctx)

    # Visit a parse tree produced by LoraParser#alias.
    def visitAlias(self, ctx: LoraParser.AliasContext):
        return ctx.ID().getText()

    # Visit a parse tree produced by LoraParser#import_statement.
    def visitImport_statement(self, ctx: LoraParser.Import_statementContext):
        module_name = ctx.ID().getText()
        alias = module_name
        if ctx.alias():
            alias = self.visit(ctx.alias())

        if alias in Context.BUILTIN_PROTOTYPES:
            raise Exception(f'Illegal module name: {alias}')

        if self.lora.variable_exists(alias):
            if ctx.alias():
                raise Exception(f'Provided alias {alias} is already taken, module might be already imported')
            raise Exception(f'Module {alias} already imported')

        file_path = module_name + '.lora'

        input_stream = FileStream(file_path)
        lexer = LoraLexer(input_stream)

        token_stream = CommonTokenStream(lexer)
        parser = LoraParser(token_stream)

        tree = parser.program()

        module = Lora()

        visitor = LoraVisitorImpl(module)

        try:
            result = visitor.visit(tree)
            raise Exception('No return statement in imported module')
        except StopExecution as e:
            imported_object = module.expression_result()
            # TODO: recursive scan for all imported prototypes
            functions = module.function_set.find_all_of_prototype(imported_object.prototype_name)

            for fun in functions:
                fun.signature.return_type = 'Any'
                fun.signature.name = fun.signature.name.replace(imported_object.prototype_name + ':', alias + ':')
                fun.signature.id = get_function_id(fun.signature.name)
                for arg in fun.signature.args:
                    arg.type = ObjectType.ANY
                    arg.prototype = 'Any'
            for fun in functions:
                self.lora.function_set.add_function(fun)
            imported_object.prototype_name = alias
            self.lora.assign_variable(alias, imported_object)
        except Exception as e:
            print(f'Cannot import module {module_name}')
            print(f'In line {visitor.current_statement_line}: {e}')

    # Visit a parse tree produced by LoraParser#typed_variable.
    def visitTyped_variable(self, ctx: LoraParser.Typed_variableContext):
        return ctx.ID(0).getText(), ctx.ID(1).getText()

    # Visit a parse tree produced by LoraParser#value.
    def visitValue(self, ctx: LoraParser.ValueContext):
        if ctx.FLOAT_VALUE():
            self.lora.add_value(Number(float(ctx.FLOAT_VALUE().getText())))
        elif ctx.INTEGER_VALUE():
            self.lora.add_value(Number(int(ctx.INTEGER_VALUE().getText())))
        elif ctx.BOOL_VALUE():
            self.lora.add_value(Boolean(ctx.BOOL_VALUE().getText() == 'True'))
        elif ctx.STRING_VALUE():
            self.lora.add_value(String(ctx.STRING_VALUE().getText()[1:-1]))
        elif ctx.NONE():
            self.lora.add_value(None)
        return self.visitChildren(ctx)

    # Visit a parse tree produced by LoraParser#variable_reference.
    def visitVariable_reference(self, ctx: LoraParser.Variable_referenceContext):
        self.lora.add_reference(ctx.getText())
        return self.visitChildren(ctx)

    # Visit a parse tree produced by LoraParser#tuple.
    def visitTuple(self, ctx: LoraParser.TupleContext):
        original_expression_stack = self.lora.swap_expression_stack([])
        self.lora.start_expression()
        self.visitChildren(ctx)
        self.lora.evaluate_expression()
        self.lora.pack_expression_result()
        result = self.lora.expression_result()
        original_expression_stack.append(result)
        self.lora.swap_expression_stack(original_expression_stack)

    # Visit a parse tree produced by LoraParser#function_call.
    def visitFunction_call(self, ctx: LoraParser.Function_callContext):
        self.lora.call_level += 1

        this_object = self.this
        self.this = None

        original_expression_stack = self.lora.swap_expression_stack([])
        self.lora.start_expression()
        if ctx.tuple_():
            self.visit(ctx.tuple_())
            evaluated_args: Tuple = self.lora.expression_result()
        else:
            evaluated_args: Tuple = Tuple([])

        function_name = ctx.ID().getText()
        if this_object is not None:
            if this_object.prototype_name is None:
                raise Exception(f"Object have no method {function_name}")
            function_name = this_object.prototype_name + ':' + function_name

        function_id = get_function_id(function_name)

        function: Function = self.lora.function_set.find_function(function_id)
        if function is None:
            callback_var = self.lora.current_context.find_variable(function_name)
            if callback_var.object.type == ObjectType.CALLBACK:
                function = callback_var.object.value

        if function is None:
            raise Exception("Cannot resolve function call: " + function_name)

        if this_object is not None:
            evaluated_args.value.insert(0, this_object)

        if function.signature.args_count != len(evaluated_args.value):
            raise Exception(f"Function {function.signature.name} expects {function.signature.args_count} arguments")

        function_context = Context()

        for index, arg in enumerate(evaluated_args.value):
            arg_signature = function.signature.args[index]
            if arg_signature.prototype != 'Any' and arg_signature.prototype != arg.prototype_name:
                raise Exception(f'Expected argument of type {arg_signature.prototype} at position {index}')
            var = Variable(arg_signature.name, arg)
            function_context.create_variable(var)

        original_context = self.lora.swap_context(function_context)

        if function.built_in:

            python_value_args = []
            for index, arg in enumerate(evaluated_args.value):
                expected_type = function.signature.args[index].type
                if expected_type != ObjectType.ANY and arg.type != expected_type:
                    raise Exception(f"Mismatched argument type at position {index}. Expected {expected_type.name}, got {arg.type}")
                python_value_args.append(
                    self.lora.marshal.lora_to_python(arg))

            result = function.python_callback(python_value_args)

            self.lora.start_expression()
            if result is not None:
                self.lora.add_value(self.lora.marshal.python_to_lora(result))
        else:
            self.visit(function.parser_context)

        if self.lora.is_expression_stack_empty():
            return_value = None
        else:
            return_value = self.lora.expression_result()

        self.lora.swap_expression_stack(original_expression_stack)
        self.lora.swap_context(original_context)

        self.lora.call_level -= 1

        if function.signature.return_type != 'Any' and function.signature.return_type != return_value.prototype_name:
            raise Exception(f"Invalid return object type, expected {function.signature.return_type}")

        self.lora.add_value(return_value)

    # Visit a parse tree produced by LoraParser#index_operator.
    def visitIndex_operator(self, ctx: LoraParser.Index_operatorContext):
        original_expression_stack = self.lora.swap_expression_stack([])
        self.lora.start_expression()
        self.visit(ctx.tuple_())
        evaluated_args: Tuple = self.lora.expression_result()
        self.lora.swap_expression_stack(original_expression_stack)
        indexes = []
        for arg in reversed(evaluated_args.value):
            self.lora.add_operator(Operator.INDEX)
            self.lora.add_value(arg)
            indexes.append(arg.value)
        return list(reversed(indexes))

    # Visit a parse tree produced by LoraParser#array.
    def visitArray(self, ctx: LoraParser.ArrayContext):
        original_expression_stack = self.lora.swap_expression_stack([])
        self.lora.start_expression()
        self.visitChildren(ctx)
        self.lora.evaluate_expression()
        self.lora.pack_expression_result()
        result = self.lora.expression_result()
        array = Array(result.value)
        original_expression_stack.append(array)
        self.lora.swap_expression_stack(original_expression_stack)

    # Visit a parse tree produced by LoraParser#object_field.
    def visitObject_field(self, ctx: LoraParser.Object_fieldContext):
        original = self.lora.swap_expression_stack([])
        self.lora.start_expression()
        self.visitChildren(ctx)
        self.lora.evaluate_expression()
        if len(self.lora.expression_stack) > 1:
            self.lora.pack_expression_result()
        result = self.lora.expression_result()
        field_name = ctx.ID().getText()
        self.lora.swap_expression_stack(original)
        return field_name, result

    # Visit a parse tree produced by LoraParser#object.
    def visitObject(self, ctx: LoraParser.ObjectContext):
        user_object = Object()
        for field in ctx.object_field():
            name, value = self.visit(field)
            user_object.context.create_variable(
                Variable(name, value))
        self.lora.add_value(user_object)


    # Visit a parse tree produced by LoraParser#attribute_operator.
    def visitAttribute_operator(self, ctx: LoraParser.Attribute_operatorContext):
        self.lora.add_id(ctx.ID().getText())
        return self.visitChildren(ctx)

    # Visit a parse tree produced by LoraParser#expression.
    def visitExpression(self, ctx: LoraParser.ExpressionContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by LoraParser#boolean_expression.
    def visitBoolean_expression(self, ctx: LoraParser.Boolean_expressionContext):
        if ctx.OR():
            self.lora.add_operator(Operator.OR)
        return self.visitChildren(ctx)

    # Visit a parse tree produced by LoraParser#boolean_term.
    def visitBoolean_term(self, ctx: LoraParser.Boolean_termContext):
        if ctx.AND():
            self.lora.add_operator(Operator.AND)
        return self.visitChildren(ctx)

    # Visit a parse tree produced by LoraParser#boolean_factor.
    def visitBoolean_factor(self, ctx: LoraParser.Boolean_factorContext):
        if ctx.NOT():
            self.lora.add_operator(Operator.NOT)
        return self.visitChildren(ctx)

    # Visit a parse tree produced by LoraParser#relational_expression.
    def visitRelational_expression(self, ctx: LoraParser.Relational_expressionContext):
        if ctx.op:
            if ctx.EQ():
                self.lora.add_operator(Operator.EQ)
            elif ctx.NEQ():
                self.lora.add_operator(Operator.NEQ)
            elif ctx.LT():
                self.lora.add_operator(Operator.LT)
            elif ctx.LTE():
                self.lora.add_operator(Operator.LTE)
            elif ctx.GT():
                self.lora.add_operator(Operator.GT)
            elif ctx.GTE():
                self.lora.add_operator(Operator.GTE)
        return self.visitChildren(ctx)

    # Visit a parse tree produced by LoraParser#additive_expression.
    def visitAdditive_expression(self, ctx: LoraParser.Additive_expressionContext):
        if ctx.op:
            if ctx.PLUS():
                self.lora.add_operator(Operator.ADD)
            if ctx.MINUS():
                self.lora.add_operator(Operator.SUB)
        return self.visitChildren(ctx)

    # Visit a parse tree produced by LoraParser#multiplicative_expression.
    def visitMultiplicative_expression(self, ctx: LoraParser.Multiplicative_expressionContext):
        if ctx.op:
            if ctx.MULT():
                self.lora.add_operator(Operator.MUL)
            if ctx.DIV():
                self.lora.add_operator(Operator.DIV)
        return self.visitChildren(ctx)

    # Visit a parse tree produced by LoraParser#primary_expression.
    def visitPrimary_expression(self, ctx: LoraParser.Primary_expressionContext):
        if ctx.index_operator():
            self.visit(ctx.index_operator())
            self.visit(ctx.primary_expression())
        elif ctx.attribute_operator():
            self.lora.add_operator(Operator.ATTR)
            self.visit(ctx.primary_expression())
            self.visit(ctx.attribute_operator())
        elif ctx.DOT() and ctx.function_call():
            original = self.lora.swap_expression_stack([])
            self.lora.start_expression()
            self.visit(ctx.primary_expression())
            self.lora.evaluate_expression()
            result = self.lora.expression_result()
            self.this = result
            self.lora.swap_expression_stack(original)
            self.visit(ctx.function_call())
        else:
            return self.visitChildren(ctx)

    # Visit a parse tree produced by LoraParser#indexed_assignment.
    def visitIndexed_assignment(self, ctx: LoraParser.Indexed_assignmentContext):
        var_name = ctx.ID().getText()
        var = self.lora.get_variable(var_name)
        if var is None:
            raise Exception(f"Undefined variable {var_name}")
        if var.object.type != ObjectType.ARRAY:
            raise Exception(f"Expected {var_name} to be array")
        indexes = self.visit(ctx.index_operator())
        self.lora.start_expression()
        if ctx.expression():
            self.visit(ctx.expression())
        elif ctx.tuple_():
            self.visit(ctx.tuple_())
        self.lora.evaluate_expression()
        result = self.lora.expression_result()
        current = var.object
        for i in indexes[:-1]:
            current = current[i]
        last = indexes[-1]
        current[last] = result

    # Visit a parse tree produced by LoraParser#typed_assignment.
    def visitTyped_assignment(self, ctx: LoraParser.Typed_assignmentContext):
        variable_name, prototype_name = self.visit(ctx.typed_variable())
        self.lora.start_expression()
        self.visit(ctx.expression())
        self.lora.evaluate_expression()
        expr_result = self.lora.expression_result()
        if prototype_name != 'Any' and expr_result.prototype_name != prototype_name:
            raise Exception(f'Expected object of type {prototype_name}')
        self.lora.assign_variable(variable_name, expr_result)

    # Visit a parse tree produced by LoraParser#property_assignment.
    def visitProperty_assignment(self, ctx: LoraParser.Property_assignmentContext):
        self.lora.start_expression()
        self.visitChildren(ctx)
        self.lora.evaluate_expression()
        expr_result = self.lora.expression_result()
        if expr_result.type == ObjectType.CALLBACK:
            raise Exception('Assigning callback to property is forbidden')

        ids_chain = [id.getText() for id in ctx.ID()]
        variable_name = ids_chain[0]
        new_prop_name = ids_chain[-1]
        intermediate_props = ids_chain[1:-1]

        variable = self.lora.get_variable(variable_name)
        if variable is None:
            raise Exception(f"Variable {variable_name} not initialized")

        current_var = variable
        for prop_name in intermediate_props:
            prop_var = current_var.object.context.find_variable(prop_name)
            if prop_var is None:
                raise Exception(f"Cannot find property {prop_name} in {current_var.name}")
            current_var = prop_var

        current_var.object.context.create_variable(Variable(new_prop_name, expr_result))

    # Visit a parse tree produced by LoraParser#assignment.
    def visitAssignment(self, ctx: LoraParser.AssignmentContext):
        self.lora.start_expression()
        children = self.visitChildren(ctx)
        self.lora.evaluate_expression()
        result = self.lora.expression_result()
        variables = [id.getText() for id in ctx.ID()]

        if len(variables) > 1 and not isinstance(result, Tuple):
            raise Exception('Expected tuple')

        values = [result] if len(variables) == 1 else result.value

        if len(variables) != len(values):
            raise Exception('Expected tuple with ' + str(len(variables)) + ' elements')

        for i, name in enumerate(variables):
            self.lora.assign_variable(name, values[i])

        return children

    # Visit a parse tree produced by LoraParser#function_parameter.
    def visitFunction_parameter(self, ctx: LoraParser.Function_parameterContext):
        if ctx.ID():
            return ctx.ID().getText(), 'Any'
        if ctx.typed_variable():
            return self.visit(ctx.typed_variable())

    # Visit a parse tree produced by LoraParser#function_parameters_list.
    def visitFunction_parameters_list(self, ctx: LoraParser.Function_parameters_listContext):
        parameters = []
        for param_ctx in ctx.function_parameter():
            param = self.visit(param_ctx)
            if param is not None:
                parameters.append(param)
        return parameters

    # Visit a parse tree produced by LoraParser#type_requirement.
    def visitType_requirement(self, ctx: LoraParser.Type_requirementContext):
        return ctx.ID().getText()

    # Visit a parse tree produced by LoraParser#function_declaration.
    def visitFunction_declaration(self, ctx: LoraParser.Function_declarationContext):
        ids = ctx.ID()
        if len(ids) > 1:
            prototype_name = ids[0].getText()
            owner = self.lora.get_variable(prototype_name)
            method_name = ids[1].getText()
            if owner is None:
                raise Exception(f'Cannot create method {method_name}, object {prototype_name} not found')
            owner.object.prototype_name = prototype_name
            function_name = prototype_name + ':' + method_name
        else:
            function_name = ids[0].getText()
        parameters = self.visit(ctx.function_parameters_list())
        code_block = ctx.code_block()
        parameters = [FunctionArgument(i, param[0], prototype=param[1]) for i, param in enumerate(parameters)]
        signature = FunctionSignature(function_name, parameters)
        if ctx.type_requirement():
            signature.return_type = self.visit(ctx.type_requirement())
        function = Function(signature, is_python_function=False, parser_context=code_block)
        self.lora.function_set.add_function(function)

    # Visit a parse tree produced by LoraParser#return_statement.
    def visitReturn_statement(self, ctx: LoraParser.Return_statementContext):
        self.current_statement_line = ctx.start.line
        self.lora.start_expression()
        self.visitChildren(ctx)

        if len(self.lora.expression_stack) == 0:
            self.lora.add_value(None)

        self.lora.evaluate_expression()

        if self.lora.call_level == 0:
            raise StopExecution()

    # Visit a parse tree produced by LoraParser#break_statement.
    def visitBreak_statement(self, ctx: LoraParser.Break_statementContext):
        self.current_statement_line = ctx.start.line
        if self.lora.current_context.loop_count > 0:
            self.lora.breaking_loop = True
        return self.visitChildren(ctx)

    # Visit a parse tree produced by LoraParser#while_loop_statement.
    def visitWhile_loop_statement(self, ctx: LoraParser.While_loop_statementContext):
        self.current_statement_line = ctx.start.line
        self.lora.current_context.loop_count += 1
        while True:
            self.lora.start_expression()
            self.visit(ctx.expression())
            self.lora.evaluate_expression()
            result = self.lora.expression_result()

            if not isinstance(result, Boolean):
                raise Exception('Expected logical expression')

            if not result.value:
                break

            self.visit(ctx.code_block())

            if self.lora.breaking_loop:
                break

        self.lora.breaking_loop = False
        self.lora.current_context.loop_count -= 1

    # Visit a parse tree produced by LoraParser#for_loop_statement.
    def visitFor_loop_statement(self, ctx: LoraParser.For_loop_statementContext):
        self.current_statement_line = ctx.start.line
        self.lora.start_expression()
        self.visit(ctx.expression())
        self.lora.evaluate_expression()
        result = self.lora.expression_result()
        if not isinstance(result, Array):
            raise Exception('Expected array to iterate')
        self.lora.current_context.loop_count += 1
        iter_name = ctx.ID().getText()
        for elem in result.value:
            self.lora.assign_variable(iter_name, elem)
            self.visit(ctx.code_block())
            if self.lora.breaking_loop:
                break
        self.lora.breaking_loop = False
        self.lora.current_context.loop_count -= 1

    # Visit a parse tree produced by LoraParser#code_block.
    def visitCode_block(self, ctx: LoraParser.Code_blockContext):
        self.current_statement_line = ctx.start.line
        for statement in ctx.statement():
            if self.lora.breaking_loop:
                break
            self.visit(statement)

    # Visit a parse tree produced by LoraParser#if_statement.
    def visitIf_statement(self, ctx: LoraParser.If_statementContext):
        self.current_statement_line = ctx.start.line
        self.lora.start_expression()
        self.visit(ctx.expression())
        self.lora.evaluate_expression()
        result = self.lora.expression_result()
        if result.value:
            self.visit(ctx.code_block())
        elif ctx.else_statement():
            self.visit(ctx.else_statement())

        return None

    # Visit a parse tree produced by LoraParser#else_statement.
    def visitElse_statement(self, ctx: LoraParser.Else_statementContext):
        self.current_statement_line = ctx.start.line
        return self.visitChildren(ctx)

    # Visit a parse tree produced by LoraParser#simple_statement.
    def visitSimple_statement(self, ctx: LoraParser.Simple_statementContext):
        self.current_statement_line = ctx.start.line
        if ctx.expression():
            self.lora.start_expression()
            children = self.visitChildren(ctx)
            self.lora.evaluate_expression()
            return children

        return self.visitChildren(ctx)

    # Visit a parse tree produced by LoraParser#statement.
    def visitStatement(self, ctx: LoraParser.StatementContext):
        self.current_statement_line = ctx.start.line
        return self.visitChildren(ctx)

# del LoraParser