import os
import socket


class User:
    """
        Этот класс предназначен для взятия хоста и имени пользователя.
        Например: name@hostname
    """

    def __init__(self):
        self.username = os.getlogin()
        self.hostname = socket.gethostname()

    def getUserName(self):
        return self.username

    def getUser(self):
        user = self.username + '@' + self.hostname + ':'
        return user
