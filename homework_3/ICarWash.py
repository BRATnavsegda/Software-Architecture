from abc import ABC, abstractmethod


class ICarWash(ABC):
    @abstractmethod
    def weep_windshield(self):
        pass

    @abstractmethod
    def weep_headlights(self):
        pass

    @abstractmethod
    def weep_mirror(self):
        pass
