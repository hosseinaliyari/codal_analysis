from abc import ABC, abstractmethod

class IMergedData(ABC):

    @abstractmethod
    def update_MergedData(self, merged_data_list):
        pass
