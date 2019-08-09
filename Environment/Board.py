from .Util import check_for_identical_rows, coord_to_pos


class Board:
    def __init__(self):
        self.board = [['-', '-', '-'] for i in range(3)]
        self.state = '012345678'
        self.all_moves = [[x, y] for x in range(3) for y in range(3)]
        self.valid_moves = self.all_moves[:]
        self.valid_indices = [i for i in range(9)]
        self.result = None
        self.last_move_index = None

    def is_position_empty(self, position):
        return position in self.valid_moves

    def set_position_value(self, position, side):
        self.last_move_index = coord_to_pos(position)
        self.valid_moves.remove(position)
        self.valid_indices.remove(self.last_move_index)
        self.change_board_state(self.state, position, side)
        row, col = position
        self.board[row][col] = side
        self.check_for_win(side)

    def change_board_state(self, current_state, position, side):
        state_number = self.all_moves.index(position)
        new_state = current_state[:state_number] + \
            side + current_state[state_number + 1:]
        self.state = new_state

    def check_for_win(self, side):
        if (check_for_identical_rows(self.board, side)):
            self.result = side
        else:
            if (not self.valid_moves):
                self.result = 'DRAW'
