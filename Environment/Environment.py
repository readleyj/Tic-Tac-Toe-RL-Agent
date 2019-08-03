from .Board import Board


class Environment:
    def __init__(self, player1, player2):
        self.board = Board()
        self.player1 = player1
        self.player2 = player2
        self.results = []

    def set_rewards(self, agent_one_reward, agent_two_reward, final=False):
        self.player1.learn_from_move(self.board.state, agent_one_reward, final)
        self.player2.learn_from_move(self.board.state, agent_two_reward, final)

    def check_game_result(self):
        if (self.board.result == self.player1.side):
            self.set_rewards(1.0, -1.0, final=True)
        elif (self.board.result == self.player2.side):
            self.set_rewards(-1.0, 1.0, final=True)
        elif (self.board.result == 'DRAW'):
            self.set_rewards(-1.0, -1.0, final=True)

    def run_game(self):
        while(self.board.result is None):
            self.player1.make_move(self.board)

            self.check_game_result()
            if (self.board.result):
                self.results.append(self.board.result)
                self.board = Board()
                break

            self.player2.make_move(self.board)

            self.check_game_result()
            if(self.board.result):
                self.results.append(self.board.result)
                self.board = Board()
                break

            self.set_rewards(0, 0)

    def train(self, num_episodes=5000, save=False):
        for episode in range(num_episodes):
            self.run_game()

            if (episode % 1000 == 0):
                completion_pct = (episode / num_episodes) * 100
                print('Episode: {}'.format(episode))
                print('{0:.2f}% complete'.format(completion_pct))

        x_wins = (self.results.count(self.player1.side) / num_episodes) * 100
        y_wins = (self.results.count(self.player2.side) / num_episodes) * 100
        draws = 100 - x_wins - y_wins
        print('Total games of {} games played'.format(num_episodes))
        print('X won {0:.2f}% of the games'.format(x_wins))
        print('O won {0:.2f}% of the games'.format(y_wins))
        print('{0:.2f}% of the games were draws'.format(draws))

        if (save):
            self.player1.save_values()
            self.player2.save_values()

    def stop_exploring(self, *agents):
        for agent in agents:
            agent.stop_exploring()
