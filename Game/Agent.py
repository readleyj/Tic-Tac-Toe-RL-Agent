from abc import ABC, abstractmethod


class Agent(ABC):
    @abstractmethod
    def make_move(self, available_moves):
        pass

    @abstractmethod
    def learn_from_move(next_state)
