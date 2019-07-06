from .Board import Board


class Environment:
    def __init__(self, player1, player2):
        self.board = Board()
        self.player1 = player1
        self.player2 = player2

    def set_rewards(self, agent_one_reward, agent_two_reward):
        self.player1.learn_from_move(self.board.state, agent_one_reward)
        self.player2.learn_from_move(self.board.state, agent_two_reward)

    def check_game_result(self):
        if (self.board.result == self.player1.side):
            self.set_rewards(1.0, -1.0)
        elif (self.board.result == self.player2.side):
            self.set_rewards(-1.0, 1.0)
        elif (self.board.result == 'DRAW'):
            self.set_rewards(-1.0, -1.0)
        else:
            self.set_rewards(0, 0)

    def run_game(self):
        while(self.board.result is None):
            self.player1.make_move(self.board)

            self.check_game_result()
            if (self.board.result):
                break

            self.player2.make_move(self.board)

            self.check_game_result()
            if(self.board.result):
                break

    def train(self, num_episodes=5000):
            for episode in range(num_episodes):
                self.run_game()

    def stop_exploring(self, *agents):
            for agent in agents:
                agent.stop_exploring()
