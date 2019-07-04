import Board from Board


class Environment:
    def __init__(self, player1, player2):
        self.board = Board()
        self.player1 = player1
        self.player2 = player2

    def set_rewards(reward_1):
        

    def run_game(self):
        while(self.board.winner is None and self.board.draw is False):
            self.player1.make_move(self.board.available_moves,
                                   self.board.current_state)
            if (self.board.winner == self.player1.side)
