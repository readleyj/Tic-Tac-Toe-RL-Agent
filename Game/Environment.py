import Board from Board


class Environment:
    def __init__(self, player1, player2):
        self.board = Board()
        self.player1 = player1
        self.player2 = player2

    def set_rewards(agent_one_reward, agent_two_reward):
        self.player1.learn_from_move(self.current_state, agent_one_reward)
        self.player2.learn_from_move(self.current_state, agent_two_reward)

    def run_game(self):
        while(self.board.winner is None and self.board.draw is False):
            self.player1.make_move(self.board.available_moves,
                                   self.board.current_state)

            if (self.board.winner == self.player1.side):
                self.set_rewards(1.0, -1.0)
                break

            self.player2.make_move(self.board.available_moves,
                                   self.board.current_state)

            if (self.board.winner == self.player2.side):
                self.set_rewards(-1.0, 1.0)
                break

            if (self.board.draw):
                self.set_rewards(-1.0, -1.0)
                break

        def train(num_episodes=3000):
            for episode in num_episodes:
                run_game()
