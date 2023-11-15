# Базовое задание:
# Согласно разработанной UML диаграмме доменных классов, разработать код на JAVA или python.
# Задание со звездочкой:
# Разработать методы для доменных классов и логику покупки билетов.
#
# Домашняя работа сдается в виде ссылки на решение, выложенное на Вашем GitHub
import decimal
from datetime import datetime

from decimal import Decimal


class Ticket:

    __id: int # _____________________в Python 3. long переименован в int, поэтому использую int______________________________________
    __departure_zone: int
    __arrival_zone: int
    __route_number: int
    __departure_time: datetime
    __arrival_time: datetime
    __buyer_id: int
    __is_used: bool
    __price: Decimal
    __place: str

    def __init__(self, id_, departure_zone, arrival_zone, route_number, departure_time, arrival_time,
                 buyer_id, price, place):
        self.__id = id_
        self.__departure_zone = departure_zone
        self.__arrival_zone = arrival_zone
        self.__route_number = route_number
        self.__departure_time = departure_time
        self.__arrival_time = arrival_time
        self.__buyer_id = buyer_id
        self.__is_used = True
        self.__price = price
        self.__place = place

    def get_id(self): # у __id и __buyer_id сеттеры не делаем
        return self.__id

    def get_departure_zone(self):
        return self.__departure_zone

    def set_departure_zone(self, departure_zone: int):
        self.__departure_zone = departure_zone

    # ну и так далее для каждого