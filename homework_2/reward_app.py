# Задание 1. Закончить разработку паттерна Фабричный метод.
# a) Добавить в пример из семинара как минимум 5 наград.
# (Задача со звездочкой)
# b) Награды должны генерироваться в соотношении: 10:10:10:10:10(ваши награды):3(золото GOLD):1(алмазы GEM)


from abc import ABC, abstractmethod
from random import randint


class IGameItem(ABC):
    @abstractmethod
    def open(self):
        pass




class ItemFabric(ABC):
    @abstractmethod
    def create_item(self):
        pass


class Gold(IGameItem):
    def open(self):
        print('Gold!')


class GoldGenerator(ItemFabric):
    def create_item(self):
        return Gold()


class Gem(IGameItem):
    def open(self):
        print('Gem!')


class GemGenerator(ItemFabric):
    def create_item(self):
        return Gem()

class Wood(IGameItem):
    def open(self):
        print('Wood!')


class WoodGenerator(ItemFabric):
    def create_item(self):
        return Wood()


class Iron(IGameItem):
    def open(self):
        print('Iron!')


class IronGenerator(ItemFabric):
    def create_item(self):
        return Iron()


class Straw(IGameItem):
    def open(self):
        print('Straw!')


class StrawGenerator(ItemFabric):
    def create_item(self):
        return Straw()


class Stone(IGameItem):
    def open(self):
        print('Stone!')


class StoneGenerator(ItemFabric):
    def create_item(self):
        return Stone()


class Berries(IGameItem):
    def open(self):
        print('Berries!')


class BerriesGenerator(ItemFabric):
    def create_item(self):
        return Berries()

class RewardsChance(ABC):

    def __init__(self, chance_dict):
        self.chance_dict = chance_dict

    def function(self):
        """
        Функция генерирует случайный ключ из словаря на основе значений в качестве весов.
        """
        max_value = 1

        for key, value in self.chance_dict.items():
            max_value += value

        result = randint(1, max_value +1)


        for key, value in self.chance_dict.items():
            if (max_value - result - value) <= 0:
                return key
            else:
                max_value -= value



    


if __name__ == '__main__':

    # Создаем словарь с возможными наградами, где ключем является награда,
    # а значением - вес награды, чем больше вес, тем больше шанс получить эту награду.

    rewards = {GoldGenerator().create_item(): 3,
               GemGenerator().create_item(): 1,
               WoodGenerator().create_item(): 10,
               IronGenerator().create_item(): 10,
               StrawGenerator().create_item(): 10,
               StoneGenerator().create_item(): 10,
               BerriesGenerator().create_item(): 10,
               }

    for i in range(200):
        RewardsChance(rewards).function().open()

    # rewards = [GoldGenerator(), GemGenerator()]
    #
    # for i in range(20):
    #     rewards[randint(0, 1)].create_item().open()