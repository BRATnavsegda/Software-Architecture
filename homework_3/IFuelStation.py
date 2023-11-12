from abc import ABC, abstractmethod


class IFuelStation(ABC):
    @abstractmethod
    def refill(self):
        pass
