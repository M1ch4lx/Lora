from enum import Enum


class Operator(Enum):
    ADD = 0
    SUB = 1
    MUL = 2
    DIV = 3
    EQ = 4
    NEQ = 5
    LT = 6
    GT = 7
    LTE = 8
    GTE = 9
    AND = 10
    OR = 11
    NOT = 12


def operator_operands_count(op):
    if op == Operator.NOT:
        return 1
    else:
        return 2
