import os
from functools import reduce

def get_files(dir):
    result = get_files_fullname(dir)
    result = map(lambda x: os.path.splitext(x)[0], result)
    result = reduce(lambda x, y: x if y in x else x + [y], result, [])

    return result

def get_files_fullname(dir):
    result = []

    for file_name in os.listdir(dir):
        if os.path.isfile(os.path.join(dir, file_name)):
            result.append(file_name)

    return result
