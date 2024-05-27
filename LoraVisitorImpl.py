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

class LoraVisitorImpl(LoraVisitor):

    def __init__(self, lora):
        self.lora = lora

    # Visit a parse tree produced by LoraParser#program.
    def visitProgram(self, ctx: LoraParser.ProgramContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by LoraParser#import_statement.
    def visitImport_statement(self, ctx: LoraParser.Import_statementContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by LoraParser#typed_variable.
    def visitTyped_variable(self, ctx: LoraParser.Typed_variableContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by LoraParser#value.
    def visitValue(self, ctx: LoraParser.ValueContext):
        print('Value')
        print(ctx.getText())

        self.lora.add_value(Number(ObjectType.FLOAT, ctx.getText()))
        return self.visitChildren(ctx)

    # Visit a parse tree produced by LoraParser#variable_reference.
    def visitVariable_reference(self, ctx: LoraParser.Variable_referenceContext):
        print(ctx.getText())
        self.lora.add_reference(ctx.getText())
        return self.visitChildren(ctx)

    # Visit a parse tree produced by LoraParser#tuple.
    def visitTuple(self, ctx: LoraParser.TupleContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by LoraParser#function_call.
    def visitFunction_call(self, ctx: LoraParser.Function_callContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by LoraParser#index_operator.
    def visitIndex_operator(self, ctx: LoraParser.Index_operatorContext):
        print('Index operator')
        print(ctx.getText())
        return self.visitChildren(ctx)

    # Visit a parse tree produced by LoraParser#array.
    def visitArray(self, ctx: LoraParser.ArrayContext):
        print('Array')
        print(ctx.getText())
        return self.visitChildren(ctx)

    # Visit a parse tree produced by LoraParser#object_field.
    def visitObject_field(self, ctx: LoraParser.Object_fieldContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by LoraParser#object.
    def visitObject(self, ctx: LoraParser.ObjectContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by LoraParser#attribute_operator.
    def visitAttribute_operator(self, ctx: LoraParser.Attribute_operatorContext):
        print('Attribute')
        print(ctx.getText())
        return self.visitChildren(ctx)

    # Visit a parse tree produced by LoraParser#expression.
    def visitExpression(self, ctx: LoraParser.ExpressionContext):
        if ctx.op:
            if ctx.PLUS():
                self.lora.add_operator(Operator.ADD)
            if ctx.MINUS():
                self.lora.add_operator(Operator.SUB)
            if ctx.MULT():
                self.lora.add_operator(Operator.MUL)
            if ctx.DIV():
                self.lora.add_operator(Operator.DIV)
            if ctx.EQ():
                self.lora.add_operator(Operator.EQ)

        return self.visitChildren(ctx)

    # Visit a parse tree produced by LoraParser#typed_assignment.
    def visitTyped_assignment(self, ctx: LoraParser.Typed_assignmentContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by LoraParser#assignment.
    def visitAssignment(self, ctx: LoraParser.AssignmentContext):
        self.lora.start_expression()
        children = self.visitChildren(ctx)
        result = self.lora.evaluate_expression()
        self.lora.assign_variable(ctx.ID().getText(), result)
        return children

    # Visit a parse tree produced by LoraParser#function_parameter.
    def visitFunction_parameter(self, ctx: LoraParser.Function_parameterContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by LoraParser#function_parameters_list.
    def visitFunction_parameters_list(self, ctx: LoraParser.Function_parameters_listContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by LoraParser#function_declaration.
    def visitFunction_declaration(self, ctx: LoraParser.Function_declarationContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by LoraParser#return_statement.
    def visitReturn_statement(self, ctx: LoraParser.Return_statementContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by LoraParser#break_statement.
    def visitBreak_statement(self, ctx: LoraParser.Break_statementContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by LoraParser#for_loop_statement.
    def visitFor_loop_statement(self, ctx: LoraParser.For_loop_statementContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by LoraParser#if_statement.
    def visitIf_statement(self, ctx: LoraParser.If_statementContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by LoraParser#else_statement.
    def visitElse_statement(self, ctx: LoraParser.Else_statementContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by LoraParser#simple_statement.
    def visitSimple_statement(self, ctx: LoraParser.Simple_statementContext):
        if ctx.expression():
            self.lora.start_expression()
            children = self.visitChildren(ctx)
            result = self.lora.evaluate_expression()
            return children

        return self.visitChildren(ctx)

    # Visit a parse tree produced by LoraParser#base_statement.
    def visitBase_statement(self, ctx: LoraParser.Base_statementContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by LoraParser#statement.
    def visitStatement(self, ctx: LoraParser.StatementContext):
        return self.visitChildren(ctx)

del LoraParser