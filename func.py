import re
from typing import Iterator, List, Any


def func_query(cmd: str, value: str, file_list: Iterator) -> List[Any]:
    if cmd == "filter":
        res = list(filter(lambda x: (x for x in file_list if value in x), file_list))
        return res
    if cmd == "map":
        res = [x.split()[value] for x in file_list]
        return res
    if cmd == 'unique':
        return list(set(value))
    if cmd == 'sort':
        return list(sorted(file_list, reverse=False))
    if cmd == 'limit':
        res = list(file_list)[:int(value)]
        return res
    if cmd == 'regex':
        compiler = re.compile(value)
        res = list(filter(lambda x: compiler.search(x), file_list))
        return res
    return []
