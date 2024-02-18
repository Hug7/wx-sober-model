from typing import List


def joint(*args, mark=" "):
    res = ''
    for a in args:
        res += mark + a
    return res


def joint_line(*args):
    return joint(*args, mark=" \n")


def joint_list(args: List):
    res = ''
    for a in args:
        res += a + ' \n'
    return res

