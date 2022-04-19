import os
from src.Basic_Func import Basic
from src.Bonus_Func import Bonus
from src.User import User
from termcolor import colored


class Shell:
    """
        В этом классе находятся статические методы.
        Главные это parser_runner и run.
        В них находится реализация запуска и парсер командной строки.
    """

    @staticmethod
    def print_extra_files(a: list, n: int):
        """
            Если в команде есть лишние аргументы, то печатает их и игнорирует.
            Это функция предназначена для избежания дубликатов.
        """
        print('{0}: there extra operand(s) {1}. They(It) will be ignored.'.
              format(colored(a[0], attrs=['bold']),
                     colored(str([a[idx] for idx in range(n, len(a))]), 'yellow', attrs=['bold'])))

    @staticmethod
    def print_not_enough(s: str):
        print('{0}: the operand specifying the file is omitted'.format(colored(s, attrs=['bold'])))

    @staticmethod
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
        bonus = Bonus()
        b = args.split()
        a = []
        i = 0
        while i < len(b):
            if b[i] != '':
                if b[i][0] == "'":
                    s = b[i][1:]
                    if b[i][-1] == "'":
                        s = b[i][1:len(b[i]) - 1]
                    else:
                        s += ' '
                        i += 1
                        while i < len(b) and b[i][-1] != "'":
                            s += b[i] + ' '
                            i += 1
                        if i < len(b):
                            s += b[i][0:len(b[i]) - 1]
                    a.append(s)
                else:
                    a.append(b[i])
            i += 1
        if a[0] == 'run':
            a[1] = os.path.abspath(a[1])
            bonus.exec_files_runner(a[1:])
        elif a[0] == 'help' or a[0] == 'ls' or a[0] == 'pwd' or a[0] == 'clear' or a[0] == 'exit':
            if len(a) > 1:
                Shell.print_extra_files(a, 1)
            if a[0] == 'ls':
                basic.ls()
            elif a[0] == 'pwd':
                basic.pwd()
            elif a[0] == 'exit':
                return 1
            elif a[0] == 'help':
                basic.help()
            else:
                os.system('clear')
        elif a[0] == 'cd' or a[0] == 'rm' or a[0] == 'rmdir' or a[0] == 'mkdir':
            if len(a) < 2:
                Shell.print_not_enough(a[0])
            else:
                if len(a) > 2:
                    Shell.print_extra_files(a, 2)
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
                Shell.print_not_enough(a[0])
            else:
                if len(a) > 3:
                    Shell.print_extra_files(a, 3)
                if a[0] == 'cp':
                    basic.cp(a[1], a[2])
                else:
                    basic.mv(a[1], a[2])
        else:
            print('Incorrect command. '
                  'Type {0} to see which commands (with their syntax and description) there are.'.
                  format(colored('help', 'yellow', attrs=['bold'])))

    @staticmethod
    def welcome():
        print(' ' + 50 * '=')
        print('Ⅱ' + 48 * ' ' + '  Ⅱ')
        print('Ⅱ' + 48 * ' ' + '  Ⅱ')
        print(colored(14 * ' ' + 'Welcome To My OWN SHELL', 'green', attrs=['bold']))
        print('Ⅱ' + 48 * ' ' + '  Ⅱ')
        print('Ⅱ' + 48 * ' ' + '  Ⅱ')
        print(' ' + 50 * '=')

    @staticmethod
    def run():
        users = User()
        os.system('clear')
        Shell.welcome()
        user = users.getUser()
        while True:
            print(colored(user, 'cyan', attrs=['bold']), end=' ')
            print(colored(
                '~' + os.path.abspath(os.curdir)[len(users.getUserName()) + 6:] + '$',
                'blue',
                attrs=['bold']),
                end=' ')
            cmd = input()
            if Shell.parser_runner(cmd) == 1:
                os.system('clear')
                break
