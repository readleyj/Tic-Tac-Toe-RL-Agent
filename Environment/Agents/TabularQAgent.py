import random
from .Agent import Agent
from ..Util import pos_to_coord
import numpy as np


class TabularQAgent(Agent):

    def __init__(self, side, epsilon=0.1, alpha=0.8, gamma=0.7):
        super().__init__(side)
        self.epsilon = epsilon
        self.alpha = alpha
        self.gamma = gamma
        self.value_table = dict()
        self.previous_state = None
        self.action_index = None

    @classmethod
    def from_saved(cls, side):
        q_agent = cls(side, epsilon=0, alpha=0, gamma=0)
        q_table = q_agent.load_values()
        q_agent.value_table = q_table
        return q_agent

    def get_q_values(self, state, final=False):
        if (state not in self.value_table):
            if (final):
                self.value_table.update({state: np.zeros(9)})
            else:
                self.value_table.update({state: np.random.rand(9)})

        return self.value_table[state]

    def make_move(self, board):
        current_state = board.state
        q_vals = self.get_q_values(current_state)

        while True:
            if (random.random() < self.epsilon):
                action_index = random.randint(0, 8)
            else:
                action_index = np.argmax(q_vals)

            if (pos_to_coord(action_index) not in board.valid_moves):
                self.value_table[current_state][action_index] = -10.0
            else:
                break

        action_coord = pos_to_coord(action_index)
        board.set_position_value(action_coord, self.side)
        self.previous_state = current_state
        self.action_index = action_index

    def learn_from_move(self, next_state, reward, final=False):
        action_coord = pos_to_coord(self.action_index)
        action_value = self.value_table[self.previous_state][self.action_index]
        q_vals = self.get_q_values(next_state, final)
        max_action_index = np.argmax(q_vals)

        action_value += self.alpha * \
            (reward + self.gamma * q_vals[max_action_index] - action_value)

        self.value_table[self.previous_state][self.action_index] = action_value

    def stop_exploring(self):
        self.epsilon = 0
