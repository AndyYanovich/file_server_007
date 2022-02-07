import os
from src.utils.random_values import create_rand_string as create_file_name


def read_file(file_name):
    if os.path.isfile(file_name):
        with open(file_name, 'r') as f:
            data = f.read()
        return f"Content :\n{data}"
    raise Exception(f"File '{file_name}' not exists!!!")


def create_file(content):
    len_file_name = 5
    file_name = create_file_name(len_file_name) + '.txt'
    while os.path.isfile(file_name):
        file_name = create_file_name(len_file_name) + '.txt'
    with open(file_name, 'w') as f:
        f.write(content)
    return f"File '{file_name}' created"


def delete_file(file_name):
    if os.path.isfile(file_name):
        os.remove(file_name)
        return f"File '{file_name}' deleted"
    raise Exception(f"File '{file_name}' not exists!!!")


def list_dir():
    res = "List dir:\n"
    list_directory = os.listdir()
    el = ''
    for el in list_directory:
        if os.path.isdir(el):
            el = '[' + el + ']'
        res += el + ' '
    return res


def change_dir(directory):
    if os.path.isdir(directory):
        os.chdir(directory)
        return f"Current dir : {os.getcwd()}"
    raise Exception(f"Directory '{directory}' not exists!!!")


def current_dir():
    return f"Current dir : {os.getcwd()}"


def get_file_permissions(file_name):
    if os.path.isfile(file_name):
        permissions = oct(os.stat(file_name).st_mode)
        return f"File {file_name} permissions: {permissions}"
    raise Exception(f"File '{file_name}' not exists!!!")


def set_file_permissions(file_name, permissions):
    if os.path.isfile(file_name):
        os.chmod(file_name, int(permissions))
        return f"Set {permissions} to {file_name}"
    raise Exception(f"File '{file_name}' not exists!!!")