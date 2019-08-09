# from abc import ABC, abstractmethod
from ..Util import save_to_npy, load_npy


class Agent:

    def __init__(self, side):
        self.side = side

    def make_move(self, available_moves):
        pass

    def learn_from_move(self, next_state, reward):
        pass

    def stop_exploring(self):
        pass

    def save_values(self):
        cls_name = self.__class__.__name__
        file_string = cls_name + '_' + self.side
        # Fix the paths
        path = './trained/' + cls_name
        save_to_npy(path, file_string, self.value_table)

    def load_values(self):
        cls_name = self.__class__.__name__
        file_string = cls_name + '_' + self.side + '.npy'
        # Fix the paths
        path = '../trained/' + cls_name + '/' + file_string
        return load_npy(path).item()