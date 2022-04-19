# There is an implementation of Basic Functionality

import os
from termcolor import colored, cprint


class Basic:
    """
        В этом классе находятся реализация базовой функциональности.
        Все методы static, так как каждая команда делает разные вещи
        и мне было удобно сделать методы static.
    """

    @staticmethod
    def ls():
        for items in os.listdir(os.path.abspath(os.curdir)):
            """
                Если файлы скрытые, то пропускаем их
            """
            if items[0] == '.':
                continue
            """ 
            Эти условия для подсветки шрифтов: 
                    для папок - голубой цвет, 
                    для исполняемых файлов - зеленый
                    для обычных - белый(по умолчанию)
            """
            if os.path.isdir(items):
                print(colored(items, 'blue', attrs=['bold']), end='\t\t')
            elif os.access(items, os.X_OK):
                print(colored(items, 'green', attrs=['bold']), end='\t\t')
            else:
                print(items, end='\t\t')
        print()

    @staticmethod
    def pwd():
        """
            Выводит абсолютный путь текущей директории
        """
        print(os.path.abspath(os.curdir))

    @staticmethod
    def cd(given_path: str):
        """
            По заданной пути перейдет из текущей директории в новую
            при этом могут быть исключения:
                1) Директория не существует
                2) Директорией не является(например, если мы зададим путь к какому-то файлу, а не каталогу)
                3) Если у вас нет доступа для изменения текущей директории на новую (ну это не очень то важно)
            которых нужно обработать.
        """
        try:
            os.chdir(given_path)
            print("Текущий рабочий каталог: {0}".format(os.getcwd()))
        except FileNotFoundError:
            print("Каталог: {0} не существует".format(given_path))
        except NotADirectoryError:
            print("{0} не каталог".format(given_path))
        except PermissionError:
            print("У вас нет прав на изменение {0}".format(given_path))

    @staticmethod
    def cp(source: str, destination: str):
        """
            Копирует содержимое файла source в файл destination.
            Если не существует:
                1) файла destination, то создастся такой файл, и
                   туда записываются данные из source.
                2) файла source, то выводит, что файл не найден
        """
        try:
            open(source, 'r')
        except FileNotFoundError as e:
            print('Source file not found!')
            return
        inp = open(source, 'r')
        out = open(destination, 'w')
        for lines in inp.readlines():
            out.write(lines)
        inp.close()
        out.close()

    @staticmethod
    def mv(source: str, destination: str):
        """
            Если destination является каталогом, то туда просто переместит файл source,
            а если destination просто файл, то переименовывает файл source на destination.
            Так как в этой функции нет параметров как в линуксовой mv, то если в каталоге destination
            или в текущей директории уже есть файл с названием source файла, то source файл просто заменит
            файл, который был в каталоге destination или в текущей директории.
        """
        if destination[-1] == '/':
            if not os.path.exists(destination[0:len(destination) - 1]):
                print('Path doesn\'t exist')
                return
            else:
                os.replace(source, destination + source)
                return
        os.replace(source, destination)

    @staticmethod
    def rm(filename: str):
        """
            Удаляет заданный файл. Если файл не существует, то выводит, что файл не найден.
        """
        try:
            os.remove(filename)
        except FileNotFoundError:
            print('File not found!')

    @staticmethod
    def rmdir(dir_name: str):
        """
            Удаляет заданный каталог. Если каталог не существует, то выводит, что нет такого каталога.
            Если заданный аргумент не является каталогом, то выводит, что аргумент не является каталогом.
            Если заданный каталог не пуст, то выводит, что каталог не пуст.
            Иначе с сообщением, что заданный каталог успешно удалён, удалит заданный каталог.
        """
        if not os.path.exists(dir_name):
            print('There is no such directory!')
        elif not os.path.isdir(dir_name):
            print('{0} is not a directory!'.format(colored(dir_name, attrs=['bold'])))
        elif len(os.listdir(dir_name)):
            print('Directory {0} isn\'t empty!'.format(colored(dir_name, 'blue', attrs=['bold'])))
        else:
            print('Directory {0} was successfully deleted!'.format(colored(dir_name, 'blue', attrs=['bold'])))
            os.rmdir(dir_name)

    @staticmethod
    def mkdir(new_dir: str):
        """
            Создаёт новый каталог. Если уже существует файл или каталог с таким именем,
            выбрасывает исключение.  Обработаем исключение с выводом, что невозможно
            создать каталог с именем new_dir, так как уже существует такой файл.
        """
        try:
            os.mkdir(new_dir)
        except OSError as error:
            print(
                'Can\'t create directory \"{0}\": File(directory) with this name already exists!'.format(
                    colored(new_dir, 'blue', attrs=['bold'])))

    @staticmethod
    def help():
        """
            Описание всех команд с их синтаксисом.
        """

        def print_syn_desc(command: str, description: str, args: str):
            print(colored(command + ' : ', 'red', attrs=['bold']))
            print(colored('  syntax: ', 'green', attrs=['bold']),
                  colored(command, attrs=['bold']) + ' ' + colored(args, 'yellow'))
            print(colored('  description: ', 'green', attrs=['bold']), description)

        print_syn_desc('ls', 'prints the contents of the current directory', '')
        print_syn_desc('pwd', 'prints the absolute path to the current directory', '')
        print_syn_desc('cd', 'changes current directory to a new given directory', '<path_to_new_directory>')
        print_syn_desc('cp', 'copies the contents of the <source> file to the <destination> file.',
                       '<source_file> <dest_file>')
        print_syn_desc('mv', 'moves <source> file to another <destination> directory or '
                             'to rename <source> file to <destination>',
                       '<source_file> [<dest_directory> or <dest_file>]')
        print_syn_desc('rm', 'removes the <source> that is given with an absolute path',
                       '<source_file>')
        print_syn_desc('rmdir', 'removes the <source> directory if it is empty',
                       '<source_dir>')
        print_syn_desc('mkdir', 'creates a <new> directory, if it doesn\'t exist.',
                       '<new_dir_name>')
        print_syn_desc('run', 'runs an executable file <source> with given <args>',
                       '<source_file> <args>')
        print_syn_desc('clear', 'cleans the terminal.',
                       '')
        print_syn_desc('exit', 'exits from the terminal.',
                       '')
