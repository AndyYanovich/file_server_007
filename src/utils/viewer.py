def get_dict_keys(info, arg_dict):
    res = info
    for key in arg_dict:
        res += '[' + key + "] "
    return res
