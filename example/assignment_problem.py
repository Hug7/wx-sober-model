from domain.constant import VarType
from domain.model import Model, Variable

if __name__ == '__main__':
    model = Model('m')
    model.add_var(Variable(name='x', is_free=False, type=VarType.INTEGER, ub=10, lb=1))
    model.add_var(Variable(name='y', is_free=False, type=VarType.INTEGER, ub=10, lb=1))
    model.to_latex(write_to_file=True, target_dir=r'/Volumes/E/code/py_poj/wx-sober-model/resource')
