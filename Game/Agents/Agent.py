from abc import ABC, abstractmethod
from ..Util import save_to_json


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
        file_string = self.__class__.__name__
        path = '../../trained'
        save_to_json(path, file_string, self.value_table)
