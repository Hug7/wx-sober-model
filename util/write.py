from datetime import datetime
import time


def generate_file_name(postfix: str = '.md'):
    dt = datetime.now()
    return f'{dt.year}_{dt.month}_{dt.day}_{dt.hour}_{dt.minute}_{dt.second}{postfix}'


def to_markdown(data, file_path, mode='w'):

    with open(file_path, mode=mode) as f:
        f.write(data)

