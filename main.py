#! /usr/bin/env python3
import argparse
import os
from src import file_service
from src import utils


def read_file():
    file_name = input("Enter file name : ")
    res = file_service.read_file(file_name)
    print(res)


def create_file():
    content = input("Enter file content : ")
    res = file_service.create_file(content)
    print(res)


def delete_file():
    file_name = input("Enter file name : ")
    res = file_service.delete_file(file_name)
    print(res)


def list_dir():
    res = file_service.list_dir()
    print(res)


def change_dir():
    directory = input("Enter dir name : ")
    res = file_service.change_dir(directory)
    print(res)


def current_dir():
    res = file_service.current_dir()
    print(res)


def get_file_permissions():
    filename = input("Enter file name: ")
    res = file_service.get_file_permissions(filename)
    print(res)


def set_file_permissions():
    filename = input("Enter file name : ")
    permissions = input("Input UNIX permissions in oct format :")
    res = file_service.set_file_permissions(filename, permissions)
    print(res)


def main():
    parser = argparse.ArgumentParser(description='Restfull file server')
    parser.add_argument('-d', '--directory', help='Working directory', default='./')
    args = parser.parse_args()
    os.chdir(args.directory)
    print(f'Working directory is {os.getcwd()}')

    commands = {
        "get": read_file,
        "create": create_file,
        "delete": delete_file,
        "ls": list_dir,
        "cd": change_dir,
        "pwd": current_dir,
        "gmod": get_file_permissions,
        "chmod": set_file_permissions
    }
    while True:
        command = input("Enter command: ")
        if command == "help" or command == "1":
            print(utils.get_dict_keys('Available commands: ', commands))
            continue
        if command == "exit" or command == "0":
            return
        if command not in commands:
            print("Unknown command")
            print(utils.get_dict_keys('Available commands: ', commands))
            continue
        command = commands[command]
        try:
            command()
        except Exception as ex:
            print(f"Error on {command} execution : {ex}")


if __name__ == "__main__":
    main()
