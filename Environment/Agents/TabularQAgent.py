import random
import numpy as np
from .Agent import Agent
from ..Util import pos_to_coord


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

    def get_q_values(self, state, actions, final=False):
        if (state not in self.value_table):
            value = 0
            action_value_pairs = {action: value for action in actions}
            self.value_table.update({state: action_value_pairs})

        return self.value_table[state]

    def get_max_q(self, state, actions):
        act_vals = self.value_table[state]
        max_action = max(act_vals, key=act_vals.get)
        max_action_value = act_vals[max_action]
        max_act_list = [key for key, val in act_vals.items()
                        if val == max_action_value]
        return random.choice(max_act_list)

    def make_move(self, board):
        current_state = board.state
        actions = board.valid_indices
        q_vals = self.get_q_values(current_state, actions)

        if (random.random() < self.epsilon):
            action_index = random.choice(board.valid_indices)
        else:
            action_index = self.get_max_q(current_state, actions)

        action_coord = pos_to_coord(action_index)
        board.set_position_value(action_coord, self.side)
        self.previous_state = current_state
        self.action_index = action_index

    def learn_from_move(self, board, reward, final=False):
        action_coord = pos_to_coord(self.action_index)
        actions = board.valid_indices
        current_state = board.state
        action_value = self.value_table[self.previous_state][self.action_index]

        if (final):
            max_action_value = 0
        else:
            q_vals = self.get_q_values(current_state, actions, final)
            max_action_index = self.get_max_q(current_state, actions)
            max_action_value = q_vals[max_action_index]

        action_value += self.alpha * \
            (reward + self.gamma * max_action_value - action_value)

        self.value_table[self.previous_state].update(
            {self.action_index: action_value})

    def stop_exploring(self):
        self.epsilon = 0
