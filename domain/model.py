import os
from dataclasses import dataclass, field
from typing import List, Union, Dict, Any, Optional

from domain.constant import VarType, RelationType
from util.exception import DataTypeUnsupportedError, DirectoryPathNotFoundError, DirectoryPathIsNotEmptyError
from util.tex_util import joint, joint_list, joint_line
from util import write
from util.write import generate_file_name


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
class Dimension:
    name: str


@dataclass()
class Gather:
    name: str


@dataclass()
class Index:
    name: str
    dim: Dimension
    gather: Gather


@dataclass()
class Variable:
    name: str
    type: VarType
    label: str = field(default='')
    is_free: bool = field(default=True)
    ub: float = field(default=None)
    lb: float = field(default=None)
    desc: str = field(default='')

    def var_bound_to_tex(self):
        if self.is_free:
            return f'{self.name} is free'
        res_str = self.name
        if self.lb is not None:
            res_str = joint(str(self.lb), RelationType.LEQ.value, res_str)
        if self.ub is not None:
            res_str = joint(res_str, RelationType.LEQ.value, str(self.ub))
        return res_str + r" \\"


@dataclass()
class Constraint:
    name: str
    lhs: str
    relation: RelationType
    rhs: str
    priority: int = field(default=-1)  # 越大优先级越高
    label: str = field(default='')


def parse_vars_bound_to_tex(vars: List[Variable]) -> List[str]:
    res = []
    for var in vars:
        res.append(var.var_bound_to_tex())
    return res


def parse_const_to_tex(consts: List[Constant]) -> List[str]:
    res = []
    for c in consts:
        res.append(c)
    return res


@dataclass()
class Model:
    name: str  # 模型名称
    vars: List[Variable] = field(default_factory=list)  # 变量集合

    def __init__(self, name=''):
        self.name = name
        self.vars = []

    def add_var(self, var: Variable):
        self.vars.append(var)

    def add_vars(self, vars: Union[List[Variable], Dict[Any, Variable]]):
        if isinstance(vars, List):
            self.vars += vars
        elif isinstance(vars, Dict):
            self.vars += list(vars.values())
        else:
            raise DataTypeUnsupportedError

    def to_latex(self, write_to_file: bool = False, target_dir: Optional[str] = None):
        res = self.parse_vars_bound_to_tex()
        print(res)
        if not write_to_file:
            return
        if target_dir is None:
            raise DirectoryPathIsNotEmptyError
        os.makedirs(target_dir, exist_ok=True)
        target_file_path = f'{target_dir}/{self.name}_{generate_file_name()}'
        write.to_markdown(res, target_file_path)

    def parse_vars_bound_to_tex(self):
        res = joint_list(parse_vars_bound_to_tex(self.vars))
        return "$$ \n" + res + "$$"

    def parse_const_to_tex(self):
        return joint_list(parse_vars_bound_to_tex(self.vars))
