import Agent.Agent
from Util import pos_to_coord


class TabularQAgent(Agent.Agent):
    def __init__(self, letter, epsilon=0.1, alpha=0.8):
        self.letter = letter
        self.epsilon = epsilon
        self.alpha = alpha
        self.value_table = dict()

    def make_move(self, available_moves, current_state):
        if current_state in self.value_table:
            # Use numpy arrays
            move_values = self.value_table[current_state]
            possible_moves = [pos_to_coord(value) for value in available_moves]
            # possible_move_values = [poss]
        
    def learn_from_move(self):
        pass
