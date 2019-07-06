import random
import Agent
from Util import pos_to_coord
import numpy as np


class TabularQAgent(Agent.Agent):
    def __init__(self, side, epsilon=0.1, alpha=0.8, gamma=0.7):
        self.side = side
        self.epsilon = epsilon
        self.alpha = alpha
        self.gamma = gamma
        self.value_table = dict()
        self.current_state = None
        self.action_index = None

    def make_move(self, available_moves, current_state):
        if (current_state not in self.value_table):
            self.value_table.update({current_state: np.random.rand(9)})

        while True:
            if (random.random() < self.epsilon):
                action_index = random.randint(0, 9)
            else:
                action_index = np.argmax(self.value_table[current_state])

            if (pos_to_coord(action_index) not in available_moves):
                self.value_table[current_state][action_index] = -1.0
            else:
                break

        action_coord = pos_to_coord(action_index)
        board.set_position_value(action_coord, self.side)
        self.current_state = board.current_state
        self.action_index = action_index

    def learn_from_move(self, next_state, reward):
        action_coord = pos_to_coord(self.action_index)
        action_value = self.value_table[self.current_state][self.action_index]
        max_action_index = np.argmax(self.value_table[next_state])

        action_value += self.alpha * \
            (reward + self.gamma * self.value_table[next_state]
             [max_action_index] - action_value)

        self.value_table[self.current_state][self.action_index] = action_value

    def stop_exploring(self):
        self.epsilon = 0
