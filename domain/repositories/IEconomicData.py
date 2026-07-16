from abc import ABC, abstractmethod

class EconomicRepository(ABC):

    @abstractmethod
    def add(self, economic_data):
        pass

    @abstractmethod
    def get_by_year(self, year):
        pass

    @abstractmethod
    def get_all(self):
        pass

    @abstractmethod
    def update(self, economic_data):
        pass

    @abstractmethod
    def delete(self, year: int):
        pass