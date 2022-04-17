# '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'
from src.Basic_Func import Basic
import os
import socket
from termcolor import colored


def parser_runner(args: str):
    """
        Функция:
            1) Парсит аргументов командной строки.
            2) Запускает код, если нет ошибок.
        Если все было без ошибок то, вызывает функции из класса Basic:
            Basic.ls() - если команда была ls.
            Basic.pwd() - если команда была pwd.
            Basic.cd(<given_path>) -  если была команда cd.
            Basic.cp(<source_file>, <destination_file>) - если была команда cp.
            Basic.mv(<source_file>, <destination_file>) - если была команда mv.
            Basic.rm(<file_name>) - если была команда rm.
            Basic.rmdir(<dir_name>) - если была команда rmdir.
            Basic.mkdir(<new_dir>) - если была команда mkdir.
        иначе выводит, что неизвестная команда, и предлагает ознакомиться с командами с помощью
        команды Basic.help().
        Если после какой-то команды, кол-во аргументов этой команды больше чем ожидалось, то предупредит об этом
        и будет работать просто игнорируя лишние аргументы.
    """
    basic = Basic()
    b = args.split(' ')
    a = []
    for items in range(len(b)):
        if not b[items] == '':
            a.append(b[items])
    print(a)
    if a[0] == 'ls' or a[0] == 'pwd' or a[0] == 'clear' or a[0] == 'exit':
        if len(a) > 1:
            print('{0}: there extra operand(s) {1}. They(It) will be ignored.'.
                  format(colored(a[0], attrs=['bold']),
                         colored(str([a[idx] for idx in range(1, len(a))]), 'yellow', attrs=['bold'])))
        if a[0] == 'ls':
            basic.ls()
        elif a[0] == 'pwd':
            basic.pwd()
        elif a[0] == 'exit':
            return 1
        else:
            os.system('clear')
    elif a[0] == 'cd' or a[0] == 'rm' or a[0] == 'rmdir' or a[0] == 'mkdir':
        if len(a) < 2:
            print('{0}: the operand specifying the file is omitted'.format(colored(a[0], attrs=['bold'])))
        else:
            if len(a) > 2:
                print('{0}: there extra operand(s) {1}. They(It) will be ignored.'.
                      format(colored(a[0], attrs=['bold']),
                             colored(str([a[idx] for idx in range(2, len(a))]), 'yellow', attrs=['bold'])))
            if a[0] == 'cd':
                basic.cd(a[1])
            elif a[0] == 'rm':
                basic.rm(a[1])
            elif a[0] == 'rmdir':
                basic.rmdir(a[1])
            else:
                basic.mkdir(a[1])
    elif a[0] == 'cp' or a[0] == 'mv':
        print(11)
        if len(a) < 3:
            print('{0}: the operand specifying the file is omitted'.format(colored(a[0], attrs=['bold'])))
        else:
            if len(a) > 3:
                print('{0}: there extra operand(s) {1}. They(It) will be ignored.'.
                      format(colored(a[0], attrs=['bold']),
                             colored(str([a[idx] for idx in range(3, len(a))]), 'yellow', attrs=['bold'])))
            if a[0] == 'cp':
                basic.cp(a[1], a[2])
            else:
                basic.mv(a[1], a[2])
    else:
        print('Incorrect command. '
              'Type {0} to see which commands (with there explanation) there are.'.
              format(colored('help', 'yellow', attrs=['bold'])))


def welcome():
    print(' ' + 50 * '=')
    print('Ⅱ' + 48 * ' ' + '  Ⅱ')
    print('Ⅱ' + 48 * ' ' + '  Ⅱ')
    print(colored(14 * ' ' + 'Welcome To My OWN SHELL', 'green', attrs=['bold']))
    print('Ⅱ' + 48 * ' ' + '  Ⅱ')
    print('Ⅱ' + 48 * ' ' + '  Ⅱ')
    print(' ' + 50 * '=')


if __name__ == '__main__':
    os.system('clear')
    welcome()
    username = os.getlogin()
    hostname = socket.gethostname()
    user = username + '@' + hostname + ':~'
    while True:
        print(colored(user, 'red', attrs=['bold']), end=' ')
        print(colored(os.path.abspath(os.curdir)[len(username) + 6:] + '$', 'blue', attrs=['bold']), end=' ')
        cmd = input()
        if parser_runner(cmd) == 1:
            os.system('clear')
            break
