from typing import List

from homework_4.Ticket import Ticket


class User:
    __id: int
    __name: str
    __tickets: List[Ticket]
    __login: str
    __password_hash_code: int
    __account_id: int

    def __init__(self, id, name, tickets, login, password_hash_code, account_id):
        self.__id = id
        self.__name = name
        self.__tickets = tickets
        self.__login = login
        self.__password_hash_code = password_hash_code
        self.__account_id = account_id

    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    # и так далее