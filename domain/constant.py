from enum import Enum


class VarType(Enum):
    INTEGER = 0
    BINARY = 1
    CONTINUOUS = 2


class RelationType(Enum):
    EQUAL = '='
    LESS = '<'
    LEQ = r'\leq'
    GREATER = '>'
    GEQ = r'\geq'


class ObjectType(Enum):
    MINIMUM = r'\min'
    MAXIMUM = r'\max'
    ARGMIN = r'\argmin'
    ARGMAX = r'\argmax'
