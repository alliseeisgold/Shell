# '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'
import os
import socket
from termcolor import colored, cprint


def ls(cur_dir=os.curdir):
    for items in os.listdir(os.path.abspath(cur_dir)):
        """
            Если файлы скрытые, то пропускаем их
        """
        if items[0] == '.':
            continue
        if os.path.isdir(items):
            print(colored(items, 'blue', attrs=['bold']), end='\t\t')
        elif os.access(items, os.X_OK):
            print(colored(items, 'green', attrs=['bold']), end='\t\t')
        else:
            print(items, end='\t\t')
    print()


def pwd():
    print(os.path.abspath(os.curdir))


def cd(given_path):
    try:
        os.chdir(given_path)
        print("Текущий рабочий каталог: {0}".format(os.getcwd()))
    except FileNotFoundError:
        print("Каталог: {0} не существует".format(given_path))
    except NotADirectoryError:
        print("{0} не каталог".format(given_path))
    except PermissionError:
        print("У вас нет прав на изменение {0}".format(given_path))


def cp(source: str, destination: str):
    inp = open(source, 'r')
    out = open(destination, 'w')
    for lines in inp.readlines():
        out.write(lines)
    inp.close()
    out.close()


def mv(source: str, destination: str):



if __name__ == '__main__':
    os.system('clear')
    username = os.getlogin()
    hostname = socket.gethostname()
    user = username + '@' + hostname + ':~'
    while True:
        print(colored(user, 'red', attrs=['bold']), end=' ')
        print(colored(os.path.abspath(os.curdir)[len(username) + 6:] + '$', 'blue', attrs=['bold']), end=' ')
        cmd = input()
        if cmd[0:2] == 'ls':
            ls()
        elif cmd[0:3] == 'pwd':
            pwd()
        elif cmd[0:2] == 'cd':
            cd(cmd[3:len(cmd)])
        elif cmd == 'exit':
            os.system('clear')
            break
        elif cmd[0:2] == 'cp':
            lst = cmd[3:len(cmd)].split(' ')
            cp(lst[0], lst[1])
        elif cmd == 'clear':
            os.system('clear')
        else:
            print('Unknown command')
