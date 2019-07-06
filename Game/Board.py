from Util import check_for_identical_rows


class Board:
    def __init__(self):
        self.board = [['-', '-', '-'] for i in range(3)]
        self.state = '123456789'
        self.all_moves = [[x, y] for x in range(3) for y in range(3)]
        self.valid_moves = self.all_moves
        self.winner = None

    def is_position_empty(self, position):
        return position in self.available_moves

    def set_position_value(self, position, side):
        self.available_moves.remove(position)
        self.state = util.change_board_state(self.state, position, side)
        row, col = position
        self.board[row - 1][col - 1] = side
        self.check_for_win(side)
        return self.state

    def change_board_state(current_state, position, side):
        state_number = self.all_moves.index(position)
        new_state = current_state[:state_number] + \
            side + current_state[state_number + 1:]
        self.state = new_state

    def check_for_win(self, side):
        if (check_for_identical_rows):
            self.winner = side
        else:
            if (not self.valid_moves):
                self.winner = 'DRAW'
