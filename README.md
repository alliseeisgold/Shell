Shell
========

**Shell** должен представлять из себя программу с частичной функциональностью sh,
bash или cmd. При запуске программа выводит приглашение и ожидает ввода одной из
команд.

Базовый функционал
=========================
1. ***ls***. Вывести список файлов и директорий для текущей директории.
2. ***pwd***. Вывести полный путь для текущей директории.
3. ***cd*** <путь>. Переход по относительному или абсолютному пути.
4. ***cp*** <имя файла> <имя файла>. Скопировать файл.
5. ***mv*** <имя файла> <имя файла>. Переместить файл.
6. ***rm*** <имя файла>. Удалить файл.
7. ***rmdir*** <имя директории>. Удалить директорию в случае, если она пуста.
8. ***mkdir*** <имя директории>. Создать директорию, если ее не было.
Все пути могут быть полными или относительными. Программа должна проверять
возможность выполнения операций (существование и несуществование файлов), и
сообщать об ошибках в случае их возникновения.

Бонусы
=====================
* **Реализация запуска исполняемых файлов или пайпов**
#### Запуск исполняемых файлов
***run*** <путь к исполняемому файлу> <аргументы>. Запускаем файл, печатаем его вывод
stdout и stderr, ожидаем завершения перед вводом след. команды. Пример:
$ run echo ‘hello’
hello
* **Тесты**

Запуск
=======

### Сначала клонируйте репозиторий
    git clone https://github.com/alliseeisgold/review_1.git
### Установите нужные библиотеки
    pip install -r requirements.txt

### Запуск
    python3 main.py