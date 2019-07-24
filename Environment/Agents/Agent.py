from abc import ABC, abstractmethod
from ..Util import save_to_npy


class Agent(ABC):
    @abstractmethod
    def make_move(self, available_moves):
        pass

    @abstractmethod
    def learn_from_move(self, next_state, reward):
        pass

    @abstractmethod
    def stop_exploring(self):
        pass

    def save_values(self):
        cls_name = self.__class__.__name__
        file_string = cls_name + '_' + self.side
        path = './trained/' + cls_name
        save_to_npy(path, file_string, self.value_table)
