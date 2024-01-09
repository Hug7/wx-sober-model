from dataclasses import dataclass, field

from constant import VarType


@dataclass()
class Constant:
    name: str
    val: float
    label: str = field(default='')
    is_free: bool = field(default=True)
    ub: float = field(default=None)
    lb: float = field(default=None)
    desc: str = field(default='')


@dataclass()
class Variable:
    name: str
    type: VarType
    label: str = field(default='')
    is_free: bool = field(default=True)
    ub: float = field(default=None)
    lb: float = field(default=None)
    desc: str = field(default='')

