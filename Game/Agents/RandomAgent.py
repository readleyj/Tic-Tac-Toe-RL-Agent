import random
from .Agent import Agent


class RandomAgent(Agent):
    def __init__(self, side):
        self.side = side

    def make_move(self, board):
        next_move = random.choice(board.valid_moves)
        board.set_position_value(next_move, self.side)

    def learn_from_move(self, next_state, reward, final):
        pass

    def stop_exploring(self):
        pass

    def save_values(self):
        pass
