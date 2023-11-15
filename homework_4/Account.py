

from decimal import Decimal


class Account:
    __user_account_id: int
    __balance: Decimal

    def __init__(self, user_account_id, balance):
        self.__user_account_id = user_account_id
        self.__balance = balance


    def get_user_account_id(self):
        return self.__user_account_id

    def get_balance(self):
        return self.__balance

    def set_balance(self, balance):
        self.__balance = balance
