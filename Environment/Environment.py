from .Board import Board


class Environment:
    def __init__(self, player1, player2):
        self.board = Board()
        self.player1 = player1
        self.player2 = player2
        self.current_player = self.player1
        self.next_player = self.player2
        self.total_moves = 0
        self.results = []

    def check_game_result(self):
        if (self.board.result == self.current_player.side):
            self.current_player.learn_from_move(self.board, 1.0, final=True)
            self.next_player.learn_from_move(self.board, -1.0, final=True)
        elif (self.board.result == 'DRAW'):
            self.current_player.learn_from_move(self.board, 0, final=True)
            self.next_player.learn_from_move(self.board, 0, final=True)

    def reset_game(self, result):
        self.results.append(result)
        self.board = Board()

    def run_game(self):
        while (self.board.result is None):
            self.current_player.make_move(self.board)
            self.total_moves += 1
            self.check_game_result()

            if(self.board.result):
                self.reset_game(self.board.result)
                break

            if (self.total_moves != 1):
                self.next_player.learn_from_move(self.board, 0, final=False)

            self.current_player, self.next_player = self.next_player, self.current_player

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
