import random
import Agent


class RandomAgent(Agent.Agent):
    def __init__(self, letter):
        self.letter = player_letter

    def make_move(self, available_moves, board):
        next_move = random.choice(available_moves)
        board.set_position_value(next_move, self.letter)
