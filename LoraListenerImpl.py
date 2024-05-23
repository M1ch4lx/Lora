from antlr4 import *
from LoraListener import LoraListener
if "." in __name__:
    from .LoraParser import LoraParser
else:
    from LoraParser import LoraParser

class LoraListenerImpl(LoraListener):

    def enterProgram(self, ctx):
        print("Entering program:", ctx.getText())

    def exitProgram(self, ctx):
        print("Exiting program:", ctx.getText())

    def enterTyped_variable(self, ctx):
        print("Entering typed variable:", ctx.getText())

    def exitTyped_variable(self, ctx):
        print("Exiting typed variable:", ctx.getText())

    def enterExpression(self, ctx):
        print("Entering expression:", ctx.getText())

    def exitExpression(self, ctx):
        print("Exiting expression:", ctx.getText())

    def enterTyped_assignment(self, ctx):
        print("Entering typed assignment:", ctx.getText())

    def exitTyped_assignment(self, ctx):
        print("Exiting typed assignment:", ctx.getText())

    def enterAssignment(self, ctx):
        print("Entering assignment:", ctx.getText())

    def exitAssignment(self, ctx):
        print("Exiting assignment:", ctx.getText())

    def enterStatement(self, ctx):
        print("Entering statement:", ctx.getText())

    def exitStatement(self, ctx):
        print("Exiting statement:", ctx.getText())

del LoraParser