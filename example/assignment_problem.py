from domain.constant import VarType
from domain.model import Model, Variable, Dimension, Space

if __name__ == '__main__':
    model = Model('m')
    dim_n = Dimension('N')
    dim_m = Dimension('M')
    space_mn = Space(name='m*n', dims=[dim_n, dim_m])
    model.add_var(Variable(name='x', type=VarType.INTEGER, ub=10, lb=1, space=space_mn))
    model.add_var(Variable(name='y', type=VarType.INTEGER, ub=10, lb=1, space=space_mn))
    model.to_latex(write_to_file=True, target_dir=r'/Volumes/E/code/py_poj/wx-sober-model/resource')
