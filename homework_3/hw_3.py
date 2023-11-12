
# ----------------------------------------------------------- PYTHON ---------------------------------------------
# 1) Переписать код в соответствии с Single Responsibility Principle:
from datetime import date
from abc import ABC, abstractmethod


class Employee:

    def __init__(self, name, dob, base_salary):
        self.name = name
        self.dob = dob
        self.base_salary = base_salary


    def get_emp_info(self):
        return f"name - {self.name} , dob - {self.dob}"


class Account:

    def __init__(self, employee: Employee):
        self.employee = employee
        self.tax = int(employee.base_salary * 0.13)
        self.net_salary = employee.base_salary - self.tax

# Подсказка: вынесите метод calculateNetSalary() в отдельный класс









# 2) Переписать код SpeedCalculation в соответствии с Open - Closed Principle:


class SpeedCalculation(ABC):

    @abstractmethod
    def calculate_allowed_speed(self):
        pass


class Vehicle:

    def __init__(self, max_speed):
        self.max_speed = max_speed



    def get_max_speed(self):
        return self.max_speed



class Bus(Vehicle, SpeedCalculation):

    def __init__(self, max_speed):

        super().__init__(max_speed)

    def calculate_allowed_speed(self):

        return self.get_max_speed() * 0.6


class Car(Vehicle, SpeedCalculation):

    def __init__(self, max_speed, type):
        super().__init__(max_speed, type)

    def calculate_allowed_speed(self):

        return self.get_max_speed() * 0.8

# Подсказка: создайте два дополнительных класса Car и Bus(наследников Vehicle), напишите метод calculateAllowedSpeed().\
# Использование этого метода позволит сделать класс SpeedCalculation соответствующим OCP








# 3) Переписать код в соответствии с Interface Segregation Principle:
import math


class CalculateArea(ABC):

    @abstractmethod
    def area(self):
        pass


class CalculateVolume(ABC):

    @abstractmethod
    def volume(self):
        pass


class Circle(CalculateArea):

    def init(self, radius):
        self.radius = radius


    def area(self):
        return 2 * math.pi * self.radius



class Cube(CalculateArea, CalculateVolume):

    def init(self, edge):
        self.edge = edge

    def area(self):
        return 6 * self.edge * self.edge

    def volume(self):
        return self.edge * self.edge * self.edge


# Подсказка: круг не объемная фигура и этому классу не нужен метод volume().











# 4) Переписать код в соответствии с Liskov Substitution Principle:


class Rectangle:

    def init(self):
        self.width = 0
        self.height = 0

    def setWidth(self, width):
        self.width = width

    def setHeight(self, height):
        self.height = height

    def area(self):
        return self.width * self.height


class Square(Rectangle):

    def setWidth(self, width):
        self.width = width
        self.height = width

    def setHeight(self, height):
        self.width = height
        self.height = height

# тут не понял почему не подходит под принцип LSP, мне кажется наследник не меняет поведение родительского класса
# ____________________________________________________________________________________________________________________








# 5) Переписать код в соответствии с Dependency Inversion Principle:


class Car:

    def init(self, engine):
        self.engine = engine

    def start(self):
        self.engine.start()


class PetrolEngine:

    def start(self):
        pass
# Разорвать зависимость классов Car и PetrolEngine. У машины же может быть DieselEngine.

# Интересно, что так как это Python, то и разрывать уже ничего не надо, тут нет привязки класса Car к PetrolEngine,
# мы можем любой вид двигателя передать в класс Car.
# Но наверное имеется ввиду что-то такое:

class Engine(ABC):
    @abstractmethod
    def start(self):
        pass


class PetrolEngine1(Engine):
    def start(self):
        pass

class DieselEngine(Engine):
    def start(self):
        pass