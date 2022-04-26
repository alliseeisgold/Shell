# Bonus Functionality
import subprocess
import os


class Bonus:
    """
        Здесь находится реализация бонусной части.
        Кроме тестов. Тесты находятся в папке tests в tests.py
    """
    @staticmethod
    def exec_files_runner(args: list):
        """
            Сначала проверяем существует ли заданный файл и потом проверяем
            является ли исполняемым. Если оба условия верны, то запускаем
            исполняемый файл с заданными аргументами.
        """
        if os.path.exists(args[0]):
            if os.access(args[0], os.X_OK):
                subprocess.run(args)
            else:
                print('This file isn\'t executable.')
        else:
            print('There isn\'t such file.')

