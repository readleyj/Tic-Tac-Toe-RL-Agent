import os
from ..Util import save_to_npy, load_npy

dir = os.path.dirname(__file__)


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
        path = '../../trained/' + cls_name + '/' + file_string
        full_path = os.path.join(dir, path)
        return load_npy(full_path).item()
