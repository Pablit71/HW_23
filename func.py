def func_query(cmd, value, file_list):
    if cmd == "filter":
        res = filter(lambda x: (x for x in file_list if value in x), file_list)
        return res
    if cmd == "map":
        value = int(value)
        res = [x.split()[value] for x in file_list]
        return res
    if cmd == 'unique':
        return list(set(value))
    if cmd == 'sort':
        return sorted(file_list, reverse=False)
    if cmd == 'limit':
        res = list(file_list)[:value]
        return res
