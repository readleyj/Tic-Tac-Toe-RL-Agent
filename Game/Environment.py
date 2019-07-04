import Board from Board


class Environment:
    def __init__(self, player1, player2):
        self.board = Board()
        self.player1 = player1
        self.player2 = player2
        self.player_1_turn = True
        self.available_moves = board.available_moves
        self.current_state = board.current_state

    def step(self):
