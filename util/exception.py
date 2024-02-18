import copy


class CustomException(Exception):
    code: str
    msg: str

    def __init__(self, code: str, msg: str):
        self.code = code
        self.msg = msg
        super().__init__(CustomException.tips(
            code=code, msg=msg
        ))

    def f(self, *args):
        res = copy.copy(self)
        res.msg = res.msg.format(*args)
        super(CustomException, res).__init__(CustomException.tips(
            code=self.code, msg=self.msg
        ))
        return res

    @staticmethod
    def tips(code: str, msg: str):
        return f"{code}:{msg}"


DataTypeUnsupportedError = CustomException("10001", "异常数据类型不支持!")
DirectoryPathIsNotEmptyError = CustomException("10003", "文件夹路径不能为空!")
DirectoryPathNotFoundError = CustomException("10002", "文件夹路径 {} 没有被发现!")


if __name__ == '__main__':
    # raise FileNotFoundError
    raise DataTypeUnsupportedError
