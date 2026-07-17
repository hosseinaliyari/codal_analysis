from abc import ABC, abstractmethod

class IFinancialAdjustments(ABC):
    @abstractmethod
    def add(self, FinancialAdjustments):
        pass
    @abstractmethod
    def get_by_symbol(self, symbol):
        pass

    @abstractmethod
    def get_all(self):
        pass

    @abstractmethod
    def update(self, economic_data):
        pass

    @abstractmethod
    def delete(self, symbol):
        pass