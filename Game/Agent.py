from abc import ABC, abstractmethod


class Agent(ABC):
    @abstractmethod
    def move(self, available_moves):
        pass
